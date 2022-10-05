from src.models.market import MarketModel
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import json
import os
import time

DATA_PATH = "data"

marketModel = MarketModel(gamma=0.9, alpha=0.5, innovation_time=10)

while marketModel.running:
    marketModel.step()

companies_left = marketModel.get_companies()
data = marketModel.raw_data

for company in companies_left:
    data.append(company.data)

for x in data:
    capital = x['Capital']
    steps = list(range(len(capital)))
    plt.plot(steps, capital, color=x['Color'])
    for i, n_p in enumerate(x["New Product"]):
        if n_p:
            plt.plot(steps[i],capital[i], marker='o', color='black') 

plt.xlabel("Time Step")
plt.ylabel("Agent Capital")

red = mpatches.Patch(color='indianred', label='Exploiter Agent')
blue = mpatches.Patch(color='royalblue', label='Innovator Agent')
green = mpatches.Patch(color='mediumseagreen', label='Balanced Agent')
product = Line2D([0], [0], marker='o', markerfacecolor='black', color='white', label='New Product Emerged')
plt.legend(handles=[red, green, blue, product])

fig_name = "fig_" + str(time.time())
plt.savefig(os.path.join(DATA_PATH, fig_name + ".pdf"))
with open(os.path.join(DATA_PATH, fig_name + ".json"), 'w') as out:
    json.dump(data, out)

plt.show()