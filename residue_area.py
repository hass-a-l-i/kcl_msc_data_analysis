import matplotlib.pyplot as plt
from matplotlib import ticker

# used to find the average solvent exposed surface area of each residue within the trimer system
# used to identify buried residues to elucidate the structure of NI01 in solution
x, y, z = [], [], []

# output residue area from gromacs
with open("resarea.xvg") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 3:
            x.append(float(cols[0]))
            y.append(float(cols[1]))
            z.append(float(cols[2]))

# 48 residues in each peptide 
thresh = .5
p1_x = x[0:48]
p1_y = y[0:48]
p1_z = z[0:48]
p2_x = x[48:96]
p2_y = y[48:96]
p2_z = z[48:96]
p3_x = x[96:144]
p3_y = y[96:144]
p3_z = z[96:144]

# focused on area and corresponding timesteps of each residue in each peptide in trimer system
p1 = zip(p1_x, p1_y)
p2 = zip(p2_x, p2_y)
p3 = zip(p3_x, p3_y)

# flag low area residues
for item in p3:
    if item[1] < thresh and item[1] > 0.1:
        print(item)

# plot a line graph with 3 lines of all 3 peptides and corresponding residues 
fig = plt.figure()
plt.style.use('seaborn-whitegrid')
ax1 = fig.add_subplot(111)
ax1.set_title("av. area per residue over trajectory")
ax1.set_xlabel('Residue #')
ax1.set_ylabel('Area')
a = [i - 1 for i in p1_x]
ax1.plot(p1_x, p1_y, c='r', linewidth=1, label='P1')
ax1.plot(p2_x, p2_y, c='b', linewidth=1, label='P2')
ax1.plot(p3_x, p3_y, c='g', linewidth=1, label='P3')
plt.hlines(y=thresh, xmin=a[0], xmax=a[-1], color='black', linestyle='--', zorder=3,
           label="Threshold of %.1f" % thresh)
plt.hlines(y=0.1, xmin=a[0], xmax=a[-1], color='c', linestyle='--', zorder=3,
           label="Threshold of 0.1")
for axis in [ax1.yaxis]:
    axis.set_major_locator(ticker.MaxNLocator(prune='lower', integer=True))
s = p1_x[::5]
plt.xticks(s)
plt.legend(frameon=True,  framealpha=1, loc="upper left")
plt.xlim(p1_x[0], p1_x[-1])
plt.ylim(0, 2.5)
plt.style.use('seaborn-whitegrid')
plt.show()
