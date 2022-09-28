from mesa import Agent, Model
import random
from src.strategies.basic import BasicStrategy
from src.entities.product import Product
from typing import Tuple
        
        
class CompanyAgent(Agent):

    def __init__(self, 
        unique_id: int, 
        model: Model, 
        position: Tuple,
        strategy: BasicStrategy):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.model = model

        self.position = position
        self.capital = random.randint(100, 10000)
        self.gamma = 0.4
        self.budget = self.gamma * self.capital
        self.product = Product()
        self.ncustomers = 0
        
        self.strategy = strategy
        self.innovation_factor = random.random()
        
        r = lambda: random.randint(0,255)
        self.color = "#%02X%02X%02X" % (r(),r(),r())
    
    def get_color(self):
        return self.color

    # Next actions based on the model context
    def step(self):
        innovation_cost = self.budget * self.strategy.innovation_factor
        exploitation_cost = self.budget * (1 - self.strategy.innovation_factor)
        self.capital -= innovation_cost + exploitation_cost
        self.budget = self.gamma * self.capital
        
        self.product.improve(1 - self.strategy.innovation_factor)
        if self.capital <= 0:
            self.model.remove_company_agent(self.unique_id)
        self.strategy.execute()

    def buy(self):
        self.capital += self.product.gain_on_product
