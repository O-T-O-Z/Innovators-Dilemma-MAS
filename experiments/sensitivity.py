from src.models.market import MarketModel
from src.agents.company_type import CompanyType
import itertools
from tqdm import tqdm
from multiprocessing import Pool
import pickle
import time

DATA_PATH = "data"
NUM_RUNS = 50

def count(data):
    df = {'F0': 0, 'F1': 0, 'F2': 0, 'F3': 0, 'F4': 0, 'F5': 0, 'F6': 0, 'F7': 0, 'F8': 0, 'F9': 0, 'F10': 0}
    for d in data:
        if d == CompanyType.F0.value:
            df["F0"] += 1
        elif d == CompanyType.F1.value:
            df["F1"] += 1
        elif d == CompanyType.F2.value:
            df["F2"] += 1
        elif d == CompanyType.F3.value:
            df["F3"] += 1
        elif d == CompanyType.F4.value:
            df["F4"] += 1
        elif d == CompanyType.F5.value:
            df["F5"] += 1
        elif d == CompanyType.F6.value:
            df["F6"] += 1
        elif d == CompanyType.F7.value:
            df["F7"] += 1
        elif d == CompanyType.F8.value:
            df["F8"] += 1
        elif d == CompanyType.F9.value:
            df["F9"] += 1
        elif d == CompanyType.F10.value:
            df["F10"] += 1
    return df


max_patience = [10, 20, 50]
alpha = [0, 0.5, 1]
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

all_combs = itertools.product(gamma, max_patience, alpha)


pool = Pool(None)
raw_data = pool.map(run_exp, all_combs)

print(raw_data)

with open("raw_data2", "wb") as f:
    pickle.dump(raw_data, f)
