from mesa import Agent, Model
import random
from src.strategies.basic import BasicStrategy
from src.entities.product import Product
from typing import Tuple
        
        
class CompanyAgent(Agent):

    def __init__(self, unique_id: int, model: Model, position: Tuple):
        super().__init__(unique_id, model)

        self.position = position
        self.capital = random.randint(100, 10000)
        self.gamma = 0.4
        self.budget = self.gamma * self.capital

        self.product = Product()
        self.ncustomers = 0
        
        self.strategy = BasicStrategy()
        self.innovation_factor = random.random()
        

    # Next actions based on the model context
    def step(self):
        innovation_cost = self.budget * self.strategy.innovation_factor
        exploitation_cost = self.budget * (1 - self.strategy.innovation_factor)
        self.capital -= innovation_cost + exploitation_cost
        self.budget = self.gamma * self.capital

    def buy(self):
        self.capital += self.product.gain_on_product
