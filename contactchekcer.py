import matplotlib.pyplot as plt
from matplotlib import ticker
#import sys

#orig_stdout = sys.stdout
#f = open('og.txt', 'a')
#sys.stdout = f
with open("hydrop2TRP+p3TRP_at8A.txt") as f:
    x, y = [], []
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))
s = []
ones = []
twos = []
threes = []
abovethrees = []
for i in y:
    if i > 0:
        s.append(i)
    if i == 1:
        ones.append(i)
    if i == 2:
        twos.append(i)
    if i == 3:
        threes.append(i)
    if i > 3:
        abovethrees.append(i)

#print("frac frames in contact =", (len(s) / len(y)))
#print("max no. contacts in single frame =", max(s))

#sys.stdout = orig_stdout
#f.close()

"""
x, y = [], []

p = ["ALA", "GLY"]

with open("hydrophobic_contacts_p2PHE+p3PHE_10A.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))
"""

#print("frac frames in contact =", (len(s) / len(y)))
#print("max no. contacts in single frame =", max(s))
av = sum(y) / len(y)
print("av. no contacts OVER TIME=", round(av))
av2 = sum(s)/len(s)
print("av no contacts within bound =", round(av2))


print("total frame no. =", len(y))
print("no. frames in contact =", len(s))
print("no. of frames with one contact =", len(ones))
print("no. of frames with two contacts =", len(twos))
print("no. of frames with three contacts =", len(threes))
print("no. of frames with more than three contacts =", len(abovethrees))
print("max no. contacts in single frame =", max(s))

r = max(y,key=y.count)
print("most stable no of contacts =", r)
print("frac frames in contact =", len(s)/len(y))


"""
fig = plt.figure()
plt.style.use('seaborn-whitegrid')
ax1 = fig.add_subplot(111)
ax1.set_title("")
ax1.set_xlabel('frame')
ax1.set_ylabel('contacts #')
l = [i * 0.001 for i in x]
ax1.plot(l, y, c='r', linewidth=1, label='the data')
for axis in [ax1.yaxis]:
    axis.set_major_locator(ticker.MaxNLocator(prune='lower', integer=True))
# plt.xlim(0, 100000)
# plt.ylim(99, 120)
plt.show()
"""