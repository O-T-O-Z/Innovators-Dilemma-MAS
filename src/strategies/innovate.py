from src.strategies.basic import BasicStrategy


class InnovateStrategy(BasicStrategy):
	"""
	Should focus on innovation.
	"""
	def __init__(self) -> None:
		super().__init__(innovation_factor=0.9, rd_quality=1)

	def execute(self):
		pass
