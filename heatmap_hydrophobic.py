import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# prints heatmap of residue - residue contacts vs time in contact on interface of the dimer that formed 
x, y, z = [], [], []

with open("frac_at_10A.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 3:
            x.append(cols[0])
            y.append(cols[1])
            z.append(float(cols[2]))
print(x)
print(y)
print(z)

e = [i/0.67 for i in z]
c = [i * 100 for i in e]
d = list(map("{}%".format, c))
print("max frac frame bound =", max(z))
data = pd.DataFrame(data={'N2 hydrophobic residues': x, 'N3 hydrophobic residues': y, 'Fraction of frames bound': c})
data = data.pivot(index='N2 hydrophobic residues', columns='N3 hydrophobic residues', values='Fraction of frames bound')
print(data)
sns.set(font_scale=1)
svm = sns.heatmap(data, cmap='coolwarm', annot=True, annot_kws={"fontsize":10}, vmax=100, vmin=0, cbar_kws={'label': 'Percentage of $T^{\mathrm{N2, N3}}_{\mathrm{dimer}}$ in contact (%)', 'ticks': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]},  square=True, linewidths=0.01, linecolor='black')
svm.invert_yaxis()
figure = svm.get_figure()
for t in svm.texts: t.set_text(t.get_text() + " %")
figure.savefig('heatmap hydrophobic dimer in trimer.pdf', bbox_inches='tight')
plt.show()

print("max frac frame bound =", max(z))
