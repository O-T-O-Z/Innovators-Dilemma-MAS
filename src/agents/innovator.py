from typing import Tuple
from src.agents.company import CompanyAgent
from mesa import Model
from typing import Tuple

class Innovator(CompanyAgent):
	"""
	Will form allies with other companies, thus earn less but innovate more.
	"""
	def __init__(self, unique_id: int, model: Model, position: Tuple) -> None:
		super().__init__(unique_id, model, position, innovation_factor=0.9, rd_quality=1)

	def execute(self):
		pass

