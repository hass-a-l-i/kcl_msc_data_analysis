import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

x, y, z = [], [], []

with open("no_contacts.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 3:
            x.append(cols[0])
            y.append(cols[1])
            z.append(float(cols[2]))
print(x)
print(y)
print(z)

c = [float(i)/max(z) for i in z]
print("max frac frame bound =", max(z))
data = pd.DataFrame(data={'N2 hydrophobic residues': x, 'N3 hydrophobic residues': y, '# contacts': z})
# data = pd.DataFrame(data={'P2 hydrophobic residues': x, 'P3 hydrophobic residues': y, 'Fraction of frames bound': c})
data = data.pivot(index='N2 hydrophobic residues', columns='N3 hydrophobic residues', values='# contacts')
# print(data)
sns.set(font_scale=1)
svm = sns.heatmap(data, cmap='coolwarm', annot=True, annot_kws={"fontsize":10}, vmax=0, vmin=2, cbar_kws={'label': 'Average number of contacts', 'ticks': [0, 1, 2]})
svm.invert_yaxis()
figure = svm.get_figure()
figure.savefig('heatmap no contacts.pdf', bbox_inches='tight')
plt.show()

print("max frac frame bound =", max(z))
