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

		r = lambda: random.randint(0, 255)
		self.color = "#%02X%02X%02X" % (r(), r(), r())

	def get_color(self):
		return self.color

	def innovate(self):
		innovation_cost = self.budget * self.strategy.innovation_factor
		self.capital -= innovation_cost

	def exploit(self):
		self.product.improve(self.strategy.exploitation_factor)
		exploitation_cost = self.budget * self.strategy.exploitation_factor
		self.capital -= exploitation_cost

	def kill(self):
		self.model.remove_company_agent(self.unique_id)

	def allocate_budget(self):
		self.budget = self.gamma * self.capital

	# Next actions based on the model context
	def step(self):
		self.innovate()
		self.exploit()
		self.strategy.execute()
		# Check if company died
		if self.capital <= 0:
			self.kill()
		self.allocate_budget()

	def set_strategy(self, strategy: BasicStrategy):
		self.strategy = strategy

	def buy(self):
		self.capital += self.product.gain_on_product
