from pydantic import BaseModel
from typing import Union, Literal

class Internat(BaseModel):
    terme_specifique: Literal['Internat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1474"
    descripteur: str = "internat"

class BataillonScolaire(BaseModel):
    terme_specifique: Literal['BataillonScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1225"
    descripteur: str = "bataillon scolaire"

class AccidentScolaire(BaseModel):
    terme_specifique: Literal['AccidentScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1142"
    descripteur: str = "accident scolaire"

class RentreeScolaire(BaseModel):
    terme_specifique: Literal['RentreeScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1282"
    descripteur: str = "rentrée scolaire"

class ServiceEducatif(BaseModel):
    terme_specifique: Literal['ServiceEducatif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-904"
    descripteur: str = "service éducatif"

class AccueilPeriscolaire(BaseModel):
    terme_specifique: Literal['AccueilPeriscolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-895"
    descripteur: str = "accueil périscolaire"

class AbsenteismeScolaire(BaseModel):
    terme_specifique: Literal['AbsenteismeScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-602"
    descripteur: str = "absentéisme scolaire"

class ParentDeleve(BaseModel):
    terme_specifique: Literal['ParentDeleve']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-498"
    descripteur: str = "parent d'élève"

class ProjetEducatif(BaseModel):
    terme_specifique: Literal['ProjetEducatif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-474"
    descripteur: str = "projet éducatif"

class Interne(BaseModel):
    terme_specifique: Literal['Interne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1244"
    descripteur: str = "interne"

class Apprenti(BaseModel):
    terme_specifique: Literal['Apprenti']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1377"
    descripteur: str = "apprenti"

class Etudiant(BaseModel):
    terme_specifique: Literal['Etudiant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-833"
    descripteur: str = "étudiant"

class Eleve(BaseModel):
    terme_specifique: Literal['Eleve']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-428"
    descripteur: str = "élève"

class PopulationScolaire(BaseModel):
    terme_specifique: Union['Eleve', 'Etudiant', 'Apprenti', 'Interne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-559"
    descripteur: str = "population scolaire"

class Psychopedagogie(BaseModel):
    terme_specifique: Literal['Psychopedagogie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1353"
    descripteur: str = "psychopédagogie"

class MedecineScolaire(BaseModel):
    terme_specifique: Union['Psychopedagogie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-998"
    descripteur: str = "médecine scolaire"

class EchecScolaire(BaseModel):
    terme_specifique: Literal['EchecScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-265"
    descripteur: str = "échec scolaire"

class VoyageScolaire(BaseModel):
    terme_specifique: Literal['VoyageScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-222"
    descripteur: str = "voyage scolaire"

class ClasseDeDecouverte(BaseModel):
    terme_specifique: Literal['ClasseDeDecouverte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-145"
    descripteur: str = "classe de découverte"

class DistributionDesPrix(BaseModel):
    terme_specifique: Literal['DistributionDesPrix']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-141"
    descripteur: str = "distribution des prix"

class EducationSpeciale(BaseModel):
    terme_specifique: Literal['EducationSpeciale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-677"
    descripteur: str = "éducation spéciale"

class ResidenceUniversitaire(BaseModel):
    terme_specifique: Literal['ResidenceUniversitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-865"
    descripteur: str = "résidence universitaire"

class FournitureScolaire(BaseModel):
    terme_specifique: Literal['FournitureScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-665"
    descripteur: str = "fourniture scolaire"

class RestaurationScolaire(BaseModel):
    terme_specifique: Literal['RestaurationScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1199"
    descripteur: str = "restauration scolaire"

class BourseDetudes(BaseModel):
    terme_specifique: Literal['BourseDetudes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-256"
    descripteur: str = "bourse d'études"

class TransportScolaire(BaseModel):
    terme_specifique: Literal['TransportScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-245"
    descripteur: str = "transport scolaire"

class OeuvresScolaires(BaseModel):
    terme_specifique: Union['TransportScolaire', 'BourseDetudes', 'RestaurationScolaire', 'FournitureScolaire', 'ResidenceUniversitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1296"
    descripteur: str = "oeuvres scolaires"

class CongesScolaires(BaseModel):
    terme_specifique: Literal['CongesScolaires']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-62"
    descripteur: str = "congés scolaires"

class RythmeScolaire(BaseModel):
    terme_specifique: Union['CongesScolaires']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1404"
    descripteur: str = "rythme scolaire"

class VieScolaire(BaseModel):
    terme_specifique: Union['RythmeScolaire', 'OeuvresScolaires', 'EducationSpeciale', 'DistributionDesPrix', 'ClasseDeDecouverte', 'VoyageScolaire', 'EchecScolaire', 'MedecineScolaire', 'PopulationScolaire', 'ProjetEducatif', 'ParentDeleve', 'AbsenteismeScolaire', 'AccueilPeriscolaire', 'ServiceEducatif', 'RentreeScolaire', 'AccidentScolaire', 'BataillonScolaire', 'Internat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1121"
    descripteur: str = "vie scolaire"

class EducationSportive(BaseModel):
    terme_specifique: Literal['EducationSportive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-798"
    descripteur: str = "éducation sportive"

class MaterielPedagogique(BaseModel):
    terme_specifique: Literal['MaterielPedagogique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1203"
    descripteur: str = "matériel pédagogique"

class BibliothequeScolaire(BaseModel):
    terme_specifique: Literal['BibliothequeScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-787"
    descripteur: str = "bibliothèque scolaire"

class Pedagogie(BaseModel):
    terme_specifique: Union['BibliothequeScolaire', 'MaterielPedagogique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-610"
    descripteur: str = "pédagogie"

class EnseignementTechnique(BaseModel):
    terme_specifique: Literal['EnseignementTechnique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1041"
    descripteur: str = "enseignement technique"

class Apprentissage(BaseModel):
    terme_specifique: Literal['Apprentissage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-958"
    descripteur: str = "apprentissage"

class EnseignementHospitalier(BaseModel):
    terme_specifique: Literal['EnseignementHospitalier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-651"
    descripteur: str = "enseignement hospitalier"

class EnseignementCommercial(BaseModel):
    terme_specifique: Literal['EnseignementCommercial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-280"
    descripteur: str = "enseignement commercial"

class EnseignementAgricole(BaseModel):
    terme_specifique: Literal['EnseignementAgricole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1405"
    descripteur: str = "enseignement agricole"

class EnseignementProfessionnel(BaseModel):
    terme_specifique: Union['EnseignementAgricole', 'EnseignementCommercial', 'EnseignementHospitalier', 'Apprentissage', 'EnseignementTechnique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1331"
    descripteur: str = "enseignement professionnel"

class TravailManuel(BaseModel):
    terme_specifique: Literal['TravailManuel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1260"
    descripteur: str = "travail manuel"

class EnseignementMenager(BaseModel):
    terme_specifique: Literal['EnseignementMenager']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1398"
    descripteur: str = "enseignement ménager"

class InstructionCivique(BaseModel):
    terme_specifique: Literal['InstructionCivique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-792"
    descripteur: str = "instruction civique"

class LangueEtrangere(BaseModel):
    terme_specifique: Literal['LangueEtrangere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-433"
    descripteur: str = "langue étrangère"

class EducationSexuelle(BaseModel):
    terme_specifique: Literal['EducationSexuelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-208"
    descripteur: str = "éducation sexuelle"

class ProgrammeScolaire(BaseModel):
    terme_specifique: Union['EducationSexuelle', 'LangueEtrangere', 'InstructionCivique', 'EnseignementMenager', 'TravailManuel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-940"
    descripteur: str = "programme scolaire"

class EnseignementReligieux(BaseModel):
    terme_specifique: Literal['EnseignementReligieux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-232"
    descripteur: str = "enseignement religieux"

class EnseignementArtistique(BaseModel):
    terme_specifique: Literal['EnseignementArtistique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1228"
    descripteur: str = "enseignement artistique"

class DisciplineUniversitaire(BaseModel):
    terme_specifique: Literal['DisciplineUniversitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-436"
    descripteur: str = "discipline universitaire"

class Enseignement(BaseModel):
    terme_specifique: Union['DisciplineUniversitaire', 'EnseignementArtistique', 'EnseignementReligieux', 'ProgrammeScolaire', 'EnseignementProfessionnel', 'Pedagogie', 'EducationSportive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-881"
    descripteur: str = "enseignement"

class ChefDetablissementScolaire(BaseModel):
    terme_specifique: Literal['ChefDetablissementScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1468"
    descripteur: str = "chef d'établissement scolaire"

class EnseignementADistance(BaseModel):
    terme_specifique: Literal['EnseignementADistance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-574"
    descripteur: str = "enseignement à distance"

class OrientationScolaire(BaseModel):
    terme_specifique: Literal['OrientationScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1349"
    descripteur: str = "orientation scolaire"

class EnseignementPreelementaire(BaseModel):
    terme_specifique: Literal['EnseignementPreelementaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-857"
    descripteur: str = "enseignement préélémentaire"

class EnseignementPrive(BaseModel):
    terme_specifique: Literal['EnseignementPrive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-952"
    descripteur: str = "enseignement privé"

class Examen(BaseModel):
    terme_specifique: Literal['Examen']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1077"
    descripteur: str = "examen"

class EnseignementSecondaire(BaseModel):
    terme_specifique: Literal['EnseignementSecondaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1306"
    descripteur: str = "enseignement secondaire"

class EnseignementPublic(BaseModel):
    terme_specifique: Literal['EnseignementPublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-954"
    descripteur: str = "enseignement public"

class EnseignementElementaire(BaseModel):
    terme_specifique: Literal['EnseignementElementaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-379"
    descripteur: str = "enseignement élémentaire"

class TitreUniversitaire(BaseModel):
    terme_specifique: Literal['TitreUniversitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-586"
    descripteur: str = "titre universitaire"

class DroitsDeScolarite(BaseModel):
    terme_specifique: Literal['DroitsDeScolarite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-294"
    descripteur: str = "droits de scolarité"

class TroubleUniversitaire(BaseModel):
    terme_specifique: Literal['TroubleUniversitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-976"
    descripteur: str = "trouble universitaire"

class EnseignementSuperieur(BaseModel):
    terme_specifique: Union['TroubleUniversitaire', 'DroitsDeScolarite', 'TitreUniversitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-251"
    descripteur: str = "enseignement supérieur"

class CarteScolaire(BaseModel):
    terme_specifique: Literal['CarteScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-198"
    descripteur: str = "carte scolaire"

class EcoleCentrale(BaseModel):
    terme_specifique: Literal['EcoleCentrale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1287"
    descripteur: str = "école centrale"

class College(BaseModel):
    terme_specifique: Literal['College']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-715"
    descripteur: str = "collège"

class Ecole(BaseModel):
    terme_specifique: Literal['Ecole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1340"
    descripteur: str = "école"

class Lycee(BaseModel):
    terme_specifique: Literal['Lycee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-580"
    descripteur: str = "lycée"

class CentreDeFormation(BaseModel):
    terme_specifique: Literal['CentreDeFormation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-304"
    descripteur: str = "centre de formation"

class GrandeEcole(BaseModel):
    terme_specifique: Literal['GrandeEcole']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-240"
    descripteur: str = "grande école"

class EtablissementDeFormationDesMaitres(BaseModel):
    terme_specifique: Literal['EtablissementDeFormationDesMaitres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-186"
    descripteur: str = "établissement de formation des maîtres"

class Universite(BaseModel):
    terme_specifique: Literal['Universite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-532"
    descripteur: str = "université"

class ConstructionScolaire(BaseModel):
    terme_specifique: Literal['ConstructionScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-921"
    descripteur: str = "construction scolaire"

class EtablissementDenseignement(BaseModel):
    terme_specifique: Union['ConstructionScolaire', 'Universite', 'EtablissementDeFormationDesMaitres', 'GrandeEcole', 'CentreDeFormation', 'Lycee', 'Ecole', 'College', 'EcoleCentrale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-662"
    descripteur: str = "établissement d'enseignement"

class ConflitScolaire(BaseModel):
    terme_specifique: Literal['ConflitScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1106"
    descripteur: str = "conflit scolaire"

class Professeur(BaseModel):
    terme_specifique: Literal['Professeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-300"
    descripteur: str = "professeur"

class MaitreDapprentissage(BaseModel):
    terme_specifique: Literal['MaitreDapprentissage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-614"
    descripteur: str = "maître d'apprentissage"

class EducateurSportif(BaseModel):
    terme_specifique: Literal['EducateurSportif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1456"
    descripteur: str = "éducateur sportif"

class Instituteur(BaseModel):
    terme_specifique: Literal['Instituteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1029"
    descripteur: str = "instituteur"

class Educateur(BaseModel):
    terme_specifique: Literal['Educateur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-350"
    descripteur: str = "éducateur"

class Enseignant(BaseModel):
    terme_specifique: Union['Educateur', 'Instituteur', 'EducateurSportif', 'MaitreDapprentissage', 'Professeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-38"
    descripteur: str = "enseignant"

class OrganisationScolaire(BaseModel):
    terme_specifique: Union['Enseignant', 'ConflitScolaire', 'EtablissementDenseignement', 'CarteScolaire', 'EnseignementSuperieur', 'EnseignementElementaire', 'EnseignementPublic', 'EnseignementSecondaire', 'Examen', 'EnseignementPrive', 'EnseignementPreelementaire', 'OrientationScolaire', 'EnseignementADistance', 'ChefDetablissementScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-499"
    descripteur: str = "organisation scolaire"

class DisciplineScientifique(BaseModel):
    terme_specifique: Literal['DisciplineScientifique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-287"
    descripteur: str = "discipline scientifique"

class SciencesPhysiques(BaseModel):
    terme_specifique: Literal['SciencesPhysiques']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1473"
    descripteur: str = "sciences physiques"

class SciencesDeLaVieEtDeLaTerre(BaseModel):
    terme_specifique: Literal['SciencesDeLaVieEtDeLaTerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1472"
    descripteur: str = "sciences de la vie et de la terre"

class SciencesAuxiliairesDeLhistoire(BaseModel):
    terme_specifique: Literal['SciencesAuxiliairesDeLhistoire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1477"
    descripteur: str = "sciences auxiliaires de l'histoire"

class HistoireLocale(BaseModel):
    terme_specifique: Literal['HistoireLocale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1476"
    descripteur: str = "histoire locale"

class HistoireDesFamilles(BaseModel):
    terme_specifique: Literal['HistoireDesFamilles']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1475"
    descripteur: str = "histoire des familles"

class RechercheHistorique(BaseModel):
    terme_specifique: Union['HistoireDesFamilles', 'HistoireLocale', 'SciencesAuxiliairesDeLhistoire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1471"
    descripteur: str = "recherche historique"

class ExpeditionScientifique(BaseModel):
    terme_specifique: Literal['ExpeditionScientifique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1470"
    descripteur: str = "expédition scientifique"

class Chercheur(BaseModel):
    terme_specifique: Literal['Chercheur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-448"
    descripteur: str = "chercheur"

class OrganismeDeRecherche(BaseModel):
    terme_specifique: Literal['OrganismeDeRecherche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-981"
    descripteur: str = "organisme de recherche"

class RechercheFondamentale(BaseModel):
    terme_specifique: Literal['RechercheFondamentale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-319"
    descripteur: str = "recherche fondamentale"

class SciencesHumaines(BaseModel):
    terme_specifique: Literal['SciencesHumaines']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1005"
    descripteur: str = "sciences humaines"

class SocieteSavante(BaseModel):
    terme_specifique: Literal['SocieteSavante']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1073"
    descripteur: str = "société savante"

class ReunionScientifique(BaseModel):
    terme_specifique: Literal['ReunionScientifique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-676"
    descripteur: str = "réunion scientifique"

class DecouverteScientifique(BaseModel):
    terme_specifique: Literal['DecouverteScientifique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-618"
    descripteur: str = "découverte scientifique"

class OrganismeGenetiquementModifie(BaseModel):
    terme_specifique: Literal['OrganismeGenetiquementModifie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1007"
    descripteur: str = "organisme génétiquement modifié"

class CultureExperimentale(BaseModel):
    terme_specifique: Literal['CultureExperimentale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1356"
    descripteur: str = "culture expérimentale"

class RechercheAppliquee(BaseModel):
    terme_specifique: Union['CultureExperimentale', 'OrganismeGenetiquementModifie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1413"
    descripteur: str = "recherche appliquée"

class RechercheScientifique(BaseModel):
    terme_specifique: Union['RechercheAppliquee', 'DecouverteScientifique', 'ReunionScientifique', 'SocieteSavante', 'SciencesHumaines', 'RechercheFondamentale', 'OrganismeDeRecherche', 'Chercheur', 'ExpeditionScientifique', 'RechercheHistorique', 'SciencesDeLaVieEtDeLaTerre', 'SciencesPhysiques', 'DisciplineScientifique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-3"
    descripteur: str = "recherche scientifique"

class EducationEtSciences(BaseModel):
    terme_specifique: Union['RechercheScientifique', 'OrganisationScolaire', 'Enseignement', 'VieScolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1302"
    descripteur: str = "éducation et sciences"
