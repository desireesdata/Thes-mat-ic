import os
import re

# Motifs d'expression régulière pour extraire les descripteurs et les ARKs
descripteur_pattern = r'descripteur:\s*str\s*=\s*"(.*?)"'
ark_pattern = r'ark:\s*str\s*=\s*"(.*?)"'

# Parcourir tous les fichiers .txt dans le dossier courant
for filename in os.listdir('.'):
    if filename.endswith('.py'):
        with open(filename, 'r', encoding='utf-8') as file:
            input_text = file.read()

        # Extraire les descripteurs et les ARKs
        all_descripteurs = re.findall(descripteur_pattern, input_text)
        all_arks = re.findall(ark_pattern, input_text)

        # Associer chaque descripteur avec l'ARK correspondant
        matches_final = list(zip(all_descripteurs, all_arks))

        # Afficher les résultats pour chaque fichier
        print(f"Résultats pour le fichier {filename}:")
        for descripteur, ark in matches_final:
            print(f"{descripteur}\t{ark}")
        print("\n")
