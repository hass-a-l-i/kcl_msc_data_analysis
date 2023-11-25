import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
import pandas as pd
import seaborn as sns


x, y = [], []

with open("contacts_test_10A.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))

maxim = max(y)
change = [1 if x == 0 else x for x in y]
frac = [float(i / maxim) for i in change]
"""
fig = plt.figure()
plt.style.use('seaborn-whitegrid')
ax1 = fig.add_subplot(111)
ax1.set_title("P2 ALA -- P3 ALA")
ax1.set_xlabel('frame')
ax1.set_ylabel('frac contacts')
ax1.plot(x, frac, c='r', linewidth=1, label='the data')
# for axis in [ax1.yaxis]:
# axis.set_major_locator(ticker.MaxNLocator(prune='lower', integer=True))
# plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()


T = 298
k_b = 1.38 * (10 ** (-23))
r = len(x)
z = [-k_b * T * np.log(i) for i in frac]

X, Y = np.meshgrid(r, r)
Z = np.reshape(z, (r, r))
plt.pcolormesh(x, y, z)

plt.show()
"""

T = 298
k_b = 1.38 * (10 ** (-23))
l = [round(i) for i in x]
z = [-k_b * T * np.log(i) for i in frac]
data = pd.DataFrame(data={'frac contacts': frac, 'time': l, 'F': z})
data = data.pivot(index='frac contacts', columns='time', values='F')
print(data)
sns.set(font_scale=1.2)
ax = sns.heatmap(data, cmap='plasma', cbar_kws={'label': 'Free E'}, annot_kws={"fontsize":14}, vmax=max(z), vmin=min(z))
ax.invert_yaxis()
plt.show()
print(z[-1], frac[-1])
print(min(z), max(z))