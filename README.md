# Traduction du Thésaurus-matières en Pydantic 

> "Le Thésaurus pour la description et l'indexation des archives locales s'applique à tous les fonds d'archives locales, publiques et privées, anciennes, modernes et contemporaines. Il a valeur réglementaire pour l’ensemble des services d’archives territoriales – régionales, départementales et communales. Il se compose du thésaurus-matières, essentiellement réservé aux expressions illustrant la notion d'objet mais accueillant aussi des termes liés à des attributions essentielles des producteurs d'archives (par exemple : police, fiscalité, aide sociale), ainsi que trois listes d'autorité ("Actions", "Typologie documentaire", "Contexte historique") contenant des descripteurs qui ne sont pas par eux-mêmes des termes d'indexation mais qu'on associera à un ou plusieurs descripteurs du thésaurus, si le contexte documentaire l'exige."[^1]

La traduction en Python, via [Pydantic](https://docs.pydantic.dev/latest/), des principales informations du graphe RDF, permet de manipuler les concepts comme des classes et les URI comme des attributs.

Les classes ont été générées à partir d'une transformation XSLT (dans /xslt). 

[^1]: http://data.culture.fr/thesaurus/page/ark:/67717/Matiere