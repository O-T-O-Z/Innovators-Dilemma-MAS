from src.models.market import MarketModel
import itertools
from src.agents.company_type import CompanyType
from src import globals
from tqdm import tqdm

NUM_RUNS = 1000
company_labels = [
    (0, CompanyType.EXPLOITER, "red"),
    (0.5, CompanyType.BALANCED, "green"),
    (0.7, CompanyType.INNOVATOR, "blue")
]
agents_per_class = 5
company_labels = list(itertools.chain(
    *[[c] * agents_per_class for c in company_labels]))
model_params = {
    "num_customers": globals.NUM_CUSTOMERS,
    "num_companies": globals.NUM_COMPANIES,
    "width": globals.WIDTH,
    "height": globals.HEIGHT,
    "company_labels": company_labels
}

data = []
for i in tqdm(range(NUM_RUNS)):
    marketModel = MarketModel(*model_params.values())
    num_iters = 0
    while marketModel.running == True:
        marketModel.step()
        num_iters += 1
    companies_left = marketModel.get_companies()
    data.append({
        "num_iterations": num_iters,
        "winning_class": companies_left[0].type.value,
        "agents_left": len(companies_left)
    })

df = {'innovator': 0, 'exploiter': 0, 'balanced': 0}
for d in data:
	if d.get('winning_class') == 'innovator':
		df["innovator"] += 1
	elif d.get('winning_class') == 'balanced':
		df["balanced"] += 1
	elif d.get('winning_class') == 'exploiter':
		df["exploiter"] += 1
print(df)