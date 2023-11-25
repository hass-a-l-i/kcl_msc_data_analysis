import matplotlib.pyplot as plt
from matplotlib import ticker

# checks whether two residues can be classed as in contact within system
with open("hydrop2TRP+p3TRP_at8A.txt") as f:
    x, y = [], []
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))
# number of contact points between atoms within the residues (i.e. with dists below cutoff)
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

# output = various information on contact info for simulation
print("frac frames in contact =", (len(s) / len(y)))
print("max no. contacts in single frame =", max(s))
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
