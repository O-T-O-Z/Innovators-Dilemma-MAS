from typing import Tuple
from src.agents.company import CompanyAgent
from mesa import Model
from typing import Tuple

class Whale(CompanyAgent):
	"""
	Will form allies with other companies, thus earn less but innovate more.
	"""
	def __init__(self, unique_id: int, model: Model, position: Tuple) -> None:
		super().__init__(unique_id, model, position, innovation_factor=0.2, rd_quality=0.5)

	def execute(self):
		pass
