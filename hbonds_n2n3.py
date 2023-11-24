import matplotlib.pyplot as plt
from matplotlib import ticker

x, b = [], []

# no_hbonds_n2n3new.xvg
with open("no_hbonds_n2n3new.xvg") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 3:
            x.append(float(cols[0]))
            b.append(float(cols[1]))
y = [i-3 for i in b]
print(sum(b)/len(b))
n = []
for i in b:
    if i > 0:
        n.append(i)
print(sum(n)/len(n))
l = [i * 0.001 for i in x]
plt.style.use('seaborn-whitegrid')
fig = plt.gcf()
ax1 = fig.add_subplot(111)
# ax1.set_title("Dimer system : P{a} and P{b} aggregation (all atom)".format(a=peptide_a, b=peptide_b))
ax1.set_xlabel('t (ns)', fontsize=14)
ax1.set_ylabel("Number of H-bonds", fontsize=14)
ax1.plot(l, b, c='tab:blue', linewidth=1, label="raw data")
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
#ax1.xaxis.major.formatter._useMathText = True
for axis in [ax1.yaxis]:
    axis.set_major_locator(ticker.MaxNLocator(prune='lower', integer=True))
plt.xlim(l[0], l[-1])
plt.ylim(0, 6)
fig = ax1.get_figure()
#fig.savefig('hbonds_n2n3.pdf')


plt.show()