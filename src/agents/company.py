from mesa import Model
import random
from src.agents.grid_agent import GridAgent
from src.entities.product import Product
from typing import Tuple


class CompanyAgent(GridAgent):

	def __init__(self,
	             unique_id: int,
	             model: Model,
	             position: Tuple,
				 innovation_factor: float = 0.8,
				 rd_quality: float = 1.0):
		super().__init__(unique_id, model, position)

		self.capital = random.randint(100, 10000)
		self.gamma = 0.4
		self.budget = self.gamma * self.capital
		self.product = Product()

		r = lambda: random.randint(0, 255)
		self.color = "#%02X%02X%02X" % (r(), r(), r())

		self.innovation_factor = innovation_factor
		self.exploitation_factor = 1 - self.innovation_factor

		self.total_innovation = 0
		self.rd_quality = rd_quality
		self.t = 0
		self.max_innovate_time = 10

	def get_color(self):
		return self.color

	def innovate(self):
		self.total_innovation += self.innovation_factor * self.rd_quality
		self.t += 1
		innovation_cost = self.budget * self.innovation_factor
		self.capital -= innovation_cost

		if self.t == self.max_innovate_time:
			prob = self.total_innovation / self.t
			if prob > random.random():
				lower_bound = self.product.get_min()
				upper_bound = lower_bound + (random.random())
				self.product = Product((lower_bound, upper_bound)) # needs new bounds
			# reset
			self.t = 0
			self.total_innovation = 0

	def exploit(self):
		self.product.improve(self.exploitation_factor)
		exploitation_cost = self.budget * self.exploitation_factor
		self.capital -= exploitation_cost

	def kill(self):
		self.model.remove_company_agent(self.unique_id)

	def allocate_budget(self):
		self.budget = self.gamma * self.capital

	# Next actions based on the model context
	def step(self):
		self.innovate()
		self.exploit()
		# Check if company died
		if self.capital <= 0:
			self.kill()
		self.allocate_budget()
		print(self.capital, self.innovation_factor)
	
	def buy(self):
		self.capital += self.product.gain_on_product
