from src.models.market import MarketModel
from tqdm import tqdm
from argparse import ArgumentParser, Namespace
from typing import List
import json
import os
from multiprocessing import freeze_support, Pool

DATA_PATH = "data_new"
args = None

def dump_data(data: List[dict], args: Namespace):
    filename = os.path.join(DATA_PATH, str(args.alpha) + "-alpha.json")
    with open(filename, 'w') as out:
        json.dump(data, out)

def run_model(inte):
    marketModel = MarketModel(0.9, 50, 0)
    num_iters = 0
    while marketModel.running == True:
        marketModel.step()
        num_iters += 1
    companies_left = marketModel.get_companies()
    return [
        {"num_iterations": num_iters,
        "winning_class": companies_left[0].type.value,
        "agents_left": len(companies_left)}
    ]


def main():
    parser = ArgumentParser(description='Experiment details.')
    parser.add_argument('num_runs', type=int, default=100, nargs='?',
                        help='the number of runs to perform')
    parser.add_argument('--gamma', type=float, default=0.9, nargs='?',
                        help='portion of capital to allocate to the budget [0,1]')
    parser.add_argument('--alpha', type=float, default=0.5, nargs='?',
                        help='importance of proximity [0,1]')
    parser.add_argument('--max_patience', type=int, default=50, nargs='?',
                        help='time steps until the product is given up')

    global args 
    args = parser.parse_args()
    assert args.gamma < 1 and args.gamma >= 0, "Gamma should be in [0,1]!"
    assert args.alpha <= 1 and args.alpha >= 0, "Alpha should be in [0,1]!"

    results = []
    print(args)

    with tqdm(range(args.num_runs)) as pbar:
        with Pool(None) as p:
            for data in p.imap_unordered(run_model, range(args.num_runs)):
                results.extend(data)
                pbar.update()
    
    dump_data(results, args)


if __name__ == "__main__":
    freeze_support()
    main()

# alpha (proximity) {0,0.25,0.5,0.75,1}
# gamma {0.3, 0.6, 0.9}
# max_patience {10, 25, 50, 75}
