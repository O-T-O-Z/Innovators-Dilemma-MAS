from typing import Type, List
import mesa
import random
import numpy as np
from mesa import Model
from src.agents.company import CompanyAgent
from src.agents.customer import CustomerAgent


class MarketModel(Model):
    """A model with some number of agents."""

    def __init__(self, 
        num_customers, 
        num_companies,
        width, 
        height):
        
        self.num_customers = num_customers
        self.num_companies = num_companies
        self.width = width
        self.height = height

        self.reset()

    def reset(self):
        self.datacollector = mesa.DataCollector(
            model_reporters={}, 
            agent_reporters={}
        )
        self.grid = mesa.space.MultiGrid(self.width, self.height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True # maybe this variable is important?
        self.companies = {}
        self.customers = {}
        self.free_cells = [x for x in range(self.width * self.height)]
        self.next_id = 0
        self._spawn_agents()
    
    # Getters
    def get_companies(self):
        return list(self.companies.values())

    def get_company(self, id):
        return self.companies[id]

    def get_customers(self):
        return list(self.customers.values())

    def get_customer(self, id):
        return self.customers[id]

    def get_next_id(self):
        val = self.next_id
        self.next_id += 1
        return val

    # Environment logic

    def _spawn_agents(self):
        self._spawn_agents_of_class(self.num_companies, CompanyAgent, self.companies)
        self._spawn_agents_of_class(self.num_customers, CustomerAgent, self.customers)

    def _get_free_cell_pos(self):
        rand_idx = random.randint(0, len(self.free_cells) - 1)
        val = self.free_cells.pop(rand_idx)
        return np.array([val % self.width, val // self.width])

    def _spawn_agents_of_class(self, n, class_: Type, ls: List):
        for _ in range(n):
            id = self.get_next_id()
            agent = class_(id, self, self._get_free_cell_pos())
            ls[id] = agent
            self.schedule.add(agent)
            self.grid.place_agent(agent, tuple(agent.position))

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
