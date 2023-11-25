import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
import pandas as pd
import seaborn as sns

# finds the fraction of contacts that each atom in the peptide dimer are apart of
# method to find the exact contact points of the peptide 
x, y = [], []

with open("contacts_test_10A.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))

# finding the fraction of contacts for each atom
maxim = max(y)
change = [1 if x == 0 else x for x in y]
frac = [float(i / maxim) for i in change]

# using boltzmann equation to find free energy on the z axis of the heatmap
T = 298
k_b = 1.38 * (10 ** (-23))
l = [round(i) for i in x]
z = [-k_b * T * np.log(i) for i in frac]

# output heatmap
data = pd.DataFrame(data={'frac contacts': frac, 'time': l, 'F': z})
data = data.pivot(index='frac contacts', columns='time', values='F')
print(data)
sns.set(font_scale=1.2)
ax = sns.heatmap(data, cmap='plasma', cbar_kws={'label': 'Free E'}, annot_kws={"fontsize":14}, vmax=max(z), vmin=min(z))
ax.invert_yaxis()
plt.show()
print(z[-1], frac[-1])
print(min(z), max(z))
