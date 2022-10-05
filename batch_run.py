from ast import arg
from src.models.market import MarketModel
from tqdm import tqdm
from argparse import ArgumentParser, Namespace
from typing import List
import json

def dump_data(data: List[dict], args: Namespace):
    filename = f"{args.alpha}-alpha.json"
    with open(filename, 'w') as out:
        json.dump(data, out)

def main():
    parser = ArgumentParser(description='Experiment details.')
    parser.add_argument('num_runs', type=int, default=100, nargs='?',
                        help='the number of runs to perform')
    parser.add_argument('--gamma', type=float, default=0.9, nargs='?',
                        help='portion of capital to allocate to the budget [0,1]')
    parser.add_argument('--alpha', type=float, default=0.5, nargs='?',
                        help='importance of proximity [0,1]')
    parser.add_argument('--innovation_time', type=int, default=5, nargs='?',
                        help='time steps until innovation might occur')

    args = parser.parse_args()
    assert args.gamma < 1 and args.gamma >= 0, "Gamma should be in [0,1]!"
    assert args.alpha <= 1 and args.alpha >= 0, "Alpha should be in [0,1]!"

    data = []
    for i in tqdm(range(args.num_runs)):
        marketModel = MarketModel(args.gamma, args.innovation_time, args.alpha)
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
    dump_data(data, args)


if __name__ == "__main__":
    main()

# innovation time {1,3,5}
# alpha (proximity) {0.25,0.5,0.75}
# gamma {0.3, 0.6, 0.9}
