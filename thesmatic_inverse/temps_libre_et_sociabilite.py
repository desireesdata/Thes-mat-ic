from pydantic import BaseModel, Field
from typing import Union, Literal

class Jeuconcours(BaseModel):
    sous_descripteur: Literal['Jeuconcours']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-814"
    descripteur: str = "jeu-concours"

class Tauromachie(BaseModel):
    sous_descripteur: Literal['Tauromachie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-393"
    descripteur: str = "tauromachie"

class AppareilDeJeu(BaseModel):
    sous_descripteur: Literal['AppareilDeJeu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1309"
    descripteur: str = "appareil de jeu"

class JeuDeCartes(BaseModel):
    sous_descripteur: Literal['JeuDeCartes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1304"
    descripteur: str = "jeu de cartes"

class CourseHippique(BaseModel):
    sous_descripteur: Literal['CourseHippique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-703"
    descripteur: str = "course hippique"

class Loterie(BaseModel):
    sous_descripteur: Literal['Loterie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-348"
    descripteur: str = "loterie"

class Casino(BaseModel):
    sous_descripteur: Literal['Casino']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-933"
    descripteur: str = "casino"

class Jeuxetparis(BaseModel):
    sous_descripteur: Union['Casino', 'Loterie', 'CourseHippique', 'JeuDeCartes', 'AppareilDeJeu'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1060"
    descripteur: str = "jeux-et-paris"

class MouvementDeJeunesse(BaseModel):
    sous_descripteur: Literal['MouvementDeJeunesse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-709"
    descripteur: str = "mouvement de jeunesse"

class AssociationDePeche(BaseModel):
    sous_descripteur: Literal['AssociationDePeche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-876"
    descripteur: str = "association de pêche"

class Pecheur(BaseModel):
    sous_descripteur: Literal['Pecheur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-381"
    descripteur: str = "pêcheur"

class LotDePeche(BaseModel):
    sous_descripteur: Literal['LotDePeche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-340"
    descripteur: str = "lot de pêche"

class PecheALaLigne(BaseModel):
    sous_descripteur: Union['LotDePeche', 'Pecheur', 'AssociationDePeche'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1182"
    descripteur: str = "pêche à la ligne"

class Chasseur(BaseModel):
    sous_descripteur: Literal['Chasseur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1091"
    descripteur: str = "chasseur"

class AssociationDeChasse(BaseModel):
    sous_descripteur: Literal['AssociationDeChasse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1371"
    descripteur: str = "association de chasse"

class LotDeChasse(BaseModel):
    sous_descripteur: Literal['LotDeChasse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-637"
    descripteur: str = "lot de chasse"

class Chasse(BaseModel):
    sous_descripteur: Union['LotDeChasse', 'AssociationDeChasse', 'Chasseur'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-389"
    descripteur: str = "chasse"

class ParcDeLoisirs(BaseModel):
    sous_descripteur: Literal['ParcDeLoisirs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-789"
    descripteur: str = "parc de loisirs"

class Carnaval(BaseModel):
    sous_descripteur: Literal['Carnaval']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1400"
    descripteur: str = "carnaval"

class BalPublic(BaseModel):
    sous_descripteur: Literal['BalPublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-380"
    descripteur: str = "bal public"

class FeteForaine(BaseModel):
    sous_descripteur: Literal['FeteForaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-79"
    descripteur: str = "fête foraine"

class Fete(BaseModel):
    sous_descripteur: Union['FeteForaine', 'BalPublic', 'Carnaval'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1437"
    descripteur: str = "fête"

class CentreDeLoisirs(BaseModel):
    sous_descripteur: Literal['CentreDeLoisirs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-684"
    descripteur: str = "centre de loisirs"

class NavigationDePlaisance(BaseModel):
    sous_descripteur: Literal['NavigationDePlaisance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-255"
    descripteur: str = "navigation de plaisance"

class AssociationSportive(BaseModel):
    sous_descripteur: Literal['AssociationSportive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1368"
    descripteur: str = "association sportive"

class Handisport(BaseModel):
    sous_descripteur: Literal['Handisport']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-850"
    descripteur: str = "handisport"

class InstallationSportive(BaseModel):
    sous_descripteur: Literal['InstallationSportive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-585"
    descripteur: str = "installation sportive"

class ManifestationSportive(BaseModel):
    sous_descripteur: Literal['ManifestationSportive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-926"
    descripteur: str = "manifestation sportive"

class JeuxOlympiques(BaseModel):
    sous_descripteur: Literal['JeuxOlympiques']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-221"
    descripteur: str = "jeux olympiques"

class DisciplineSportive(BaseModel):
    sous_descripteur: Literal['DisciplineSportive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-335"
    descripteur: str = "discipline sportive"

class Sport(BaseModel):
    sous_descripteur: Union['DisciplineSportive', 'JeuxOlympiques', 'ManifestationSportive', 'InstallationSportive', 'Handisport', 'AssociationSportive'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-639"
    descripteur: str = "sport"

class Loisir(BaseModel):
    sous_descripteur: Union['Sport', 'NavigationDePlaisance', 'CentreDeLoisirs', 'Fete', 'ParcDeLoisirs', 'Chasse', 'PecheALaLigne', 'MouvementDeJeunesse', 'Jeuxetparis', 'Tauromachie', 'Jeuconcours'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1173"
    descripteur: str = "loisir"

class Mobilier(BaseModel):
    sous_descripteur: Literal['Mobilier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-900"
    descripteur: str = "mobilier"

class EspaceDomestique(BaseModel):
    sous_descripteur: Literal['EspaceDomestique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-416"
    descripteur: str = "espace domestique"

class ComptabilitePrivee(BaseModel):
    sous_descripteur: Literal['ComptabilitePrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-686"
    descripteur: str = "comptabilité privée"

class Vetement(BaseModel):
    sous_descripteur: Literal['Vetement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1252"
    descripteur: str = "vêtement"

class AnimalDeCompagnie(BaseModel):
    sous_descripteur: Literal['AnimalDeCompagnie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1042"
    descripteur: str = "animal de compagnie"

class Alimentation(BaseModel):
    sous_descripteur: Literal['Alimentation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-782"
    descripteur: str = "alimentation"

class ActiviteMenagere(BaseModel):
    sous_descripteur: Literal['ActiviteMenagere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-183"
    descripteur: str = "activité ménagère"

class VieQuotidienne(BaseModel):
    sous_descripteur: Union['ActiviteMenagere', 'Alimentation', 'AnimalDeCompagnie', 'Vetement', 'ComptabilitePrivee', 'EspaceDomestique', 'Mobilier'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-373"
    descripteur: str = "vie quotidienne"

class ManifestationCulturelle(BaseModel):
    sous_descripteur: Literal['ManifestationCulturelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-834"
    descripteur: str = "manifestation culturelle"

class Artiste(BaseModel):
    sous_descripteur: Literal['Artiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-963"
    descripteur: str = "artiste"

class AnimateurSocioculturel(BaseModel):
    sous_descripteur: Literal['AnimateurSocioculturel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-899"
    descripteur: str = "animateur socioculturel"

class ActionCulturelle(BaseModel):
    sous_descripteur: Union['AnimateurSocioculturel'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-338"
    descripteur: str = "action culturelle"

class UniversitePopulaire(BaseModel):
    sous_descripteur: Literal['UniversitePopulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1407"
    descripteur: str = "université populaire"

class EducationPopulaire(BaseModel):
    sous_descripteur: Union['UniversitePopulaire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-86"
    descripteur: str = "éducation populaire"

class ObjetDart(BaseModel):
    sous_descripteur: Literal['ObjetDart']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-825"
    descripteur: str = "objet d'art"

class EdificeClasse(BaseModel):
    sous_descripteur: Literal['EdificeClasse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-658"
    descripteur: str = "édifice classé"

class MonumentHistorique(BaseModel):
    sous_descripteur: Literal['MonumentHistorique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-995"
    descripteur: str = "monument historique"

class PatrimoineArchitectural(BaseModel):
    sous_descripteur: Literal['PatrimoineArchitectural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1500"
    descripteur: str = "patrimoine architectural"

class PatrimoineIconographique(BaseModel):
    sous_descripteur: Literal['PatrimoineIconographique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1223"
    descripteur: str = "patrimoine iconographique"

class PatrimoineEcrit(BaseModel):
    sous_descripteur: Literal['PatrimoineEcrit']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1337"
    descripteur: str = "patrimoine écrit"

class PatrimoineAudiovisuel(BaseModel):
    sous_descripteur: Literal['PatrimoineAudiovisuel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1343"
    descripteur: str = "patrimoine audiovisuel"

class PatrimoineNumerique(BaseModel):
    sous_descripteur: Literal['PatrimoineNumerique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-889"
    descripteur: str = "patrimoine numérique"

class PatrimoineScientifiqueEtTechnique(BaseModel):
    sous_descripteur: Literal['PatrimoineScientifiqueEtTechnique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-484"
    descripteur: str = "patrimoine scientifique et technique"

class PatrimoineEthnologique(BaseModel):
    sous_descripteur: Literal['PatrimoineEthnologique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-991"
    descripteur: str = "patrimoine ethnologique"

class LangueRegionale(BaseModel):
    sous_descripteur: Literal['LangueRegionale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-562"
    descripteur: str = "langue régionale"

class OeuvreDart(BaseModel):
    sous_descripteur: Literal['OeuvreDart']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-226"
    descripteur: str = "oeuvre d'art"

class PatrimoineCulturel(BaseModel):
    sous_descripteur: Union['OeuvreDart', 'LangueRegionale', 'PatrimoineEthnologique', 'PatrimoineScientifiqueEtTechnique', 'PatrimoineNumerique', 'PatrimoineAudiovisuel', 'PatrimoineEcrit', 'PatrimoineIconographique', 'PatrimoineArchitectural', 'MonumentHistorique', 'EdificeClasse', 'ObjetDart'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-123"
    descripteur: str = "patrimoine culturel"

class CompagnieTheatrale(BaseModel):
    sous_descripteur: Literal['CompagnieTheatrale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1180"
    descripteur: str = "compagnie théâtrale"

class CompagnieChoregraphique(BaseModel):
    sous_descripteur: Literal['CompagnieChoregraphique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-689"
    descripteur: str = "compagnie chorégraphique"

class Cirque(BaseModel):
    sous_descripteur: Literal['Cirque']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-297"
    descripteur: str = "cirque"

class FormationMusicale(BaseModel):
    sous_descripteur: Literal['FormationMusicale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-75"
    descripteur: str = "formation musicale"

class EntrepriseDeSpectacle(BaseModel):
    sous_descripteur: Union['FormationMusicale', 'Cirque', 'CompagnieChoregraphique', 'CompagnieTheatrale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1311"
    descripteur: str = "entreprise de spectacle"

class ArtsPlastiques(BaseModel):
    sous_descripteur: Literal['ArtsPlastiques']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-897"
    descripteur: str = "arts plastiques"

class Musique(BaseModel):
    sous_descripteur: Literal['Musique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-731"
    descripteur: str = "musique"

class ArtDramatique(BaseModel):
    sous_descripteur: Literal['ArtDramatique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-514"
    descripteur: str = "art dramatique"

class Litterature(BaseModel):
    sous_descripteur: Literal['Litterature']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-360"
    descripteur: str = "littérature"

class CreationAudiovisuelle(BaseModel):
    sous_descripteur: Literal['CreationAudiovisuelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-330"
    descripteur: str = "création audiovisuelle"

class Cinema(BaseModel):
    sous_descripteur: Literal['Cinema']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1110"
    descripteur: str = "cinéma"

class Architecture(BaseModel):
    sous_descripteur: Literal['Architecture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-160"
    descripteur: str = "architecture"

class Danse(BaseModel):
    sous_descripteur: Literal['Danse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-43"
    descripteur: str = "danse"

class Art(BaseModel):
    sous_descripteur: Union['Danse', 'Architecture', 'Cinema', 'CreationAudiovisuelle', 'Litterature', 'ArtDramatique', 'Musique', 'ArtsPlastiques'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-608"
    descripteur: str = "art"

class CentreDeDocumentation(BaseModel):
    sous_descripteur: Literal['CentreDeDocumentation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1034"
    descripteur: str = "centre de documentation"

class Bibliotheque(BaseModel):
    sous_descripteur: Literal['Bibliotheque']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1459"
    descripteur: str = "bibliothèque"

class SalleDeSpectacles(BaseModel):
    sous_descripteur: Literal['SalleDeSpectacles']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1241"
    descripteur: str = "salle de spectacles"

class SalleDesFetes(BaseModel):
    sous_descripteur: Literal['SalleDesFetes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-305"
    descripteur: str = "salle des fêtes"

class MaisonDesJeunes(BaseModel):
    sous_descripteur: Literal['MaisonDesJeunes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-871"
    descripteur: str = "maison des jeunes"

class CentreDarchives(BaseModel):
    sous_descripteur: Literal['CentreDarchives']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-254"
    descripteur: str = "centre d'archives"

class KiosqueAMusique(BaseModel):
    sous_descripteur: Literal['KiosqueAMusique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-693"
    descripteur: str = "kiosque à musique"

class Mediatheque(BaseModel):
    sous_descripteur: Literal['Mediatheque']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-578"
    descripteur: str = "médiathèque"

class Musee(BaseModel):
    sous_descripteur: Literal['Musee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-114"
    descripteur: str = "musée"

class Conservatoire(BaseModel):
    sous_descripteur: Literal['Conservatoire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-704"
    descripteur: str = "conservatoire"

class FoyerRural(BaseModel):
    sous_descripteur: Literal['FoyerRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-332"
    descripteur: str = "foyer rural"

class EquipementSocioculturel(BaseModel):
    sous_descripteur: Union['FoyerRural', 'Conservatoire', 'Musee', 'Mediatheque', 'KiosqueAMusique', 'CentreDarchives', 'MaisonDesJeunes', 'SalleDesFetes', 'SalleDeSpectacles', 'Bibliotheque', 'CentreDeDocumentation'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-213"
    descripteur: str = "équipement socioculturel"

class Mecenat(BaseModel):
    sous_descripteur: Literal['Mecenat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1198"
    descripteur: str = "mécénat"

class ArcheologieDuSol(BaseModel):
    sous_descripteur: Literal['ArcheologieDuSol']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1469"
    descripteur: str = "archéologie du sol"

class ArcheologieSousmarine(BaseModel):
    sous_descripteur: Literal['ArcheologieSousmarine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1017"
    descripteur: str = "archéologie sous-marine"

class ArcheologieSubaquatique(BaseModel):
    sous_descripteur: Literal['ArcheologieSubaquatique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-664"
    descripteur: str = "archéologie subaquatique"

class ArcheologieAerienne(BaseModel):
    sous_descripteur: Literal['ArcheologieAerienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-540"
    descripteur: str = "archéologie aérienne"

class Archeologie(BaseModel):
    sous_descripteur: Union['ArcheologieAerienne', 'ArcheologieSubaquatique', 'ArcheologieSousmarine', 'ArcheologieDuSol'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-648"
    descripteur: str = "archéologie"

class Culture(BaseModel):
    sous_descripteur: Union['Archeologie', 'Mecenat', 'EquipementSocioculturel', 'Art', 'EntrepriseDeSpectacle', 'PatrimoineCulturel', 'EducationPopulaire', 'ActionCulturelle', 'Artiste', 'ManifestationCulturelle'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-786"
    descripteur: str = "culture"

class Cyclotourisme(BaseModel):
    sous_descripteur: Literal['Cyclotourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1272"
    descripteur: str = "cyclotourisme"

class OrganismeLocalDeTourisme(BaseModel):
    sous_descripteur: Literal['OrganismeLocalDeTourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1378"
    descripteur: str = "organisme local de tourisme"

class CircuitTouristique(BaseModel):
    sous_descripteur: Literal['CircuitTouristique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1102"
    descripteur: str = "circuit touristique"

class TourismeUrbain(BaseModel):
    sous_descripteur: Literal['TourismeUrbain']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-827"
    descripteur: str = "tourisme urbain"

class TourismeRural(BaseModel):
    sous_descripteur: Literal['TourismeRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1144"
    descripteur: str = "tourisme rural"

class CampingCaravaning(BaseModel):
    sous_descripteur: Literal['CampingCaravaning']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1290"
    descripteur: str = "camping caravaning"

class GuideInterprete(BaseModel):
    sous_descripteur: Literal['GuideInterprete']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1068"
    descripteur: str = "guide interprète"

class AgenceDeVoyages(BaseModel):
    sous_descripteur: Literal['AgenceDeVoyages']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-697"
    descripteur: str = "agence de voyages"

class TourismeDeMontagne(BaseModel):
    sous_descripteur: Literal['TourismeDeMontagne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-687"
    descripteur: str = "tourisme de montagne"

class MaisonFamilialeDeVacances(BaseModel):
    sous_descripteur: Literal['MaisonFamilialeDeVacances']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1415"
    descripteur: str = "maison familiale de vacances"

class AubergeDeJeunesse(BaseModel):
    sous_descripteur: Literal['AubergeDeJeunesse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-237"
    descripteur: str = "auberge de jeunesse"

class CentreDeVacances(BaseModel):
    sous_descripteur: Literal['CentreDeVacances']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-311"
    descripteur: str = "centre de vacances"

class TourismeSocial(BaseModel):
    sous_descripteur: Union['CentreDeVacances', 'AubergeDeJeunesse', 'MaisonFamilialeDeVacances'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1412"
    descripteur: str = "tourisme social"

class AssociationDeTourisme(BaseModel):
    sous_descripteur: Literal['AssociationDeTourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-154"
    descripteur: str = "association de tourisme"

class TourismeFluvial(BaseModel):
    sous_descripteur: Literal['TourismeFluvial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-37"
    descripteur: str = "tourisme fluvial"

class CheminDeRandonnee(BaseModel):
    sous_descripteur: Literal['CheminDeRandonnee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-24"
    descripteur: str = "chemin de randonnée"

class TourismeBalneaire(BaseModel):
    sous_descripteur: Literal['TourismeBalneaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-342"
    descripteur: str = "tourisme balnéaire"

class TerrainDeCamping(BaseModel):
    sous_descripteur: Literal['TerrainDeCamping']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1342"
    descripteur: str = "terrain de camping"

class RestaurantDeTourisme(BaseModel):
    sous_descripteur: Literal['RestaurantDeTourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-935"
    descripteur: str = "restaurant de tourisme"

class ResidenceDeTourisme(BaseModel):
    sous_descripteur: Literal['ResidenceDeTourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-600"
    descripteur: str = "résidence de tourisme"

class RefugeDeMontagne(BaseModel):
    sous_descripteur: Literal['RefugeDeMontagne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-125"
    descripteur: str = "refuge de montagne"

class HotelDeTourisme(BaseModel):
    sous_descripteur: Literal['HotelDeTourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-225"
    descripteur: str = "hôtel de tourisme"

class GiteRural(BaseModel):
    sous_descripteur: Literal['GiteRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-366"
    descripteur: str = "gîte rural"

class EquipementTouristique(BaseModel):
    sous_descripteur: Union['GiteRural', 'HotelDeTourisme', 'RefugeDeMontagne', 'ResidenceDeTourisme', 'RestaurantDeTourisme', 'TerrainDeCamping'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-909"
    descripteur: str = "équipement touristique"

class Tourisme(BaseModel):
    sous_descripteur: Union['EquipementTouristique', 'TourismeBalneaire', 'CheminDeRandonnee', 'TourismeFluvial', 'AssociationDeTourisme', 'TourismeSocial', 'TourismeDeMontagne', 'AgenceDeVoyages', 'GuideInterprete', 'CampingCaravaning', 'TourismeRural', 'TourismeUrbain', 'CircuitTouristique', 'OrganismeLocalDeTourisme', 'Cyclotourisme'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-632"
    descripteur: str = "tourisme"

class TempsLibreEtSociabilite(BaseModel):
    sous_descripteur: Union['Tourisme', 'Culture', 'VieQuotidienne', 'Loisir'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1359"
    descripteur: str = "temps libre et sociabilité"
