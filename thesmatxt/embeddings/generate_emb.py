import numpy as np
import json
from mistralai import Mistral

api_key = "880wKshluD14ADTcQjuyRFMbk7M1i129"
model = "mistral-embed"
client = Mistral(api_key=api_key)

def parse_hierarchy_from_file(filepath):
    hierarchy = {}
    with open(filepath, 'r') as file:
        stack = [hierarchy]
        for line in file:
            # Supprimer uniquement les espaces à la fin de la ligne
            line = line.rstrip()
            # print(f"Original line: '{line}'") 
            if line:
                # Compter le nombre de barres obliques pour déterminer le niveau d'indentation
                indent = 0
                while line.startswith('/'):
                    line = line[1:]
                    indent += 1
                # print(f"Indented line: '{line}', Indent: {indent}") 
                # Ajouter l'élément au bon niveau de la hiérarchie
                current_level = stack[indent]
                current_level[line] = {}
                stack = stack[:indent + 1]
                stack.append(current_level[line])
    return hierarchy

def get_full_path(element, hierarchy, path=None):
    if path is None:
        path = []
    path.append(element)
    if element in hierarchy:
        for sub_element in hierarchy[element]:
            yield from get_full_path(sub_element, hierarchy[element], path.copy())
    else:
        yield " > ".join(path)

# Chemin vers le fichier texte
filepath = 'vocabulary.txt'

# Lire et parser le fichier
hierarchy = parse_hierarchy_from_file(filepath)

# Imprimer la hiérarchie pour le débogage
print("Parsed Hierarchy:")
print(hierarchy)

# Générer les chemins complets pour chaque élément de niveau supérieur
full_paths = []
for top_level_element in hierarchy:
    full_paths.extend(list(get_full_path(top_level_element, hierarchy)))

# Imprimer les chemins pour le débogage
print("Generated Paths:")
for path in full_paths:
    print(path)

# Vérifier si la liste des chemins est vide
if not full_paths:
    raise ValueError("No paths were generated. Check the hierarchy parsing.")
# Générer les embeddings pour chaque chemin
embeddings_batch_response = client.embeddings.create(
    model=model,
    inputs=full_paths,
)

# Extraire les embeddings de la réponse
embeddings = [embedding.embedding for embedding in embeddings_batch_response.data]

# Sauvegarder les embeddings et les étiquettes dans un fichier JSON
output_data = {
    "embeddings": embeddings,
    "labels": full_paths
}

with open('vectors/hierarchical_embeddings.json', 'w') as json_file:
    json.dump(output_data, json_file)

# Afficher les chemins et les embeddings (optionnel)
for path, embedding in zip(full_paths, embeddings):
    print(f"Path: {path}\nEmbedding: {embedding[:5]}...\n")
