import matplotlib.pyplot as plt
from matplotlib import ticker

x, y = [], []

with open("area_trimer.xvg") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))


fig = plt.figure()
plt.style.use('seaborn-whitegrid')
ax1 = fig.add_subplot(111)
ax1.set_title("")
ax1.set_xlabel('time (ns)')
ax1.set_ylabel('area $(nm/S2/N)$')
l = [i * 0.001 for i in x]
ax1.plot(l,y, c='r',  linewidth=1, label='the data')
for axis in [ax1.yaxis]:
    axis.set_major_locator(ticker.MaxNLocator(prune='lower', integer=True))
#plt.xlim(0, 100000)
#plt.ylim(99, 120)
plt.show()