from pydantic import BaseModel
from typing import Union, Literal

class Democratie(BaseModel):
    sous_descripteur: Literal['Democratie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1229"
    descripteur: str = "démocratie"

class DroitCommunautaire(BaseModel):
    sous_descripteur: Literal['DroitCommunautaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-965"
    descripteur: str = "droit communautaire"

class Legislation(BaseModel):
    sous_descripteur: Literal['Legislation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-765"
    descripteur: str = "législation"

class Institutions(BaseModel):
    sous_descripteur: Literal['Institutions']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-385"
    descripteur: str = "institutions"

class ChefDEtat(BaseModel):
    sous_descripteur: Literal['ChefDEtat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1460"
    descripteur: str = "chef d'État"

class Republique(BaseModel):
    sous_descripteur: Literal['Republique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-710"
    descripteur: str = "république"

class Monarchie(BaseModel):
    sous_descripteur: Literal['Monarchie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-346"
    descripteur: str = "monarchie"

class Etat(BaseModel):
    sous_descripteur: Union['Monarchie', 'Republique', 'ChefDEtat'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-476"
    descripteur: str = "État"

class Constitution(BaseModel):
    sous_descripteur: Literal['Constitution']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-113"
    descripteur: str = "constitution"

class DroitPublic(BaseModel):
    sous_descripteur: Union['Constitution', 'Etat', 'Institutions', 'Legislation', 'DroitCommunautaire', 'Democratie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1259"
    descripteur: str = "droit public"

class Province(BaseModel):
    sous_descripteur: Literal['Province']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-999"
    descripteur: str = "province"

class CirconscriptionFiscale(BaseModel):
    sous_descripteur: Literal['CirconscriptionFiscale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-708"
    descripteur: str = "circonscription fiscale"

class Generalite(BaseModel):
    sous_descripteur: Literal['Generalite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-638"
    descripteur: str = "généralité"

class Pays(BaseModel):
    sous_descripteur: Literal['Pays']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1372"
    descripteur: str = "pays"

class Senechaussee(BaseModel):
    sous_descripteur: Literal['Senechaussee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-812"
    descripteur: str = "sénéchaussée"

class AgglomerationUrbaine(BaseModel):
    sous_descripteur: Literal['AgglomerationUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1035"
    descripteur: str = "agglomération urbaine"

class DomaineRoyal(BaseModel):
    sous_descripteur: Literal['DomaineRoyal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1043"
    descripteur: str = "domaine royal"

class DistrictRevolutionnaire(BaseModel):
    sous_descripteur: Literal['DistrictRevolutionnaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1328"
    descripteur: str = "district révolutionnaire"

class Arrondissement(BaseModel):
    sous_descripteur: Literal['Arrondissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1064"
    descripteur: str = "arrondissement"

class Seigneurie(BaseModel):
    sous_descripteur: Literal['Seigneurie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-454"
    descripteur: str = "seigneurie"

class LimiteTerritoriale(BaseModel):
    sous_descripteur: Literal['LimiteTerritoriale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-349"
    descripteur: str = "limite territoriale"

class RessortJudiciaire(BaseModel):
    sous_descripteur: Literal['RessortJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-299"
    descripteur: str = "ressort judiciaire"

class Canton(BaseModel):
    sous_descripteur: Literal['Canton']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-645"
    descripteur: str = "canton"

class CirconscriptionTerritoriale(BaseModel):
    sous_descripteur: Union['Canton', 'RessortJudiciaire', 'LimiteTerritoriale', 'Seigneurie', 'Arrondissement', 'DistrictRevolutionnaire', 'DomaineRoyal', 'AgglomerationUrbaine', 'Senechaussee', 'Pays', 'Generalite', 'CirconscriptionFiscale', 'Province'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-601"
    descripteur: str = "circonscription territoriale"

class HotelDeLaPrefecture(BaseModel):
    sous_descripteur: Literal['HotelDeLaPrefecture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1289"
    descripteur: str = "hôtel de la préfecture"

class HotelCommunautaire(BaseModel):
    sous_descripteur: Literal['HotelCommunautaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1160"
    descripteur: str = "hôtel communautaire"

class HotelDeRegion(BaseModel):
    sous_descripteur: Literal['HotelDeRegion']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1059"
    descripteur: str = "hôtel de région"

class HotelDeLaSousprefecture(BaseModel):
    sous_descripteur: Literal['HotelDeLaSousprefecture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-794"
    descripteur: str = "hôtel de la sous-préfecture"

class HotelDeVille(BaseModel):
    sous_descripteur: Literal['HotelDeVille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-712"
    descripteur: str = "hôtel de ville"

class PalaisDeJustice(BaseModel):
    sous_descripteur: Literal['PalaisDeJustice']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-356"
    descripteur: str = "palais de justice"

class CiteAdministrative(BaseModel):
    sous_descripteur: Literal['CiteAdministrative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-351"
    descripteur: str = "cité administrative"

class HotelDuDepartement(BaseModel):
    sous_descripteur: Literal['HotelDuDepartement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-273"
    descripteur: str = "hôtel du département"

class BatimentAdministratif(BaseModel):
    sous_descripteur: Union['HotelDuDepartement', 'CiteAdministrative', 'PalaisDeJustice', 'HotelDeVille', 'HotelDeLaSousprefecture', 'HotelDeRegion', 'HotelCommunautaire', 'HotelDeLaPrefecture'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1227"
    descripteur: str = "bâtiment administratif"

class AdministrationPrefectorale(BaseModel):
    sous_descripteur: Literal['AdministrationPrefectorale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-621"
    descripteur: str = "administration préfectorale"

class ServiceDeconcentre(BaseModel):
    sous_descripteur: Literal['ServiceDeconcentre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1088"
    descripteur: str = "service déconcentré"

class AdministrationLocaleDAncienRegime(BaseModel):
    sous_descripteur: Literal['AdministrationLocaleDAncienRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1040"
    descripteur: str = "administration locale d'Ancien Régime"

class AdministrationCommunale(BaseModel):
    sous_descripteur: Literal['AdministrationCommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1435"
    descripteur: str = "administration communale"

class EtablissementPublicLocal(BaseModel):
    sous_descripteur: Literal['EtablissementPublicLocal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1422"
    descripteur: str = "établissement public local"

class ServiceExterieur(BaseModel):
    sous_descripteur: Literal['ServiceExterieur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-575"
    descripteur: str = "service extérieur"

class AdministrationCentrale(BaseModel):
    sous_descripteur: Literal['AdministrationCentrale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1044"
    descripteur: str = "administration centrale"

class OrganismeAdministratifEuropeen(BaseModel):
    sous_descripteur: Literal['OrganismeAdministratifEuropeen']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-771"
    descripteur: str = "organisme administratif européen"

class EtablissementPublicNational(BaseModel):
    sous_descripteur: Literal['EtablissementPublicNational']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1109"
    descripteur: str = "établissement public national"

class AdministrationRegionale(BaseModel):
    sous_descripteur: Literal['AdministrationRegionale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-422"
    descripteur: str = "administration régionale"

class OrganismeParapublic(BaseModel):
    sous_descripteur: Literal['OrganismeParapublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-387"
    descripteur: str = "organisme parapublic"

class AdministrationCantonaleDepoqueRevolutionnaire(BaseModel):
    sous_descripteur: Literal['AdministrationCantonaleDepoqueRevolutionnaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-368"
    descripteur: str = "administration cantonale d'époque révolutionnaire"

class AdministrationDepartementale(BaseModel):
    sous_descripteur: Literal['AdministrationDepartementale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-260"
    descripteur: str = "administration départementale"

class OrganismeConsultatif(BaseModel):
    sous_descripteur: Literal['OrganismeConsultatif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-131"
    descripteur: str = "organisme consultatif"

class StructureAdministrative(BaseModel):
    sous_descripteur: Union['OrganismeConsultatif', 'AdministrationDepartementale', 'AdministrationCantonaleDepoqueRevolutionnaire', 'OrganismeParapublic', 'AdministrationRegionale', 'EtablissementPublicNational', 'OrganismeAdministratifEuropeen', 'AdministrationCentrale', 'ServiceExterieur', 'EtablissementPublicLocal', 'AdministrationCommunale', 'AdministrationLocaleDAncienRegime', 'ServiceDeconcentre', 'AdministrationPrefectorale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-435"
    descripteur: str = "structure administrative"

class Deconcentration(BaseModel):
    sous_descripteur: Literal['Deconcentration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1452"
    descripteur: str = "déconcentration"

class Delocalisation(BaseModel):
    sous_descripteur: Literal['Delocalisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-276"
    descripteur: str = "délocalisation"

class Regionalisation(BaseModel):
    sous_descripteur: Literal['Regionalisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-55"
    descripteur: str = "régionalisation"

class Decentralisation(BaseModel):
    sous_descripteur: Literal['Decentralisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1083"
    descripteur: str = "décentralisation"

class TransfertDeCompetences(BaseModel):
    sous_descripteur: Union['Decentralisation', 'Regionalisation', 'Delocalisation', 'Deconcentration'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-347"
    descripteur: str = "transfert de compétences"

class EtatsProvinciaux(BaseModel):
    sous_descripteur: Literal['EtatsProvinciaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1451"
    descripteur: str = "états provinciaux"

class ConseilCommunautaire(BaseModel):
    sous_descripteur: Literal['ConseilCommunautaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1122"
    descripteur: str = "conseil communautaire"

class ConseilDadministration(BaseModel):
    sous_descripteur: Literal['ConseilDadministration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-769"
    descripteur: str = "conseil d'administration"

class AssembleeGenerale(BaseModel):
    sous_descripteur: Literal['AssembleeGenerale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-555"
    descripteur: str = "assemblée générale"

class EtatsGeneraux(BaseModel):
    sous_descripteur: Literal['EtatsGeneraux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-275"
    descripteur: str = "états généraux"

class ConseilMunicipal(BaseModel):
    sous_descripteur: Literal['ConseilMunicipal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-159"
    descripteur: str = "conseil municipal"

class ConseilDarrondissement(BaseModel):
    sous_descripteur: Literal['ConseilDarrondissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-874"
    descripteur: str = "conseil d'arrondissement"

class ConseilGeneral(BaseModel):
    sous_descripteur: Literal['ConseilGeneral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-367"
    descripteur: str = "conseil général"

class AssembleeNationale(BaseModel):
    sous_descripteur: Literal['AssembleeNationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-175"
    descripteur: str = "assemblée nationale"

class AssembleeEuropeenne(BaseModel):
    sous_descripteur: Literal['AssembleeEuropeenne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-922"
    descripteur: str = "assemblée européenne"

class ConseilRegional(BaseModel):
    sous_descripteur: Literal['ConseilRegional']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1237"
    descripteur: str = "conseil régional"

class OrganeDeliberant(BaseModel):
    sous_descripteur: Union['ConseilRegional', 'AssembleeEuropeenne', 'AssembleeNationale', 'ConseilGeneral', 'ConseilDarrondissement', 'ConseilMunicipal', 'EtatsGeneraux', 'AssembleeGenerale', 'ConseilDadministration', 'ConseilCommunautaire', 'EtatsProvinciaux'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1157"
    descripteur: str = "organe délibérant"

class ConcoursAdministratif(BaseModel):
    sous_descripteur: Literal['ConcoursAdministratif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1071"
    descripteur: str = "concours administratif"

class AgentNonTitulaire(BaseModel):
    sous_descripteur: Literal['AgentNonTitulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-657"
    descripteur: str = "agent non titulaire"

class ConseilDeDiscipline(BaseModel):
    sous_descripteur: Literal['ConseilDeDiscipline']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-507"
    descripteur: str = "conseil de discipline"

class AgentDeLadministrationRoyale(BaseModel):
    sous_descripteur: Literal['AgentDeLadministrationRoyale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1417"
    descripteur: str = "agent de l'administration royale"

class FonctionnaireTerritorial(BaseModel):
    sous_descripteur: Literal['FonctionnaireTerritorial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-353"
    descripteur: str = "fonctionnaire territorial"

class AgentDeDroitPrive(BaseModel):
    sous_descripteur: Literal['AgentDeDroitPrive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-218"
    descripteur: str = "agent de droit privé"

class FonctionnaireDeLUnionEuropeenne(BaseModel):
    sous_descripteur: Literal['FonctionnaireDeLUnionEuropeenne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-195"
    descripteur: str = "fonctionnaire de l'Union européenne"

class FonctionnaireHospitalier(BaseModel):
    sous_descripteur: Literal['FonctionnaireHospitalier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1414"
    descripteur: str = "fonctionnaire hospitalier"

class FonctionnaireDeLEtat(BaseModel):
    sous_descripteur: Literal['FonctionnaireDeLEtat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1056"
    descripteur: str = "fonctionnaire de l'État"

class Personnel(BaseModel):
    sous_descripteur: Union['FonctionnaireDeLEtat', 'FonctionnaireHospitalier', 'FonctionnaireDeLUnionEuropeenne', 'AgentDeDroitPrive', 'FonctionnaireTerritorial', 'AgentDeLadministrationRoyale', 'ConseilDeDiscipline', 'AgentNonTitulaire', 'ConcoursAdministratif'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-805"
    descripteur: str = "personnel"

class Commune(BaseModel):
    sous_descripteur: Literal['Commune']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-317"
    descripteur: str = "commune"

class EtablissementPublicDeCooperationIntercommunale(BaseModel):
    sous_descripteur: Literal['EtablissementPublicDeCooperationIntercommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1238"
    descripteur: str = "établissement public de coopération intercommunale"

class CooperationInterregionale(BaseModel):
    sous_descripteur: Literal['CooperationInterregionale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-199"
    descripteur: str = "coopération interrégionale"

class Departement(BaseModel):
    sous_descripteur: Literal['Departement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1449"
    descripteur: str = "département"

class RegroupementDeCommunes(BaseModel):
    sous_descripteur: Literal['RegroupementDeCommunes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-594"
    descripteur: str = "regroupement de communes"

class Region(BaseModel):
    sous_descripteur: Literal['Region']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1079"
    descripteur: str = "région"

class CollectiviteLocale(BaseModel):
    sous_descripteur: Union['Region', 'RegroupementDeCommunes', 'Departement', 'CooperationInterregionale', 'EtablissementPublicDeCooperationIntercommunale', 'Commune'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-73"
    descripteur: str = "collectivité locale"

class AdministrationGenerale(BaseModel):
    sous_descripteur: Union['CollectiviteLocale', 'Personnel', 'OrganeDeliberant', 'TransfertDeCompetences', 'StructureAdministrative', 'BatimentAdministratif', 'CirconscriptionTerritoriale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1345"
    descripteur: str = "administration générale"

class EquipementDeSecours(BaseModel):
    sous_descripteur: Literal['EquipementDeSecours']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1462"
    descripteur: str = "équipement de secours"

class SapeurPompier(BaseModel):
    sous_descripteur: Literal['SapeurPompier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1430"
    descripteur: str = "sapeur pompier"

class SauvetageEnMer(BaseModel):
    sous_descripteur: Literal['SauvetageEnMer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1033"
    descripteur: str = "sauvetage en mer"

class AideMedicaleUrgente(BaseModel):
    sous_descripteur: Literal['AideMedicaleUrgente']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-646"
    descripteur: str = "aide médicale urgente"

class PoliceSecours(BaseModel):
    sous_descripteur: Literal['PoliceSecours']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-278"
    descripteur: str = "police secours"

class Secours(BaseModel):
    sous_descripteur: Union['PoliceSecours', 'AideMedicaleUrgente', 'SauvetageEnMer', 'SapeurPompier', 'EquipementDeSecours'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1000"
    descripteur: str = "secours"

class ImmeubleDeGrandeHauteur(BaseModel):
    sous_descripteur: Literal['ImmeubleDeGrandeHauteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1219"
    descripteur: str = "immeuble de grande hauteur"

class TransportDeMatieresDangereuses(BaseModel):
    sous_descripteur: Literal['TransportDeMatieresDangereuses']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1151"
    descripteur: str = "transport de matières dangereuses"

class CatastropheNaturelle(BaseModel):
    sous_descripteur: Literal['CatastropheNaturelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-698"
    descripteur: str = "catastrophe naturelle"

class CatastropheIndustrielle(BaseModel):
    sous_descripteur: Literal['CatastropheIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1055"
    descripteur: str = "catastrophe industrielle"

class Inondation(BaseModel):
    sous_descripteur: Literal['Inondation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1393"
    descripteur: str = "inondation"

class Incendie(BaseModel):
    sous_descripteur: Literal['Incendie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-284"
    descripteur: str = "incendie"

class Sinistre(BaseModel):
    sous_descripteur: Union['Incendie', 'Inondation', 'CatastropheIndustrielle', 'CatastropheNaturelle'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-67"
    descripteur: str = "sinistre"

class AppareilAPressionDeVapeur(BaseModel):
    sous_descripteur: Literal['AppareilAPressionDeVapeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-126"
    descripteur: str = "appareil à pression de vapeur"

class AccidentDesTransports(BaseModel):
    sous_descripteur: Literal['AccidentDesTransports']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1221"
    descripteur: str = "accident des transports"

class InstallationClassee(BaseModel):
    sous_descripteur: Literal['InstallationClassee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-887"
    descripteur: str = "installation classée"

class EtablissementRecevantDuPublic(BaseModel):
    sous_descripteur: Literal['EtablissementRecevantDuPublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-478"
    descripteur: str = "établissement recevant du public"

class SecuriteRoutiere(BaseModel):
    sous_descripteur: Literal['SecuriteRoutiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-628"
    descripteur: str = "sécurité routière"

class ProtectionCivile(BaseModel):
    sous_descripteur: Union['SecuriteRoutiere', 'EtablissementRecevantDuPublic', 'InstallationClassee', 'AccidentDesTransports', 'AppareilAPressionDeVapeur', 'Sinistre', 'TransportDeMatieresDangereuses', 'ImmeubleDeGrandeHauteur', 'Secours'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-147"
    descripteur: str = "protection civile"

class Contribuable(BaseModel):
    sous_descripteur: Literal['Contribuable']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1123"
    descripteur: str = "contribuable"

class FiscaliteDirecteRevolutionnaire(BaseModel):
    sous_descripteur: Literal['FiscaliteDirecteRevolutionnaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1165"
    descripteur: str = "fiscalité directe révolutionnaire"

class TimbreFiscal(BaseModel):
    sous_descripteur: Literal['TimbreFiscal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1387"
    descripteur: str = "timbre fiscal"

class RecouvrementFiscal(BaseModel):
    sous_descripteur: Literal['RecouvrementFiscal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-791"
    descripteur: str = "recouvrement fiscal"

class DroitsDomaniauxDAncienRegime(BaseModel):
    sous_descripteur: Literal['DroitsDomaniauxDAncienRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-623"
    descripteur: str = "droits domaniaux d'Ancien Régime"

class DroitsReserves(BaseModel):
    sous_descripteur: Literal['DroitsReserves']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-853"
    descripteur: str = "droits réservés"

class OfficeDAncienRegime(BaseModel):
    sous_descripteur: Literal['OfficeDAncienRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-780"
    descripteur: str = "office d'Ancien Régime"

class TaxeExtraordinaireDAncienRegime(BaseModel):
    sous_descripteur: Union['OfficeDAncienRegime', 'DroitsReserves'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-462"
    descripteur: str = "taxe extraordinaire d'Ancien Régime"

class ExonerationFiscale(BaseModel):
    sous_descripteur: Literal['ExonerationFiscale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-434"
    descripteur: str = "exonération fiscale"

class DroitsDeDouane(BaseModel):
    sous_descripteur: Literal['DroitsDeDouane']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-410"
    descripteur: str = "droits de douane"

class DroitsDeSuccession(BaseModel):
    sous_descripteur: Literal['DroitsDeSuccession']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-542"
    descripteur: str = "droits de succession"

class Enregistrement(BaseModel):
    sous_descripteur: Union['DroitsDeSuccession'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-306"
    descripteur: str = "enregistrement"

class Contrebande(BaseModel):
    sous_descripteur: Literal['Contrebande']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1370"
    descripteur: str = "contrebande"

class FraudeFiscale(BaseModel):
    sous_descripteur: Union['Contrebande'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-295"
    descripteur: str = "fraude fiscale"

class CorveeRoyale(BaseModel):
    sous_descripteur: Literal['CorveeRoyale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-262"
    descripteur: str = "corvée royale"

class TaxeDhabitation(BaseModel):
    sous_descripteur: Literal['TaxeDhabitation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1298"
    descripteur: str = "taxe d'habitation"

class TaxeDeSejour(BaseModel):
    sous_descripteur: Literal['TaxeDeSejour']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1002"
    descripteur: str = "taxe de séjour"

class DroitDesPauvres(BaseModel):
    sous_descripteur: Literal['DroitDesPauvres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-298"
    descripteur: str = "droit des pauvres"

class DroitDePlace(BaseModel):
    sous_descripteur: Literal['DroitDePlace']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-641"
    descripteur: str = "droit de place"

class ImpotsProvinciauxDAncienRegime(BaseModel):
    sous_descripteur: Literal['ImpotsProvinciauxDAncienRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1016"
    descripteur: str = "impôts provinciaux d'Ancien Régime"

class Octroi(BaseModel):
    sous_descripteur: Literal['Octroi']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1316"
    descripteur: str = "octroi"

class ImpotsLocaux(BaseModel):
    sous_descripteur: Union['Octroi', 'ImpotsProvinciauxDAncienRegime', 'DroitDePlace', 'DroitDesPauvres', 'TaxeDeSejour', 'TaxeDhabitation'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-241"
    descripteur: str = "impôts locaux"

class RedevanceParafiscale(BaseModel):
    sous_descripteur: Literal['RedevanceParafiscale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1350"
    descripteur: str = "redevance parafiscale"

class ImpotSurLeRevenu(BaseModel):
    sous_descripteur: Literal['ImpotSurLeRevenu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1375"
    descripteur: str = "impôt sur le revenu"

class ImpotSocial(BaseModel):
    sous_descripteur: Literal['ImpotSocial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-930"
    descripteur: str = "impôt social"

class ImpotSurLaFortune(BaseModel):
    sous_descripteur: Literal['ImpotSurLaFortune']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-188"
    descripteur: str = "impôt sur la fortune"

class FiscaliteDesPersonnes(BaseModel):
    sous_descripteur: Union['ImpotSurLaFortune', 'ImpotSocial', 'ImpotSurLeRevenu'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1376"
    descripteur: str = "fiscalité des personnes"

class TaxeFonciere(BaseModel):
    sous_descripteur: Literal['TaxeFonciere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-807"
    descripteur: str = "taxe foncière"

class Cadastre(BaseModel):
    sous_descripteur: Literal['Cadastre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-463"
    descripteur: str = "cadastre"

class EvaluationFonciere(BaseModel):
    sous_descripteur: Literal['EvaluationFonciere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-132"
    descripteur: str = "évaluation foncière"

class PubliciteFonciere(BaseModel):
    sous_descripteur: Literal['PubliciteFonciere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1215"
    descripteur: str = "publicité foncière"

class FiscaliteImmobiliere(BaseModel):
    sous_descripteur: Union['PubliciteFonciere', 'EvaluationFonciere', 'Cadastre', 'TaxeFonciere'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1058"
    descripteur: str = "fiscalité immobilière"

class DroitsDeCirculation(BaseModel):
    sous_descripteur: Literal['DroitsDeCirculation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1086"
    descripteur: str = "droits de circulation"

class MonopolesFiscaux(BaseModel):
    sous_descripteur: Literal['MonopolesFiscaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-975"
    descripteur: str = "monopoles fiscaux"

class FiscalitePetroliere(BaseModel):
    sous_descripteur: Literal['FiscalitePetroliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-90"
    descripteur: str = "fiscalité pétrolière"

class ContributionsIndirectes(BaseModel):
    sous_descripteur: Union['FiscalitePetroliere', 'MonopolesFiscaux', 'DroitsDeCirculation'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-398"
    descripteur: str = "contributions indirectes"

class TaxeDapprentissage(BaseModel):
    sous_descripteur: Literal['TaxeDapprentissage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1031"
    descripteur: str = "taxe d'apprentissage"

class ImpotSurLesSocietes(BaseModel):
    sous_descripteur: Literal['ImpotSurLesSocietes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1136"
    descripteur: str = "impôt sur les sociétés"

class TaxeSurLeChiffreDaffaires(BaseModel):
    sous_descripteur: Literal['TaxeSurLeChiffreDaffaires']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-205"
    descripteur: str = "taxe sur le chiffre d'affaires"

class ImpotSurLesBenefices(BaseModel):
    sous_descripteur: Literal['ImpotSurLesBenefices']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-71"
    descripteur: str = "impôt sur les bénéfices"

class TaxeProfessionnelle(BaseModel):
    sous_descripteur: Literal['TaxeProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-640"
    descripteur: str = "taxe professionnelle"

class FiscaliteProfessionnelle(BaseModel):
    sous_descripteur: Union['TaxeProfessionnelle', 'ImpotSurLesBenefices', 'TaxeSurLeChiffreDaffaires', 'ImpotSurLesSocietes', 'TaxeDapprentissage'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-669"
    descripteur: str = "fiscalité professionnelle"

class FiscaliteDirecteDAncienRegime(BaseModel):
    sous_descripteur: Literal['FiscaliteDirecteDAncienRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-47"
    descripteur: str = "fiscalité directe d'Ancien Régime"

class Fiscalite(BaseModel):
    sous_descripteur: Union['FiscaliteDirecteDAncienRegime', 'FiscaliteProfessionnelle', 'ContributionsIndirectes', 'FiscaliteImmobiliere', 'FiscaliteDesPersonnes', 'RedevanceParafiscale', 'ImpotsLocaux', 'CorveeRoyale', 'FraudeFiscale', 'Enregistrement', 'DroitsDeDouane', 'ExonerationFiscale', 'TaxeExtraordinaireDAncienRegime', 'DroitsDomaniauxDAncienRegime', 'RecouvrementFiscal', 'TimbreFiscal', 'FiscaliteDirecteRevolutionnaire', 'Contribuable'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-829"
    descripteur: str = "fiscalité"

class Alleu(BaseModel):
    sous_descripteur: Literal['Alleu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-688"
    descripteur: str = "alleu"

class Reformation(BaseModel):
    sous_descripteur: Literal['Reformation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1429"
    descripteur: str = "réformation"

class AgentSeigneurial(BaseModel):
    sous_descripteur: Literal['AgentSeigneurial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-561"
    descripteur: str = "agent seigneurial"

class Reconnaissances(BaseModel):
    sous_descripteur: Literal['Reconnaissances']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-285"
    descripteur: str = "reconnaissances"

class AdministrationSeigneuriale(BaseModel):
    sous_descripteur: Union['Reconnaissances', 'AgentSeigneurial', 'Reformation'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-943"
    descripteur: str = "administration seigneuriale"

class DroitsHonorifiques(BaseModel):
    sous_descripteur: Literal['DroitsHonorifiques']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-282"
    descripteur: str = "droits honorifiques"

class DenombrementSeigneurial(BaseModel):
    sous_descripteur: Literal['DenombrementSeigneurial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1313"
    descripteur: str = "dénombrement seigneurial"

class SermentDeFidelite(BaseModel):
    sous_descripteur: Literal['SermentDeFidelite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-553"
    descripteur: str = "serment de fidélité"

class Hommage(BaseModel):
    sous_descripteur: Literal['Hommage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-239"
    descripteur: str = "hommage"

class Feodalite(BaseModel):
    sous_descripteur: Union['Hommage', 'SermentDeFidelite', 'DenombrementSeigneurial'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-718"
    descripteur: str = "féodalité"

class DroitsSeigneuriaux(BaseModel):
    sous_descripteur: Literal['DroitsSeigneuriaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1115"
    descripteur: str = "droits seigneuriaux"

class DroitsDusage(BaseModel):
    sous_descripteur: Literal['DroitsDusage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1333"
    descripteur: str = "droits d'usage"

class Coutumes(BaseModel):
    sous_descripteur: Literal['Coutumes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-155"
    descripteur: str = "coutumes"

class PrivilegesDesCommunautes(BaseModel):
    sous_descripteur: Union['Coutumes', 'DroitsDusage'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-29"
    descripteur: str = "privilèges des communautés"

class RegimeSeigneurial(BaseModel):
    sous_descripteur: Union['PrivilegesDesCommunautes', 'DroitsSeigneuriaux', 'Feodalite', 'DroitsHonorifiques', 'AdministrationSeigneuriale', 'Alleu'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-842"
    descripteur: str = "régime seigneurial"

class PoliceDesEaux(BaseModel):
    sous_descripteur: Literal['PoliceDesEaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-522"
    descripteur: str = "police des eaux"

class Marechaussee(BaseModel):
    sous_descripteur: Literal['Marechaussee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1425"
    descripteur: str = "maréchaussée"

class PoliceUrbaine(BaseModel):
    sous_descripteur: Literal['PoliceUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1093"
    descripteur: str = "police urbaine"

class PoliceMunicipale(BaseModel):
    sous_descripteur: Literal['PoliceMunicipale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-668"
    descripteur: str = "police municipale"

class GardeForestier(BaseModel):
    sous_descripteur: Literal['GardeForestier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-694"
    descripteur: str = "garde forestier"

class GardeParticulier(BaseModel):
    sous_descripteur: Literal['GardeParticulier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-749"
    descripteur: str = "garde particulier"

class Gendarmerie(BaseModel):
    sous_descripteur: Literal['Gendarmerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1135"
    descripteur: str = "gendarmerie"

class AgentDeLaForcePublique(BaseModel):
    sous_descripteur: Union['Gendarmerie', 'GardeParticulier', 'GardeForestier', 'PoliceMunicipale', 'PoliceUrbaine', 'Marechaussee'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1172"
    descripteur: str = "agent de la force publique"

class PoliceDesCultes(BaseModel):
    sous_descripteur: Literal['PoliceDesCultes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-863"
    descripteur: str = "police des cultes"

class PoliceDeLaPeche(BaseModel):
    sous_descripteur: Literal['PoliceDeLaPeche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-735"
    descripteur: str = "police de la pêche"

class LieutenantDeLouveterie(BaseModel):
    sous_descripteur: Literal['LieutenantDeLouveterie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1338"
    descripteur: str = "lieutenant de louveterie"

class PoliceDeLaChasse(BaseModel):
    sous_descripteur: Union['LieutenantDeLouveterie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1114"
    descripteur: str = "police de la chasse"

class Arrestation(BaseModel):
    sous_descripteur: Literal['Arrestation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1411"
    descripteur: str = "arrestation"

class IndividuRecherche(BaseModel):
    sous_descripteur: Literal['IndividuRecherche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-652"
    descripteur: str = "individu recherché"

class InterditDeSejour(BaseModel):
    sous_descripteur: Literal['InterditDeSejour']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1054"
    descripteur: str = "interdit de séjour"

class GardeAVue(BaseModel):
    sous_descripteur: Literal['GardeAVue']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-271"
    descripteur: str = "garde à vue"

class PoliceJudiciaire(BaseModel):
    sous_descripteur: Union['GardeAVue', 'InterditDeSejour', 'IndividuRecherche', 'Arrestation'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-468"
    descripteur: str = "police judiciaire"

class PoliceDesJeux(BaseModel):
    sous_descripteur: Literal['PoliceDesJeux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-253"
    descripteur: str = "police des jeux"

class EtablissementInterditAuxMineurs(BaseModel):
    sous_descripteur: Literal['EtablissementInterditAuxMineurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1347"
    descripteur: str = "établissement interdit aux mineurs"

class Prostitution(BaseModel):
    sous_descripteur: Literal['Prostitution']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-598"
    descripteur: str = "prostitution"

class Pornographie(BaseModel):
    sous_descripteur: Literal['Pornographie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-201"
    descripteur: str = "pornographie"

class PoliceDesMoeurs(BaseModel):
    sous_descripteur: Union['Pornographie', 'Prostitution', 'EtablissementInterditAuxMineurs'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1396"
    descripteur: str = "police des moeurs"

class PoliceDesTransports(BaseModel):
    sous_descripteur: Literal['PoliceDesTransports']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-102"
    descripteur: str = "police des transports"

class ReconduiteALaFrontiere(BaseModel):
    sous_descripteur: Literal['ReconduiteALaFrontiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-867"
    descripteur: str = "reconduite à la frontière"

class Clandestin(BaseModel):
    sous_descripteur: Literal['Clandestin']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-417"
    descripteur: str = "clandestin"

class CirculationDesPersonnes(BaseModel):
    sous_descripteur: Literal['CirculationDesPersonnes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-32"
    descripteur: str = "circulation des personnes"

class PoliceDesFrontieres(BaseModel):
    sous_descripteur: Literal['PoliceDesFrontieres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-630"
    descripteur: str = "police des frontières"

class SurveillanceDuTerritoire(BaseModel):
    sous_descripteur: Union['PoliceDesFrontieres', 'CirculationDesPersonnes', 'Clandestin', 'ReconduiteALaFrontiere'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1269"
    descripteur: str = "surveillance du territoire"

class TransportDeCorps(BaseModel):
    sous_descripteur: Literal['TransportDeCorps']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-545"
    descripteur: str = "transport de corps"

class RechercheDansLinteretDesFamilles(BaseModel):
    sous_descripteur: Literal['RechercheDansLinteretDesFamilles']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1300"
    descripteur: str = "recherche dans l'intérêt des familles"

class SejourDesEtrangers(BaseModel):
    sous_descripteur: Literal['SejourDesEtrangers']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-204"
    descripteur: str = "séjour des étrangers"

class DetentionDarmes(BaseModel):
    sous_descripteur: Literal['DetentionDarmes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-418"
    descripteur: str = "détention d'armes"

class ProfessionReglementee(BaseModel):
    sous_descripteur: Literal['ProfessionReglementee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-962"
    descripteur: str = "profession réglementée"

class PompesFunebres(BaseModel):
    sous_descripteur: Literal['PompesFunebres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1461"
    descripteur: str = "pompes funèbres"

class PoliceAdministrative(BaseModel):
    sous_descripteur: Union['PompesFunebres', 'ProfessionReglementee', 'DetentionDarmes', 'SejourDesEtrangers', 'RechercheDansLinteretDesFamilles', 'TransportDeCorps'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-28"
    descripteur: str = "police administrative"

class MaintienDeLordre(BaseModel):
    sous_descripteur: Literal['MaintienDeLordre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-17"
    descripteur: str = "maintien de l'ordre"

class Police(BaseModel):
    sous_descripteur: Union['MaintienDeLordre', 'PoliceAdministrative', 'SurveillanceDuTerritoire', 'PoliceDesTransports', 'PoliceDesMoeurs', 'PoliceDesJeux', 'PoliceJudiciaire', 'PoliceDeLaChasse', 'PoliceDeLaPeche', 'PoliceDesCultes', 'AgentDeLaForcePublique', 'PoliceDesEaux'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-471"
    descripteur: str = "police"

class CommandePublique(BaseModel):
    sous_descripteur: Literal['CommandePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1161"
    descripteur: str = "commande publique"

class Monnaie(BaseModel):
    sous_descripteur: Literal['Monnaie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-726"
    descripteur: str = "monnaie"

class RecetteFiscale(BaseModel):
    sous_descripteur: Literal['RecetteFiscale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1245"
    descripteur: str = "recette fiscale"

class DettePublique(BaseModel):
    sous_descripteur: Literal['DettePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-993"
    descripteur: str = "dette publique"

class DepenseDeFonctionnement(BaseModel):
    sous_descripteur: Literal['DepenseDeFonctionnement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-464"
    descripteur: str = "dépense de fonctionnement"

class DepenseDinvestissement(BaseModel):
    sous_descripteur: Literal['DepenseDinvestissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-206"
    descripteur: str = "dépense d'investissement"

class FondsEuropeen(BaseModel):
    sous_descripteur: Literal['FondsEuropeen']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-117"
    descripteur: str = "fonds européen"

class RecetteNonFiscale(BaseModel):
    sous_descripteur: Literal['RecetteNonFiscale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-112"
    descripteur: str = "recette non fiscale"

class ComptabilitePublique(BaseModel):
    sous_descripteur: Union['RecetteNonFiscale', 'FondsEuropeen', 'DepenseDinvestissement', 'DepenseDeFonctionnement', 'DettePublique', 'RecetteFiscale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-747"
    descripteur: str = "comptabilité publique"

class DomainePublicFluvial(BaseModel):
    sous_descripteur: Literal['DomainePublicFluvial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1258"
    descripteur: str = "domaine public fluvial"

class Servitude(BaseModel):
    sous_descripteur: Literal['Servitude']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-802"
    descripteur: str = "servitude"

class OccupationTemporaireDuDomainePublic(BaseModel):
    sous_descripteur: Literal['OccupationTemporaireDuDomainePublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-423"
    descripteur: str = "occupation temporaire du domaine public"

class DomainePublicMaritime(BaseModel):
    sous_descripteur: Literal['DomainePublicMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-35"
    descripteur: str = "domaine public maritime"

class DomainePublic(BaseModel):
    sous_descripteur: Union['DomainePublicMaritime', 'OccupationTemporaireDuDomainePublic', 'Servitude', 'DomainePublicFluvial'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1127"
    descripteur: str = "domaine public"

class ConcessionDomaniale(BaseModel):
    sous_descripteur: Literal['ConcessionDomaniale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1113"
    descripteur: str = "concession domaniale"

class AlienationDomaniale(BaseModel):
    sous_descripteur: Literal['AlienationDomaniale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-377"
    descripteur: str = "aliénation domaniale"

class DomaineImmobilier(BaseModel):
    sous_descripteur: Literal['DomaineImmobilier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-383"
    descripteur: str = "domaine immobilier"

class BiensDepartementaux(BaseModel):
    sous_descripteur: Literal['BiensDepartementaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-495"
    descripteur: str = "biens départementaux"

class ConcessionFuneraire(BaseModel):
    sous_descripteur: Literal['ConcessionFuneraire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-93"
    descripteur: str = "concession funéraire"

class BiensRegionaux(BaseModel):
    sous_descripteur: Literal['BiensRegionaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-616"
    descripteur: str = "biens régionaux"

class AcquisitionDomaniale(BaseModel):
    sous_descripteur: Literal['AcquisitionDomaniale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-333"
    descripteur: str = "acquisition domaniale"

class BienAdministre(BaseModel):
    sous_descripteur: Literal['BienAdministre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-766"
    descripteur: str = "bien administré"

class BiensCommunaux(BaseModel):
    sous_descripteur: Literal['BiensCommunaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-690"
    descripteur: str = "biens communaux"

class BiensNationaux(BaseModel):
    sous_descripteur: Literal['BiensNationaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1051"
    descripteur: str = "biens nationaux"

class BiensIntercommunaux(BaseModel):
    sous_descripteur: Literal['BiensIntercommunaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1433"
    descripteur: str = "biens intercommunaux"

class DomaineMobilier(BaseModel):
    sous_descripteur: Literal['DomaineMobilier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-763"
    descripteur: str = "domaine mobilier"

class ProduitDomanial(BaseModel):
    sous_descripteur: Literal['ProduitDomanial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1070"
    descripteur: str = "produit domanial"

class ProprietePublique(BaseModel):
    sous_descripteur: Union['ProduitDomanial', 'DomaineMobilier', 'BiensIntercommunaux', 'BiensNationaux', 'BiensCommunaux', 'BienAdministre', 'AcquisitionDomaniale', 'BiensRegionaux', 'ConcessionFuneraire', 'BiensDepartementaux', 'DomaineImmobilier', 'AlienationDomaniale', 'ConcessionDomaniale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-11"
    descripteur: str = "propriété publique"

class FinancesDepartementales(BaseModel):
    sous_descripteur: Literal['FinancesDepartementales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1138"
    descripteur: str = "finances départementales"

class FinancesIntercommunales(BaseModel):
    sous_descripteur: Literal['FinancesIntercommunales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-354"
    descripteur: str = "finances intercommunales"

class FinancesCommunales(BaseModel):
    sous_descripteur: Literal['FinancesCommunales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-888"
    descripteur: str = "finances communales"

class FinancesRegionales(BaseModel):
    sous_descripteur: Literal['FinancesRegionales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-6"
    descripteur: str = "finances régionales"

class FinancesLocales(BaseModel):
    sous_descripteur: Union['FinancesRegionales', 'FinancesCommunales', 'FinancesIntercommunales', 'FinancesDepartementales'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-376"
    descripteur: str = "finances locales"

class FinancesPubliques(BaseModel):
    sous_descripteur: Union['FinancesLocales', 'ProprietePublique', 'DomainePublic', 'ComptabilitePublique', 'Monnaie', 'CommandePublique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1222"
    descripteur: str = "finances publiques"

class Administration(BaseModel):
    sous_descripteur: Union['FinancesPubliques', 'Police', 'RegimeSeigneurial', 'Fiscalite', 'ProtectionCivile', 'AdministrationGenerale', 'DroitPublic'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1317"
    descripteur: str = "administration"
