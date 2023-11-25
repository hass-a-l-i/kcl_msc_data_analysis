import matplotlib.pyplot as plt
from matplotlib import ticker

# find the radius of gyration of each peptide in the system
x, y, a, b, c, d = [], [], [], [], [], []

# opening all files with radius of gyration output for each peptide and plotting on single graph
thresh = 8

with open("rgyr_s1.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))

with open("rgyr_s2.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            a.append(float(cols[0]))
            b.append(float(cols[1]))

with open("rgyr_s3.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            c.append(float(cols[0]))
            d.append(float(cols[1]))

x = [round(i) for i in x]
print("timeframe =", x[-1] - x[0])
print(sum(y)/len(y))
print(max(y))

plt.style.use('seaborn-whitegrid')
fig = plt.gcf()
ax1 = fig.add_subplot(111)
# ax1.set_title("Dimer system : P{a} and P{b} aggregation (all atom)".format(a=peptide_a, b=peptide_b))
ax1.set_xlabel('t (ns)', fontsize=12)
ax1.set_ylabel("$R_g$ ($\AA$)", fontsize=12)
l = [i * 0.001 for i in x]
ax1.plot(l, y, c='tab:blue', linewidth=1, label="S1")
ax1.plot(l, b, c='tab:red', linewidth=1, label="S2")
ax1.plot(l, d, c='tab:green', linewidth=1, label="S3")

print("s1 av =", sum(y)/len(y))
print("s2 av =", sum(b)/len(b))
print("s3 av =", sum(d)/len(d))

for axis in [ax1.yaxis]:
    axis.set_major_locator(ticker.MaxNLocator(prune='lower', integer=True))

#plt.hlines(y=thresh, xmin=0, xmax=max(x), color='black', linestyle='--', zorder=3,
           #label="Bonding Threshold of %.1f $\AA$" % thresh)
#box = ax1.get_position()
#ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
# ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlim(l[0], l[-1])
plt.ylim(9, 15)
plt.legend(loc="upper left", frameon=True)
#plt.ylim(9.68, 10.32)
#plt.ylim(8, 12)
plt.savefig("rgyr trimer SA-I.pdf", bbox_inches='tight')
plt.show()
