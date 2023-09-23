import os
import subprocess
import time


filename = "dockerImages.txt"

# Créer le dossier results s'il n'existe pas déjà
if not os.path.exists("results"):
    os.makedirs("results")

# Ouvrir le fichier et lire les noms d'images ligne par ligne
with open(filename) as f:
    for line in f:
        # Supprimer les espaces blancs et les sauts de ligne
        image_name = line.strip()
        
        # Exécuter snyk pour l'image Docker si le test précédent a duré plus de 5 min
        filename = f"results/{image_name.replace('/', '-')}.txt"
        if not os.path.exists(filename) or time.time() - os.path.getmtime(filename) > 300:
            print(f"snyk container test {image_name}")
            command = f"snyk container test {image_name}"
            
            try:
                result = subprocess.run(command, shell=True, capture_output=True, timeout=300)
            except subprocess.TimeoutExpired:
                print(f"Le test pour l'image {image_name} a expiré après 5 minutes.")
                continue
            
            # Afficher les résultats de la commande
            print(f"Résultat pour l'image {image_name}:")
            print(result.stdout.decode())
            print(result.stderr.decode())

            # Enregistrer les résultats dans un fichier
            with open(filename, "w") as f:
                f.write(result.stdout.decode())

