from src.models.market import MarketModel
from src.agents.company_type import CompanyType
import itertools
from tqdm import tqdm
from multiprocessing import Pool
import pickle
import time

DATA_PATH = "data"
NUM_RUNS = 50

# def dump_data(data, name):
#     filename = os.join(DATA_PATH, str(args.innovation_time) + "-innovation_time.json")
#     with open(filename, 'w') as out:
#         json.dump(data, out)

def count(data):
    df = {'innovator': 0, 'exploiter': 0, 'balanced': 0}
    for d in data:
        if d == CompanyType.INNOVATOR.value:
            df["innovator"] += 1
        elif d == CompanyType.BALANCED.value:
            df["balanced"] += 1
        elif d == CompanyType.EXPLOITER.value:
            df["exploiter"] += 1
    return df


innovation_time = [1, 3, 5, 10]
alpha = [0.25, 0.5, 0.75]
gamma = [0.3, 0.6, 0.9]

raw_data = []

def run_exp(comb):
    exp = []
    for i in tqdm(range(NUM_RUNS)):
        marketModel = MarketModel(*comb)
        num_iters = 0
        stopped = False
        while marketModel.running == True:
            marketModel.step()
            num_iters += 1
            if num_iters > 5000:
                stopped = True
                break
        if stopped:
            print(comb, "was stopped")
            continue
        companies_left = marketModel.get_companies()

        exp.append(companies_left[0].type.value)
    val = (comb, count(exp))
    print(val)
    return val

def test(comb):
    run_exp(comb)

all_combs = itertools.product(gamma, innovation_time, alpha)
# for comb in all_combs:
#     run_exp(comb)


pool = Pool(14)
raw_data = pool.map(run_exp, all_combs)

print(raw_data)

with open("raw_data2", "wb") as f:
    pickle.dump(raw_data, f)

# with open("raw_data2", "rb") as f:
#     arr = pickle.load(f)
     