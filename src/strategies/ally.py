from src.strategies.basic import BasicStrategy


class AllianceStrategy(BasicStrategy):
	"""
	Will form allies with other companies, thus earn less but innovate more.
	"""
	def __init__(self, company) -> None:
		super().__init__(company, innovation_factor=0.9, rd_quality=1)

	def execute(self):
		pass