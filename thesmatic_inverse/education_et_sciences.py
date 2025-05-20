from pydantic import BaseModel
from typing import Union, Literal

class Internat(BaseModel):
    sous_descripteur: Literal['Internat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1474"
    descripteur: str = "internat"

class BataillonScolaire(BaseModel):
    sous_descripteur: Literal['BataillonScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1225"
    descripteur: str = "bataillon scolaire"

class AccidentScolaire(BaseModel):
    sous_descripteur: Literal['AccidentScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1142"
    descripteur: str = "accident scolaire"

class RentreeScolaire(BaseModel):
    sous_descripteur: Literal['RentreeScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1282"
    descripteur: str = "rentrée scolaire"

class ServiceEducatif(BaseModel):
    sous_descripteur: Literal['ServiceEducatif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-904"
    descripteur: str = "service éducatif"

class AccueilPeriscolaire(BaseModel):
    sous_descripteur: Literal['AccueilPeriscolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-895"
    descripteur: str = "accueil périscolaire"

class AbsenteismeScolaire(BaseModel):
    sous_descripteur: Literal['AbsenteismeScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-602"
    descripteur: str = "absentéisme scolaire"

class ParentDeleve(BaseModel):
    sous_descripteur: Literal['ParentDeleve']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-498"
    descripteur: str = "parent d'élève"

class ProjetEducatif(BaseModel):
    sous_descripteur: Literal['ProjetEducatif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-474"
    descripteur: str = "projet éducatif"

class Interne(BaseModel):
    sous_descripteur: Literal['Interne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1244"
    descripteur: str = "interne"

class Apprenti(BaseModel):
    sous_descripteur: Literal['Apprenti']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1377"
    descripteur: str = "apprenti"

class Etudiant(BaseModel):
    sous_descripteur: Literal['Etudiant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-833"
    descripteur: str = "étudiant"

class Eleve(BaseModel):
    sous_descripteur: Literal['Eleve']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-428"
    descripteur: str = "élève"

class PopulationScolaire(BaseModel):
    sous_descripteur: Union['Eleve', 'Etudiant', 'Apprenti', 'Interne'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-559"
    descripteur: str = "population scolaire"

class Psychopedagogie(BaseModel):
    sous_descripteur: Literal['Psychopedagogie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1353"
    descripteur: str = "psychopédagogie"

class MedecineScolaire(BaseModel):
    sous_descripteur: Union['Psychopedagogie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-998"
    descripteur: str = "médecine scolaire"

class EchecScolaire(BaseModel):
    sous_descripteur: Literal['EchecScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-265"
    descripteur: str = "échec scolaire"

class VoyageScolaire(BaseModel):
    sous_descripteur: Literal['VoyageScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-222"
    descripteur: str = "voyage scolaire"

class ClasseDeDecouverte(BaseModel):
    sous_descripteur: Literal['ClasseDeDecouverte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-145"
    descripteur: str = "classe de découverte"

class DistributionDesPrix(BaseModel):
    sous_descripteur: Literal['DistributionDesPrix']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-141"
    descripteur: str = "distribution des prix"

class EducationSpeciale(BaseModel):
    sous_descripteur: Literal['EducationSpeciale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-677"
    descripteur: str = "éducation spéciale"

class ResidenceUniversitaire(BaseModel):
    sous_descripteur: Literal['ResidenceUniversitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-865"
    descripteur: str = "résidence universitaire"

class FournitureScolaire(BaseModel):
    sous_descripteur: Literal['FournitureScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-665"
    descripteur: str = "fourniture scolaire"

class RestaurationScolaire(BaseModel):
    sous_descripteur: Literal['RestaurationScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1199"
    descripteur: str = "restauration scolaire"

class BourseDetudes(BaseModel):
    sous_descripteur: Literal['BourseDetudes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-256"
    descripteur: str = "bourse d'études"

class TransportScolaire(BaseModel):
    sous_descripteur: Literal['TransportScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-245"
    descripteur: str = "transport scolaire"

class OeuvresScolaires(BaseModel):
    sous_descripteur: Union['TransportScolaire', 'BourseDetudes', 'RestaurationScolaire', 'FournitureScolaire', 'ResidenceUniversitaire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1296"
    descripteur: str = "oeuvres scolaires"

class CongesScolaires(BaseModel):
    sous_descripteur: Literal['CongesScolaires']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-62"
    descripteur: str = "congés scolaires"

class RythmeScolaire(BaseModel):
    sous_descripteur: Union['CongesScolaires'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1404"
    descripteur: str = "rythme scolaire"

class VieScolaire(BaseModel):
    sous_descripteur: Union['RythmeScolaire', 'OeuvresScolaires', 'EducationSpeciale', 'DistributionDesPrix', 'ClasseDeDecouverte', 'VoyageScolaire', 'EchecScolaire', 'MedecineScolaire', 'PopulationScolaire', 'ProjetEducatif', 'ParentDeleve', 'AbsenteismeScolaire', 'AccueilPeriscolaire', 'ServiceEducatif', 'RentreeScolaire', 'AccidentScolaire', 'BataillonScolaire', 'Internat'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1121"
    descripteur: str = "vie scolaire"

class EducationSportive(BaseModel):
    sous_descripteur: Literal['EducationSportive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-798"
    descripteur: str = "éducation sportive"

class MaterielPedagogique(BaseModel):
    sous_descripteur: Literal['MaterielPedagogique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1203"
    descripteur: str = "matériel pédagogique"

class BibliothequeScolaire(BaseModel):
    sous_descripteur: Literal['BibliothequeScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-787"
    descripteur: str = "bibliothèque scolaire"

class Pedagogie(BaseModel):
    sous_descripteur: Union['BibliothequeScolaire', 'MaterielPedagogique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-610"
    descripteur: str = "pédagogie"

class EnseignementTechnique(BaseModel):
    sous_descripteur: Literal['EnseignementTechnique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1041"
    descripteur: str = "enseignement technique"

class Apprentissage(BaseModel):
    sous_descripteur: Literal['Apprentissage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-958"
    descripteur: str = "apprentissage"

class EnseignementHospitalier(BaseModel):
    sous_descripteur: Literal['EnseignementHospitalier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-651"
    descripteur: str = "enseignement hospitalier"

class EnseignementCommercial(BaseModel):
    sous_descripteur: Literal['EnseignementCommercial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-280"
    descripteur: str = "enseignement commercial"

class EnseignementAgricole(BaseModel):
    sous_descripteur: Literal['EnseignementAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1405"
    descripteur: str = "enseignement agricole"

class EnseignementProfessionnel(BaseModel):
    sous_descripteur: Union['EnseignementAgricole', 'EnseignementCommercial', 'EnseignementHospitalier', 'Apprentissage', 'EnseignementTechnique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1331"
    descripteur: str = "enseignement professionnel"

class TravailManuel(BaseModel):
    sous_descripteur: Literal['TravailManuel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1260"
    descripteur: str = "travail manuel"

class EnseignementMenager(BaseModel):
    sous_descripteur: Literal['EnseignementMenager']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1398"
    descripteur: str = "enseignement ménager"

class InstructionCivique(BaseModel):
    sous_descripteur: Literal['InstructionCivique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-792"
    descripteur: str = "instruction civique"

class LangueEtrangere(BaseModel):
    sous_descripteur: Literal['LangueEtrangere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-433"
    descripteur: str = "langue étrangère"

class EducationSexuelle(BaseModel):
    sous_descripteur: Literal['EducationSexuelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-208"
    descripteur: str = "éducation sexuelle"

class ProgrammeScolaire(BaseModel):
    sous_descripteur: Union['EducationSexuelle', 'LangueEtrangere', 'InstructionCivique', 'EnseignementMenager', 'TravailManuel'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-940"
    descripteur: str = "programme scolaire"

class EnseignementReligieux(BaseModel):
    sous_descripteur: Literal['EnseignementReligieux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-232"
    descripteur: str = "enseignement religieux"

class EnseignementArtistique(BaseModel):
    sous_descripteur: Literal['EnseignementArtistique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1228"
    descripteur: str = "enseignement artistique"

class DisciplineUniversitaire(BaseModel):
    sous_descripteur: Literal['DisciplineUniversitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-436"
    descripteur: str = "discipline universitaire"

class Enseignement(BaseModel):
    sous_descripteur: Union['DisciplineUniversitaire', 'EnseignementArtistique', 'EnseignementReligieux', 'ProgrammeScolaire', 'EnseignementProfessionnel', 'Pedagogie', 'EducationSportive'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-881"
    descripteur: str = "enseignement"

class ChefDetablissementScolaire(BaseModel):
    sous_descripteur: Literal['ChefDetablissementScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1468"
    descripteur: str = "chef d'établissement scolaire"

class EnseignementADistance(BaseModel):
    sous_descripteur: Literal['EnseignementADistance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-574"
    descripteur: str = "enseignement à distance"

class OrientationScolaire(BaseModel):
    sous_descripteur: Literal['OrientationScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1349"
    descripteur: str = "orientation scolaire"

class EnseignementPreelementaire(BaseModel):
    sous_descripteur: Literal['EnseignementPreelementaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-857"
    descripteur: str = "enseignement préélémentaire"

class EnseignementPrive(BaseModel):
    sous_descripteur: Literal['EnseignementPrive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-952"
    descripteur: str = "enseignement privé"

class Examen(BaseModel):
    sous_descripteur: Literal['Examen']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1077"
    descripteur: str = "examen"

class EnseignementSecondaire(BaseModel):
    sous_descripteur: Literal['EnseignementSecondaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1306"
    descripteur: str = "enseignement secondaire"

class EnseignementPublic(BaseModel):
    sous_descripteur: Literal['EnseignementPublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-954"
    descripteur: str = "enseignement public"

class EnseignementElementaire(BaseModel):
    sous_descripteur: Literal['EnseignementElementaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-379"
    descripteur: str = "enseignement élémentaire"

class TitreUniversitaire(BaseModel):
    sous_descripteur: Literal['TitreUniversitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-586"
    descripteur: str = "titre universitaire"

class DroitsDeScolarite(BaseModel):
    sous_descripteur: Literal['DroitsDeScolarite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-294"
    descripteur: str = "droits de scolarité"

class TroubleUniversitaire(BaseModel):
    sous_descripteur: Literal['TroubleUniversitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-976"
    descripteur: str = "trouble universitaire"

class EnseignementSuperieur(BaseModel):
    sous_descripteur: Union['TroubleUniversitaire', 'DroitsDeScolarite', 'TitreUniversitaire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-251"
    descripteur: str = "enseignement supérieur"

class CarteScolaire(BaseModel):
    sous_descripteur: Literal['CarteScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-198"
    descripteur: str = "carte scolaire"

class EcoleCentrale(BaseModel):
    sous_descripteur: Literal['EcoleCentrale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1287"
    descripteur: str = "école centrale"

class College(BaseModel):
    sous_descripteur: Literal['College']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-715"
    descripteur: str = "collège"

class Ecole(BaseModel):
    sous_descripteur: Literal['Ecole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1340"
    descripteur: str = "école"

class Lycee(BaseModel):
    sous_descripteur: Literal['Lycee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-580"
    descripteur: str = "lycée"

class CentreDeFormation(BaseModel):
    sous_descripteur: Literal['CentreDeFormation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-304"
    descripteur: str = "centre de formation"

class GrandeEcole(BaseModel):
    sous_descripteur: Literal['GrandeEcole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-240"
    descripteur: str = "grande école"

class EtablissementDeFormationDesMaitres(BaseModel):
    sous_descripteur: Literal['EtablissementDeFormationDesMaitres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-186"
    descripteur: str = "établissement de formation des maîtres"

class Universite(BaseModel):
    sous_descripteur: Literal['Universite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-532"
    descripteur: str = "université"

class ConstructionScolaire(BaseModel):
    sous_descripteur: Literal['ConstructionScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-921"
    descripteur: str = "construction scolaire"

class EtablissementDenseignement(BaseModel):
    sous_descripteur: Union['ConstructionScolaire', 'Universite', 'EtablissementDeFormationDesMaitres', 'GrandeEcole', 'CentreDeFormation', 'Lycee', 'Ecole', 'College', 'EcoleCentrale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-662"
    descripteur: str = "établissement d'enseignement"

class ConflitScolaire(BaseModel):
    sous_descripteur: Literal['ConflitScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1106"
    descripteur: str = "conflit scolaire"

class Professeur(BaseModel):
    sous_descripteur: Literal['Professeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-300"
    descripteur: str = "professeur"

class MaitreDapprentissage(BaseModel):
    sous_descripteur: Literal['MaitreDapprentissage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-614"
    descripteur: str = "maître d'apprentissage"

class EducateurSportif(BaseModel):
    sous_descripteur: Literal['EducateurSportif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1456"
    descripteur: str = "éducateur sportif"

class Instituteur(BaseModel):
    sous_descripteur: Literal['Instituteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1029"
    descripteur: str = "instituteur"

class Educateur(BaseModel):
    sous_descripteur: Literal['Educateur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-350"
    descripteur: str = "éducateur"

class Enseignant(BaseModel):
    sous_descripteur: Union['Educateur', 'Instituteur', 'EducateurSportif', 'MaitreDapprentissage', 'Professeur'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-38"
    descripteur: str = "enseignant"

class OrganisationScolaire(BaseModel):
    sous_descripteur: Union['Enseignant', 'ConflitScolaire', 'EtablissementDenseignement', 'CarteScolaire', 'EnseignementSuperieur', 'EnseignementElementaire', 'EnseignementPublic', 'EnseignementSecondaire', 'Examen', 'EnseignementPrive', 'EnseignementPreelementaire', 'OrientationScolaire', 'EnseignementADistance', 'ChefDetablissementScolaire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-499"
    descripteur: str = "organisation scolaire"

class DisciplineScientifique(BaseModel):
    sous_descripteur: Literal['DisciplineScientifique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-287"
    descripteur: str = "discipline scientifique"

class SciencesPhysiques(BaseModel):
    sous_descripteur: Literal['SciencesPhysiques']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1473"
    descripteur: str = "sciences physiques"

class SciencesDeLaVieEtDeLaTerre(BaseModel):
    sous_descripteur: Literal['SciencesDeLaVieEtDeLaTerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1472"
    descripteur: str = "sciences de la vie et de la terre"

class SciencesAuxiliairesDeLhistoire(BaseModel):
    sous_descripteur: Literal['SciencesAuxiliairesDeLhistoire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1477"
    descripteur: str = "sciences auxiliaires de l'histoire"

class HistoireLocale(BaseModel):
    sous_descripteur: Literal['HistoireLocale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1476"
    descripteur: str = "histoire locale"

class HistoireDesFamilles(BaseModel):
    sous_descripteur: Literal['HistoireDesFamilles']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1475"
    descripteur: str = "histoire des familles"

class RechercheHistorique(BaseModel):
    sous_descripteur: Union['HistoireDesFamilles', 'HistoireLocale', 'SciencesAuxiliairesDeLhistoire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1471"
    descripteur: str = "recherche historique"

class ExpeditionScientifique(BaseModel):
    sous_descripteur: Literal['ExpeditionScientifique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1470"
    descripteur: str = "expédition scientifique"

class Chercheur(BaseModel):
    sous_descripteur: Literal['Chercheur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-448"
    descripteur: str = "chercheur"

class OrganismeDeRecherche(BaseModel):
    sous_descripteur: Literal['OrganismeDeRecherche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-981"
    descripteur: str = "organisme de recherche"

class RechercheFondamentale(BaseModel):
    sous_descripteur: Literal['RechercheFondamentale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-319"
    descripteur: str = "recherche fondamentale"

class SciencesHumaines(BaseModel):
    sous_descripteur: Literal['SciencesHumaines']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1005"
    descripteur: str = "sciences humaines"

class SocieteSavante(BaseModel):
    sous_descripteur: Literal['SocieteSavante']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1073"
    descripteur: str = "société savante"

class ReunionScientifique(BaseModel):
    sous_descripteur: Literal['ReunionScientifique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-676"
    descripteur: str = "réunion scientifique"

class DecouverteScientifique(BaseModel):
    sous_descripteur: Literal['DecouverteScientifique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-618"
    descripteur: str = "découverte scientifique"

class OrganismeGenetiquementModifie(BaseModel):
    sous_descripteur: Literal['OrganismeGenetiquementModifie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1007"
    descripteur: str = "organisme génétiquement modifié"

class CultureExperimentale(BaseModel):
    sous_descripteur: Literal['CultureExperimentale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1356"
    descripteur: str = "culture expérimentale"

class RechercheAppliquee(BaseModel):
    sous_descripteur: Union['CultureExperimentale', 'OrganismeGenetiquementModifie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1413"
    descripteur: str = "recherche appliquée"

class RechercheScientifique(BaseModel):
    sous_descripteur: Union['RechercheAppliquee', 'DecouverteScientifique', 'ReunionScientifique', 'SocieteSavante', 'SciencesHumaines', 'RechercheFondamentale', 'OrganismeDeRecherche', 'Chercheur', 'ExpeditionScientifique', 'RechercheHistorique', 'SciencesDeLaVieEtDeLaTerre', 'SciencesPhysiques', 'DisciplineScientifique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-3"
    descripteur: str = "recherche scientifique"

class EducationEtSciences(BaseModel):
    sous_descripteur: Union['RechercheScientifique', 'OrganisationScolaire', 'Enseignement', 'VieScolaire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1302"
    descripteur: str = "éducation et sciences"
