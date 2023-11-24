import matplotlib.pyplot as plt
from itertools import cycle, islice
import pandas as pd

x, y, z = [], [], []

with open("sai_trimer_sasa.xvg") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 3:
            x.append(float(cols[0]))
            y.append(float(cols[1]))
            z.append(float(cols[2]))
thresh = 0.04386
p1_x = x[0:48]
p1_y = y[0:48]
p1_z = z[0:48]
p2_x = x[48:96]
p2_y = y[48:96]
p2_z = z[48:96]
p3_x = x[96:144]
p3_y = y[96:144]
p3_z = z[96:144]
p1 = zip(p1_x, p1_y)
p2 = zip(p2_x, p2_y)
p3 = zip(p3_x, p3_y)

t = ["A", "A", "F", "M", "K", "L", "I", "Q", "F", "L", "A", "T", "K", "G", "Q", "K", "T", "V", "S", "K", "L", "A", "W",
     "K", "H", "K", "G", "T", "I", "L", "K", "W",
     "I", "N", "A", "G", "Q", "S", "F", "E", "W", "I", "Y", "K", "Q", "I", "K", "K"]
q = list(zip(t, p2_y))
w, e = [], []
for item in q:
    if 0 < item[1] < thresh:
        w.append(item)
    if thresh < item[1] < 3:
        e.append(item)
print(w)
u = []
for item in w:
    u.append(item[0])
hydro = ["A", "V", "L", "W", "G", "I", "M", "F"]
charged = ["K", "E"]
b = set(u) & set(hydro)
d = set(u) & set(charged)
#print("hydrophobic percentage =", len(b) / len(u) * 100)
print("residues", b)
#print("charged percentage =", len(d) / len(u) * 100)
print("residues", d)
k = []

e1 = []
e2 = []
e3 = []
for i in p1_y:
    if i > thresh:
        e1.append(i)
for i in p2_y:
    if i > thresh:
        e2.append(i)
for i in p3_y:
    if i > thresh:
        e3.append(i)
#for item in p3:
    #if item[1] < thresh and item[1] > 0.1:
        #print(item)

l = []
for i in p1_x:
    l.append(round(i))

total = sum(e1) + sum(e2)
print("tot_eff =", total)
total2 = sum(p1_y) + sum(p2_y)
print("tot =", total2)
print("tot pep 1 =", sum(e1))
print("tot pep 2 =", sum(e2))
print("tot pep 3 =", sum(e3))
print("av =", (sum(e1)+sum(e2)+sum(e3))/3)
# l = ["A", "A", "F", "M", "K", "L", "I", "Q", "F", "L", "A", "T", "K", "G", "Q", "K", "V", "S", "L", "A", "W", "K", "H", "K", "G", "T", "I", "L", "K", "W",
# "I", "N", "A", "G", "Q", "S", "F", "E", "W", "I", "Y", "K", "Q", "I", "K", "K", "L", "W"]

df = pd.DataFrame({'S1': p1_y,
                   'S2': p2_y,
                   'S3': p3_y}, index=l)

# N3 here too if have

my_colors = list(islice(cycle(['tab:blue', 'tab:red', 'tab:green']), None, len(df)))
s = l[::3]
ax = df.plot.bar(rot=0, color=my_colors, width=0.75)
ax.set_xlabel("Residue number", fontsize=12)
ax.set_ylabel("Average SASA (nm$^2$)", fontsize=12)#
plt.xticks(s)
plt.ylim(0, 2.5)
plt.hlines(y=thresh, xmin=0, xmax=60, color='black', linestyle='--', zorder=3,
           label="$A^{\mathrm{av}}_{\mathrm{thresh}}$ = %.5f nm$^2$" % thresh)
plt.legend(loc="upper left", frameon=False)
fig = ax.get_figure()
#fig.savefig('resarea_bars_bound_SA_I.pdf')
fig.savefig('resarea_bars_SA-I_trimer.pdf')

plt.show()
