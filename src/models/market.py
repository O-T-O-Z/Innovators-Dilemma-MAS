from typing import Type, Any
import mesa
import random
import numpy as np
from mesa import Model
from src.agents.grid_agent import GridAgent
from src.agents.company import CompanyAgent
from src.agents.whale import Whale
from src.agents.customer import CustomerAgent
from src import globals
from src.models.scheduler import RandomActivationByTypeFiltered


class MarketModel(Model):
	"""A model with some number of agents."""

	def __init__(self, num_customers, num_companies, width, height, *args: Any, **kwargs: Any):
		super().__init__(*args, **kwargs)
		self.num_customers = num_customers
		self.num_companies = num_companies
		self.width = width
		self.height = height

		self.reset()

	def reset(self):
		self.grid = mesa.space.MultiGrid(self.width, self.height, True)
		self.schedule = RandomActivationByTypeFiltered(self)
		self.running = True  # maybe this variable is important?
		self.companies = {}
		self.customers = {}
		self.free_cells = [x for x in range(self.width * self.height)]
		self.id = 0
		self._spawn_agents()
		self.__init_data_collector()
		
	def __init_data_collector(self):
		reporters = {}

		for i, agent in enumerate(self.companies.values()):
			def caller(m,a=agent): 
				"""
				Whatever you do, never edit this function. Especially the a=agent part.
				If want to see the end of the world go to: https://stackoverflow.com/questions/54288926/python-loops-and-closures
				"""
				return m.schedule.get_capital(a)

			reporters["Label_" + str(i)] = caller
		
		self.datacollector = mesa.DataCollector(reporters)
		self.datacollector.collect(self)

	def get_next_id(self):
		val = self.id
		self.id += 1
		return val

	# Environment logic

	def _spawn_agents(self):
		self._spawn_companies()
		self._spawn_customers()

	def _get_free_cell_pos(self):
		rand_idx = random.randint(0, len(self.free_cells) - 1)
		val = self.free_cells.pop(rand_idx)
		return val % self.width, val // self.width

	def _spawn_companies(self):
		for _ in range(self.num_companies):
			company = CompanyAgent(self.get_next_id(), self, self._get_free_cell_pos(), innovation_factor=random.random())
			self._add_agent(company, self.companies)
	
	def _spawn_customers(self):
		for _ in range(self.num_customers):
			company = CustomerAgent(self.get_next_id(), self, self._get_free_cell_pos())
			self._add_agent(company, self.customers)

	def _add_agent(self, agent, dict_: dict):
		dict_[agent.get_id()] = agent
		self.schedule.add(agent)
		self.grid.place_agent(agent, agent.get_position())

	def remove_company_agent(self, id: int):
		company = self.companies[id]
		self.grid.remove_agent(company)
		self.schedule.remove(company)
		del self.companies[id]

	def step(self):
		self.schedule.step()
		self.datacollector.collect(self)

	def get_companies(self):
		return list(self.companies.values())

	def get_customers(self):
		return list(self.customers.values())

