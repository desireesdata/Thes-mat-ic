from pydantic import BaseModel, Field
from typing import Union, Literal
                
class Agriculture(BaseModel):
    sous_descripteur: Union['EconomieRurale', 'Foret', 'ProductionAgricole'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-246"
    descripteur: str = "agriculture"
class EconomieRurale(BaseModel):
    sous_descripteur: Union['BatimentAgricole', 'AmenagementRural', 'Agriculteur', 'HydrauliqueAgricole', 'MarinPecheur', 'UsagesAgricolesLocaux', 'PratiquesAgraires', 'ExploitationAgricole', 'ViePastorale', 'MaterielAgricole', 'ConcoursAgricole'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1134"
    descripteur: str = "économie rurale"
class BatimentAgricole(BaseModel):
    sous_descripteur: Literal['BatimentAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-40"
    descripteur: str = "bâtiment agricole"
class AmenagementRural(BaseModel):
    sous_descripteur: Union['TerreInculte', 'AssociationSyndicaleDeProprietaires', 'RemembrementRural'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1047"
    descripteur: str = "aménagement rural"
class TerreInculte(BaseModel):
    sous_descripteur: Literal['TerreInculte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-57"
    descripteur: str = "terre inculte"
class AssociationSyndicaleDeProprietaires(BaseModel):
    sous_descripteur: Literal['AssociationSyndicaleDeProprietaires']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-866"
    descripteur: str = "association syndicale de propriétaires"
class RemembrementRural(BaseModel):
    sous_descripteur: Literal['RemembrementRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-472"
    descripteur: str = "remembrement rural"
class Agriculteur(BaseModel):
    sous_descripteur: Union['ExploitantForestier', 'Eleveur', 'Berger', 'SalarieAgricole', 'JeuneAgriculteur', 'ExploitantAgricole'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-419"
    descripteur: str = "agriculteur"
class ExploitantForestier(BaseModel):
    sous_descripteur: Literal['ExploitantForestier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-832"
    descripteur: str = "exploitant forestier"
class Eleveur(BaseModel):
    sous_descripteur: Literal['Eleveur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-546"
    descripteur: str = "éleveur"
class Berger(BaseModel):
    sous_descripteur: Literal['Berger']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1107"
    descripteur: str = "berger"
class SalarieAgricole(BaseModel):
    sous_descripteur: Literal['SalarieAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-179"
    descripteur: str = "salarié agricole"
class JeuneAgriculteur(BaseModel):
    sous_descripteur: Literal['JeuneAgriculteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-449"
    descripteur: str = "jeune agriculteur"
class ExploitantAgricole(BaseModel):
    sous_descripteur: Literal['ExploitantAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1209"
    descripteur: str = "exploitant agricole"
class HydrauliqueAgricole(BaseModel):
    sous_descripteur: Union['BarrageHydraulique', 'Irrigation', 'Drainage'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-9"
    descripteur: str = "hydraulique agricole"
class BarrageHydraulique(BaseModel):
    sous_descripteur: Literal['BarrageHydraulique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-242"
    descripteur: str = "barrage hydraulique"
class Irrigation(BaseModel):
    sous_descripteur: Literal['Irrigation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-133"
    descripteur: str = "irrigation"
class Drainage(BaseModel):
    sous_descripteur: Literal['Drainage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-211"
    descripteur: str = "drainage"
class MarinPecheur(BaseModel):
    sous_descripteur: Literal['MarinPecheur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-584"
    descripteur: str = "marin pêcheur"
class UsagesAgricolesLocaux(BaseModel):
    sous_descripteur: Literal['UsagesAgricolesLocaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1324"
    descripteur: str = "usages agricoles locaux"
class PratiquesAgraires(BaseModel):
    sous_descripteur: Union['Ecobuage', 'AgricultureBiologique', 'AmeliorationDesSols', 'Assolement', 'Battage'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1018"
    descripteur: str = "pratiques agraires"
class Ecobuage(BaseModel):
    sous_descripteur: Literal['Ecobuage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-293"
    descripteur: str = "écobuage"
class AgricultureBiologique(BaseModel):
    sous_descripteur: Literal['AgricultureBiologique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-323"
    descripteur: str = "agriculture biologique"
class AmeliorationDesSols(BaseModel):
    sous_descripteur: Literal['AmeliorationDesSols']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-582"
    descripteur: str = "amélioration des sols"
class Assolement(BaseModel):
    sous_descripteur: Literal['Assolement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1026"
    descripteur: str = "assolement"
class Battage(BaseModel):
    sous_descripteur: Literal['Battage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1360"
    descripteur: str = "battage"
class ExploitationAgricole(BaseModel):
    sous_descripteur: Union['CooperativeAgricole', 'BauxRuraux', 'GroupementDeProducteurs', 'SocieteDinteretCollectifAgricole'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1099"
    descripteur: str = "exploitation agricole"
class CooperativeAgricole(BaseModel):
    sous_descripteur: Literal['CooperativeAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-491"
    descripteur: str = "coopérative agricole"
class BauxRuraux(BaseModel):
    sous_descripteur: Literal['BauxRuraux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1235"
    descripteur: str = "baux ruraux"
class GroupementDeProducteurs(BaseModel):
    sous_descripteur: Literal['GroupementDeProducteurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-875"
    descripteur: str = "groupement de producteurs"
class SocieteDinteretCollectifAgricole(BaseModel):
    sous_descripteur: Literal['SocieteDinteretCollectifAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1261"
    descripteur: str = "société d'intérêt collectif agricole"
class ViePastorale(BaseModel):
    sous_descripteur: Union['Transhumance'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-743"
    descripteur: str = "vie pastorale"
class Transhumance(BaseModel):
    sous_descripteur: Literal['Transhumance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1075"
    descripteur: str = "transhumance"
class MaterielAgricole(BaseModel):
    sous_descripteur: Literal['MaterielAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-925"
    descripteur: str = "matériel agricole"
class ConcoursAgricole(BaseModel):
    sous_descripteur: Literal['ConcoursAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1463"
    descripteur: str = "concours agricole"
class Foret(BaseModel):
    sous_descripteur: Union['Bois', 'ForetDomaniale', 'ForetCommunale', 'DroitsDusageForestiers', 'Vacants', 'Sylviculture', 'ForetPrivee', 'AmenagementForestier'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-750"
    descripteur: str = "forêt"
class Bois(BaseModel):
    sous_descripteur: Union['CoupeDeBois', 'CharbonDeBois'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-643"
    descripteur: str = "bois"
class CoupeDeBois(BaseModel):
    sous_descripteur: Literal['CoupeDeBois']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-7"
    descripteur: str = "coupe de bois"
class CharbonDeBois(BaseModel):
    sous_descripteur: Literal['CharbonDeBois']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1112"
    descripteur: str = "charbon de bois"
class ForetDomaniale(BaseModel):
    sous_descripteur: Union['ConcessionForestiere'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1095"
    descripteur: str = "forêt domaniale"
class ConcessionForestiere(BaseModel):
    sous_descripteur: Literal['ConcessionForestiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-96"
    descripteur: str = "concession forestière"
class ForetCommunale(BaseModel):
    sous_descripteur: Literal['ForetCommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-325"
    descripteur: str = "forêt communale"
class DroitsDusageForestiers(BaseModel):
    sous_descripteur: Union['Paturage'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-252"
    descripteur: str = "droits d'usage forestiers"
class Paturage(BaseModel):
    sous_descripteur: Literal['Paturage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-670"
    descripteur: str = "pâturage"
class Vacants(BaseModel):
    sous_descripteur: Literal['Vacants']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-31"
    descripteur: str = "vacants"
class Sylviculture(BaseModel):
    sous_descripteur: Union['Defrichement', 'Reboisement'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-400"
    descripteur: str = "sylviculture"
class Defrichement(BaseModel):
    sous_descripteur: Literal['Defrichement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-105"
    descripteur: str = "défrichement"
class Reboisement(BaseModel):
    sous_descripteur: Literal['Reboisement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1213"
    descripteur: str = "reboisement"
class ForetPrivee(BaseModel):
    sous_descripteur: Literal['ForetPrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-741"
    descripteur: str = "forêt privée"
class AmenagementForestier(BaseModel):
    sous_descripteur: Literal['AmenagementForestier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1036"
    descripteur: str = "aménagement forestier"
class ProductionAgricole(BaseModel):
    sous_descripteur: Union['Viticulture', 'ProtectionSanitaireDuCheptel', 'CultureIndustrielle', 'Elevage', 'BoissonAlcoolisee', 'Horticulture', 'CalamiteAgricole', 'ProtectionDesVegetaux', 'Apiculture', 'Aquaculture', 'Peche'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-421"
    descripteur: str = "production agricole"
class Viticulture(BaseModel):
    sous_descripteur: Literal['Viticulture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-49"
    descripteur: str = "viticulture"
class ProtectionSanitaireDuCheptel(BaseModel):
    sous_descripteur: Union['MedecineVeterinaire', 'PharmacieVeterinaire', 'MaladieDesAnimaux'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1167"
    descripteur: str = "protection sanitaire du cheptel"
class MedecineVeterinaire(BaseModel):
    sous_descripteur: Literal['MedecineVeterinaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-56"
    descripteur: str = "médecine vétérinaire"
class PharmacieVeterinaire(BaseModel):
    sous_descripteur: Literal['PharmacieVeterinaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-439"
    descripteur: str = "pharmacie vétérinaire"
class MaladieDesAnimaux(BaseModel):
    sous_descripteur: Literal['MaladieDesAnimaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1362"
    descripteur: str = "maladie des animaux"
class CultureIndustrielle(BaseModel):
    sous_descripteur: Union['PlanteTinctoriale', 'PlanteTextile', 'Oleagineux', 'Cereale', 'Tabac', 'Sucre'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1325"
    descripteur: str = "culture industrielle"
class PlanteTinctoriale(BaseModel):
    sous_descripteur: Literal['PlanteTinctoriale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-64"
    descripteur: str = "plante tinctoriale"
class PlanteTextile(BaseModel):
    sous_descripteur: Literal['PlanteTextile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-447"
    descripteur: str = "plante textile"
class Oleagineux(BaseModel):
    sous_descripteur: Literal['Oleagineux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-283"
    descripteur: str = "oléagineux"
class Cereale(BaseModel):
    sous_descripteur: Literal['Cereale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-590"
    descripteur: str = "céréale"
class Tabac(BaseModel):
    sous_descripteur: Literal['Tabac']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1049"
    descripteur: str = "tabac"
class Sucre(BaseModel):
    sous_descripteur: Literal['Sucre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1418"
    descripteur: str = "sucre"
class Elevage(BaseModel):
    sous_descripteur: Union['VerASoie', 'Abattoir', 'ReproductionAnimale', 'Betail', 'Viande', 'ProduitLaitier', 'Oeuf', 'AlimentDuBetail', 'Volaille', 'Equide'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1013"
    descripteur: str = "élevage"
class VerASoie(BaseModel):
    sous_descripteur: Literal['VerASoie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-238"
    descripteur: str = "ver à soie"
class Abattoir(BaseModel):
    sous_descripteur: Literal['Abattoir']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1092"
    descripteur: str = "abattoir"
class ReproductionAnimale(BaseModel):
    sous_descripteur: Literal['ReproductionAnimale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-310"
    descripteur: str = "reproduction animale"
class Betail(BaseModel):
    sous_descripteur: Literal['Betail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-620"
    descripteur: str = "bétail"
class Viande(BaseModel):
    sous_descripteur: Literal['Viande']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1410"
    descripteur: str = "viande"
class ProduitLaitier(BaseModel):
    sous_descripteur: Literal['ProduitLaitier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-655"
    descripteur: str = "produit laitier"
class Oeuf(BaseModel):
    sous_descripteur: Literal['Oeuf']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1011"
    descripteur: str = "oeuf"
class AlimentDuBetail(BaseModel):
    sous_descripteur: Literal['AlimentDuBetail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1389"
    descripteur: str = "aliment du bétail"
class Volaille(BaseModel):
    sous_descripteur: Literal['Volaille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1440"
    descripteur: str = "volaille"
class Equide(BaseModel):
    sous_descripteur: Literal['Equide']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1464"
    descripteur: str = "équidé"
class BoissonAlcoolisee(BaseModel):
    sous_descripteur: Union['Vin', 'Eaudevie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-603"
    descripteur: str = "boisson alcoolisée"
class Vin(BaseModel):
    sous_descripteur: Literal['Vin']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-136"
    descripteur: str = "vin"
class Eaudevie(BaseModel):
    sous_descripteur: Literal['Eaudevie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-223"
    descripteur: str = "eau-de-vie"
class Horticulture(BaseModel):
    sous_descripteur: Union['Fruit', 'Fleur', 'ProduitMaraicher'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-631"
    descripteur: str = "horticulture"
class Fruit(BaseModel):
    sous_descripteur: Literal['Fruit']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-162"
    descripteur: str = "fruit"
class Fleur(BaseModel):
    sous_descripteur: Literal['Fleur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-604"
    descripteur: str = "fleur"
class ProduitMaraicher(BaseModel):
    sous_descripteur: Literal['ProduitMaraicher']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1220"
    descripteur: str = "produit maraîcher"
class CalamiteAgricole(BaseModel):
    sous_descripteur: Union['Secheresse', 'Gelee', 'Grele'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-202"
    descripteur: str = "calamité agricole"
class Secheresse(BaseModel):
    sous_descripteur: Literal['Secheresse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-309"
    descripteur: str = "sécheresse"
class Gelee(BaseModel):
    sous_descripteur: Literal['Gelee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-854"
    descripteur: str = "gelée"
class Grele(BaseModel):
    sous_descripteur: Literal['Grele']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-683"
    descripteur: str = "grêle"
class ProtectionDesVegetaux(BaseModel):
    sous_descripteur: Union['MaladieDesVegetaux', 'AnimalNuisible'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-289"
    descripteur: str = "protection des végétaux"
class MaladieDesVegetaux(BaseModel):
    sous_descripteur: Literal['MaladieDesVegetaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-982"
    descripteur: str = "maladie des végétaux"
class AnimalNuisible(BaseModel):
    sous_descripteur: Literal['AnimalNuisible']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-461"
    descripteur: str = "animal nuisible"
class Apiculture(BaseModel):
    sous_descripteur: Literal['Apiculture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-415"
    descripteur: str = "apiculture"
class Aquaculture(BaseModel):
    sous_descripteur: Union['Pisciculture', 'Conchyliculture'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-986"
    descripteur: str = "aquaculture"
class Pisciculture(BaseModel):
    sous_descripteur: Literal['Pisciculture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-531"
    descripteur: str = "pisciculture"
class Conchyliculture(BaseModel):
    sous_descripteur: Literal['Conchyliculture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-890"
    descripteur: str = "conchyliculture"
class Peche(BaseModel):
    sous_descripteur: Union['PecheMaritime', 'PecheEnEauDouce', 'Poisson'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-653"
    descripteur: str = "pêche"
class PecheMaritime(BaseModel):
    sous_descripteur: Literal['PecheMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1395"
    descripteur: str = "pêche maritime"
class PecheEnEauDouce(BaseModel):
    sous_descripteur: Literal['PecheEnEauDouce']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-425"
    descripteur: str = "pêche en eau douce"
class Poisson(BaseModel):
    sous_descripteur: Literal['Poisson']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1067"
    descripteur: str = "poisson"
