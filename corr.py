data = [((0.3, 1, 0.25), {'innovator': 8, 'exploiter': 16, 'balanced': 26}), ((0.3, 1, 0.5), {'innovator': 3, 'exploiter': 25, 'balanced': 22}), ((0.3, 1, 0.75), {'innovator': 0, 'exploiter': 39, 'balanced': 5}), ((0.3, 3, 0.25), {'innovator': 15, 'exploiter': 10, 'balanced': 25}), ((0.3, 3, 0.5), {'innovator': 11, 'exploiter': 5, 'balanced': 34}), ((0.3, 3, 0.75), {'innovator': 10, 'exploiter': 18, 'balanced': 22}), ((0.3, 5, 0.25), {'innovator': 19, 'exploiter': 8, 'balanced': 23}), ((0.3, 5, 0.5), {'innovator': 20, 'exploiter': 6, 'balanced': 24}), ((0.3, 5, 0.75), {'innovator': 19, 'exploiter': 8, 'balanced': 23}), ((0.3, 10, 0.25), {'innovator': 20, 'exploiter': 6, 'balanced': 24}), ((0.3, 10, 0.5), {'innovator': 18, 'exploiter': 4, 'balanced': 28}), ((0.3, 10, 0.75), {'innovator': 21, 'exploiter': 8, 'balanced': 21}), ((0.6, 1, 0.25), {'innovator': 16, 'exploiter': 10, 'balanced': 24}), ((0.6, 1, 0.5), {'innovator': 7, 'exploiter': 21, 'balanced': 22}), ((0.6, 1, 0.75), {'innovator': 8, 'exploiter': 30, 'balanced': 12}), ((0.6, 3, 0.25), {'innovator': 27, 'exploiter': 7, 'balanced': 16}), ((0.6, 3, 0.5), {'innovator': 21, 'exploiter': 10, 'balanced': 19}), ((0.6, 3, 0.75), {'innovator': 15, 'exploiter': 19, 'balanced': 16}), ((0.6, 5, 0.25), {'innovator': 12, 'exploiter': 11, 'balanced': 27}), ((0.6, 5, 0.5), {'innovator': 15, 'exploiter': 8, 'balanced': 27}), ((0.6, 5, 0.75), {'innovator': 12, 'exploiter': 16, 'balanced': 22}), ((0.6, 10, 0.25), {'innovator': 5, 'exploiter': 22, 'balanced': 23}), ((0.6, 10, 0.5), {'innovator': 14, 'exploiter': 8, 'balanced': 28}), ((0.6, 10, 0.75), {'innovator': 16, 'exploiter': 10, 'balanced': 24}), ((0.9, 1, 0.25), {'innovator': 17, 'exploiter': 6, 'balanced': 27}), ((0.9, 1, 0.5), {'innovator': 15, 'exploiter': 17, 'balanced': 18}), ((0.9, 1, 0.75), {'innovator': 15, 'exploiter': 24, 'balanced': 11}), ((0.9, 3, 0.25), {'innovator': 16, 'exploiter': 19, 'balanced': 15}), ((0.9, 3, 0.5), {'innovator': 9, 'exploiter': 17, 'balanced': 24}), ((0.9, 3, 0.75), {'innovator': 11, 'exploiter': 20, 'balanced': 19}), ((0.9, 5, 0.25), {'innovator': 1, 'exploiter': 37, 'balanced': 12}), ((0.9, 5, 0.5), {'innovator': 4, 'exploiter': 27, 'balanced': 19}), ((0.9, 5, 0.75), {'innovator': 6, 'exploiter': 21, 'balanced': 23}), ((0.9, 10, 0.25), {'innovator': 0, 'exploiter': 41, 'balanced': 9}), ((0.9, 10, 0.5), {'innovator': 4, 'exploiter': 28, 'balanced': 18}), ((0.9, 10, 0.75), {'innovator': 4, 'exploiter': 24, 'balanced': 22})]

from scipy.stats import pearsonr
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

innovation_time = [1, 3, 5, 10]
alpha = [0.25, 0.5, 0.75]
gamma = [0.3, 0.6, 0.9]

names = ['innovator', 'exploiter', 'balanced']
parameters = [gamma, innovation_time, alpha]

hm = np.zeros((3, 3))

for j, param in enumerate(parameters): 
    for i, n in enumerate(names):
        arr = []
        for p in param:
            for comb, val in data:
                if p == comb[j]:
                    arr.append([val[n], p])
        arr = np.array(arr)
        corr = pearsonr(arr[:,0], arr[:,1])[0]
        hm[j][i] = corr

print(hm)
sns.heatmap(hm, annot=True, xticklabels=[x.title() for x in names], 
            yticklabels=["Gamma", "Alpha", "Innovation Time"], 
            annot_kws={"fontsize":14}, cbar_kws={'label': 'Pearson Correlation'})
plt.savefig("corr.pdf")
plt.show()
