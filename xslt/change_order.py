import re
import glob
import os

# Chemin vers le répertoire contenant les fichiers d'origine
input_directory_path = '../thesmatic/*'

# Chemin vers le répertoire où les fichiers modifiés seront enregistrés
output_directory_path = '../thesmatic_inverse/'

# Créer le répertoire de sortie s'il n'existe pas
os.makedirs(output_directory_path, exist_ok=True)

# Lister tous les fichiers .txt dans le répertoire d'entrée
file_paths = glob.glob(input_directory_path)

for file_path in file_paths:
    # Lire le contenu du fichier
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Utiliser l'expression régulière pour trouver toutes les classes
    classes = re.findall(r'(class.*\n\s*sous_descripteur:.*\n\s*ark:.*\n\s*descripteur:.*\n)', content)

    # Inverser l'ordre des classes
    classes.reverse()

    # Ajouter l'en-tête à chaque classe
    header = "from pydantic import BaseModel, Field\nfrom typing import Union, Literal\n\n"
    new_content = header + '\n'.join(classes)

    # Déterminer le chemin du fichier de sortie
    output_file_path = os.path.join(output_directory_path, os.path.basename(file_path))

    # Écrire le fichier modifié dans le répertoire de sortie
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

print("L'ordre des classes a été inversé et l'en-tête a été ajouté à tous les fichiers. Les fichiers modifiés ont été enregistrés dans le répertoire de sortie.")
