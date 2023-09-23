import os

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

