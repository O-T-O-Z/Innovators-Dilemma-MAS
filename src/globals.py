import mesa
import itertools
from src.agents.company_type import CompanyType

sliders = {
    "alpha": mesa.visualization.Slider("Proximity (alpha) Decision Factor", min_value=0, max_value=1, step=0.1, value=0.5),
    "gamma": mesa.visualization.Slider("Budget Allocation", min_value=0, max_value=0.9, step=0.1, value=0.9),
    "max_patience": mesa.visualization.Slider("Max Patience", min_value=1, max_value=20, step=1, value=5)
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
NUM_CUSTOMERS = 2485

WIDTH = 50
HEIGHT = 50
