import sys
from collections import Counter
import matplotlib.pyplot as plt

filename = sys.argv[1]

tlow = 0
tmedium=0
thigh = 0
tcritical = 0
tableau=[]

with open(filename, 'r') as file:
    for line in file:
        if 'Low severity vulnerability' in line:
            tlow+=1
        if 'Medium severity vulnerability' in line:
            tmedium+=1
        if 'High severity vulnerability' in line:
            thigh+=1
        if 'Critical severity vulnerability' in line:
            tcritical+=1
            
            
tableau.append(tlow)
tableau.append(tmedium)
tableau.append(thigh)
tableau.append(tcritical)

compter_desc = Counter(tableau)
sorted_desc = sorted(compter_desc.items(), key=lambda x: x[1], reverse=True)

labels = ['Low','Medium','High','Critical']
values = [tableau[0],tableau[1],tableau[2],tableau[3]]

fig1, ax1 = plt.subplots()
ax1.pie(values, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')


total = sum(values)
plt.text(-1.9, 1.0, f"Total: {total}")
plt.text(-1.9, 0.9, f"Low: {values[0]}")
plt.text(-1.9, 0.8, f"Medium: {values[1]}")
plt.text(-1.9, 0.7, f"High: {values[2]}")
plt.text(-1.9, 0.6, f"Critical: {values[3]}")

plt.show()

