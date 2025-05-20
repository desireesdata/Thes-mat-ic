from pydantic import BaseModel
from typing import Union, Literal

class Sorcellerie(BaseModel):
    sous_descripteur: Literal['Sorcellerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-836"
    descripteur: str = "sorcellerie"

class Magie(BaseModel):
    sous_descripteur: Union['Sorcellerie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1364"
    descripteur: str = "magie"

class Mythe(BaseModel):
    sous_descripteur: Literal['Mythe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1046"
    descripteur: str = "mythe"

class CroyancesPopulaires(BaseModel):
    sous_descripteur: Union['Mythe'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1015"
    descripteur: str = "croyances populaires"

class Spiritisme(BaseModel):
    sous_descripteur: Literal['Spiritisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-901"
    descripteur: str = "spiritisme"

class Graphologie(BaseModel):
    sous_descripteur: Literal['Graphologie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-386"
    descripteur: str = "graphologie"

class Alchimie(BaseModel):
    sous_descripteur: Literal['Alchimie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-784"
    descripteur: str = "alchimie"

class Astrologie(BaseModel):
    sous_descripteur: Literal['Astrologie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1111"
    descripteur: str = "astrologie"

class Esoterisme(BaseModel):
    sous_descripteur: Literal['Esoterisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-39"
    descripteur: str = "ésotérisme"

class SciencesParalleles(BaseModel):
    sous_descripteur: Union['Esoterisme', 'Astrologie', 'Alchimie', 'Graphologie', 'Spiritisme'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-172"
    descripteur: str = "sciences parallèles"

class CroyancesEtSciencesParalleles(BaseModel):
    sous_descripteur: Union['SciencesParalleles', 'CroyancesPopulaires', 'Magie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1439"
    descripteur: str = "croyances et sciences parallèles"

class DecoupageElectoral(BaseModel):
    sous_descripteur: Literal['DecoupageElectoral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-459"
    descripteur: str = "découpage électoral"

class CollegeElectoral(BaseModel):
    sous_descripteur: Literal['CollegeElectoral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-675"
    descripteur: str = "collège électoral"

class DroitsCiviques(BaseModel):
    sous_descripteur: Literal['DroitsCiviques']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-911"
    descripteur: str = "droits civiques"

class Electeur(BaseModel):
    sous_descripteur: Union['DroitsCiviques', 'CollegeElectoral'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-450"
    descripteur: str = "électeur"

class CampagneElectorale(BaseModel):
    sous_descripteur: Literal['CampagneElectorale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-177"
    descripteur: str = "campagne électorale"

class ElectionLegislative(BaseModel):
    sous_descripteur: Literal['ElectionLegislative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1254"
    descripteur: str = "élection législative"

class ElectionAuConseilDarrondissement(BaseModel):
    sous_descripteur: Literal['ElectionAuConseilDarrondissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-401"
    descripteur: str = "élection au conseil d'arrondissement"

class Referendum(BaseModel):
    sous_descripteur: Literal['Referendum']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-321"
    descripteur: str = "référendum"

class ElectionSenatoriale(BaseModel):
    sous_descripteur: Literal['ElectionSenatoriale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1383"
    descripteur: str = "élection sénatoriale"

class ElectionPresidentielle(BaseModel):
    sous_descripteur: Literal['ElectionPresidentielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-624"
    descripteur: str = "élection présidentielle"

class ElectionEuropeenne(BaseModel):
    sous_descripteur: Literal['ElectionEuropeenne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-870"
    descripteur: str = "élection européenne"

class ElectionMunicipale(BaseModel):
    sous_descripteur: Literal['ElectionMunicipale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-171"
    descripteur: str = "élection municipale"

class ElectionCantonale(BaseModel):
    sous_descripteur: Literal['ElectionCantonale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-923"
    descripteur: str = "élection cantonale"

class ElectionRegionale(BaseModel):
    sous_descripteur: Literal['ElectionRegionale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1081"
    descripteur: str = "élection régionale"

class ElectionPolitique(BaseModel):
    sous_descripteur: Union['ElectionRegionale', 'ElectionCantonale', 'ElectionMunicipale', 'ElectionEuropeenne', 'ElectionPresidentielle', 'ElectionSenatoriale', 'Referendum', 'ElectionAuConseilDarrondissement', 'ElectionLegislative'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-107"
    descripteur: str = "élection politique"

class PresidentDetablissementPublicDeCooperationIntercommunale(BaseModel):
    sous_descripteur: Literal['PresidentDetablissementPublicDeCooperationIntercommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-893"
    descripteur: str = "président d'établissement public de coopération intercommunale"

class Echevin(BaseModel):
    sous_descripteur: Literal['Echevin']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-512"
    descripteur: str = "échevin"

class ConseillerDarrondissement(BaseModel):
    sous_descripteur: Literal['ConseillerDarrondissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-438"
    descripteur: str = "conseiller d'arrondissement"

class ConseillerGeneral(BaseModel):
    sous_descripteur: Literal['ConseillerGeneral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-721"
    descripteur: str = "conseiller général"

class PresidentDuConseilGeneral(BaseModel):
    sous_descripteur: Literal['PresidentDuConseilGeneral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1250"
    descripteur: str = "président du conseil général"

class Parlementaire(BaseModel):
    sous_descripteur: Literal['Parlementaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-902"
    descripteur: str = "parlementaire"

class ConseillerMunicipal(BaseModel):
    sous_descripteur: Literal['ConseillerMunicipal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1188"
    descripteur: str = "conseiller municipal"

class Maire(BaseModel):
    sous_descripteur: Literal['Maire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1251"
    descripteur: str = "maire"

class ConseillerRegional(BaseModel):
    sous_descripteur: Literal['ConseillerRegional']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1382"
    descripteur: str = "conseiller régional"

class PresidentDuConseilRegional(BaseModel):
    sous_descripteur: Literal['PresidentDuConseilRegional']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-54"
    descripteur: str = "président du conseil régional"

class Elu(BaseModel):
    sous_descripteur: Union['PresidentDuConseilRegional', 'ConseillerRegional', 'Maire', 'ConseillerMunicipal', 'Parlementaire', 'PresidentDuConseilGeneral', 'ConseillerGeneral', 'ConseillerDarrondissement', 'Echevin', 'PresidentDetablissementPublicDeCooperationIntercommunale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-868"
    descripteur: str = "élu"

class ElectionProfessionnelle(BaseModel):
    sous_descripteur: Literal['ElectionProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1061"
    descripteur: str = "élection professionnelle"

class ElectionSociale(BaseModel):
    sous_descripteur: Union['ElectionProfessionnelle'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1214"
    descripteur: str = "élection sociale"

class Election(BaseModel):
    sous_descripteur: Union['ElectionSociale', 'Elu', 'ElectionPolitique', 'CampagneElectorale', 'Electeur', 'DecoupageElectoral'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1152"
    descripteur: str = "élection"

class Heresie(BaseModel):
    sous_descripteur: Literal['Heresie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1369"
    descripteur: str = "hérésie"

class TemporelEcclesiastique(BaseModel):
    sous_descripteur: Literal['TemporelEcclesiastique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-864"
    descripteur: str = "temporel ecclésiastique"

class EdificeCultuel(BaseModel):
    sous_descripteur: Literal['EdificeCultuel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-820"
    descripteur: str = "édifice cultuel"

class MinistreDuCulte(BaseModel):
    sous_descripteur: Literal['MinistreDuCulte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-424"
    descripteur: str = "ministre du culte"

class Taonsme(BaseModel):
    sous_descripteur: Literal['Taonsme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1401"
    descripteur: str = "taoïsme"

class Protestantisme(BaseModel):
    sous_descripteur: Literal['Protestantisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1367"
    descripteur: str = "protestantisme"

class Bouddhisme(BaseModel):
    sous_descripteur: Literal['Bouddhisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1175"
    descripteur: str = "bouddhisme"

class ReligionOrthodoxe(BaseModel):
    sous_descripteur: Literal['ReligionOrthodoxe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-980"
    descripteur: str = "religion orthodoxe"

class Catholicisme(BaseModel):
    sous_descripteur: Literal['Catholicisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-740"
    descripteur: str = "catholicisme"

class Chamanisme(BaseModel):
    sous_descripteur: Literal['Chamanisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-716"
    descripteur: str = "chamanisme"

class Islam(BaseModel):
    sous_descripteur: Literal['Islam']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-636"
    descripteur: str = "islam"

class Hindouisme(BaseModel):
    sous_descripteur: Literal['Hindouisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-303"
    descripteur: str = "hindouisme"

class Judansme(BaseModel):
    sous_descripteur: Literal['Judansme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-281"
    descripteur: str = "judaïsme"

class Culte(BaseModel):
    sous_descripteur: Union['Judansme', 'Hindouisme', 'Islam', 'Chamanisme', 'Catholicisme', 'ReligionOrthodoxe', 'Bouddhisme', 'Protestantisme', 'Taonsme'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1179"
    descripteur: str = "culte"

class Presbytere(BaseModel):
    sous_descripteur: Literal['Presbytere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-257"
    descripteur: str = "presbytère"

class LivreSaint(BaseModel):
    sous_descripteur: Literal['LivreSaint']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1305"
    descripteur: str = "livre saint"

class Theologie(BaseModel):
    sous_descripteur: Literal['Theologie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1197"
    descripteur: str = "théologie"

class Spiritualite(BaseModel):
    sous_descripteur: Literal['Spiritualite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-552"
    descripteur: str = "spiritualité"

class Mysticisme(BaseModel):
    sous_descripteur: Literal['Mysticisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-530"
    descripteur: str = "mysticisme"

class Miracle(BaseModel):
    sous_descripteur: Literal['Miracle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-165"
    descripteur: str = "miracle"

class VieSpirituelle(BaseModel):
    sous_descripteur: Union['Miracle', 'Mysticisme', 'Spiritualite', 'Theologie', 'LivreSaint'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1210"
    descripteur: str = "vie spirituelle"

class Impiete(BaseModel):
    sous_descripteur: Literal['Impiete']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-69"
    descripteur: str = "impiété"

class ManifestationAntireligieuse(BaseModel):
    sous_descripteur: Union['Impiete'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-485"
    descripteur: str = "manifestation antireligieuse"

class Concile(BaseModel):
    sous_descripteur: Literal['Concile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1183"
    descripteur: str = "concile"

class Missions(BaseModel):
    sous_descripteur: Literal['Missions']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1291"
    descripteur: str = "missions"

class Papaute(BaseModel):
    sous_descripteur: Literal['Papaute']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-918"
    descripteur: str = "papauté"

class SeminaireReligieux(BaseModel):
    sous_descripteur: Literal['SeminaireReligieux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-967"
    descripteur: str = "séminaire religieux"

class AdministrationDiocesaine(BaseModel):
    sous_descripteur: Literal['AdministrationDiocesaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1053"
    descripteur: str = "administration diocésaine"

class FabriqueDeglise(BaseModel):
    sous_descripteur: Literal['FabriqueDeglise']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-811"
    descripteur: str = "fabrique d'église"

class Inquisition(BaseModel):
    sous_descripteur: Literal['Inquisition']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-539"
    descripteur: str = "inquisition"

class InstitutionMonastique(BaseModel):
    sous_descripteur: Literal['InstitutionMonastique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-529"
    descripteur: str = "institution monastique"

class AssembleeGeneraleDuClerge(BaseModel):
    sous_descripteur: Literal['AssembleeGeneraleDuClerge']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-407"
    descripteur: str = "assemblée générale du clergé"

class CirconscriptionEcclesiastique(BaseModel):
    sous_descripteur: Literal['CirconscriptionEcclesiastique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-66"
    descripteur: str = "circonscription ecclésiastique"

class InstitutionEcclesiastique(BaseModel):
    sous_descripteur: Union['CirconscriptionEcclesiastique', 'AssembleeGeneraleDuClerge', 'InstitutionMonastique', 'Inquisition', 'FabriqueDeglise', 'AdministrationDiocesaine', 'SeminaireReligieux', 'Papaute', 'Missions', 'Concile'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-793"
    descripteur: str = "institution ecclésiastique"

class Tiersordre(BaseModel):
    sous_descripteur: Literal['Tiersordre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-917"
    descripteur: str = "tiers-ordre"

class SocieteDeCharite(BaseModel):
    sous_descripteur: Literal['SocieteDeCharite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1391"
    descripteur: str = "société de charité"

class Confrerie(BaseModel):
    sous_descripteur: Literal['Confrerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-58"
    descripteur: str = "confrérie"

class Congregation(BaseModel):
    sous_descripteur: Literal['Congregation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-633"
    descripteur: str = "congrégation"

class AssociationCultuelle(BaseModel):
    sous_descripteur: Union['Congregation', 'Confrerie', 'SocieteDeCharite', 'Tiersordre'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-74"
    descripteur: str = "association cultuelle"

class ServiceReligieux(BaseModel):
    sous_descripteur: Literal['ServiceReligieux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1493"
    descripteur: str = "service religieux"

class Pelerinage(BaseModel):
    sous_descripteur: Literal['Pelerinage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1492"
    descripteur: str = "pèlerinage"

class PratiqueReligieuse(BaseModel):
    sous_descripteur: Union['Pelerinage', 'ServiceReligieux'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-128"
    descripteur: str = "pratique religieuse"

class VieReligieuse(BaseModel):
    sous_descripteur: Union['PratiqueReligieuse', 'AssociationCultuelle', 'InstitutionEcclesiastique', 'ManifestationAntireligieuse', 'VieSpirituelle', 'Presbytere', 'Culte', 'MinistreDuCulte', 'EdificeCultuel', 'TemporelEcclesiastique', 'Heresie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-804"
    descripteur: str = "vie religieuse"

class Atheisme(BaseModel):
    sous_descripteur: Literal['Atheisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1247"
    descripteur: str = "athéisme"

class DroitsDeLhomme(BaseModel):
    sous_descripteur: Literal['DroitsDeLhomme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1239"
    descripteur: str = "droits de l'homme"

class Racisme(BaseModel):
    sous_descripteur: Literal['Racisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-496"
    descripteur: str = "racisme"

class Antisemitisme(BaseModel):
    sous_descripteur: Literal['Antisemitisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1297"
    descripteur: str = "antisémitisme"

class PersecutionReligieuse(BaseModel):
    sous_descripteur: Literal['PersecutionReligieuse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-181"
    descripteur: str = "persécution religieuse"

class Tolerance(BaseModel):
    sous_descripteur: Union['PersecutionReligieuse', 'Antisemitisme', 'Racisme'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-453"
    descripteur: str = "tolérance"

class Philosophie(BaseModel):
    sous_descripteur: Literal['Philosophie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-143"
    descripteur: str = "philosophie"

class VieIntellectuelle(BaseModel):
    sous_descripteur: Literal['VieIntellectuelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-896"
    descripteur: str = "vie intellectuelle"

class MouvementDidees(BaseModel):
    sous_descripteur: Union['VieIntellectuelle', 'Philosophie', 'Tolerance', 'DroitsDeLhomme', 'Atheisme'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-33"
    descripteur: str = "mouvement d'idées"

class MouvementPacifiste(BaseModel):
    sous_descripteur: Literal['MouvementPacifiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-318"
    descripteur: str = "mouvement pacifiste"

class MouvementHomosexuel(BaseModel):
    sous_descripteur: Literal['MouvementHomosexuel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-115"
    descripteur: str = "mouvement homosexuel"

class MouvementAutonomiste(BaseModel):
    sous_descripteur: Literal['MouvementAutonomiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-803"
    descripteur: str = "mouvement autonomiste"

class MouvementFeministe(BaseModel):
    sous_descripteur: Literal['MouvementFeministe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1218"
    descripteur: str = "mouvement féministe"

class Bonapartisme(BaseModel):
    sous_descripteur: Literal['Bonapartisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-174"
    descripteur: str = "bonapartisme"

class Royalisme(BaseModel):
    sous_descripteur: Literal['Royalisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-229"
    descripteur: str = "royalisme"

class ExtremeGauche(BaseModel):
    sous_descripteur: Literal['ExtremeGauche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1207"
    descripteur: str = "extrême gauche"

class ExtremeDroite(BaseModel):
    sous_descripteur: Literal['ExtremeDroite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1322"
    descripteur: str = "extrême droite"

class Radicalisme(BaseModel):
    sous_descripteur: Literal['Radicalisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1390"
    descripteur: str = "radicalisme"

class Liberalisme(BaseModel):
    sous_descripteur: Literal['Liberalisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-266"
    descripteur: str = "libéralisme"

class MouvementOuvrier(BaseModel):
    sous_descripteur: Literal['MouvementOuvrier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-391"
    descripteur: str = "mouvement ouvrier"

class Clericalisme(BaseModel):
    sous_descripteur: Literal['Clericalisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-197"
    descripteur: str = "cléricalisme"

class MouvementEtudiant(BaseModel):
    sous_descripteur: Literal['MouvementEtudiant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1339"
    descripteur: str = "mouvement étudiant"

class MouvementRegionaliste(BaseModel):
    sous_descripteur: Literal['MouvementRegionaliste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-720"
    descripteur: str = "mouvement régionaliste"

class Gaullisme(BaseModel):
    sous_descripteur: Literal['Gaullisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-605"
    descripteur: str = "gaullisme"

class Communisme(BaseModel):
    sous_descripteur: Literal['Communisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-526"
    descripteur: str = "communisme"

class Colonialisme(BaseModel):
    sous_descripteur: Literal['Colonialisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-538"
    descripteur: str = "colonialisme"

class MouvementEcologiste(BaseModel):
    sous_descripteur: Literal['MouvementEcologiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1177"
    descripteur: str = "mouvement écologiste"

class Nationalisme(BaseModel):
    sous_descripteur: Literal['Nationalisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1278"
    descripteur: str = "nationalisme"

class Anarchisme(BaseModel):
    sous_descripteur: Literal['Anarchisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-634"
    descripteur: str = "anarchisme"

class Anticapitalisme(BaseModel):
    sous_descripteur: Literal['Anticapitalisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-288"
    descripteur: str = "anticapitalisme"

class Socialisme(BaseModel):
    sous_descripteur: Literal['Socialisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1021"
    descripteur: str = "socialisme"

class Republicanisme(BaseModel):
    sous_descripteur: Literal['Republicanisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-170"
    descripteur: str = "républicanisme"

class Centrisme(BaseModel):
    sous_descripteur: Literal['Centrisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-110"
    descripteur: str = "centrisme"

class Fascisme(BaseModel):
    sous_descripteur: Literal['Fascisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-919"
    descripteur: str = "fascisme"

class MouvementLanque(BaseModel):
    sous_descripteur: Literal['MouvementLanque']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-70"
    descripteur: str = "mouvement laïque"

class MouvementPolitiqueEtSocietal(BaseModel):
    sous_descripteur: Union['MouvementLanque', 'Fascisme', 'Centrisme', 'Republicanisme', 'Socialisme', 'Anticapitalisme', 'Anarchisme', 'Nationalisme', 'MouvementEcologiste', 'Colonialisme', 'Communisme', 'Gaullisme', 'MouvementRegionaliste', 'MouvementEtudiant', 'Clericalisme', 'MouvementOuvrier', 'Liberalisme', 'Radicalisme', 'ExtremeDroite', 'ExtremeGauche', 'Royalisme', 'Bonapartisme', 'MouvementFeministe', 'MouvementAutonomiste', 'MouvementHomosexuel', 'MouvementPacifiste'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-87"
    descripteur: str = "mouvement politique et sociétal"

class Dissident(BaseModel):
    sous_descripteur: Literal['Dissident']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-821"
    descripteur: str = "dissident"

class CongresPolitique(BaseModel):
    sous_descripteur: Literal['CongresPolitique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-363"
    descripteur: str = "congrès politique"

class MilitantPolitique(BaseModel):
    sous_descripteur: Literal['MilitantPolitique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-78"
    descripteur: str = "militant politique"

class PartiPolitique(BaseModel):
    sous_descripteur: Union['MilitantPolitique', 'CongresPolitique', 'Dissident'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1169"
    descripteur: str = "parti politique"

class EcritSubversif(BaseModel):
    sous_descripteur: Literal['EcritSubversif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-729"
    descripteur: str = "écrit subversif"

class Clandestinite(BaseModel):
    sous_descripteur: Literal['Clandestinite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-382"
    descripteur: str = "clandestinité"

class ProposSubversif(BaseModel):
    sous_descripteur: Literal['ProposSubversif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-249"
    descripteur: str = "propos subversif"

class ChansonSubversive(BaseModel):
    sous_descripteur: Literal['ChansonSubversive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-18"
    descripteur: str = "chanson subversive"

class ActeDopposition(BaseModel):
    sous_descripteur: Union['ChansonSubversive', 'ProposSubversif', 'Clandestinite', 'EcritSubversif'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-727"
    descripteur: str = "acte d'opposition"

class ViePolitique(BaseModel):
    sous_descripteur: Union['ActeDopposition', 'PartiPolitique', 'MouvementPolitiqueEtSocietal'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-22"
    descripteur: str = "vie politique"

class ManifestationDadhesionAuRegime(BaseModel):
    sous_descripteur: Literal['ManifestationDadhesionAuRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1491"
    descripteur: str = "manifestation d'adhésion au régime"

class ManifestationAntinationale(BaseModel):
    sous_descripteur: Literal['ManifestationAntinationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1490"
    descripteur: str = "manifestation antinationale"

class MouvementPopulaire(BaseModel):
    sous_descripteur: Literal['MouvementPopulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1153"
    descripteur: str = "mouvement populaire"

class ManifestationDeProtestation(BaseModel):
    sous_descripteur: Literal['ManifestationDeProtestation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-796"
    descripteur: str = "manifestation de protestation"

class ReunionPublique(BaseModel):
    sous_descripteur: Literal['ReunionPublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-891"
    descripteur: str = "réunion publique"

class ManifestationPublique(BaseModel):
    sous_descripteur: Union['ReunionPublique', 'ManifestationDeProtestation', 'MouvementPopulaire', 'ManifestationAntinationale', 'ManifestationDadhesionAuRegime'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1489"
    descripteur: str = "manifestation publique"

class Armoiries(BaseModel):
    sous_descripteur: Literal['Armoiries']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1478"
    descripteur: str = "armoiries"

class DistinctionHonorifique(BaseModel):
    sous_descripteur: Literal['DistinctionHonorifique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1200"
    descripteur: str = "distinction honorifique"

class BaptemeCivil(BaseModel):
    sous_descripteur: Literal['BaptemeCivil']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1124"
    descripteur: str = "baptême civil"

class Commemoration(BaseModel):
    sous_descripteur: Literal['Commemoration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-953"
    descripteur: str = "commémoration"

class Secte(BaseModel):
    sous_descripteur: Literal['Secte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-818"
    descripteur: str = "secte"

class Propagande(BaseModel):
    sous_descripteur: Literal['Propagande']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1274"
    descripteur: str = "propagande"

class Jumelage(BaseModel):
    sous_descripteur: Literal['Jumelage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-753"
    descripteur: str = "jumelage"

class OpinionPublique(BaseModel):
    sous_descripteur: Literal['OpinionPublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-681"
    descripteur: str = "opinion publique"

class Censure(BaseModel):
    sous_descripteur: Literal['Censure']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-528"
    descripteur: str = "censure"

class FeteNationale(BaseModel):
    sous_descripteur: Literal['FeteNationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1125"
    descripteur: str = "fête nationale"

class Drapeau(BaseModel):
    sous_descripteur: Literal['Drapeau']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-757"
    descripteur: str = "drapeau"

class HymneNational(BaseModel):
    sous_descripteur: Literal['HymneNational']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-660"
    descripteur: str = "hymne national"

class CostumeOfficiel(BaseModel):
    sous_descripteur: Literal['CostumeOfficiel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-515"
    descripteur: str = "costume officiel"

class SymboliqueOfficielle(BaseModel):
    sous_descripteur: Union['CostumeOfficiel', 'HymneNational', 'Drapeau', 'FeteNationale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1126"
    descripteur: str = "symbolique officielle"

class Personnalite(BaseModel):
    sous_descripteur: Literal['Personnalite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-473"
    descripteur: str = "personnalité"

class FrancMaeon(BaseModel):
    sous_descripteur: Literal['FrancMaeon']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-361"
    descripteur: str = "franc maçon"

class SocieteSecrete(BaseModel):
    sous_descripteur: Union['FrancMaeon'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-370"
    descripteur: str = "société secrète"

class RelationsAvecLesUsagers(BaseModel):
    sous_descripteur: Literal['RelationsAvecLesUsagers']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-761"
    descripteur: str = "relations avec les usagers"

class CommunicationInstitutionnelle(BaseModel):
    sous_descripteur: Literal['CommunicationInstitutionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-308"
    descripteur: str = "communication institutionnelle"

class InterventionDelu(BaseModel):
    sous_descripteur: Literal['InterventionDelu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-685"
    descripteur: str = "intervention d'élu"

class RelationsPubliques(BaseModel):
    sous_descripteur: Union['InterventionDelu', 'CommunicationInstitutionnelle', 'RelationsAvecLesUsagers'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1388"
    descripteur: str = "relations publiques"

class PresseRegionale(BaseModel):
    sous_descripteur: Literal['PresseRegionale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1358"
    descripteur: str = "presse régionale"

class PublicationInterne(BaseModel):
    sous_descripteur: Literal['PublicationInterne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-968"
    descripteur: str = "publication interne"

class Journaliste(BaseModel):
    sous_descripteur: Literal['Journaliste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1186"
    descripteur: str = "journaliste"

class DepotLegal(BaseModel):
    sous_descripteur: Literal['DepotLegal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-813"
    descripteur: str = "dépôt légal"

class ReporterPhotographe(BaseModel):
    sous_descripteur: Literal['ReporterPhotographe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-576"
    descripteur: str = "reporter photographe"

class Presse(BaseModel):
    sous_descripteur: Union['ReporterPhotographe', 'DepotLegal', 'Journaliste', 'PublicationInterne', 'PresseRegionale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-140"
    descripteur: str = "presse"

class DeuilPublic(BaseModel):
    sous_descripteur: Literal['DeuilPublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1488"
    descripteur: str = "deuil public"

class CeremonieMilitaire(BaseModel):
    sous_descripteur: Literal['CeremonieMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1486"
    descripteur: str = "cérémonie militaire"

class Inauguration(BaseModel):
    sous_descripteur: Literal['Inauguration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1335"
    descripteur: str = "inauguration"

class ReceptionOfficielle(BaseModel):
    sous_descripteur: Literal['ReceptionOfficielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-194"
    descripteur: str = "réception officielle"

class PrierePublique(BaseModel):
    sous_descripteur: Literal['PrierePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1310"
    descripteur: str = "prière publique"

class EntreeSolennelle(BaseModel):
    sous_descripteur: Literal['EntreeSolennelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-936"
    descripteur: str = "entrée solennelle"

class VisiteOfficielle(BaseModel):
    sous_descripteur: Literal['VisiteOfficielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-606"
    descripteur: str = "visite officielle"

class CeremoniePublique(BaseModel):
    sous_descripteur: Union['VisiteOfficielle', 'EntreeSolennelle', 'PrierePublique', 'ReceptionOfficielle', 'Inauguration', 'CeremonieMilitaire', 'DeuilPublic'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-21"
    descripteur: str = "cérémonie publique"

class SocieteRevolutionnaire(BaseModel):
    sous_descripteur: Literal['SocieteRevolutionnaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-16"
    descripteur: str = "société révolutionnaire"

class Donsetlegs(BaseModel):
    sous_descripteur: Literal['Donsetlegs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-838"
    descripteur: str = "dons-et-legs"

class AssociationReconnueDutilitePublique(BaseModel):
    sous_descripteur: Literal['AssociationReconnueDutilitePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-997"
    descripteur: str = "association reconnue d'utilité publique"

class Fondation(BaseModel):
    sous_descripteur: Literal['Fondation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1379"
    descripteur: str = "fondation"

class Association(BaseModel):
    sous_descripteur: Union['Fondation', 'AssociationReconnueDutilitePublique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-760"
    descripteur: str = "association"

class ViePublique(BaseModel):
    sous_descripteur: Union['Association', 'Donsetlegs', 'SocieteRevolutionnaire', 'CeremoniePublique', 'Presse', 'RelationsPubliques', 'SocieteSecrete', 'Personnalite', 'SymboliqueOfficielle', 'Censure', 'OpinionPublique', 'Jumelage', 'Propagande', 'Secte', 'Commemoration', 'BaptemeCivil', 'DistinctionHonorifique', 'Armoiries', 'ManifestationPublique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1174"
    descripteur: str = "vie publique"

class Opinion(BaseModel):
    sous_descripteur: Union['ViePublique', 'ViePolitique', 'MouvementDidees', 'VieReligieuse', 'Election', 'CroyancesEtSciencesParalleles'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-906"
    descripteur: str = "opinion"
