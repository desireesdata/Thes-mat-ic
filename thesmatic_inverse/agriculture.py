from pydantic import BaseModel
from typing import Union, Literal

class Poisson(BaseModel):
    terme_specifique: Literal['Poisson']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1067"
    descripteur: str = "poisson"

class PecheEnEauDouce(BaseModel):
    terme_specifique: Literal['PecheEnEauDouce']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-425"
    descripteur: str = "pêche en eau douce"

class PecheMaritime(BaseModel):
    terme_specifique: Literal['PecheMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1395"
    descripteur: str = "pêche maritime"

class Peche(BaseModel):
    terme_specifique: Union['PecheMaritime', 'PecheEnEauDouce', 'Poisson']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-653"
    descripteur: str = "pêche"

class Conchyliculture(BaseModel):
    terme_specifique: Literal['Conchyliculture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-890"
    descripteur: str = "conchyliculture"

class Pisciculture(BaseModel):
    terme_specifique: Literal['Pisciculture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-531"
    descripteur: str = "pisciculture"

class Aquaculture(BaseModel):
    terme_specifique: Union['Pisciculture', 'Conchyliculture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-986"
    descripteur: str = "aquaculture"

class Apiculture(BaseModel):
    terme_specifique: Literal['Apiculture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-415"
    descripteur: str = "apiculture"

class AnimalNuisible(BaseModel):
    terme_specifique: Literal['AnimalNuisible']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-461"
    descripteur: str = "animal nuisible"

class MaladieDesVegetaux(BaseModel):
    terme_specifique: Literal['MaladieDesVegetaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-982"
    descripteur: str = "maladie des végétaux"

class ProtectionDesVegetaux(BaseModel):
    terme_specifique: Union['MaladieDesVegetaux', 'AnimalNuisible']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-289"
    descripteur: str = "protection des végétaux"

class Grele(BaseModel):
    terme_specifique: Literal['Grele']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-683"
    descripteur: str = "grêle"

class Gelee(BaseModel):
    terme_specifique: Literal['Gelee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-854"
    descripteur: str = "gelée"

class Secheresse(BaseModel):
    terme_specifique: Literal['Secheresse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-309"
    descripteur: str = "sécheresse"

class CalamiteAgricole(BaseModel):
    terme_specifique: Union['Secheresse', 'Gelee', 'Grele']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-202"
    descripteur: str = "calamité agricole"

class ProduitMaraicher(BaseModel):
    terme_specifique: Literal['ProduitMaraicher']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1220"
    descripteur: str = "produit maraîcher"

class Fleur(BaseModel):
    terme_specifique: Literal['Fleur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-604"
    descripteur: str = "fleur"

class Fruit(BaseModel):
    terme_specifique: Literal['Fruit']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-162"
    descripteur: str = "fruit"

class Horticulture(BaseModel):
    terme_specifique: Union['Fruit', 'Fleur', 'ProduitMaraicher']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-631"
    descripteur: str = "horticulture"

class Eaudevie(BaseModel):
    terme_specifique: Literal['Eaudevie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-223"
    descripteur: str = "eau-de-vie"

class Vin(BaseModel):
    terme_specifique: Literal['Vin']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-136"
    descripteur: str = "vin"

class BoissonAlcoolisee(BaseModel):
    terme_specifique: Union['Vin', 'Eaudevie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-603"
    descripteur: str = "boisson alcoolisée"

class Equide(BaseModel):
    terme_specifique: Literal['Equide']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1464"
    descripteur: str = "équidé"

class Volaille(BaseModel):
    terme_specifique: Literal['Volaille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1440"
    descripteur: str = "volaille"

class AlimentDuBetail(BaseModel):
    terme_specifique: Literal['AlimentDuBetail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1389"
    descripteur: str = "aliment du bétail"

class Oeuf(BaseModel):
    terme_specifique: Literal['Oeuf']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1011"
    descripteur: str = "oeuf"

class ProduitLaitier(BaseModel):
    terme_specifique: Literal['ProduitLaitier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-655"
    descripteur: str = "produit laitier"

class Viande(BaseModel):
    terme_specifique: Literal['Viande']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1410"
    descripteur: str = "viande"

class Betail(BaseModel):
    terme_specifique: Literal['Betail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-620"
    descripteur: str = "bétail"

class ReproductionAnimale(BaseModel):
    terme_specifique: Literal['ReproductionAnimale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-310"
    descripteur: str = "reproduction animale"

class Abattoir(BaseModel):
    terme_specifique: Literal['Abattoir']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1092"
    descripteur: str = "abattoir"

class VerASoie(BaseModel):
    terme_specifique: Literal['VerASoie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-238"
    descripteur: str = "ver à soie"

class Elevage(BaseModel):
    terme_specifique: Union['VerASoie', 'Abattoir', 'ReproductionAnimale', 'Betail', 'Viande', 'ProduitLaitier', 'Oeuf', 'AlimentDuBetail', 'Volaille', 'Equide']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1013"
    descripteur: str = "élevage"

class Sucre(BaseModel):
    terme_specifique: Literal['Sucre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1418"
    descripteur: str = "sucre"

class Tabac(BaseModel):
    terme_specifique: Literal['Tabac']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1049"
    descripteur: str = "tabac"

class Cereale(BaseModel):
    terme_specifique: Literal['Cereale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-590"
    descripteur: str = "céréale"

class Oleagineux(BaseModel):
    terme_specifique: Literal['Oleagineux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-283"
    descripteur: str = "oléagineux"

class PlanteTextile(BaseModel):
    terme_specifique: Literal['PlanteTextile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-447"
    descripteur: str = "plante textile"

class PlanteTinctoriale(BaseModel):
    terme_specifique: Literal['PlanteTinctoriale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-64"
    descripteur: str = "plante tinctoriale"

class CultureIndustrielle(BaseModel):
    terme_specifique: Union['PlanteTinctoriale', 'PlanteTextile', 'Oleagineux', 'Cereale', 'Tabac', 'Sucre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1325"
    descripteur: str = "culture industrielle"

class MaladieDesAnimaux(BaseModel):
    terme_specifique: Literal['MaladieDesAnimaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1362"
    descripteur: str = "maladie des animaux"

class PharmacieVeterinaire(BaseModel):
    terme_specifique: Literal['PharmacieVeterinaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-439"
    descripteur: str = "pharmacie vétérinaire"

class MedecineVeterinaire(BaseModel):
    terme_specifique: Literal['MedecineVeterinaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-56"
    descripteur: str = "médecine vétérinaire"

class ProtectionSanitaireDuCheptel(BaseModel):
    terme_specifique: Union['MedecineVeterinaire', 'PharmacieVeterinaire', 'MaladieDesAnimaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1167"
    descripteur: str = "protection sanitaire du cheptel"

class Viticulture(BaseModel):
    terme_specifique: Literal['Viticulture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-49"
    descripteur: str = "viticulture"

class ProductionAgricole(BaseModel):
    terme_specifique: Union['Viticulture', 'ProtectionSanitaireDuCheptel', 'CultureIndustrielle', 'Elevage', 'BoissonAlcoolisee', 'Horticulture', 'CalamiteAgricole', 'ProtectionDesVegetaux', 'Apiculture', 'Aquaculture', 'Peche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-421"
    descripteur: str = "production agricole"

class AmenagementForestier(BaseModel):
    terme_specifique: Literal['AmenagementForestier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1036"
    descripteur: str = "aménagement forestier"

class ForetPrivee(BaseModel):
    terme_specifique: Literal['ForetPrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-741"
    descripteur: str = "forêt privée"

class Reboisement(BaseModel):
    terme_specifique: Literal['Reboisement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1213"
    descripteur: str = "reboisement"

class Defrichement(BaseModel):
    terme_specifique: Literal['Defrichement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-105"
    descripteur: str = "défrichement"

class Sylviculture(BaseModel):
    terme_specifique: Union['Defrichement', 'Reboisement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-400"
    descripteur: str = "sylviculture"

class Vacants(BaseModel):
    terme_specifique: Literal['Vacants']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-31"
    descripteur: str = "vacants"

class Paturage(BaseModel):
    terme_specifique: Literal['Paturage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-670"
    descripteur: str = "pâturage"

class DroitsDusageForestiers(BaseModel):
    terme_specifique: Union['Paturage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-252"
    descripteur: str = "droits d'usage forestiers"

class ForetCommunale(BaseModel):
    terme_specifique: Literal['ForetCommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-325"
    descripteur: str = "forêt communale"

class ConcessionForestiere(BaseModel):
    terme_specifique: Literal['ConcessionForestiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-96"
    descripteur: str = "concession forestière"

class ForetDomaniale(BaseModel):
    terme_specifique: Union['ConcessionForestiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1095"
    descripteur: str = "forêt domaniale"

class CharbonDeBois(BaseModel):
    terme_specifique: Literal['CharbonDeBois']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1112"
    descripteur: str = "charbon de bois"

class CoupeDeBois(BaseModel):
    terme_specifique: Literal['CoupeDeBois']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-7"
    descripteur: str = "coupe de bois"

class Bois(BaseModel):
    terme_specifique: Union['CoupeDeBois', 'CharbonDeBois']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-643"
    descripteur: str = "bois"

class Foret(BaseModel):
    terme_specifique: Union['Bois', 'ForetDomaniale', 'ForetCommunale', 'DroitsDusageForestiers', 'Vacants', 'Sylviculture', 'ForetPrivee', 'AmenagementForestier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-750"
    descripteur: str = "forêt"

class ConcoursAgricole(BaseModel):
    terme_specifique: Literal['ConcoursAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1463"
    descripteur: str = "concours agricole"

class MaterielAgricole(BaseModel):
    terme_specifique: Literal['MaterielAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-925"
    descripteur: str = "matériel agricole"

class Transhumance(BaseModel):
    terme_specifique: Literal['Transhumance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1075"
    descripteur: str = "transhumance"

class ViePastorale(BaseModel):
    terme_specifique: Union['Transhumance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-743"
    descripteur: str = "vie pastorale"

class SocieteDinteretCollectifAgricole(BaseModel):
    terme_specifique: Literal['SocieteDinteretCollectifAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1261"
    descripteur: str = "société d'intérêt collectif agricole"

class GroupementDeProducteurs(BaseModel):
    terme_specifique: Literal['GroupementDeProducteurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-875"
    descripteur: str = "groupement de producteurs"

class BauxRuraux(BaseModel):
    terme_specifique: Literal['BauxRuraux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1235"
    descripteur: str = "baux ruraux"

class CooperativeAgricole(BaseModel):
    terme_specifique: Literal['CooperativeAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-491"
    descripteur: str = "coopérative agricole"

class ExploitationAgricole(BaseModel):
    terme_specifique: Union['CooperativeAgricole', 'BauxRuraux', 'GroupementDeProducteurs', 'SocieteDinteretCollectifAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1099"
    descripteur: str = "exploitation agricole"

class Battage(BaseModel):
    terme_specifique: Literal['Battage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1360"
    descripteur: str = "battage"

class Assolement(BaseModel):
    terme_specifique: Literal['Assolement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1026"
    descripteur: str = "assolement"

class AmeliorationDesSols(BaseModel):
    terme_specifique: Literal['AmeliorationDesSols']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-582"
    descripteur: str = "amélioration des sols"

class AgricultureBiologique(BaseModel):
    terme_specifique: Literal['AgricultureBiologique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-323"
    descripteur: str = "agriculture biologique"

class Ecobuage(BaseModel):
    terme_specifique: Literal['Ecobuage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-293"
    descripteur: str = "écobuage"

class PratiquesAgraires(BaseModel):
    terme_specifique: Union['Ecobuage', 'AgricultureBiologique', 'AmeliorationDesSols', 'Assolement', 'Battage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1018"
    descripteur: str = "pratiques agraires"

class UsagesAgricolesLocaux(BaseModel):
    terme_specifique: Literal['UsagesAgricolesLocaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1324"
    descripteur: str = "usages agricoles locaux"

class MarinPecheur(BaseModel):
    terme_specifique: Literal['MarinPecheur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-584"
    descripteur: str = "marin pêcheur"

class Drainage(BaseModel):
    terme_specifique: Literal['Drainage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-211"
    descripteur: str = "drainage"

class Irrigation(BaseModel):
    terme_specifique: Literal['Irrigation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-133"
    descripteur: str = "irrigation"

class BarrageHydraulique(BaseModel):
    terme_specifique: Literal['BarrageHydraulique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-242"
    descripteur: str = "barrage hydraulique"

class HydrauliqueAgricole(BaseModel):
    terme_specifique: Union['BarrageHydraulique', 'Irrigation', 'Drainage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-9"
    descripteur: str = "hydraulique agricole"

class ExploitantAgricole(BaseModel):
    terme_specifique: Literal['ExploitantAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1209"
    descripteur: str = "exploitant agricole"

class JeuneAgriculteur(BaseModel):
    terme_specifique: Literal['JeuneAgriculteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-449"
    descripteur: str = "jeune agriculteur"

class SalarieAgricole(BaseModel):
    terme_specifique: Literal['SalarieAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-179"
    descripteur: str = "salarié agricole"

class Berger(BaseModel):
    terme_specifique: Literal['Berger']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1107"
    descripteur: str = "berger"

class Eleveur(BaseModel):
    terme_specifique: Literal['Eleveur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-546"
    descripteur: str = "éleveur"

class ExploitantForestier(BaseModel):
    terme_specifique: Literal['ExploitantForestier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-832"
    descripteur: str = "exploitant forestier"

class Agriculteur(BaseModel):
    terme_specifique: Union['ExploitantForestier', 'Eleveur', 'Berger', 'SalarieAgricole', 'JeuneAgriculteur', 'ExploitantAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-419"
    descripteur: str = "agriculteur"

class RemembrementRural(BaseModel):
    terme_specifique: Literal['RemembrementRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-472"
    descripteur: str = "remembrement rural"

class AssociationSyndicaleDeProprietaires(BaseModel):
    terme_specifique: Literal['AssociationSyndicaleDeProprietaires']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-866"
    descripteur: str = "association syndicale de propriétaires"

class TerreInculte(BaseModel):
    terme_specifique: Literal['TerreInculte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-57"
    descripteur: str = "terre inculte"

class AmenagementRural(BaseModel):
    terme_specifique: Union['TerreInculte', 'AssociationSyndicaleDeProprietaires', 'RemembrementRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1047"
    descripteur: str = "aménagement rural"

class BatimentAgricole(BaseModel):
    terme_specifique: Literal['BatimentAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-40"
    descripteur: str = "bâtiment agricole"

class EconomieRurale(BaseModel):
    terme_specifique: Union['BatimentAgricole', 'AmenagementRural', 'Agriculteur', 'HydrauliqueAgricole', 'MarinPecheur', 'UsagesAgricolesLocaux', 'PratiquesAgraires', 'ExploitationAgricole', 'ViePastorale', 'MaterielAgricole', 'ConcoursAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1134"
    descripteur: str = "économie rurale"

class Agriculture(BaseModel):
    terme_specifique: Union['EconomieRurale', 'Foret', 'ProductionAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-246"
    descripteur: str = "agriculture"
