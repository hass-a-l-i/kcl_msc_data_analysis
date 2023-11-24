import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby, count

from matplotlib import ticker

peptide_a = 1
peptide_b = 2
peptide_c = 3

x, y, a, b, c, d = [], [], [], [], [], []

thresh = 8

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
l = [i * 0.001 for i in x]
j = [round(i) for i in l]
h = []
lst = zip(j,y)
print(l)
for item in lst:
    if 520 < float(item[0]) < 540:
        h.append(float(item[1]))
print(sum(h)/len(h))
print(min(h))
print(max(h))
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