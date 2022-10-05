from src.models.market import MarketModel
import itertools
from src.agents.company_type import CompanyType
from src import globals
from tqdm import tqdm

NUM_RUNS = 10
company_labels = [
    (0, CompanyType.EXPLOITER, "red"), 
    (0.5, CompanyType.BALANCED, "green"), 
    (0.7, CompanyType.INNOVATOR, "blue")
]
agents_per_class = 5
company_labels = list(itertools.chain(*[[c] * agents_per_class for c in company_labels]))
model_params = {
    "num_customers": globals.NUM_CUSTOMERS,
    "num_companies": globals.NUM_COMPANIES, 
    "width": globals.WIDTH, 
    "height": globals.HEIGHT,
    "company_labels": company_labels
}

for i in tqdm(range(NUM_RUNS)):
	marketModel = MarketModel(*model_params.values())
	while marketModel.running == True:
		marketModel.step()
