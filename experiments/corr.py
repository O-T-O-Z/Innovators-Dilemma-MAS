from scipy.stats import spearmanr
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import pickle
import os
from src import globals
import math

path = "~/Downloads/raw_data2"
output_path = "figures"

with open(os.path.expanduser(path), "rb") as f:
    data = pickle.load(f)

max_patience = [10, 20, 50]
alpha = [0, 0.5, 1]
gamma = [0.3, 0.6, 0.9]

names = [x[1].value for x in globals.company_labels]
parameters = [gamma, max_patience, alpha]

corrs = np.zeros((len(parameters), len(names)))
p_vals = np.zeros((len(parameters), len(names)))

for j, param in enumerate(parameters): 
    for i, n in enumerate(names):
        arr = []
        for p in param:
            for comb, val in data:
                if p == comb[j]:
                    arr.append([val[n], p])
        arr = np.array(arr)
        print(arr.shape)
        corr, p_value = spearmanr(arr[:,0], arr[:,1])
        corr = 0 if math.isnan(corr) else corr
        corrs[j][i] = corr
        p_vals[j][i] = p_value

print(p_vals)
plt.figure(figsize=(13,5))
sns.heatmap(corrs, mask=p_vals >= 0.05, annot=True, annot_kws={"fontsize":14}, cbar_kws={'label': 'Spearman Correlation'})

sns.heatmap(corrs, mask=p_vals < 0.05, annot=True, cbar=False,xticklabels=[x.title() for x in names], linewidths=1, linecolor='white',
            cmap=sns.color_palette("Greys", n_colors=1, desat=1), yticklabels=["Gamma", "Max Patience", "Alpha"], 
            annot_kws={"fontsize":14})


plt.xlabel("Company Type", fontsize=12)
plt.ylabel("Parameter", fontsize=12, labelpad=20)
plt.margins(x=0, y=0)
plt.savefig(os.path.join(output_path, "corr.pdf"), bbox_inches="tight")
plt.show()


default = (0.3, 50, 0.5)


for param, arr in data:
    if param == default:
        plt.bar(arr.keys(), arr.values())
        plt.xlabel("Company Type", fontsize=12)
        plt.ylabel("Win Rate Frequency", fontsize=12)
        plt.savefig(os.path.join(output_path, "win_rate.pdf"))
        plt.show()
        break
