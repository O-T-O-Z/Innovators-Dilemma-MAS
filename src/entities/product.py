import numpy as np
import random

class Product:

	def __init__(self, pbounds=[0, 1], gain_on_product=100, innovation_time=1) -> None:
		self.pbounds = pbounds
		self.x = -0.5
		self.performance = 0
		self.gain_on_product = gain_on_product
		self.innovation_time = innovation_time
		self.__compute_performance()

	def __compute_performance(self):
		x = self.x / self.innovation_time
		val = 1 / (1 + np.exp(-x))
		val *= self.pbounds[1] - self.pbounds[0]
		val += self.pbounds[0]
		self.performance = val

	def improve(self, exploitation_factor):
		self.x += exploitation_factor * random.random()
		self.__compute_performance()

	def get_performance(self):
		return self.performance

	def get_min(self):
		return self.pbounds[1] / 2
