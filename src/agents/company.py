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
				 color: str,
				 innovation_factor: float = 0.8,
				 rd_quality: float = 1.0):
		super().__init__(unique_id, model, position)

		self.capital = random.randint(100, 10000)
		self.gamma = 0.4
		self.budget = self.gamma * self.capital
		self.product = Product()
		self.color = color

		self.innovation_factor = innovation_factor
		self.exploitation_factor = 1 - self.innovation_factor

		self.total_innovation = 0
		self.rd_quality = rd_quality
		self.t = 0
		self.max_innovate_time = 5
		self.n_customers = 1 # prevent immediate removal

	def get_color(self):
		return self.color

	def __innovate(self):
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

	def __exploit(self):
		self.product.improve(self.exploitation_factor)
		exploitation_cost = self.budget * self.exploitation_factor
		self.capital -= exploitation_cost

	def __life_check(self):
		if self.n_customers <= 0:
			self.model.remove_company_agent(self.unique_id)
		self.n_customers = 0

	def __allocate_budget(self):
		self.budget = self.gamma * self.capital

	def step(self):
		self.__innovate()
		self.__exploit()
		self.__life_check()
		self.__allocate_budget()

		print(self.capital, self.innovation_factor)
	
	def buy(self):
		self.capital += self.product.gain_on_product
		self.n_customers += 1
