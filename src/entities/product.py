import numpy as np


class Product:

	def __init__(self, pbounds=[0, 1], gain_on_product=100) -> None:
		self.pbounds = pbounds
		self.x = 0
		self.performance = 0
		self.__compute_performance()
		self.gain_on_product = gain_on_product

	def __compute_performance(self):
		val = 1 / (1 + np.exp(-self.x - 0.5))
		val *= self.pbounds[1] - self.pbounds[0]
		val += self.pbounds[0]
		self.performance = val

	def improve(self, exploitation_factor):
		self.x += exploitation_factor
		self.__compute_performance()

	def get_performance(self):
		return self.performance

	def get_min(self):
		return self.pbounds[1] / 2
