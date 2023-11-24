import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby, count
from matplotlib import ticker

# plots the graph for the minimum distances between any 2 peptides in the system at each timestep
# output for 3 peptide system was three lines representing min dist of all 3C2 combinations
peptide_a = 1
peptide_b = 2
peptide_c = 3

x, y, a, b, c, d = [], [], [], [], [], []

# define ouor threshold below which bonding takes place'
thresh = 8

# open all of the minimum dists found from simulation for each peptide pair in system
with open("real_min_p1_p2_ni01.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))

with open("real_min_p1_p3_ni01.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            a.append(float(cols[0]))
            b.append(float(cols[1]))

with open("real_min_p2_p3_ni01.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            c.append(float(cols[0]))
            d.append(float(cols[1]))

# normalising the units => making distance to nanometres
# x,y is p1-p2, a,b is p1-p3 and c,d is p2-p3
l = [i * 0.001 for i in x]
j = [round(i) for i in l]
h = []

# create the tuple for our nm dists and time steps
lst = zip(j,y)
print(l)

# post inspecting graph can find points where between a 2 different times the distance was below the threshold for binding
# this period subsequently analysed
lower_bound = 520
upper_bound = 540
for item in lst:
    if lower_bound < float(item[0]) < upper_bound:
        h.append(float(item[1]))

# find the average, minimum and maximum distance across the defined binding time
print(sum(h)/len(h))
print(min(h))
print(max(h))

# plot the graph with 3C2 lines of minimum dists between peptide pairs
def graph():
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    #ax1.set_title("Trimer system".format(a=peptide_a, b=peptide_b), fontsize=16)
    ax1.set_xlabel('t (ns)', fontsize=12)
    ax1.set_ylabel("$d_\mathrm{min}$ ($\AA$)", fontsize=12)
    ax1.plot(l, y, c='tab:red', linewidth=1, label="N1 - N2")
    ax1.plot(l, b, c='tab:green', linewidth=1, label="N1 - N3")
    ax1.plot(l, d, c='tab:blue', linewidth=1, label="N2 - N3")
    # plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    # ax1.xaxis.major.formatter._useMathText = True

    plt.hlines(y=thresh, xmin=0, xmax=max(x), color='k', linestyle='--', zorder=3,
               label="$d_{\mathrm{dimer}}$ = %d $\AA$"%thresh) # = %.1f $\AA$" % round(thresh)
    # box = ax1.get_position()
    # ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax1.legend(frameon=True, loc='upper left') #, bbox_to_anchor=(1, 0.5)
    for axis in [ax1.yaxis]:
        axis.set_major_locator(ticker.MaxNLocator(prune='lower', integer=True))
    plt.xlim(l[0], l[-1])
    plt.ylim(0, 80)
    fig.savefig("NI01 trimer thresh={c}A.pdf".format(a=peptide_a, b=peptide_b, c=thresh), bbox_inches='tight')
    plt.show()


graph()

input('Press ENTER to exit')
