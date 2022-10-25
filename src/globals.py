import mesa
import itertools
from src.agents.company_type import CompanyType

sliders = {
    "alpha": mesa.visualization.Slider("Proximity (alpha) Decision Factor", min_value=0, max_value=1, step=0.1, value=0.5),
    "gamma": mesa.visualization.Slider("Budget Allocation", min_value=0, max_value=0.9, step=0.1, value=0.3),
    "max_patience": mesa.visualization.Slider("Max Patience", min_value=10, max_value=100, step=10, value=50)
}


# company_labels = [
#     (0, CompanyType.EXPLOITER, "red"),
#     (0.5, CompanyType.BALANCED, "green"),
#     (0.7, CompanyType.INNOVATOR, "blue")
# ]
company_labels = [
    (0, CompanyType.F0, "red"),
    (0.1, CompanyType.F1, "purple"),
    (0.2, CompanyType.F2, "black"),
    (0.3, CompanyType.F3, "blue"),
    (0.4, CompanyType.F4, "yellow"),
    (0.5, CompanyType.F5, "green"),
    (0.6, CompanyType.F6, "pink"),
    (0.7, CompanyType.F7, "orange"),
    (0.8, CompanyType.F8, "cyan"),
    (0.9, CompanyType.F9, "magenta"),
    (1, CompanyType.F10, "brown"),
]
agents_per_class = 3
COMPANY_LABELS = list(itertools.chain(
    *[[c] * agents_per_class for c in company_labels]))

NUM_COMPANIES = 33
NUM_CUSTOMERS = 9768

WIDTH = 99
HEIGHT = 99
