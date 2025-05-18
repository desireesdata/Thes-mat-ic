from pydantic import BaseModel
from typing import Union, Literal
                
class TempsLibreEtSociabilite(BaseModel):
    terme_specifique: Union['Tourisme', 'Culture', 'VieQuotidienne', 'Loisir']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1359"
    descripteur: str = "temps libre et sociabilité"
class Tourisme(BaseModel):
    terme_specifique: Union['EquipementTouristique', 'TourismeBalneaire', 'CheminDeRandonnee', 'TourismeFluvial', 'AssociationDeTourisme', 'TourismeSocial', 'TourismeDeMontagne', 'AgenceDeVoyages', 'GuideInterprete', 'CampingCaravaning', 'TourismeRural', 'TourismeUrbain', 'CircuitTouristique', 'OrganismeLocalDeTourisme', 'Cyclotourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-632"
    descripteur: str = "tourisme"
class EquipementTouristique(BaseModel):
    terme_specifique: Union['GiteRural', 'HotelDeTourisme', 'RefugeDeMontagne', 'ResidenceDeTourisme', 'RestaurantDeTourisme', 'TerrainDeCamping']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-909"
    descripteur: str = "équipement touristique"
class GiteRural(BaseModel):
    terme_specifique: Literal['GiteRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-366"
    descripteur: str = "gîte rural"
class HotelDeTourisme(BaseModel):
    terme_specifique: Literal['HotelDeTourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-225"
    descripteur: str = "hôtel de tourisme"
class RefugeDeMontagne(BaseModel):
    terme_specifique: Literal['RefugeDeMontagne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-125"
    descripteur: str = "refuge de montagne"
class ResidenceDeTourisme(BaseModel):
    terme_specifique: Literal['ResidenceDeTourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-600"
    descripteur: str = "résidence de tourisme"
class RestaurantDeTourisme(BaseModel):
    terme_specifique: Literal['RestaurantDeTourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-935"
    descripteur: str = "restaurant de tourisme"
class TerrainDeCamping(BaseModel):
    terme_specifique: Literal['TerrainDeCamping']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1342"
    descripteur: str = "terrain de camping"
class TourismeBalneaire(BaseModel):
    terme_specifique: Literal['TourismeBalneaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-342"
    descripteur: str = "tourisme balnéaire"
class CheminDeRandonnee(BaseModel):
    terme_specifique: Literal['CheminDeRandonnee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-24"
    descripteur: str = "chemin de randonnée"
class TourismeFluvial(BaseModel):
    terme_specifique: Literal['TourismeFluvial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-37"
    descripteur: str = "tourisme fluvial"
class AssociationDeTourisme(BaseModel):
    terme_specifique: Literal['AssociationDeTourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-154"
    descripteur: str = "association de tourisme"
class TourismeSocial(BaseModel):
    terme_specifique: Union['CentreDeVacances', 'AubergeDeJeunesse', 'MaisonFamilialeDeVacances']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1412"
    descripteur: str = "tourisme social"
class CentreDeVacances(BaseModel):
    terme_specifique: Literal['CentreDeVacances']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-311"
    descripteur: str = "centre de vacances"
class AubergeDeJeunesse(BaseModel):
    terme_specifique: Literal['AubergeDeJeunesse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-237"
    descripteur: str = "auberge de jeunesse"
class MaisonFamilialeDeVacances(BaseModel):
    terme_specifique: Literal['MaisonFamilialeDeVacances']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1415"
    descripteur: str = "maison familiale de vacances"
class TourismeDeMontagne(BaseModel):
    terme_specifique: Literal['TourismeDeMontagne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-687"
    descripteur: str = "tourisme de montagne"
class AgenceDeVoyages(BaseModel):
    terme_specifique: Literal['AgenceDeVoyages']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-697"
    descripteur: str = "agence de voyages"
class GuideInterprete(BaseModel):
    terme_specifique: Literal['GuideInterprete']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1068"
    descripteur: str = "guide interprète"
class CampingCaravaning(BaseModel):
    terme_specifique: Literal['CampingCaravaning']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1290"
    descripteur: str = "camping caravaning"
class TourismeRural(BaseModel):
    terme_specifique: Literal['TourismeRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1144"
    descripteur: str = "tourisme rural"
class TourismeUrbain(BaseModel):
    terme_specifique: Literal['TourismeUrbain']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-827"
    descripteur: str = "tourisme urbain"
class CircuitTouristique(BaseModel):
    terme_specifique: Literal['CircuitTouristique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1102"
    descripteur: str = "circuit touristique"
class OrganismeLocalDeTourisme(BaseModel):
    terme_specifique: Literal['OrganismeLocalDeTourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1378"
    descripteur: str = "organisme local de tourisme"
class Cyclotourisme(BaseModel):
    terme_specifique: Literal['Cyclotourisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1272"
    descripteur: str = "cyclotourisme"
class Culture(BaseModel):
    terme_specifique: Union['Archeologie', 'Mecenat', 'EquipementSocioculturel', 'Art', 'EntrepriseDeSpectacle', 'PatrimoineCulturel', 'EducationPopulaire', 'ActionCulturelle', 'Artiste', 'ManifestationCulturelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-786"
    descripteur: str = "culture"
class Archeologie(BaseModel):
    terme_specifique: Union['ArcheologieAerienne', 'ArcheologieSubaquatique', 'ArcheologieSousmarine', 'ArcheologieDuSol']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-648"
    descripteur: str = "archéologie"
class ArcheologieAerienne(BaseModel):
    terme_specifique: Literal['ArcheologieAerienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-540"
    descripteur: str = "archéologie aérienne"
class ArcheologieSubaquatique(BaseModel):
    terme_specifique: Literal['ArcheologieSubaquatique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-664"
    descripteur: str = "archéologie subaquatique"
class ArcheologieSousmarine(BaseModel):
    terme_specifique: Literal['ArcheologieSousmarine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1017"
    descripteur: str = "archéologie sous-marine"
class ArcheologieDuSol(BaseModel):
    terme_specifique: Literal['ArcheologieDuSol']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1469"
    descripteur: str = "archéologie du sol"
class Mecenat(BaseModel):
    terme_specifique: Literal['Mecenat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1198"
    descripteur: str = "mécénat"
class EquipementSocioculturel(BaseModel):
    terme_specifique: Union['FoyerRural', 'Conservatoire', 'Musee', 'Mediatheque', 'KiosqueAMusique', 'CentreDarchives', 'MaisonDesJeunes', 'SalleDesFetes', 'SalleDeSpectacles', 'Bibliotheque', 'CentreDeDocumentation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-213"
    descripteur: str = "équipement socioculturel"
class FoyerRural(BaseModel):
    terme_specifique: Literal['FoyerRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-332"
    descripteur: str = "foyer rural"
class Conservatoire(BaseModel):
    terme_specifique: Literal['Conservatoire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-704"
    descripteur: str = "conservatoire"
class Musee(BaseModel):
    terme_specifique: Literal['Musee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-114"
    descripteur: str = "musée"
class Mediatheque(BaseModel):
    terme_specifique: Literal['Mediatheque']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-578"
    descripteur: str = "médiathèque"
class KiosqueAMusique(BaseModel):
    terme_specifique: Literal['KiosqueAMusique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-693"
    descripteur: str = "kiosque à musique"
class CentreDarchives(BaseModel):
    terme_specifique: Literal['CentreDarchives']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-254"
    descripteur: str = "centre d'archives"
class MaisonDesJeunes(BaseModel):
    terme_specifique: Literal['MaisonDesJeunes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-871"
    descripteur: str = "maison des jeunes"
class SalleDesFetes(BaseModel):
    terme_specifique: Literal['SalleDesFetes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-305"
    descripteur: str = "salle des fêtes"
class SalleDeSpectacles(BaseModel):
    terme_specifique: Literal['SalleDeSpectacles']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1241"
    descripteur: str = "salle de spectacles"
class Bibliotheque(BaseModel):
    terme_specifique: Literal['Bibliotheque']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1459"
    descripteur: str = "bibliothèque"
class CentreDeDocumentation(BaseModel):
    terme_specifique: Literal['CentreDeDocumentation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1034"
    descripteur: str = "centre de documentation"
class Art(BaseModel):
    terme_specifique: Union['Danse', 'Architecture', 'Cinema', 'CreationAudiovisuelle', 'Litterature', 'ArtDramatique', 'Musique', 'ArtsPlastiques']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-608"
    descripteur: str = "art"
class Danse(BaseModel):
    terme_specifique: Literal['Danse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-43"
    descripteur: str = "danse"
class Architecture(BaseModel):
    terme_specifique: Literal['Architecture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-160"
    descripteur: str = "architecture"
class Cinema(BaseModel):
    terme_specifique: Literal['Cinema']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1110"
    descripteur: str = "cinéma"
class CreationAudiovisuelle(BaseModel):
    terme_specifique: Literal['CreationAudiovisuelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-330"
    descripteur: str = "création audiovisuelle"
class Litterature(BaseModel):
    terme_specifique: Literal['Litterature']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-360"
    descripteur: str = "littérature"
class ArtDramatique(BaseModel):
    terme_specifique: Literal['ArtDramatique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-514"
    descripteur: str = "art dramatique"
class Musique(BaseModel):
    terme_specifique: Literal['Musique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-731"
    descripteur: str = "musique"
class ArtsPlastiques(BaseModel):
    terme_specifique: Literal['ArtsPlastiques']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-897"
    descripteur: str = "arts plastiques"
class EntrepriseDeSpectacle(BaseModel):
    terme_specifique: Union['FormationMusicale', 'Cirque', 'CompagnieChoregraphique', 'CompagnieTheatrale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1311"
    descripteur: str = "entreprise de spectacle"
class FormationMusicale(BaseModel):
    terme_specifique: Literal['FormationMusicale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-75"
    descripteur: str = "formation musicale"
class Cirque(BaseModel):
    terme_specifique: Literal['Cirque']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-297"
    descripteur: str = "cirque"
class CompagnieChoregraphique(BaseModel):
    terme_specifique: Literal['CompagnieChoregraphique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-689"
    descripteur: str = "compagnie chorégraphique"
class CompagnieTheatrale(BaseModel):
    terme_specifique: Literal['CompagnieTheatrale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1180"
    descripteur: str = "compagnie théâtrale"
class PatrimoineCulturel(BaseModel):
    terme_specifique: Union['OeuvreDart', 'LangueRegionale', 'PatrimoineEthnologique', 'PatrimoineScientifiqueEtTechnique', 'PatrimoineNumerique', 'PatrimoineAudiovisuel', 'PatrimoineEcrit', 'PatrimoineIconographique', 'PatrimoineArchitectural', 'MonumentHistorique', 'EdificeClasse', 'ObjetDart']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-123"
    descripteur: str = "patrimoine culturel"
class OeuvreDart(BaseModel):
    terme_specifique: Literal['OeuvreDart']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-226"
    descripteur: str = "oeuvre d'art"
class LangueRegionale(BaseModel):
    terme_specifique: Literal['LangueRegionale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-562"
    descripteur: str = "langue régionale"
class PatrimoineEthnologique(BaseModel):
    terme_specifique: Literal['PatrimoineEthnologique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-991"
    descripteur: str = "patrimoine ethnologique"
class PatrimoineScientifiqueEtTechnique(BaseModel):
    terme_specifique: Literal['PatrimoineScientifiqueEtTechnique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-484"
    descripteur: str = "patrimoine scientifique et technique"
class PatrimoineNumerique(BaseModel):
    terme_specifique: Literal['PatrimoineNumerique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-889"
    descripteur: str = "patrimoine numérique"
class PatrimoineAudiovisuel(BaseModel):
    terme_specifique: Literal['PatrimoineAudiovisuel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1343"
    descripteur: str = "patrimoine audiovisuel"
class PatrimoineEcrit(BaseModel):
    terme_specifique: Literal['PatrimoineEcrit']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1337"
    descripteur: str = "patrimoine écrit"
class PatrimoineIconographique(BaseModel):
    terme_specifique: Literal['PatrimoineIconographique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1223"
    descripteur: str = "patrimoine iconographique"
class PatrimoineArchitectural(BaseModel):
    terme_specifique: Literal['PatrimoineArchitectural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1500"
    descripteur: str = "patrimoine architectural"
class MonumentHistorique(BaseModel):
    terme_specifique: Literal['MonumentHistorique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-995"
    descripteur: str = "monument historique"
class EdificeClasse(BaseModel):
    terme_specifique: Literal['EdificeClasse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-658"
    descripteur: str = "édifice classé"
class ObjetDart(BaseModel):
    terme_specifique: Literal['ObjetDart']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-825"
    descripteur: str = "objet d'art"
class EducationPopulaire(BaseModel):
    terme_specifique: Union['UniversitePopulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-86"
    descripteur: str = "éducation populaire"
class UniversitePopulaire(BaseModel):
    terme_specifique: Literal['UniversitePopulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1407"
    descripteur: str = "université populaire"
class ActionCulturelle(BaseModel):
    terme_specifique: Union['AnimateurSocioculturel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-338"
    descripteur: str = "action culturelle"
class AnimateurSocioculturel(BaseModel):
    terme_specifique: Literal['AnimateurSocioculturel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-899"
    descripteur: str = "animateur socioculturel"
class Artiste(BaseModel):
    terme_specifique: Literal['Artiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-963"
    descripteur: str = "artiste"
class ManifestationCulturelle(BaseModel):
    terme_specifique: Literal['ManifestationCulturelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-834"
    descripteur: str = "manifestation culturelle"
class VieQuotidienne(BaseModel):
    terme_specifique: Union['ActiviteMenagere', 'Alimentation', 'AnimalDeCompagnie', 'Vetement', 'ComptabilitePrivee', 'EspaceDomestique', 'Mobilier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-373"
    descripteur: str = "vie quotidienne"
class ActiviteMenagere(BaseModel):
    terme_specifique: Literal['ActiviteMenagere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-183"
    descripteur: str = "activité ménagère"
class Alimentation(BaseModel):
    terme_specifique: Literal['Alimentation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-782"
    descripteur: str = "alimentation"
class AnimalDeCompagnie(BaseModel):
    terme_specifique: Literal['AnimalDeCompagnie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1042"
    descripteur: str = "animal de compagnie"
class Vetement(BaseModel):
    terme_specifique: Literal['Vetement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1252"
    descripteur: str = "vêtement"
class ComptabilitePrivee(BaseModel):
    terme_specifique: Literal['ComptabilitePrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-686"
    descripteur: str = "comptabilité privée"
class EspaceDomestique(BaseModel):
    terme_specifique: Literal['EspaceDomestique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-416"
    descripteur: str = "espace domestique"
class Mobilier(BaseModel):
    terme_specifique: Literal['Mobilier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-900"
    descripteur: str = "mobilier"
class Loisir(BaseModel):
    terme_specifique: Union['Sport', 'NavigationDePlaisance', 'CentreDeLoisirs', 'Fete', 'ParcDeLoisirs', 'Chasse', 'PecheALaLigne', 'MouvementDeJeunesse', 'Jeuxetparis', 'Tauromachie', 'Jeuconcours']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1173"
    descripteur: str = "loisir"
class Sport(BaseModel):
    terme_specifique: Union['DisciplineSportive', 'JeuxOlympiques', 'ManifestationSportive', 'InstallationSportive', 'Handisport', 'AssociationSportive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-639"
    descripteur: str = "sport"
class DisciplineSportive(BaseModel):
    terme_specifique: Literal['DisciplineSportive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-335"
    descripteur: str = "discipline sportive"
class JeuxOlympiques(BaseModel):
    terme_specifique: Literal['JeuxOlympiques']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-221"
    descripteur: str = "jeux olympiques"
class ManifestationSportive(BaseModel):
    terme_specifique: Literal['ManifestationSportive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-926"
    descripteur: str = "manifestation sportive"
class InstallationSportive(BaseModel):
    terme_specifique: Literal['InstallationSportive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-585"
    descripteur: str = "installation sportive"
class Handisport(BaseModel):
    terme_specifique: Literal['Handisport']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-850"
    descripteur: str = "handisport"
class AssociationSportive(BaseModel):
    terme_specifique: Literal['AssociationSportive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1368"
    descripteur: str = "association sportive"
class NavigationDePlaisance(BaseModel):
    terme_specifique: Literal['NavigationDePlaisance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-255"
    descripteur: str = "navigation de plaisance"
class CentreDeLoisirs(BaseModel):
    terme_specifique: Literal['CentreDeLoisirs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-684"
    descripteur: str = "centre de loisirs"
class Fete(BaseModel):
    terme_specifique: Union['FeteForaine', 'BalPublic', 'Carnaval']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1437"
    descripteur: str = "fête"
class FeteForaine(BaseModel):
    terme_specifique: Literal['FeteForaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-79"
    descripteur: str = "fête foraine"
class BalPublic(BaseModel):
    terme_specifique: Literal['BalPublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-380"
    descripteur: str = "bal public"
class Carnaval(BaseModel):
    terme_specifique: Literal['Carnaval']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1400"
    descripteur: str = "carnaval"
class ParcDeLoisirs(BaseModel):
    terme_specifique: Literal['ParcDeLoisirs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-789"
    descripteur: str = "parc de loisirs"
class Chasse(BaseModel):
    terme_specifique: Union['LotDeChasse', 'AssociationDeChasse', 'Chasseur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-389"
    descripteur: str = "chasse"
class LotDeChasse(BaseModel):
    terme_specifique: Literal['LotDeChasse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-637"
    descripteur: str = "lot de chasse"
class AssociationDeChasse(BaseModel):
    terme_specifique: Literal['AssociationDeChasse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1371"
    descripteur: str = "association de chasse"
class Chasseur(BaseModel):
    terme_specifique: Literal['Chasseur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1091"
    descripteur: str = "chasseur"
class PecheALaLigne(BaseModel):
    terme_specifique: Union['LotDePeche', 'Pecheur', 'AssociationDePeche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1182"
    descripteur: str = "pêche à la ligne"
class LotDePeche(BaseModel):
    terme_specifique: Literal['LotDePeche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-340"
    descripteur: str = "lot de pêche"
class Pecheur(BaseModel):
    terme_specifique: Literal['Pecheur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-381"
    descripteur: str = "pêcheur"
class AssociationDePeche(BaseModel):
    terme_specifique: Literal['AssociationDePeche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-876"
    descripteur: str = "association de pêche"
class MouvementDeJeunesse(BaseModel):
    terme_specifique: Literal['MouvementDeJeunesse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-709"
    descripteur: str = "mouvement de jeunesse"
class Jeuxetparis(BaseModel):
    terme_specifique: Union['Casino', 'Loterie', 'CourseHippique', 'JeuDeCartes', 'AppareilDeJeu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1060"
    descripteur: str = "jeux-et-paris"
class Casino(BaseModel):
    terme_specifique: Literal['Casino']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-933"
    descripteur: str = "casino"
class Loterie(BaseModel):
    terme_specifique: Literal['Loterie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-348"
    descripteur: str = "loterie"
class CourseHippique(BaseModel):
    terme_specifique: Literal['CourseHippique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-703"
    descripteur: str = "course hippique"
class JeuDeCartes(BaseModel):
    terme_specifique: Literal['JeuDeCartes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1304"
    descripteur: str = "jeu de cartes"
class AppareilDeJeu(BaseModel):
    terme_specifique: Literal['AppareilDeJeu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1309"
    descripteur: str = "appareil de jeu"
class Tauromachie(BaseModel):
    terme_specifique: Literal['Tauromachie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-393"
    descripteur: str = "tauromachie"
class Jeuconcours(BaseModel):
    terme_specifique: Literal['Jeuconcours']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-814"
    descripteur: str = "jeu-concours"
