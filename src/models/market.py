from typing import Type
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
        self.datacollector = mesa.DataCollector(
            model_reporters={}, 
            agent_reporters={}
        )

    def reset(self):
        self.grid = mesa.space.MultiGrid(self.width, self.height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True # maybe this variable is important?
        self.companies = {}
        self.customers = {}
        self.free_cells = [x for x in range(self.width * self.height)]
    
    # Getters
    def get_companies(self):
        return self.companies.items()

    def get_company(self, id):
        return self.companies[id]

    def get_customers(self):
        return self.customers.items()

    def get_customer(self, id):
        return self.customers[id]

    # Environment logic

    def _spawn_agents(self):
        self._spawn_agents_of_class(self.num_companies, CompanyAgent)
        self._spawn_agents_of_class(self.num_customers, CustomerAgent)

    def _get_free_cell_pos(self):
        rand_idx = random.randint(0, len(self.free_cells))
        self.free_cells.pop(rand_idx)
        return np.array(rand_idx % self.width, rand_idx / self.width)

    def _spawn_agents_of_class(self, n, class_: Type):
        for id in range(n):
            agent = class_(id, self, self._get_free_cell_pos())
            self.schedule.add(agent)
            self.grid.place_agent(agent, agent.position)
            self.companies.append(agent)

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
