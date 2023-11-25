import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

x, y, z = [], [], []

with open("new_correlation_10A.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))
x = sorted(x)
y = sorted(y)
plt.style.use('seaborn-whitegrid')
fig = plt.gcf()
ax1 = fig.add_subplot(111)
# ax1.set_title("Dimer system : P{a} and P{b} aggregation (all atom)".format(a=peptide_a, b=peptide_b))
ax1.set_xlabel('Percentage of $T^{\mathrm{N2, N3}}_{\mathrm{dimer}}$ in contact (%)', fontsize=12)
ax1.set_ylabel("Average number of contacts", fontsize=12)
x = np. array(x)
y = np. array(y)
d = [i/0.67 for i in x]
e = [i * 100 for i in d]
print(d)
print(e)
a = e[:-2]
b = y[:-2]
c = e[-3:]
d = y[-3:]
#m, b = np. polyfit(x, y, 1)
plt. plot(a, b, 'o', color="tab:blue", label="Bound < 90% of $T^{\mathrm{N2, N3}}_{\mathrm{dimer}}$")
plt. plot(c, d, 'o', color="tab:red", label="Bound > 90% of $T^{\mathrm{N2, N3}}_{\mathrm{dimer}}$")
plt.legend(loc="upper left", frameon=True)
#plt.xlim(0, 70)
#plt.ylim(0, 1.3)
for axis in [ax1.xaxis]:
    axis.set_major_locator(ticker.MaxNLocator(prune='lower'))
fig.savefig("correlation.pdf", bbox_inches='tight')
plt.show()