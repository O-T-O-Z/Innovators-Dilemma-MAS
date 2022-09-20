from mesa import Agent, Model
import numpy as np
from src.strategies.basic import BasicStrategy
from typing import Tuple

class CompanyProduct():

    def __init__(self, pbounds=[0, 1]) -> None:
        self.pbounds = pbounds
        self.x = 0
        self.performance = 0
        self.__compute_performance()
    
    def __compute_performance(self):
        val =  1/(1 + np.exp(-self.x))
        val += 0.5
        val *= self.pbounds[1] - self.pbounds[0]
        val += self.pbounds[0]
        self.performance = val
        
    def improve(self):
        self.x += 1
        self.__compute_performance()
    
    def get_performance(self):
        return self.performance
        
        
class CompanyAgent(Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id: int, model: Model, x, y):
        super().__init__(unique_id, model)
        self.capital = 100
        self.product = CompanyProduct()
        self.ncustomers = 0
        self.position = (x, y)
        self.strategy = BasicStrategy()
        resources_spent_per_step = 0
        self.innovation_cost = self.strategy.innovation_factor * resources_spent_per_step
        self.exploitation_cost = (1-self.strategy.innovation_factor) * resources_spent_per_step

    # Next actions based on the model context
    def step(self):
        pass

    def compute_profit(self):
        val = self.product.performance * self.ncustomers
        return val

    def check_empty_cell():
        pass
    
    def explore():
        pass

    def exploit():
        pass

    def get_pos():
        pass

    def get_proximity(pos: Tuple):
        pass