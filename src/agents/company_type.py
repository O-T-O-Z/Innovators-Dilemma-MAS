from enum import Enum

class CompanyType(str, Enum):
	INNOVATOR = "average innovator capital"
	EXPLOITER = "average exploiter capital"
	BALANCED = "average balanced capital"