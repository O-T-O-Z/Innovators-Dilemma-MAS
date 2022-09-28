from src.strategies.basic import BasicStrategy


class WhaleStrategy(BasicStrategy):
	"""
	Will buy companies to advance innovation, rather than innovating themselves. Should exploit in the meantime.
	"""

	def __init__(self, company) -> None:
		super().__init__(company, innovation_factor=0.2, rd_quality=0.5)

	def execute(self):
		pass