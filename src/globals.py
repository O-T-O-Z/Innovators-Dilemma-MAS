import mesa
import itertools
from src.agents.company_type import CompanyType

sliders = {
    "proximity_df": mesa.visualization.Slider("Proximity Decision Factor", 20, 1, 50),
    "performance_df": mesa.visualization.Slider("Performance Decision Factor", 20, 1, 50),
    "innovation_factor": mesa.visualization.Slider("Innovation Factor", 0, 0, 100)
}


company_labels = [
    (0, CompanyType.EXPLOITER, "red"),
    (0.5, CompanyType.BALANCED, "green"),
    (0.7, CompanyType.INNOVATOR, "blue")
]
agents_per_class = 5
COMPANY_LABELS = list(itertools.chain(
    *[[c] * agents_per_class for c in company_labels]))

NUM_COMPANIES = 15
NUM_CUSTOMERS = 385

WIDTH = 20
HEIGHT = 20
