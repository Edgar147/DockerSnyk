import sys
from collections import Counter
import matplotlib.pyplot as plt

filename = sys.argv[1]

tableau = []

with open(filename, 'r') as file:
    for line in file:
        if 'Description' in line:
            mot = line.split(':')[1].strip()
            tableau.append(mot)

compter_desc = Counter(tableau)
sorted_desc = sorted(compter_desc.items(), key=lambda x: x[1], reverse=True)

labels = [mot for mot, count in sorted_desc]
sizes = [count for mot, count in sorted_desc]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')

plt.show()

