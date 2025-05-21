from pydantic import BaseModel, Field
from typing import Union, Literal

class Mer(BaseModel):
    sous_descripteur: Literal['Mer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1318"
    descripteur: str = "mer"

class LutteContreLerosion(BaseModel):
    sous_descripteur: Literal['LutteContreLerosion']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-990"
    descripteur: str = "lutte contre l'érosion"

class CommissaireEnqueteur(BaseModel):
    sous_descripteur: Literal['CommissaireEnqueteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-840"
    descripteur: str = "commissaire enquêteur"

class Expropriation(BaseModel):
    sous_descripteur: Literal['Expropriation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1361"
    descripteur: str = "expropriation"

class TravauxDutilitePublique(BaseModel):
    sous_descripteur: Union['Expropriation', 'CommissaireEnqueteur'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-971"
    descripteur: str = "travaux d'utilité publique"

class Bathymetrie(BaseModel):
    sous_descripteur: Literal['Bathymetrie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1205"
    descripteur: str = "bathymétrie"

class Cartographie(BaseModel):
    sous_descripteur: Union['Bathymetrie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1143"
    descripteur: str = "cartographie"

class Biodiversite(BaseModel):
    sous_descripteur: Literal['Biodiversite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1303"
    descripteur: str = "biodiversité"

class FloreSauvage(BaseModel):
    sous_descripteur: Literal['FloreSauvage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1211"
    descripteur: str = "flore sauvage"

class ReserveNaturelle(BaseModel):
    sous_descripteur: Literal['ReserveNaturelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-599"
    descripteur: str = "réserve naturelle"

class ParcNaturel(BaseModel):
    sous_descripteur: Literal['ParcNaturel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1057"
    descripteur: str = "parc naturel"

class FauneSauvage(BaseModel):
    sous_descripteur: Literal['FauneSauvage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1357"
    descripteur: str = "faune sauvage"

class Site(BaseModel):
    sous_descripteur: Literal['Site']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-233"
    descripteur: str = "site"

class EspeceProtegee(BaseModel):
    sous_descripteur: Literal['EspeceProtegee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-130"
    descripteur: str = "espèce protégée"

class AssociationDeDefenseDeLenvironnement(BaseModel):
    sous_descripteur: Literal['AssociationDeDefenseDeLenvironnement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-458"
    descripteur: str = "association de défense de l'environnement"

class ProtectionDeLaNature(BaseModel):
    sous_descripteur: Union['AssociationDeDefenseDeLenvironnement', 'EspeceProtegee', 'Site', 'FauneSauvage', 'ParcNaturel', 'ReserveNaturelle', 'FloreSauvage', 'Biodiversite'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1365"
    descripteur: str = "protection de la nature"

class ZoneDeMarais(BaseModel):
    sous_descripteur: Literal['ZoneDeMarais']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1185"
    descripteur: str = "zone de marais"

class Deforestation(BaseModel):
    sous_descripteur: Literal['Deforestation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-91"
    descripteur: str = "déforestation"

class EspaceNaturelSensible(BaseModel):
    sous_descripteur: Union['Deforestation', 'ZoneDeMarais'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-739"
    descripteur: str = "espace naturel sensible"

class Intemperies(BaseModel):
    sous_descripteur: Literal['Intemperies']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1481"
    descripteur: str = "intempéries"

class Canicule(BaseModel):
    sous_descripteur: Literal['Canicule']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1480"
    descripteur: str = "canicule"

class Meteorologie(BaseModel):
    sous_descripteur: Union['Canicule', 'Intemperies'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-663"
    descripteur: str = "météorologie"

class PollutionDuSol(BaseModel):
    sous_descripteur: Literal['PollutionDuSol']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1501"
    descripteur: str = "pollution du sol"

class PollutionDeLaMer(BaseModel):
    sous_descripteur: Literal['PollutionDeLaMer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-327"
    descripteur: str = "pollution de la mer"

class PollutionSonore(BaseModel):
    sous_descripteur: Literal['PollutionSonore']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-375"
    descripteur: str = "pollution sonore"

class PollutionDesEaux(BaseModel):
    sous_descripteur: Literal['PollutionDesEaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1420"
    descripteur: str = "pollution des eaux"

class PollutionAtmospherique(BaseModel):
    sous_descripteur: Literal['PollutionAtmospherique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-714"
    descripteur: str = "pollution atmosphérique"

class PollutionVisuelle(BaseModel):
    sous_descripteur: Literal['PollutionVisuelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-157"
    descripteur: str = "pollution visuelle"

class Pollution(BaseModel):
    sous_descripteur: Union['PollutionVisuelle', 'PollutionAtmospherique', 'PollutionDesEaux', 'PollutionSonore', 'PollutionDeLaMer', 'PollutionDuSol'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-286"
    descripteur: str = "pollution"

class RestaurationDesTerrainsEnMontagne(BaseModel):
    sous_descripteur: Literal['RestaurationDesTerrainsEnMontagne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1004"
    descripteur: str = "restauration des terrains en montagne"

class Montagne(BaseModel):
    sous_descripteur: Union['RestaurationDesTerrainsEnMontagne'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-334"
    descripteur: str = "montagne"

class DechargePublique(BaseModel):
    sous_descripteur: Literal['DechargePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1159"
    descripteur: str = "décharge publique"

class UsineDincineration(BaseModel):
    sous_descripteur: Literal['UsineDincineration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-722"
    descripteur: str = "usine d'incinération"

class DechetHospitalier(BaseModel):
    sous_descripteur: Literal['DechetHospitalier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-800"
    descripteur: str = "déchet hospitalier"

class OrduresMenageres(BaseModel):
    sous_descripteur: Literal['OrduresMenageres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1129"
    descripteur: str = "ordures ménagères"

class DechetAnimal(BaseModel):
    sous_descripteur: Literal['DechetAnimal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-378"
    descripteur: str = "déchet animal"

class DechetRadioactif(BaseModel):
    sous_descripteur: Literal['DechetRadioactif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-36"
    descripteur: str = "déchet radioactif"

class DechetIndustriel(BaseModel):
    sous_descripteur: Literal['DechetIndustriel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-442"
    descripteur: str = "déchet industriel"

class TraitementDesDechets(BaseModel):
    sous_descripteur: Union['DechetIndustriel', 'DechetRadioactif', 'DechetAnimal', 'OrduresMenageres', 'DechetHospitalier', 'UsineDincineration', 'DechargePublique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-362"
    descripteur: str = "traitement des déchets"

class DefenseContreLaMer(BaseModel):
    sous_descripteur: Literal['DefenseContreLaMer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1108"
    descripteur: str = "défense contre la mer"

class Plage(BaseModel):
    sous_descripteur: Literal['Plage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-14"
    descripteur: str = "plage"

class Littoral(BaseModel):
    sous_descripteur: Union['Plage', 'DefenseContreLaMer'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-762"
    descripteur: str = "littoral"

class EauPluviale(BaseModel):
    sous_descripteur: Literal['EauPluviale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1288"
    descripteur: str = "eau pluviale"

class TraitementDesEauxUsees(BaseModel):
    sous_descripteur: Literal['TraitementDesEauxUsees']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-589"
    descripteur: str = "traitement des eaux usées"

class Chenal(BaseModel):
    sous_descripteur: Literal['Chenal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-243"
    descripteur: str = "chenal"

class EauSouterraine(BaseModel):
    sous_descripteur: Literal['EauSouterraine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-149"
    descripteur: str = "eau souterraine"

class NappeDeau(BaseModel):
    sous_descripteur: Literal['NappeDeau']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1276"
    descripteur: str = "nappe d'eau"

class CoursDeau(BaseModel):
    sous_descripteur: Literal['CoursDeau']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-607"
    descripteur: str = "cours d'eau"

class PriseDeau(BaseModel):
    sous_descripteur: Literal['PriseDeau']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-944"
    descripteur: str = "prise d'eau"

class AmenagementDesEaux(BaseModel):
    sous_descripteur: Literal['AmenagementDesEaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-988"
    descripteur: str = "aménagement des eaux"

class Eau(BaseModel):
    sous_descripteur: Union['AmenagementDesEaux', 'PriseDeau', 'CoursDeau', 'NappeDeau', 'EauSouterraine', 'Chenal', 'TraitementDesEauxUsees', 'EauPluviale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-695"
    descripteur: str = "eau"

class Environnement(BaseModel):
    sous_descripteur: Union['Eau', 'Littoral', 'TraitementDesDechets', 'Montagne', 'Pollution', 'Meteorologie', 'EspaceNaturelSensible', 'ProtectionDeLaNature', 'Cartographie', 'TravauxDutilitePublique', 'LutteContreLerosion', 'Mer'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1074"
    descripteur: str = "environnement"

class Fleurissement(BaseModel):
    sous_descripteur: Literal['Fleurissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-778"
    descripteur: str = "fleurissement"

class SecteurSauvegarde(BaseModel):
    sous_descripteur: Literal['SecteurSauvegarde']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1105"
    descripteur: str = "secteur sauvegardé"

class Reconstruction(BaseModel):
    sous_descripteur: Literal['Reconstruction']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-444"
    descripteur: str = "reconstruction"

class EtalementUrbain(BaseModel):
    sous_descripteur: Literal['EtalementUrbain']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1246"
    descripteur: str = "étalement urbain"

class MobilierUrbain(BaseModel):
    sous_descripteur: Literal['MobilierUrbain']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1131"
    descripteur: str = "mobilier urbain"

class DecorationUrbaine(BaseModel):
    sous_descripteur: Literal['DecorationUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-168"
    descripteur: str = "décoration urbaine"

class ZoneDamenagement(BaseModel):
    sous_descripteur: Literal['ZoneDamenagement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-858"
    descripteur: str = "zone d'aménagement"

class FricheIndustrielle(BaseModel):
    sous_descripteur: Literal['FricheIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-469"
    descripteur: str = "friche industrielle"

class AssociationFonciereUrbaine(BaseModel):
    sous_descripteur: Literal['AssociationFonciereUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-138"
    descripteur: str = "association foncière urbaine"

class ReserveFonciere(BaseModel):
    sous_descripteur: Literal['ReserveFonciere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1193"
    descripteur: str = "réserve foncière"

class AmenagementFoncier(BaseModel):
    sous_descripteur: Union['ReserveFonciere', 'AssociationFonciereUrbaine', 'FricheIndustrielle', 'ZoneDamenagement'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1266"
    descripteur: str = "aménagement foncier"

class Urbaniste(BaseModel):
    sous_descripteur: Literal['Urbaniste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-84"
    descripteur: str = "urbaniste"

class RestaurationImmobiliere(BaseModel):
    sous_descripteur: Literal['RestaurationImmobiliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-124"
    descripteur: str = "restauration immobilière"

class RestructurationUrbaine(BaseModel):
    sous_descripteur: Literal['RestructurationUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1097"
    descripteur: str = "restructuration urbaine"

class Lotissement(BaseModel):
    sous_descripteur: Literal['Lotissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-475"
    descripteur: str = "lotissement"

class OperationDurbanisme(BaseModel):
    sous_descripteur: Union['Lotissement', 'RestructurationUrbaine', 'RestaurationImmobiliere'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-83"
    descripteur: str = "opération d'urbanisme"

class DistributionDeGaz(BaseModel):
    sous_descripteur: Literal['DistributionDeGaz']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1295"
    descripteur: str = "distribution de gaz"

class Canalisation(BaseModel):
    sous_descripteur: Literal['Canalisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-856"
    descripteur: str = "canalisation"

class EauPotable(BaseModel):
    sous_descripteur: Literal['EauPotable']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-537"
    descripteur: str = "eau potable"

class ChauffageUrbain(BaseModel):
    sous_descripteur: Literal['ChauffageUrbain']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-510"
    descripteur: str = "chauffage urbain"

class DistributionElectrique(BaseModel):
    sous_descripteur: Literal['DistributionElectrique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-937"
    descripteur: str = "distribution électrique"

class EclairagePublic(BaseModel):
    sous_descripteur: Literal['EclairagePublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-63"
    descripteur: str = "éclairage public"

class ReseauDeDistribution(BaseModel):
    sous_descripteur: Union['EclairagePublic', 'DistributionElectrique', 'ChauffageUrbain', 'EauPotable', 'Canalisation', 'DistributionDeGaz'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-755"
    descripteur: str = "réseau de distribution"

class InstallationSanitairePublique(BaseModel):
    sous_descripteur: Literal['InstallationSanitairePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1482"
    descripteur: str = "installation sanitaire publique"

class Fontaine(BaseModel):
    sous_descripteur: Literal['Fontaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-835"
    descripteur: str = "fontaine"

class HorlogePublique(BaseModel):
    sous_descripteur: Literal['HorlogePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-570"
    descripteur: str = "horloge publique"

class Lavoir(BaseModel):
    sous_descripteur: Literal['Lavoir']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1320"
    descripteur: str = "lavoir"

class Puits(BaseModel):
    sous_descripteur: Literal['Puits']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-884"
    descripteur: str = "puits"

class Halle(BaseModel):
    sous_descripteur: Literal['Halle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-960"
    descripteur: str = "halle"

class PlacePublique(BaseModel):
    sous_descripteur: Literal['PlacePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1216"
    descripteur: str = "place publique"

class AireDeJeux(BaseModel):
    sous_descripteur: Literal['AireDeJeux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-549"
    descripteur: str = "aire de jeux"

class ChampDeFoire(BaseModel):
    sous_descripteur: Literal['ChampDeFoire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-465"
    descripteur: str = "champ de foire"

class AireDeStationnement(BaseModel):
    sous_descripteur: Literal['AireDeStationnement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1128"
    descripteur: str = "aire de stationnement"

class BatimentPolyvalent(BaseModel):
    sous_descripteur: Literal['BatimentPolyvalent']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-34"
    descripteur: str = "bâtiment polyvalent"

class EspaceVert(BaseModel):
    sous_descripteur: Literal['EspaceVert']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-403"
    descripteur: str = "espace vert"

class Cimetiere(BaseModel):
    sous_descripteur: Literal['Cimetiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-773"
    descripteur: str = "cimetière"

class EquipementCollectif(BaseModel):
    sous_descripteur: Union['Cimetiere', 'EspaceVert', 'BatimentPolyvalent', 'AireDeStationnement', 'ChampDeFoire', 'AireDeJeux', 'PlacePublique', 'Halle', 'Puits', 'Lavoir', 'HorlogePublique', 'Fontaine', 'InstallationSanitairePublique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-508"
    descripteur: str = "équipement collectif"

class Urbanisme(BaseModel):
    sous_descripteur: Union['EquipementCollectif', 'ReseauDeDistribution', 'OperationDurbanisme', 'Urbaniste', 'AmenagementFoncier', 'DecorationUrbaine', 'MobilierUrbain', 'EtalementUrbain', 'Reconstruction', 'SecteurSauvegarde', 'Fleurissement'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-209"
    descripteur: str = "urbanisme"

class Telepherique(BaseModel):
    sous_descripteur: Literal['Telepherique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1087"
    descripteur: str = "téléphérique"

class VoiePietonne(BaseModel):
    sous_descripteur: Literal['VoiePietonne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1120"
    descripteur: str = "voie piétonne"

class PromenadePlantee(BaseModel):
    sous_descripteur: Literal['PromenadePlantee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-754"
    descripteur: str = "promenade plantée"

class PisteCyclable(BaseModel):
    sous_descripteur: Literal['PisteCyclable']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-502"
    descripteur: str = "piste cyclable"

class LiaisonDouce(BaseModel):
    sous_descripteur: Union['PisteCyclable', 'PromenadePlantee', 'VoiePietonne'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-661"
    descripteur: str = "liaison douce"

class VoieNavigable(BaseModel):
    sous_descripteur: Literal['VoieNavigable']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-326"
    descripteur: str = "voie navigable"

class OuvrageDart(BaseModel):
    sous_descripteur: Literal['OuvrageDart']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-48"
    descripteur: str = "ouvrage d'art"

class VoieFerreeDinteretNational(BaseModel):
    sous_descripteur: Literal['VoieFerreeDinteretNational']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-985"
    descripteur: str = "voie ferrée d'intérêt national"

class VoieFerreeDinteretLocal(BaseModel):
    sous_descripteur: Literal['VoieFerreeDinteretLocal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-443"
    descripteur: str = "voie ferrée d'intérêt local"

class VoieFerreeDesQuais(BaseModel):
    sous_descripteur: Literal['VoieFerreeDesQuais']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1206"
    descripteur: str = "voie ferrée des quais"

class VoieFerreePrivee(BaseModel):
    sous_descripteur: Literal['VoieFerreePrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-30"
    descripteur: str = "voie ferrée privée"

class ReseauFerroviaire(BaseModel):
    sous_descripteur: Union['VoieFerreePrivee', 'VoieFerreeDesQuais', 'VoieFerreeDinteretLocal', 'VoieFerreeDinteretNational'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-736"
    descripteur: str = "réseau ferroviaire"

class VoieIntercommunale(BaseModel):
    sous_descripteur: Literal['VoieIntercommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1380"
    descripteur: str = "voie intercommunale"

class RouteDepartementale(BaseModel):
    sous_descripteur: Literal['RouteDepartementale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1147"
    descripteur: str = "route départementale"

class RouteForestiere(BaseModel):
    sous_descripteur: Literal['RouteForestiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-734"
    descripteur: str = "route forestière"

class Autoroute(BaseModel):
    sous_descripteur: Literal['Autoroute']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-451"
    descripteur: str = "autoroute"

class VoieCommunale(BaseModel):
    sous_descripteur: Literal['VoieCommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-395"
    descripteur: str = "voie communale"

class VoiePrivee(BaseModel):
    sous_descripteur: Literal['VoiePrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-76"
    descripteur: str = "voie privée"

class RouteNationale(BaseModel):
    sous_descripteur: Literal['RouteNationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-5"
    descripteur: str = "route nationale"

class CheminRural(BaseModel):
    sous_descripteur: Literal['CheminRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-908"
    descripteur: str = "chemin rural"

class ReseauRoutier(BaseModel):
    sous_descripteur: Union['CheminRural', 'RouteNationale', 'VoiePrivee', 'VoieCommunale', 'Autoroute', 'RouteForestiere', 'RouteDepartementale', 'VoieIntercommunale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1149"
    descripteur: str = "réseau routier"

class VoieDeCommunication(BaseModel):
    sous_descripteur: Union['ReseauRoutier', 'ReseauFerroviaire', 'OuvrageDart', 'VoieNavigable', 'LiaisonDouce', 'Telepherique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1334"
    descripteur: str = "voie de communication"

class LogementDeFonction(BaseModel):
    sous_descripteur: Literal['LogementDeFonction']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1448"
    descripteur: str = "logement de fonction"

class HabitationALoyerModere(BaseModel):
    sous_descripteur: Literal['HabitationALoyerModere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1065"
    descripteur: str = "habitation à loyer modéré"

class JardinFamilial(BaseModel):
    sous_descripteur: Literal['JardinFamilial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1409"
    descripteur: str = "jardin familial"

class Foyer(BaseModel):
    sous_descripteur: Literal['Foyer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-626"
    descripteur: str = "foyer"

class LogementSocial(BaseModel):
    sous_descripteur: Union['Foyer', 'JardinFamilial', 'HabitationALoyerModere'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1001"
    descripteur: str = "logement social"

class Demolition(BaseModel):
    sous_descripteur: Literal['Demolition']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-671"
    descripteur: str = "démolition"

class SyndicDeCopropriete(BaseModel):
    sous_descripteur: Literal['SyndicDeCopropriete']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1045"
    descripteur: str = "syndic de copropriété"

class CentreVille(BaseModel):
    sous_descripteur: Literal['CentreVille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1230"
    descripteur: str = "centre ville"

class HabitatPeriurbain(BaseModel):
    sous_descripteur: Literal['HabitatPeriurbain']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-774"
    descripteur: str = "habitat périurbain"

class HabitatUrbain(BaseModel):
    sous_descripteur: Union['HabitatPeriurbain', 'CentreVille'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1133"
    descripteur: str = "habitat urbain"

class AgentImmobilier(BaseModel):
    sous_descripteur: Literal['AgentImmobilier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-437"
    descripteur: str = "agent immobilier"

class MarcheImmobilier(BaseModel):
    sous_descripteur: Union['AgentImmobilier'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-706"
    descripteur: str = "marché immobilier"

class HabitatInsalubre(BaseModel):
    sous_descripteur: Literal['HabitatInsalubre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-523"
    descripteur: str = "habitat insalubre"

class AmeliorationDeLhabitat(BaseModel):
    sous_descripteur: Union['HabitatInsalubre'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1170"
    descripteur: str = "amélioration de l'habitat"

class LogementCollectif(BaseModel):
    sous_descripteur: Literal['LogementCollectif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-772"
    descripteur: str = "logement collectif"

class LogementIndividuel(BaseModel):
    sous_descripteur: Literal['LogementIndividuel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-656"
    descripteur: str = "logement individuel"

class LoyerImmobilier(BaseModel):
    sous_descripteur: Literal['LoyerImmobilier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1130"
    descripteur: str = "loyer immobilier"

class ExpulsionLocative(BaseModel):
    sous_descripteur: Literal['ExpulsionLocative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-302"
    descripteur: str = "expulsion locative"

class Logement(BaseModel):
    sous_descripteur: Union['ExpulsionLocative', 'LoyerImmobilier', 'LogementIndividuel', 'LogementCollectif'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-290"
    descripteur: str = "logement"

class SurveillanceDesBatiments(BaseModel):
    sous_descripteur: Literal['SurveillanceDesBatiments']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-441"
    descripteur: str = "surveillance des bâtiments"

class ParticipationDesEmployeurs(BaseModel):
    sous_descripteur: Literal['ParticipationDesEmployeurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-914"
    descripteur: str = "participation des employeurs"

class Chantier(BaseModel):
    sous_descripteur: Literal['Chantier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-595"
    descripteur: str = "chantier"

class SondageGeologique(BaseModel):
    sous_descripteur: Literal['SondageGeologique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-292"
    descripteur: str = "sondage géologique"

class EntrepriseDuBatiment(BaseModel):
    sous_descripteur: Literal['EntrepriseDuBatiment']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-227"
    descripteur: str = "entreprise du bâtiment"

class OuvrierDuBatiment(BaseModel):
    sous_descripteur: Literal['OuvrierDuBatiment']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1346"
    descripteur: str = "ouvrier du bâtiment"

class SocieteDeConstruction(BaseModel):
    sous_descripteur: Literal['SocieteDeConstruction']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-654"
    descripteur: str = "société de construction"

class Construction(BaseModel):
    sous_descripteur: Union['SocieteDeConstruction', 'OuvrierDuBatiment', 'EntrepriseDuBatiment', 'SondageGeologique', 'Chantier', 'ParticipationDesEmployeurs'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-396"
    descripteur: str = "construction"

class Architecte(BaseModel):
    sous_descripteur: Literal['Architecte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-738"
    descripteur: str = "architecte"

class RequisitionDeLogement(BaseModel):
    sous_descripteur: Literal['RequisitionDeLogement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-72"
    descripteur: str = "réquisition de logement"

class AccessionALaPropriete(BaseModel):
    sous_descripteur: Literal['AccessionALaPropriete']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-153"
    descripteur: str = "accession à la propriété"

class AidePubliqueAuLogement(BaseModel):
    sous_descripteur: Union['AccessionALaPropriete'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-41"
    descripteur: str = "aide publique au logement"

class VentePubliqueImmobiliere(BaseModel):
    sous_descripteur: Literal['VentePubliqueImmobiliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1438"
    descripteur: str = "vente publique immobilière"

class HabitatRural(BaseModel):
    sous_descripteur: Literal['HabitatRural']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1"
    descripteur: str = "habitat rural"

class Immobilier(BaseModel):
    sous_descripteur: Union['HabitatRural', 'VentePubliqueImmobiliere', 'AidePubliqueAuLogement', 'RequisitionDeLogement', 'Architecte', 'Construction', 'SurveillanceDesBatiments', 'Logement', 'AmeliorationDeLhabitat', 'MarcheImmobilier', 'HabitatUrbain', 'SyndicDeCopropriete', 'Demolition', 'LogementSocial', 'LogementDeFonction'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-556"
    descripteur: str = "immobilier"

class Equipement(BaseModel):
    sous_descripteur: Union['Immobilier', 'VoieDeCommunication', 'Urbanisme', 'Environnement'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1262"
    descripteur: str = "équipement"
