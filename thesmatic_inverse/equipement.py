from pydantic import BaseModel
from typing import Union, Literal

class Mer(BaseModel):
    terme_specifique: Literal['Mer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1318"
    descripteur: str = "mer"

class LutteContreLerosion(BaseModel):
    terme_specifique: Literal['LutteContreLerosion']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-990"
    descripteur: str = "lutte contre l'érosion"

class CommissaireEnqueteur(BaseModel):
    terme_specifique: Literal['CommissaireEnqueteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-840"
    descripteur: str = "commissaire enquêteur"

class Expropriation(BaseModel):
    terme_specifique: Literal['Expropriation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1361"
    descripteur: str = "expropriation"

class TravauxDutilitePublique(BaseModel):
    terme_specifique: Union['Expropriation', 'CommissaireEnqueteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-971"
    descripteur: str = "travaux d'utilité publique"

class Bathymetrie(BaseModel):
    terme_specifique: Literal['Bathymetrie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1205"
    descripteur: str = "bathymétrie"

class Cartographie(BaseModel):
    terme_specifique: Union['Bathymetrie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1143"
    descripteur: str = "cartographie"

class Biodiversite(BaseModel):
    terme_specifique: Literal['Biodiversite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1303"
    descripteur: str = "biodiversité"

class FloreSauvage(BaseModel):
    terme_specifique: Literal['FloreSauvage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1211"
    descripteur: str = "flore sauvage"

class ReserveNaturelle(BaseModel):
    terme_specifique: Literal['ReserveNaturelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-599"
    descripteur: str = "réserve naturelle"

class ParcNaturel(BaseModel):
    terme_specifique: Literal['ParcNaturel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1057"
    descripteur: str = "parc naturel"

class FauneSauvage(BaseModel):
    terme_specifique: Literal['FauneSauvage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1357"
    descripteur: str = "faune sauvage"

class Site(BaseModel):
    terme_specifique: Literal['Site']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-233"
    descripteur: str = "site"

class EspeceProtegee(BaseModel):
    terme_specifique: Literal['EspeceProtegee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-130"
    descripteur: str = "espèce protégée"

class AssociationDeDefenseDeLenvironnement(BaseModel):
    terme_specifique: Literal['AssociationDeDefenseDeLenvironnement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-458"
    descripteur: str = "association de défense de l'environnement"

class ProtectionDeLaNature(BaseModel):
    terme_specifique: Union['AssociationDeDefenseDeLenvironnement', 'EspeceProtegee', 'Site', 'FauneSauvage', 'ParcNaturel', 'ReserveNaturelle', 'FloreSauvage', 'Biodiversite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1365"
    descripteur: str = "protection de la nature"

class ZoneDeMarais(BaseModel):
    terme_specifique: Literal['ZoneDeMarais']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1185"
    descripteur: str = "zone de marais"

class Deforestation(BaseModel):
    terme_specifique: Literal['Deforestation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-91"
    descripteur: str = "déforestation"

class EspaceNaturelSensible(BaseModel):
    terme_specifique: Union['Deforestation', 'ZoneDeMarais']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-739"
    descripteur: str = "espace naturel sensible"

class Intemperies(BaseModel):
    terme_specifique: Literal['Intemperies']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1481"
    descripteur: str = "intempéries"

class Canicule(BaseModel):
    terme_specifique: Literal['Canicule']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1480"
    descripteur: str = "canicule"

class Meteorologie(BaseModel):
    terme_specifique: Union['Canicule', 'Intemperies']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-663"
    descripteur: str = "météorologie"

class PollutionDuSol(BaseModel):
    terme_specifique: Literal['PollutionDuSol']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1501"
    descripteur: str = "pollution du sol"

class PollutionDeLaMer(BaseModel):
    terme_specifique: Literal['PollutionDeLaMer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-327"
    descripteur: str = "pollution de la mer"

class PollutionSonore(BaseModel):
    terme_specifique: Literal['PollutionSonore']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-375"
    descripteur: str = "pollution sonore"

class PollutionDesEaux(BaseModel):
    terme_specifique: Literal['PollutionDesEaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1420"
    descripteur: str = "pollution des eaux"

class PollutionAtmospherique(BaseModel):
    terme_specifique: Literal['PollutionAtmospherique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-714"
    descripteur: str = "pollution atmosphérique"

class PollutionVisuelle(BaseModel):
    terme_specifique: Literal['PollutionVisuelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-157"
    descripteur: str = "pollution visuelle"

class Pollution(BaseModel):
    terme_specifique: Union['PollutionVisuelle', 'PollutionAtmospherique', 'PollutionDesEaux', 'PollutionSonore', 'PollutionDeLaMer', 'PollutionDuSol']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-286"
    descripteur: str = "pollution"

class RestaurationDesTerrainsEnMontagne(BaseModel):
    terme_specifique: Literal['RestaurationDesTerrainsEnMontagne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1004"
    descripteur: str = "restauration des terrains en montagne"

class Montagne(BaseModel):
    terme_specifique: Union['RestaurationDesTerrainsEnMontagne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-334"
    descripteur: str = "montagne"

class DechargePublique(BaseModel):
    terme_specifique: Literal['DechargePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1159"
    descripteur: str = "décharge publique"

class UsineDincineration(BaseModel):
    terme_specifique: Literal['UsineDincineration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-722"
    descripteur: str = "usine d'incinération"

class DechetHospitalier(BaseModel):
    terme_specifique: Literal['DechetHospitalier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-800"
    descripteur: str = "déchet hospitalier"

class OrduresMenageres(BaseModel):
    terme_specifique: Literal['OrduresMenageres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1129"
    descripteur: str = "ordures ménagères"

class DechetAnimal(BaseModel):
    terme_specifique: Literal['DechetAnimal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-378"
    descripteur: str = "déchet animal"

class DechetRadioactif(BaseModel):
    terme_specifique: Literal['DechetRadioactif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-36"
    descripteur: str = "déchet radioactif"

class DechetIndustriel(BaseModel):
    terme_specifique: Literal['DechetIndustriel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-442"
    descripteur: str = "déchet industriel"

class TraitementDesDechets(BaseModel):
    terme_specifique: Union['DechetIndustriel', 'DechetRadioactif', 'DechetAnimal', 'OrduresMenageres', 'DechetHospitalier', 'UsineDincineration', 'DechargePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-362"
    descripteur: str = "traitement des déchets"

class DefenseContreLaMer(BaseModel):
    terme_specifique: Literal['DefenseContreLaMer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1108"
    descripteur: str = "défense contre la mer"

class Plage(BaseModel):
    terme_specifique: Literal['Plage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-14"
    descripteur: str = "plage"

class Littoral(BaseModel):
    terme_specifique: Union['Plage', 'DefenseContreLaMer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-762"
    descripteur: str = "littoral"

class EauPluviale(BaseModel):
    terme_specifique: Literal['EauPluviale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1288"
    descripteur: str = "eau pluviale"

class TraitementDesEauxUsees(BaseModel):
    terme_specifique: Literal['TraitementDesEauxUsees']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-589"
    descripteur: str = "traitement des eaux usées"

class Chenal(BaseModel):
    terme_specifique: Literal['Chenal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-243"
    descripteur: str = "chenal"

class EauSouterraine(BaseModel):
    terme_specifique: Literal['EauSouterraine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-149"
    descripteur: str = "eau souterraine"

class NappeDeau(BaseModel):
    terme_specifique: Literal['NappeDeau']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1276"
    descripteur: str = "nappe d'eau"

class CoursDeau(BaseModel):
    terme_specifique: Literal['CoursDeau']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-607"
    descripteur: str = "cours d'eau"

class PriseDeau(BaseModel):
    terme_specifique: Literal['PriseDeau']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-944"
    descripteur: str = "prise d'eau"

class AmenagementDesEaux(BaseModel):
    terme_specifique: Literal['AmenagementDesEaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-988"
    descripteur: str = "aménagement des eaux"

class Eau(BaseModel):
    terme_specifique: Union['AmenagementDesEaux', 'PriseDeau', 'CoursDeau', 'NappeDeau', 'EauSouterraine', 'Chenal', 'TraitementDesEauxUsees', 'EauPluviale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-695"
    descripteur: str = "eau"

class Environnement(BaseModel):
    terme_specifique: Union['Eau', 'Littoral', 'TraitementDesDechets', 'Montagne', 'Pollution', 'Meteorologie', 'EspaceNaturelSensible', 'ProtectionDeLaNature', 'Cartographie', 'TravauxDutilitePublique', 'LutteContreLerosion', 'Mer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1074"
    descripteur: str = "environnement"

class Fleurissement(BaseModel):
    terme_specifique: Literal['Fleurissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-778"
    descripteur: str = "fleurissement"

class SecteurSauvegarde(BaseModel):
    terme_specifique: Literal['SecteurSauvegarde']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1105"
    descripteur: str = "secteur sauvegardé"

class Reconstruction(BaseModel):
    terme_specifique: Literal['Reconstruction']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-444"
    descripteur: str = "reconstruction"

class EtalementUrbain(BaseModel):
    terme_specifique: Literal['EtalementUrbain']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1246"
    descripteur: str = "étalement urbain"

class MobilierUrbain(BaseModel):
    terme_specifique: Literal['MobilierUrbain']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1131"
    descripteur: str = "mobilier urbain"

class DecorationUrbaine(BaseModel):
    terme_specifique: Literal['DecorationUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-168"
    descripteur: str = "décoration urbaine"

class ZoneDamenagement(BaseModel):
    terme_specifique: Literal['ZoneDamenagement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-858"
    descripteur: str = "zone d'aménagement"

class FricheIndustrielle(BaseModel):
    terme_specifique: Literal['FricheIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-469"
    descripteur: str = "friche industrielle"

class AssociationFonciereUrbaine(BaseModel):
    terme_specifique: Literal['AssociationFonciereUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-138"
    descripteur: str = "association foncière urbaine"

class ReserveFonciere(BaseModel):
    terme_specifique: Literal['ReserveFonciere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1193"
    descripteur: str = "réserve foncière"

class AmenagementFoncier(BaseModel):
    terme_specifique: Union['ReserveFonciere', 'AssociationFonciereUrbaine', 'FricheIndustrielle', 'ZoneDamenagement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1266"
    descripteur: str = "aménagement foncier"

class Urbaniste(BaseModel):
    terme_specifique: Literal['Urbaniste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-84"
    descripteur: str = "urbaniste"

class RestaurationImmobiliere(BaseModel):
    terme_specifique: Literal['RestaurationImmobiliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-124"
    descripteur: str = "restauration immobilière"

class RestructurationUrbaine(BaseModel):
    terme_specifique: Literal['RestructurationUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1097"
    descripteur: str = "restructuration urbaine"

class Lotissement(BaseModel):
    terme_specifique: Literal['Lotissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-475"
    descripteur: str = "lotissement"

class OperationDurbanisme(BaseModel):
    terme_specifique: Union['Lotissement', 'RestructurationUrbaine', 'RestaurationImmobiliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-83"
    descripteur: str = "opération d'urbanisme"

class DistributionDeGaz(BaseModel):
    terme_specifique: Literal['DistributionDeGaz']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1295"
    descripteur: str = "distribution de gaz"

class Canalisation(BaseModel):
    terme_specifique: Literal['Canalisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-856"
    descripteur: str = "canalisation"

class EauPotable(BaseModel):
    terme_specifique: Literal['EauPotable']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-537"
    descripteur: str = "eau potable"

class ChauffageUrbain(BaseModel):
    terme_specifique: Literal['ChauffageUrbain']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-510"
    descripteur: str = "chauffage urbain"

class DistributionElectrique(BaseModel):
    terme_specifique: Literal['DistributionElectrique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-937"
    descripteur: str = "distribution électrique"

class EclairagePublic(BaseModel):
    terme_specifique: Literal['EclairagePublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-63"
    descripteur: str = "éclairage public"

class ReseauDeDistribution(BaseModel):
    terme_specifique: Union['EclairagePublic', 'DistributionElectrique', 'ChauffageUrbain', 'EauPotable', 'Canalisation', 'DistributionDeGaz']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-755"
    descripteur: str = "réseau de distribution"

class InstallationSanitairePublique(BaseModel):
    terme_specifique: Literal['InstallationSanitairePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1482"
    descripteur: str = "installation sanitaire publique"

class Fontaine(BaseModel):
    terme_specifique: Literal['Fontaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-835"
    descripteur: str = "fontaine"

class HorlogePublique(BaseModel):
    terme_specifique: Literal['HorlogePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-570"
    descripteur: str = "horloge publique"

class Lavoir(BaseModel):
    terme_specifique: Literal['Lavoir']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1320"
    descripteur: str = "lavoir"

class Puits(BaseModel):
    terme_specifique: Literal['Puits']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-884"
    descripteur: str = "puits"

class Halle(BaseModel):
    terme_specifique: Literal['Halle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-960"
    descripteur: str = "halle"

class PlacePublique(BaseModel):
    terme_specifique: Literal['PlacePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1216"
    descripteur: str = "place publique"

class AireDeJeux(BaseModel):
    terme_specifique: Literal['AireDeJeux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-549"
    descripteur: str = "aire de jeux"

class ChampDeFoire(BaseModel):
    terme_specifique: Literal['ChampDeFoire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-465"
    descripteur: str = "champ de foire"

class AireDeStationnement(BaseModel):
    terme_specifique: Literal['AireDeStationnement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1128"
    descripteur: str = "aire de stationnement"

class BatimentPolyvalent(BaseModel):
    terme_specifique: Literal['BatimentPolyvalent']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-34"
    descripteur: str = "bâtiment polyvalent"

class EspaceVert(BaseModel):
    terme_specifique: Literal['EspaceVert']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-403"
    descripteur: str = "espace vert"

class Cimetiere(BaseModel):
    terme_specifique: Literal['Cimetiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-773"
    descripteur: str = "cimetière"

class EquipementCollectif(BaseModel):
    terme_specifique: Union['Cimetiere', 'EspaceVert', 'BatimentPolyvalent', 'AireDeStationnement', 'ChampDeFoire', 'AireDeJeux', 'PlacePublique', 'Halle', 'Puits', 'Lavoir', 'HorlogePublique', 'Fontaine', 'InstallationSanitairePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-508"
    descripteur: str = "équipement collectif"

class Urbanisme(BaseModel):
    terme_specifique: Union['EquipementCollectif', 'ReseauDeDistribution', 'OperationDurbanisme', 'Urbaniste', 'AmenagementFoncier', 'DecorationUrbaine', 'MobilierUrbain', 'EtalementUrbain', 'Reconstruction', 'SecteurSauvegarde', 'Fleurissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-209"
    descripteur: str = "urbanisme"

class Telepherique(BaseModel):
    terme_specifique: Literal['Telepherique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1087"
    descripteur: str = "téléphérique"

class VoiePietonne(BaseModel):
    terme_specifique: Literal['VoiePietonne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1120"
    descripteur: str = "voie piétonne"

class PromenadePlantee(BaseModel):
    terme_specifique: Literal['PromenadePlantee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-754"
    descripteur: str = "promenade plantée"

class PisteCyclable(BaseModel):
    terme_specifique: Literal['PisteCyclable']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-502"
    descripteur: str = "piste cyclable"

class LiaisonDouce(BaseModel):
    terme_specifique: Union['PisteCyclable', 'PromenadePlantee', 'VoiePietonne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-661"
    descripteur: str = "liaison douce"

class VoieNavigable(BaseModel):
    terme_specifique: Literal['VoieNavigable']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-326"
    descripteur: str = "voie navigable"

class OuvrageDart(BaseModel):
    terme_specifique: Literal['OuvrageDart']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-48"
    descripteur: str = "ouvrage d'art"

class VoieFerreeDinteretNational(BaseModel):
    terme_specifique: Literal['VoieFerreeDinteretNational']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-985"
    descripteur: str = "voie ferrée d'intérêt national"

class VoieFerreeDinteretLocal(BaseModel):
    terme_specifique: Literal['VoieFerreeDinteretLocal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-443"
    descripteur: str = "voie ferrée d'intérêt local"

class VoieFerreeDesQuais(BaseModel):
    terme_specifique: Literal['VoieFerreeDesQuais']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1206"
    descripteur: str = "voie ferrée des quais"

class VoieFerreePrivee(BaseModel):
    terme_specifique: Literal['VoieFerreePrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-30"
    descripteur: str = "voie ferrée privée"

class ReseauFerroviaire(BaseModel):
    terme_specifique: Union['VoieFerreePrivee', 'VoieFerreeDesQuais', 'VoieFerreeDinteretLocal', 'VoieFerreeDinteretNational']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-736"
    descripteur: str = "réseau ferroviaire"

class VoieIntercommunale(BaseModel):
    terme_specifique: Literal['VoieIntercommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1380"
    descripteur: str = "voie intercommunale"

class RouteDepartementale(BaseModel):
    terme_specifique: Literal['RouteDepartementale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1147"
    descripteur: str = "route départementale"

class RouteForestiere(BaseModel):
    terme_specifique: Literal['RouteForestiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-734"
    descripteur: str = "route forestière"

class Autoroute(BaseModel):
    terme_specifique: Literal['Autoroute']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-451"
    descripteur: str = "autoroute"

class VoieCommunale(BaseModel):
    terme_specifique: Literal['VoieCommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-395"
    descripteur: str = "voie communale"

class VoiePrivee(BaseModel):
    terme_specifique: Literal['VoiePrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-76"
    descripteur: str = "voie privée"

class RouteNationale(BaseModel):
    terme_specifique: Literal['RouteNationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-5"
    descripteur: str = "route nationale"

class CheminRural(BaseModel):
    terme_specifique: Literal['CheminRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-908"
    descripteur: str = "chemin rural"

class ReseauRoutier(BaseModel):
    terme_specifique: Union['CheminRural', 'RouteNationale', 'VoiePrivee', 'VoieCommunale', 'Autoroute', 'RouteForestiere', 'RouteDepartementale', 'VoieIntercommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1149"
    descripteur: str = "réseau routier"

class VoieDeCommunication(BaseModel):
    terme_specifique: Union['ReseauRoutier', 'ReseauFerroviaire', 'OuvrageDart', 'VoieNavigable', 'LiaisonDouce', 'Telepherique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1334"
    descripteur: str = "voie de communication"

class LogementDeFonction(BaseModel):
    terme_specifique: Literal['LogementDeFonction']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1448"
    descripteur: str = "logement de fonction"

class HabitationALoyerModere(BaseModel):
    terme_specifique: Literal['HabitationALoyerModere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1065"
    descripteur: str = "habitation à loyer modéré"

class JardinFamilial(BaseModel):
    terme_specifique: Literal['JardinFamilial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1409"
    descripteur: str = "jardin familial"

class Foyer(BaseModel):
    terme_specifique: Literal['Foyer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-626"
    descripteur: str = "foyer"

class LogementSocial(BaseModel):
    terme_specifique: Union['Foyer', 'JardinFamilial', 'HabitationALoyerModere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1001"
    descripteur: str = "logement social"

class Demolition(BaseModel):
    terme_specifique: Literal['Demolition']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-671"
    descripteur: str = "démolition"

class SyndicDeCopropriete(BaseModel):
    terme_specifique: Literal['SyndicDeCopropriete']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1045"
    descripteur: str = "syndic de copropriété"

class CentreVille(BaseModel):
    terme_specifique: Literal['CentreVille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1230"
    descripteur: str = "centre ville"

class HabitatPeriurbain(BaseModel):
    terme_specifique: Literal['HabitatPeriurbain']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-774"
    descripteur: str = "habitat périurbain"

class HabitatUrbain(BaseModel):
    terme_specifique: Union['HabitatPeriurbain', 'CentreVille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1133"
    descripteur: str = "habitat urbain"

class AgentImmobilier(BaseModel):
    terme_specifique: Literal['AgentImmobilier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-437"
    descripteur: str = "agent immobilier"

class MarcheImmobilier(BaseModel):
    terme_specifique: Union['AgentImmobilier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-706"
    descripteur: str = "marché immobilier"

class HabitatInsalubre(BaseModel):
    terme_specifique: Literal['HabitatInsalubre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-523"
    descripteur: str = "habitat insalubre"

class AmeliorationDeLhabitat(BaseModel):
    terme_specifique: Union['HabitatInsalubre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1170"
    descripteur: str = "amélioration de l'habitat"

class LogementCollectif(BaseModel):
    terme_specifique: Literal['LogementCollectif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-772"
    descripteur: str = "logement collectif"

class LogementIndividuel(BaseModel):
    terme_specifique: Literal['LogementIndividuel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-656"
    descripteur: str = "logement individuel"

class LoyerImmobilier(BaseModel):
    terme_specifique: Literal['LoyerImmobilier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1130"
    descripteur: str = "loyer immobilier"

class ExpulsionLocative(BaseModel):
    terme_specifique: Literal['ExpulsionLocative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-302"
    descripteur: str = "expulsion locative"

class Logement(BaseModel):
    terme_specifique: Union['ExpulsionLocative', 'LoyerImmobilier', 'LogementIndividuel', 'LogementCollectif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-290"
    descripteur: str = "logement"

class SurveillanceDesBatiments(BaseModel):
    terme_specifique: Literal['SurveillanceDesBatiments']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-441"
    descripteur: str = "surveillance des bâtiments"

class ParticipationDesEmployeurs(BaseModel):
    terme_specifique: Literal['ParticipationDesEmployeurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-914"
    descripteur: str = "participation des employeurs"

class Chantier(BaseModel):
    terme_specifique: Literal['Chantier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-595"
    descripteur: str = "chantier"

class SondageGeologique(BaseModel):
    terme_specifique: Literal['SondageGeologique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-292"
    descripteur: str = "sondage géologique"

class EntrepriseDuBatiment(BaseModel):
    terme_specifique: Literal['EntrepriseDuBatiment']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-227"
    descripteur: str = "entreprise du bâtiment"

class OuvrierDuBatiment(BaseModel):
    terme_specifique: Literal['OuvrierDuBatiment']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1346"
    descripteur: str = "ouvrier du bâtiment"

class SocieteDeConstruction(BaseModel):
    terme_specifique: Literal['SocieteDeConstruction']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-654"
    descripteur: str = "société de construction"

class Construction(BaseModel):
    terme_specifique: Union['SocieteDeConstruction', 'OuvrierDuBatiment', 'EntrepriseDuBatiment', 'SondageGeologique', 'Chantier', 'ParticipationDesEmployeurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-396"
    descripteur: str = "construction"

class Architecte(BaseModel):
    terme_specifique: Literal['Architecte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-738"
    descripteur: str = "architecte"

class RequisitionDeLogement(BaseModel):
    terme_specifique: Literal['RequisitionDeLogement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-72"
    descripteur: str = "réquisition de logement"

class AccessionALaPropriete(BaseModel):
    terme_specifique: Literal['AccessionALaPropriete']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-153"
    descripteur: str = "accession à la propriété"

class AidePubliqueAuLogement(BaseModel):
    terme_specifique: Union['AccessionALaPropriete']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-41"
    descripteur: str = "aide publique au logement"

class VentePubliqueImmobiliere(BaseModel):
    terme_specifique: Literal['VentePubliqueImmobiliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1438"
    descripteur: str = "vente publique immobilière"

class HabitatRural(BaseModel):
    terme_specifique: Literal['HabitatRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1"
    descripteur: str = "habitat rural"

class Immobilier(BaseModel):
    terme_specifique: Union['HabitatRural', 'VentePubliqueImmobiliere', 'AidePubliqueAuLogement', 'RequisitionDeLogement', 'Architecte', 'Construction', 'SurveillanceDesBatiments', 'Logement', 'AmeliorationDeLhabitat', 'MarcheImmobilier', 'HabitatUrbain', 'SyndicDeCopropriete', 'Demolition', 'LogementSocial', 'LogementDeFonction']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-556"
    descripteur: str = "immobilier"

class Equipement(BaseModel):
    terme_specifique: Union['Immobilier', 'VoieDeCommunication', 'Urbanisme', 'Environnement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1262"
    descripteur: str = "équipement"
