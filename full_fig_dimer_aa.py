import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(2, 4)
gs.update(wspace=0.5)

x, y = [], []

with open("new_min_1_2_trimer.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))

both = zip(x, y)

a, b = [], []

with open("new_min_1_3_trimer.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            a.append(float(cols[0]))
            b.append(float(cols[1]))

both1 = zip(a, b)

c, d = [], []

with open("new_min_2_3_trimer.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            c.append(float(cols[0]))
            d.append(float(cols[1]))

both = zip(c, d)

thresh = 10

line_width = 1

plt.style.use('seaborn-whitegrid')

fig = plt.figure()
ax1 = plt.subplot(gs[0, :2], )
plt.plot(x, y, 'c', linewidth=line_width)
plt.xlabel('time (ps)')
plt.ylabel('Minimum distance between P1 and P2 ($\AA$)')
plt.xlim(x[0], x[-1])
plt.ylim(0, 60)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
ax1.xaxis.major.formatter._useMathText = True
plt.hlines(y=thresh, xmin=0, xmax=max(x), color='black', linestyle='--', zorder=3)

ax2 = plt.subplot(gs[0, 2:])
plt.plot(a, b, 'c', linewidth=line_width)
plt.xlabel('time (ps)')
plt.ylabel('Minimum distance between P1 and P3 ($\AA$)')
plt.xlim(x[0], x[-1])
plt.ylim(0, 60)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
ax2.xaxis.major.formatter._useMathText = True
plt.hlines(y=thresh, xmin=0, xmax=max(x), color='black', linestyle='--', zorder=3)


ax3 = plt.subplot(gs[1, 1:3])
plt.plot(c, d, 'c', linewidth=line_width)
plt.xlabel('time (ps)')
plt.ylabel('Minimum distance between P2 and P3 ($\AA$)')
plt.xlim(x[0], x[-1])
plt.ylim(0, 60)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
ax3.xaxis.major.formatter._useMathText = True
plt.hlines(y=thresh, xmin=0, xmax=max(x), color='black', linestyle='--', zorder=3)

plt.show()

# plt.savefig("P{a}-P{b} trimer thresh={c}A.pdf".format(a=peptide_a, b=peptide_b, c=thresh), bbox_inches='tight')
