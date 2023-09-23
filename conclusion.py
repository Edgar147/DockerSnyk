import os
import matplotlib.pyplot as plt

folder = "results"

total_files = 0
critical_files = 0

for filename in os.listdir(folder):
    with open(os.path.join(folder, filename), "r") as f:
        lines = f.readlines()
        total_files += 1
        for line in lines:
            if "Critical severity vulnerability" in line:
                critical_files += 1
                print(f"{filename} has at least one Critical vulnerability")
                break

print(f"Total fichiers: {total_files}")
print(f"Fichiers contenant 'Critical severity vulnerability': {critical_files}")

#Diagramme circulaire 
labels = ['Non critical files', 'Critical Files']
sizes = [total_files-critical_files, critical_files]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')

total_text = f"Total files: {total_files}"
critical_text = f"Critical files: {critical_files}"
ax.text(1, -0.01, total_text, transform=ax.transAxes, ha='center')
ax.text(1, -0.1, critical_text, transform=ax.transAxes, ha='center')

plt.show()

