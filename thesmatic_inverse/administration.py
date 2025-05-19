from pydantic import BaseModel
from typing import Union, Literal

class Democratie(BaseModel):
    terme_specifique: Literal['Democratie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1229"
    descripteur: str = "démocratie"

class DroitCommunautaire(BaseModel):
    terme_specifique: Literal['DroitCommunautaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-965"
    descripteur: str = "droit communautaire"

class Legislation(BaseModel):
    terme_specifique: Literal['Legislation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-765"
    descripteur: str = "législation"

class Institutions(BaseModel):
    terme_specifique: Literal['Institutions']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-385"
    descripteur: str = "institutions"

class ChefDEtat(BaseModel):
    terme_specifique: Literal['ChefDEtat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1460"
    descripteur: str = "chef d'État"

class Republique(BaseModel):
    terme_specifique: Literal['Republique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-710"
    descripteur: str = "république"

class Monarchie(BaseModel):
    terme_specifique: Literal['Monarchie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-346"
    descripteur: str = "monarchie"

class Etat(BaseModel):
    terme_specifique: Union['Monarchie', 'Republique', 'ChefDEtat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-476"
    descripteur: str = "État"

class Constitution(BaseModel):
    terme_specifique: Literal['Constitution']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-113"
    descripteur: str = "constitution"

class DroitPublic(BaseModel):
    terme_specifique: Union['Constitution', 'Etat', 'Institutions', 'Legislation', 'DroitCommunautaire', 'Democratie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1259"
    descripteur: str = "droit public"

class Province(BaseModel):
    terme_specifique: Literal['Province']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-999"
    descripteur: str = "province"

class CirconscriptionFiscale(BaseModel):
    terme_specifique: Literal['CirconscriptionFiscale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-708"
    descripteur: str = "circonscription fiscale"

class Generalite(BaseModel):
    terme_specifique: Literal['Generalite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-638"
    descripteur: str = "généralité"

class Pays(BaseModel):
    terme_specifique: Literal['Pays']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1372"
    descripteur: str = "pays"

class Senechaussee(BaseModel):
    terme_specifique: Literal['Senechaussee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-812"
    descripteur: str = "sénéchaussée"

class AgglomerationUrbaine(BaseModel):
    terme_specifique: Literal['AgglomerationUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1035"
    descripteur: str = "agglomération urbaine"

class DomaineRoyal(BaseModel):
    terme_specifique: Literal['DomaineRoyal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1043"
    descripteur: str = "domaine royal"

class DistrictRevolutionnaire(BaseModel):
    terme_specifique: Literal['DistrictRevolutionnaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1328"
    descripteur: str = "district révolutionnaire"

class Arrondissement(BaseModel):
    terme_specifique: Literal['Arrondissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1064"
    descripteur: str = "arrondissement"

class Seigneurie(BaseModel):
    terme_specifique: Literal['Seigneurie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-454"
    descripteur: str = "seigneurie"

class LimiteTerritoriale(BaseModel):
    terme_specifique: Literal['LimiteTerritoriale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-349"
    descripteur: str = "limite territoriale"

class RessortJudiciaire(BaseModel):
    terme_specifique: Literal['RessortJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-299"
    descripteur: str = "ressort judiciaire"

class Canton(BaseModel):
    terme_specifique: Literal['Canton']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-645"
    descripteur: str = "canton"

class CirconscriptionTerritoriale(BaseModel):
    terme_specifique: Union['Canton', 'RessortJudiciaire', 'LimiteTerritoriale', 'Seigneurie', 'Arrondissement', 'DistrictRevolutionnaire', 'DomaineRoyal', 'AgglomerationUrbaine', 'Senechaussee', 'Pays', 'Generalite', 'CirconscriptionFiscale', 'Province']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-601"
    descripteur: str = "circonscription territoriale"

class HotelDeLaPrefecture(BaseModel):
    terme_specifique: Literal['HotelDeLaPrefecture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1289"
    descripteur: str = "hôtel de la préfecture"

class HotelCommunautaire(BaseModel):
    terme_specifique: Literal['HotelCommunautaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1160"
    descripteur: str = "hôtel communautaire"

class HotelDeRegion(BaseModel):
    terme_specifique: Literal['HotelDeRegion']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1059"
    descripteur: str = "hôtel de région"

class HotelDeLaSousprefecture(BaseModel):
    terme_specifique: Literal['HotelDeLaSousprefecture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-794"
    descripteur: str = "hôtel de la sous-préfecture"

class HotelDeVille(BaseModel):
    terme_specifique: Literal['HotelDeVille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-712"
    descripteur: str = "hôtel de ville"

class PalaisDeJustice(BaseModel):
    terme_specifique: Literal['PalaisDeJustice']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-356"
    descripteur: str = "palais de justice"

class CiteAdministrative(BaseModel):
    terme_specifique: Literal['CiteAdministrative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-351"
    descripteur: str = "cité administrative"

class HotelDuDepartement(BaseModel):
    terme_specifique: Literal['HotelDuDepartement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-273"
    descripteur: str = "hôtel du département"

class BatimentAdministratif(BaseModel):
    terme_specifique: Union['HotelDuDepartement', 'CiteAdministrative', 'PalaisDeJustice', 'HotelDeVille', 'HotelDeLaSousprefecture', 'HotelDeRegion', 'HotelCommunautaire', 'HotelDeLaPrefecture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1227"
    descripteur: str = "bâtiment administratif"

class AdministrationPrefectorale(BaseModel):
    terme_specifique: Literal['AdministrationPrefectorale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-621"
    descripteur: str = "administration préfectorale"

class ServiceDeconcentre(BaseModel):
    terme_specifique: Literal['ServiceDeconcentre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1088"
    descripteur: str = "service déconcentré"

class AdministrationLocaleDAncienRegime(BaseModel):
    terme_specifique: Literal['AdministrationLocaleDAncienRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1040"
    descripteur: str = "administration locale d'Ancien Régime"

class AdministrationCommunale(BaseModel):
    terme_specifique: Literal['AdministrationCommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1435"
    descripteur: str = "administration communale"

class EtablissementPublicLocal(BaseModel):
    terme_specifique: Literal['EtablissementPublicLocal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1422"
    descripteur: str = "établissement public local"

class ServiceExterieur(BaseModel):
    terme_specifique: Literal['ServiceExterieur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-575"
    descripteur: str = "service extérieur"

class AdministrationCentrale(BaseModel):
    terme_specifique: Literal['AdministrationCentrale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1044"
    descripteur: str = "administration centrale"

class OrganismeAdministratifEuropeen(BaseModel):
    terme_specifique: Literal['OrganismeAdministratifEuropeen']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-771"
    descripteur: str = "organisme administratif européen"

class EtablissementPublicNational(BaseModel):
    terme_specifique: Literal['EtablissementPublicNational']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1109"
    descripteur: str = "établissement public national"

class AdministrationRegionale(BaseModel):
    terme_specifique: Literal['AdministrationRegionale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-422"
    descripteur: str = "administration régionale"

class OrganismeParapublic(BaseModel):
    terme_specifique: Literal['OrganismeParapublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-387"
    descripteur: str = "organisme parapublic"

class AdministrationCantonaleDepoqueRevolutionnaire(BaseModel):
    terme_specifique: Literal['AdministrationCantonaleDepoqueRevolutionnaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-368"
    descripteur: str = "administration cantonale d'époque révolutionnaire"

class AdministrationDepartementale(BaseModel):
    terme_specifique: Literal['AdministrationDepartementale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-260"
    descripteur: str = "administration départementale"

class OrganismeConsultatif(BaseModel):
    terme_specifique: Literal['OrganismeConsultatif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-131"
    descripteur: str = "organisme consultatif"

class StructureAdministrative(BaseModel):
    terme_specifique: Union['OrganismeConsultatif', 'AdministrationDepartementale', 'AdministrationCantonaleDepoqueRevolutionnaire', 'OrganismeParapublic', 'AdministrationRegionale', 'EtablissementPublicNational', 'OrganismeAdministratifEuropeen', 'AdministrationCentrale', 'ServiceExterieur', 'EtablissementPublicLocal', 'AdministrationCommunale', 'AdministrationLocaleDAncienRegime', 'ServiceDeconcentre', 'AdministrationPrefectorale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-435"
    descripteur: str = "structure administrative"

class Deconcentration(BaseModel):
    terme_specifique: Literal['Deconcentration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1452"
    descripteur: str = "déconcentration"

class Delocalisation(BaseModel):
    terme_specifique: Literal['Delocalisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-276"
    descripteur: str = "délocalisation"

class Regionalisation(BaseModel):
    terme_specifique: Literal['Regionalisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-55"
    descripteur: str = "régionalisation"

class Decentralisation(BaseModel):
    terme_specifique: Literal['Decentralisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1083"
    descripteur: str = "décentralisation"

class TransfertDeCompetences(BaseModel):
    terme_specifique: Union['Decentralisation', 'Regionalisation', 'Delocalisation', 'Deconcentration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-347"
    descripteur: str = "transfert de compétences"

class EtatsProvinciaux(BaseModel):
    terme_specifique: Literal['EtatsProvinciaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1451"
    descripteur: str = "états provinciaux"

class ConseilCommunautaire(BaseModel):
    terme_specifique: Literal['ConseilCommunautaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1122"
    descripteur: str = "conseil communautaire"

class ConseilDadministration(BaseModel):
    terme_specifique: Literal['ConseilDadministration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-769"
    descripteur: str = "conseil d'administration"

class AssembleeGenerale(BaseModel):
    terme_specifique: Literal['AssembleeGenerale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-555"
    descripteur: str = "assemblée générale"

class EtatsGeneraux(BaseModel):
    terme_specifique: Literal['EtatsGeneraux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-275"
    descripteur: str = "états généraux"

class ConseilMunicipal(BaseModel):
    terme_specifique: Literal['ConseilMunicipal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-159"
    descripteur: str = "conseil municipal"

class ConseilDarrondissement(BaseModel):
    terme_specifique: Literal['ConseilDarrondissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-874"
    descripteur: str = "conseil d'arrondissement"

class ConseilGeneral(BaseModel):
    terme_specifique: Literal['ConseilGeneral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-367"
    descripteur: str = "conseil général"

class AssembleeNationale(BaseModel):
    terme_specifique: Literal['AssembleeNationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-175"
    descripteur: str = "assemblée nationale"

class AssembleeEuropeenne(BaseModel):
    terme_specifique: Literal['AssembleeEuropeenne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-922"
    descripteur: str = "assemblée européenne"

class ConseilRegional(BaseModel):
    terme_specifique: Literal['ConseilRegional']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1237"
    descripteur: str = "conseil régional"

class OrganeDeliberant(BaseModel):
    terme_specifique: Union['ConseilRegional', 'AssembleeEuropeenne', 'AssembleeNationale', 'ConseilGeneral', 'ConseilDarrondissement', 'ConseilMunicipal', 'EtatsGeneraux', 'AssembleeGenerale', 'ConseilDadministration', 'ConseilCommunautaire', 'EtatsProvinciaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1157"
    descripteur: str = "organe délibérant"

class ConcoursAdministratif(BaseModel):
    terme_specifique: Literal['ConcoursAdministratif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1071"
    descripteur: str = "concours administratif"

class AgentNonTitulaire(BaseModel):
    terme_specifique: Literal['AgentNonTitulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-657"
    descripteur: str = "agent non titulaire"

class ConseilDeDiscipline(BaseModel):
    terme_specifique: Literal['ConseilDeDiscipline']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-507"
    descripteur: str = "conseil de discipline"

class AgentDeLadministrationRoyale(BaseModel):
    terme_specifique: Literal['AgentDeLadministrationRoyale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1417"
    descripteur: str = "agent de l'administration royale"

class FonctionnaireTerritorial(BaseModel):
    terme_specifique: Literal['FonctionnaireTerritorial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-353"
    descripteur: str = "fonctionnaire territorial"

class AgentDeDroitPrive(BaseModel):
    terme_specifique: Literal['AgentDeDroitPrive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-218"
    descripteur: str = "agent de droit privé"

class FonctionnaireDeLUnionEuropeenne(BaseModel):
    terme_specifique: Literal['FonctionnaireDeLUnionEuropeenne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-195"
    descripteur: str = "fonctionnaire de l'Union européenne"

class FonctionnaireHospitalier(BaseModel):
    terme_specifique: Literal['FonctionnaireHospitalier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1414"
    descripteur: str = "fonctionnaire hospitalier"

class FonctionnaireDeLEtat(BaseModel):
    terme_specifique: Literal['FonctionnaireDeLEtat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1056"
    descripteur: str = "fonctionnaire de l'État"

class Personnel(BaseModel):
    terme_specifique: Union['FonctionnaireDeLEtat', 'FonctionnaireHospitalier', 'FonctionnaireDeLUnionEuropeenne', 'AgentDeDroitPrive', 'FonctionnaireTerritorial', 'AgentDeLadministrationRoyale', 'ConseilDeDiscipline', 'AgentNonTitulaire', 'ConcoursAdministratif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-805"
    descripteur: str = "personnel"

class Commune(BaseModel):
    terme_specifique: Literal['Commune']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-317"
    descripteur: str = "commune"

class EtablissementPublicDeCooperationIntercommunale(BaseModel):
    terme_specifique: Literal['EtablissementPublicDeCooperationIntercommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1238"
    descripteur: str = "établissement public de coopération intercommunale"

class CooperationInterregionale(BaseModel):
    terme_specifique: Literal['CooperationInterregionale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-199"
    descripteur: str = "coopération interrégionale"

class Departement(BaseModel):
    terme_specifique: Literal['Departement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1449"
    descripteur: str = "département"

class RegroupementDeCommunes(BaseModel):
    terme_specifique: Literal['RegroupementDeCommunes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-594"
    descripteur: str = "regroupement de communes"

class Region(BaseModel):
    terme_specifique: Literal['Region']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1079"
    descripteur: str = "région"

class CollectiviteLocale(BaseModel):
    terme_specifique: Union['Region', 'RegroupementDeCommunes', 'Departement', 'CooperationInterregionale', 'EtablissementPublicDeCooperationIntercommunale', 'Commune']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-73"
    descripteur: str = "collectivité locale"

class AdministrationGenerale(BaseModel):
    terme_specifique: Union['CollectiviteLocale', 'Personnel', 'OrganeDeliberant', 'TransfertDeCompetences', 'StructureAdministrative', 'BatimentAdministratif', 'CirconscriptionTerritoriale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1345"
    descripteur: str = "administration générale"

class EquipementDeSecours(BaseModel):
    terme_specifique: Literal['EquipementDeSecours']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1462"
    descripteur: str = "équipement de secours"

class SapeurPompier(BaseModel):
    terme_specifique: Literal['SapeurPompier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1430"
    descripteur: str = "sapeur pompier"

class SauvetageEnMer(BaseModel):
    terme_specifique: Literal['SauvetageEnMer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1033"
    descripteur: str = "sauvetage en mer"

class AideMedicaleUrgente(BaseModel):
    terme_specifique: Literal['AideMedicaleUrgente']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-646"
    descripteur: str = "aide médicale urgente"

class PoliceSecours(BaseModel):
    terme_specifique: Literal['PoliceSecours']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-278"
    descripteur: str = "police secours"

class Secours(BaseModel):
    terme_specifique: Union['PoliceSecours', 'AideMedicaleUrgente', 'SauvetageEnMer', 'SapeurPompier', 'EquipementDeSecours']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1000"
    descripteur: str = "secours"

class ImmeubleDeGrandeHauteur(BaseModel):
    terme_specifique: Literal['ImmeubleDeGrandeHauteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1219"
    descripteur: str = "immeuble de grande hauteur"

class TransportDeMatieresDangereuses(BaseModel):
    terme_specifique: Literal['TransportDeMatieresDangereuses']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1151"
    descripteur: str = "transport de matières dangereuses"

class CatastropheNaturelle(BaseModel):
    terme_specifique: Literal['CatastropheNaturelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-698"
    descripteur: str = "catastrophe naturelle"

class CatastropheIndustrielle(BaseModel):
    terme_specifique: Literal['CatastropheIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1055"
    descripteur: str = "catastrophe industrielle"

class Inondation(BaseModel):
    terme_specifique: Literal['Inondation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1393"
    descripteur: str = "inondation"

class Incendie(BaseModel):
    terme_specifique: Literal['Incendie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-284"
    descripteur: str = "incendie"

class Sinistre(BaseModel):
    terme_specifique: Union['Incendie', 'Inondation', 'CatastropheIndustrielle', 'CatastropheNaturelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-67"
    descripteur: str = "sinistre"

class AppareilAPressionDeVapeur(BaseModel):
    terme_specifique: Literal['AppareilAPressionDeVapeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-126"
    descripteur: str = "appareil à pression de vapeur"

class AccidentDesTransports(BaseModel):
    terme_specifique: Literal['AccidentDesTransports']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1221"
    descripteur: str = "accident des transports"

class InstallationClassee(BaseModel):
    terme_specifique: Literal['InstallationClassee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-887"
    descripteur: str = "installation classée"

class EtablissementRecevantDuPublic(BaseModel):
    terme_specifique: Literal['EtablissementRecevantDuPublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-478"
    descripteur: str = "établissement recevant du public"

class SecuriteRoutiere(BaseModel):
    terme_specifique: Literal['SecuriteRoutiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-628"
    descripteur: str = "sécurité routière"

class ProtectionCivile(BaseModel):
    terme_specifique: Union['SecuriteRoutiere', 'EtablissementRecevantDuPublic', 'InstallationClassee', 'AccidentDesTransports', 'AppareilAPressionDeVapeur', 'Sinistre', 'TransportDeMatieresDangereuses', 'ImmeubleDeGrandeHauteur', 'Secours']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-147"
    descripteur: str = "protection civile"

class Contribuable(BaseModel):
    terme_specifique: Literal['Contribuable']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1123"
    descripteur: str = "contribuable"

class FiscaliteDirecteRevolutionnaire(BaseModel):
    terme_specifique: Literal['FiscaliteDirecteRevolutionnaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1165"
    descripteur: str = "fiscalité directe révolutionnaire"

class TimbreFiscal(BaseModel):
    terme_specifique: Literal['TimbreFiscal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1387"
    descripteur: str = "timbre fiscal"

class RecouvrementFiscal(BaseModel):
    terme_specifique: Literal['RecouvrementFiscal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-791"
    descripteur: str = "recouvrement fiscal"

class DroitsDomaniauxDAncienRegime(BaseModel):
    terme_specifique: Literal['DroitsDomaniauxDAncienRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-623"
    descripteur: str = "droits domaniaux d'Ancien Régime"

class DroitsReserves(BaseModel):
    terme_specifique: Literal['DroitsReserves']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-853"
    descripteur: str = "droits réservés"

class OfficeDAncienRegime(BaseModel):
    terme_specifique: Literal['OfficeDAncienRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-780"
    descripteur: str = "office d'Ancien Régime"

class TaxeExtraordinaireDAncienRegime(BaseModel):
    terme_specifique: Union['OfficeDAncienRegime', 'DroitsReserves']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-462"
    descripteur: str = "taxe extraordinaire d'Ancien Régime"

class ExonerationFiscale(BaseModel):
    terme_specifique: Literal['ExonerationFiscale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-434"
    descripteur: str = "exonération fiscale"

class DroitsDeDouane(BaseModel):
    terme_specifique: Literal['DroitsDeDouane']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-410"
    descripteur: str = "droits de douane"

class DroitsDeSuccession(BaseModel):
    terme_specifique: Literal['DroitsDeSuccession']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-542"
    descripteur: str = "droits de succession"

class Enregistrement(BaseModel):
    terme_specifique: Union['DroitsDeSuccession']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-306"
    descripteur: str = "enregistrement"

class Contrebande(BaseModel):
    terme_specifique: Literal['Contrebande']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1370"
    descripteur: str = "contrebande"

class FraudeFiscale(BaseModel):
    terme_specifique: Union['Contrebande']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-295"
    descripteur: str = "fraude fiscale"

class CorveeRoyale(BaseModel):
    terme_specifique: Literal['CorveeRoyale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-262"
    descripteur: str = "corvée royale"

class TaxeDhabitation(BaseModel):
    terme_specifique: Literal['TaxeDhabitation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1298"
    descripteur: str = "taxe d'habitation"

class TaxeDeSejour(BaseModel):
    terme_specifique: Literal['TaxeDeSejour']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1002"
    descripteur: str = "taxe de séjour"

class DroitDesPauvres(BaseModel):
    terme_specifique: Literal['DroitDesPauvres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-298"
    descripteur: str = "droit des pauvres"

class DroitDePlace(BaseModel):
    terme_specifique: Literal['DroitDePlace']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-641"
    descripteur: str = "droit de place"

class ImpotsProvinciauxDAncienRegime(BaseModel):
    terme_specifique: Literal['ImpotsProvinciauxDAncienRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1016"
    descripteur: str = "impôts provinciaux d'Ancien Régime"

class Octroi(BaseModel):
    terme_specifique: Literal['Octroi']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1316"
    descripteur: str = "octroi"

class ImpotsLocaux(BaseModel):
    terme_specifique: Union['Octroi', 'ImpotsProvinciauxDAncienRegime', 'DroitDePlace', 'DroitDesPauvres', 'TaxeDeSejour', 'TaxeDhabitation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-241"
    descripteur: str = "impôts locaux"

class RedevanceParafiscale(BaseModel):
    terme_specifique: Literal['RedevanceParafiscale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1350"
    descripteur: str = "redevance parafiscale"

class ImpotSurLeRevenu(BaseModel):
    terme_specifique: Literal['ImpotSurLeRevenu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1375"
    descripteur: str = "impôt sur le revenu"

class ImpotSocial(BaseModel):
    terme_specifique: Literal['ImpotSocial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-930"
    descripteur: str = "impôt social"

class ImpotSurLaFortune(BaseModel):
    terme_specifique: Literal['ImpotSurLaFortune']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-188"
    descripteur: str = "impôt sur la fortune"

class FiscaliteDesPersonnes(BaseModel):
    terme_specifique: Union['ImpotSurLaFortune', 'ImpotSocial', 'ImpotSurLeRevenu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1376"
    descripteur: str = "fiscalité des personnes"

class TaxeFonciere(BaseModel):
    terme_specifique: Literal['TaxeFonciere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-807"
    descripteur: str = "taxe foncière"

class Cadastre(BaseModel):
    terme_specifique: Literal['Cadastre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-463"
    descripteur: str = "cadastre"

class EvaluationFonciere(BaseModel):
    terme_specifique: Literal['EvaluationFonciere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-132"
    descripteur: str = "évaluation foncière"

class PubliciteFonciere(BaseModel):
    terme_specifique: Literal['PubliciteFonciere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1215"
    descripteur: str = "publicité foncière"

class FiscaliteImmobiliere(BaseModel):
    terme_specifique: Union['PubliciteFonciere', 'EvaluationFonciere', 'Cadastre', 'TaxeFonciere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1058"
    descripteur: str = "fiscalité immobilière"

class DroitsDeCirculation(BaseModel):
    terme_specifique: Literal['DroitsDeCirculation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1086"
    descripteur: str = "droits de circulation"

class MonopolesFiscaux(BaseModel):
    terme_specifique: Literal['MonopolesFiscaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-975"
    descripteur: str = "monopoles fiscaux"

class FiscalitePetroliere(BaseModel):
    terme_specifique: Literal['FiscalitePetroliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-90"
    descripteur: str = "fiscalité pétrolière"

class ContributionsIndirectes(BaseModel):
    terme_specifique: Union['FiscalitePetroliere', 'MonopolesFiscaux', 'DroitsDeCirculation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-398"
    descripteur: str = "contributions indirectes"

class TaxeDapprentissage(BaseModel):
    terme_specifique: Literal['TaxeDapprentissage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1031"
    descripteur: str = "taxe d'apprentissage"

class ImpotSurLesSocietes(BaseModel):
    terme_specifique: Literal['ImpotSurLesSocietes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1136"
    descripteur: str = "impôt sur les sociétés"

class TaxeSurLeChiffreDaffaires(BaseModel):
    terme_specifique: Literal['TaxeSurLeChiffreDaffaires']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-205"
    descripteur: str = "taxe sur le chiffre d'affaires"

class ImpotSurLesBenefices(BaseModel):
    terme_specifique: Literal['ImpotSurLesBenefices']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-71"
    descripteur: str = "impôt sur les bénéfices"

class TaxeProfessionnelle(BaseModel):
    terme_specifique: Literal['TaxeProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-640"
    descripteur: str = "taxe professionnelle"

class FiscaliteProfessionnelle(BaseModel):
    terme_specifique: Union['TaxeProfessionnelle', 'ImpotSurLesBenefices', 'TaxeSurLeChiffreDaffaires', 'ImpotSurLesSocietes', 'TaxeDapprentissage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-669"
    descripteur: str = "fiscalité professionnelle"

class FiscaliteDirecteDAncienRegime(BaseModel):
    terme_specifique: Literal['FiscaliteDirecteDAncienRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-47"
    descripteur: str = "fiscalité directe d'Ancien Régime"

class Fiscalite(BaseModel):
    terme_specifique: Union['FiscaliteDirecteDAncienRegime', 'FiscaliteProfessionnelle', 'ContributionsIndirectes', 'FiscaliteImmobiliere', 'FiscaliteDesPersonnes', 'RedevanceParafiscale', 'ImpotsLocaux', 'CorveeRoyale', 'FraudeFiscale', 'Enregistrement', 'DroitsDeDouane', 'ExonerationFiscale', 'TaxeExtraordinaireDAncienRegime', 'DroitsDomaniauxDAncienRegime', 'RecouvrementFiscal', 'TimbreFiscal', 'FiscaliteDirecteRevolutionnaire', 'Contribuable']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-829"
    descripteur: str = "fiscalité"

class Alleu(BaseModel):
    terme_specifique: Literal['Alleu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-688"
    descripteur: str = "alleu"

class Reformation(BaseModel):
    terme_specifique: Literal['Reformation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1429"
    descripteur: str = "réformation"

class AgentSeigneurial(BaseModel):
    terme_specifique: Literal['AgentSeigneurial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-561"
    descripteur: str = "agent seigneurial"

class Reconnaissances(BaseModel):
    terme_specifique: Literal['Reconnaissances']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-285"
    descripteur: str = "reconnaissances"

class AdministrationSeigneuriale(BaseModel):
    terme_specifique: Union['Reconnaissances', 'AgentSeigneurial', 'Reformation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-943"
    descripteur: str = "administration seigneuriale"

class DroitsHonorifiques(BaseModel):
    terme_specifique: Literal['DroitsHonorifiques']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-282"
    descripteur: str = "droits honorifiques"

class DenombrementSeigneurial(BaseModel):
    terme_specifique: Literal['DenombrementSeigneurial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1313"
    descripteur: str = "dénombrement seigneurial"

class SermentDeFidelite(BaseModel):
    terme_specifique: Literal['SermentDeFidelite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-553"
    descripteur: str = "serment de fidélité"

class Hommage(BaseModel):
    terme_specifique: Literal['Hommage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-239"
    descripteur: str = "hommage"

class Feodalite(BaseModel):
    terme_specifique: Union['Hommage', 'SermentDeFidelite', 'DenombrementSeigneurial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-718"
    descripteur: str = "féodalité"

class DroitsSeigneuriaux(BaseModel):
    terme_specifique: Literal['DroitsSeigneuriaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1115"
    descripteur: str = "droits seigneuriaux"

class DroitsDusage(BaseModel):
    terme_specifique: Literal['DroitsDusage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1333"
    descripteur: str = "droits d'usage"

class Coutumes(BaseModel):
    terme_specifique: Literal['Coutumes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-155"
    descripteur: str = "coutumes"

class PrivilegesDesCommunautes(BaseModel):
    terme_specifique: Union['Coutumes', 'DroitsDusage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-29"
    descripteur: str = "privilèges des communautés"

class RegimeSeigneurial(BaseModel):
    terme_specifique: Union['PrivilegesDesCommunautes', 'DroitsSeigneuriaux', 'Feodalite', 'DroitsHonorifiques', 'AdministrationSeigneuriale', 'Alleu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-842"
    descripteur: str = "régime seigneurial"

class PoliceDesEaux(BaseModel):
    terme_specifique: Literal['PoliceDesEaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-522"
    descripteur: str = "police des eaux"

class Marechaussee(BaseModel):
    terme_specifique: Literal['Marechaussee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1425"
    descripteur: str = "maréchaussée"

class PoliceUrbaine(BaseModel):
    terme_specifique: Literal['PoliceUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1093"
    descripteur: str = "police urbaine"

class PoliceMunicipale(BaseModel):
    terme_specifique: Literal['PoliceMunicipale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-668"
    descripteur: str = "police municipale"

class GardeForestier(BaseModel):
    terme_specifique: Literal['GardeForestier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-694"
    descripteur: str = "garde forestier"

class GardeParticulier(BaseModel):
    terme_specifique: Literal['GardeParticulier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-749"
    descripteur: str = "garde particulier"

class Gendarmerie(BaseModel):
    terme_specifique: Literal['Gendarmerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1135"
    descripteur: str = "gendarmerie"

class AgentDeLaForcePublique(BaseModel):
    terme_specifique: Union['Gendarmerie', 'GardeParticulier', 'GardeForestier', 'PoliceMunicipale', 'PoliceUrbaine', 'Marechaussee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1172"
    descripteur: str = "agent de la force publique"

class PoliceDesCultes(BaseModel):
    terme_specifique: Literal['PoliceDesCultes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-863"
    descripteur: str = "police des cultes"

class PoliceDeLaPeche(BaseModel):
    terme_specifique: Literal['PoliceDeLaPeche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-735"
    descripteur: str = "police de la pêche"

class LieutenantDeLouveterie(BaseModel):
    terme_specifique: Literal['LieutenantDeLouveterie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1338"
    descripteur: str = "lieutenant de louveterie"

class PoliceDeLaChasse(BaseModel):
    terme_specifique: Union['LieutenantDeLouveterie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1114"
    descripteur: str = "police de la chasse"

class Arrestation(BaseModel):
    terme_specifique: Literal['Arrestation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1411"
    descripteur: str = "arrestation"

class IndividuRecherche(BaseModel):
    terme_specifique: Literal['IndividuRecherche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-652"
    descripteur: str = "individu recherché"

class InterditDeSejour(BaseModel):
    terme_specifique: Literal['InterditDeSejour']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1054"
    descripteur: str = "interdit de séjour"

class GardeAVue(BaseModel):
    terme_specifique: Literal['GardeAVue']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-271"
    descripteur: str = "garde à vue"

class PoliceJudiciaire(BaseModel):
    terme_specifique: Union['GardeAVue', 'InterditDeSejour', 'IndividuRecherche', 'Arrestation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-468"
    descripteur: str = "police judiciaire"

class PoliceDesJeux(BaseModel):
    terme_specifique: Literal['PoliceDesJeux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-253"
    descripteur: str = "police des jeux"

class EtablissementInterditAuxMineurs(BaseModel):
    terme_specifique: Literal['EtablissementInterditAuxMineurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1347"
    descripteur: str = "établissement interdit aux mineurs"

class Prostitution(BaseModel):
    terme_specifique: Literal['Prostitution']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-598"
    descripteur: str = "prostitution"

class Pornographie(BaseModel):
    terme_specifique: Literal['Pornographie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-201"
    descripteur: str = "pornographie"

class PoliceDesMoeurs(BaseModel):
    terme_specifique: Union['Pornographie', 'Prostitution', 'EtablissementInterditAuxMineurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1396"
    descripteur: str = "police des moeurs"

class PoliceDesTransports(BaseModel):
    terme_specifique: Literal['PoliceDesTransports']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-102"
    descripteur: str = "police des transports"

class ReconduiteALaFrontiere(BaseModel):
    terme_specifique: Literal['ReconduiteALaFrontiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-867"
    descripteur: str = "reconduite à la frontière"

class Clandestin(BaseModel):
    terme_specifique: Literal['Clandestin']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-417"
    descripteur: str = "clandestin"

class CirculationDesPersonnes(BaseModel):
    terme_specifique: Literal['CirculationDesPersonnes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-32"
    descripteur: str = "circulation des personnes"

class PoliceDesFrontieres(BaseModel):
    terme_specifique: Literal['PoliceDesFrontieres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-630"
    descripteur: str = "police des frontières"

class SurveillanceDuTerritoire(BaseModel):
    terme_specifique: Union['PoliceDesFrontieres', 'CirculationDesPersonnes', 'Clandestin', 'ReconduiteALaFrontiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1269"
    descripteur: str = "surveillance du territoire"

class TransportDeCorps(BaseModel):
    terme_specifique: Literal['TransportDeCorps']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-545"
    descripteur: str = "transport de corps"

class RechercheDansLinteretDesFamilles(BaseModel):
    terme_specifique: Literal['RechercheDansLinteretDesFamilles']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1300"
    descripteur: str = "recherche dans l'intérêt des familles"

class SejourDesEtrangers(BaseModel):
    terme_specifique: Literal['SejourDesEtrangers']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-204"
    descripteur: str = "séjour des étrangers"

class DetentionDarmes(BaseModel):
    terme_specifique: Literal['DetentionDarmes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-418"
    descripteur: str = "détention d'armes"

class ProfessionReglementee(BaseModel):
    terme_specifique: Literal['ProfessionReglementee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-962"
    descripteur: str = "profession réglementée"

class PompesFunebres(BaseModel):
    terme_specifique: Literal['PompesFunebres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1461"
    descripteur: str = "pompes funèbres"

class PoliceAdministrative(BaseModel):
    terme_specifique: Union['PompesFunebres', 'ProfessionReglementee', 'DetentionDarmes', 'SejourDesEtrangers', 'RechercheDansLinteretDesFamilles', 'TransportDeCorps']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-28"
    descripteur: str = "police administrative"

class MaintienDeLordre(BaseModel):
    terme_specifique: Literal['MaintienDeLordre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-17"
    descripteur: str = "maintien de l'ordre"

class Police(BaseModel):
    terme_specifique: Union['MaintienDeLordre', 'PoliceAdministrative', 'SurveillanceDuTerritoire', 'PoliceDesTransports', 'PoliceDesMoeurs', 'PoliceDesJeux', 'PoliceJudiciaire', 'PoliceDeLaChasse', 'PoliceDeLaPeche', 'PoliceDesCultes', 'AgentDeLaForcePublique', 'PoliceDesEaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-471"
    descripteur: str = "police"

class CommandePublique(BaseModel):
    terme_specifique: Literal['CommandePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1161"
    descripteur: str = "commande publique"

class Monnaie(BaseModel):
    terme_specifique: Literal['Monnaie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-726"
    descripteur: str = "monnaie"

class RecetteFiscale(BaseModel):
    terme_specifique: Literal['RecetteFiscale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1245"
    descripteur: str = "recette fiscale"

class DettePublique(BaseModel):
    terme_specifique: Literal['DettePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-993"
    descripteur: str = "dette publique"

class DepenseDeFonctionnement(BaseModel):
    terme_specifique: Literal['DepenseDeFonctionnement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-464"
    descripteur: str = "dépense de fonctionnement"

class DepenseDinvestissement(BaseModel):
    terme_specifique: Literal['DepenseDinvestissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-206"
    descripteur: str = "dépense d'investissement"

class FondsEuropeen(BaseModel):
    terme_specifique: Literal['FondsEuropeen']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-117"
    descripteur: str = "fonds européen"

class RecetteNonFiscale(BaseModel):
    terme_specifique: Literal['RecetteNonFiscale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-112"
    descripteur: str = "recette non fiscale"

class ComptabilitePublique(BaseModel):
    terme_specifique: Union['RecetteNonFiscale', 'FondsEuropeen', 'DepenseDinvestissement', 'DepenseDeFonctionnement', 'DettePublique', 'RecetteFiscale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-747"
    descripteur: str = "comptabilité publique"

class DomainePublicFluvial(BaseModel):
    terme_specifique: Literal['DomainePublicFluvial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1258"
    descripteur: str = "domaine public fluvial"

class Servitude(BaseModel):
    terme_specifique: Literal['Servitude']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-802"
    descripteur: str = "servitude"

class OccupationTemporaireDuDomainePublic(BaseModel):
    terme_specifique: Literal['OccupationTemporaireDuDomainePublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-423"
    descripteur: str = "occupation temporaire du domaine public"

class DomainePublicMaritime(BaseModel):
    terme_specifique: Literal['DomainePublicMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-35"
    descripteur: str = "domaine public maritime"

class DomainePublic(BaseModel):
    terme_specifique: Union['DomainePublicMaritime', 'OccupationTemporaireDuDomainePublic', 'Servitude', 'DomainePublicFluvial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1127"
    descripteur: str = "domaine public"

class ConcessionDomaniale(BaseModel):
    terme_specifique: Literal['ConcessionDomaniale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1113"
    descripteur: str = "concession domaniale"

class AlienationDomaniale(BaseModel):
    terme_specifique: Literal['AlienationDomaniale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-377"
    descripteur: str = "aliénation domaniale"

class DomaineImmobilier(BaseModel):
    terme_specifique: Literal['DomaineImmobilier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-383"
    descripteur: str = "domaine immobilier"

class BiensDepartementaux(BaseModel):
    terme_specifique: Literal['BiensDepartementaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-495"
    descripteur: str = "biens départementaux"

class ConcessionFuneraire(BaseModel):
    terme_specifique: Literal['ConcessionFuneraire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-93"
    descripteur: str = "concession funéraire"

class BiensRegionaux(BaseModel):
    terme_specifique: Literal['BiensRegionaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-616"
    descripteur: str = "biens régionaux"

class AcquisitionDomaniale(BaseModel):
    terme_specifique: Literal['AcquisitionDomaniale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-333"
    descripteur: str = "acquisition domaniale"

class BienAdministre(BaseModel):
    terme_specifique: Literal['BienAdministre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-766"
    descripteur: str = "bien administré"

class BiensCommunaux(BaseModel):
    terme_specifique: Literal['BiensCommunaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-690"
    descripteur: str = "biens communaux"

class BiensNationaux(BaseModel):
    terme_specifique: Literal['BiensNationaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1051"
    descripteur: str = "biens nationaux"

class BiensIntercommunaux(BaseModel):
    terme_specifique: Literal['BiensIntercommunaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1433"
    descripteur: str = "biens intercommunaux"

class DomaineMobilier(BaseModel):
    terme_specifique: Literal['DomaineMobilier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-763"
    descripteur: str = "domaine mobilier"

class ProduitDomanial(BaseModel):
    terme_specifique: Literal['ProduitDomanial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1070"
    descripteur: str = "produit domanial"

class ProprietePublique(BaseModel):
    terme_specifique: Union['ProduitDomanial', 'DomaineMobilier', 'BiensIntercommunaux', 'BiensNationaux', 'BiensCommunaux', 'BienAdministre', 'AcquisitionDomaniale', 'BiensRegionaux', 'ConcessionFuneraire', 'BiensDepartementaux', 'DomaineImmobilier', 'AlienationDomaniale', 'ConcessionDomaniale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-11"
    descripteur: str = "propriété publique"

class FinancesDepartementales(BaseModel):
    terme_specifique: Literal['FinancesDepartementales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1138"
    descripteur: str = "finances départementales"

class FinancesIntercommunales(BaseModel):
    terme_specifique: Literal['FinancesIntercommunales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-354"
    descripteur: str = "finances intercommunales"

class FinancesCommunales(BaseModel):
    terme_specifique: Literal['FinancesCommunales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-888"
    descripteur: str = "finances communales"

class FinancesRegionales(BaseModel):
    terme_specifique: Literal['FinancesRegionales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-6"
    descripteur: str = "finances régionales"

class FinancesLocales(BaseModel):
    terme_specifique: Union['FinancesRegionales', 'FinancesCommunales', 'FinancesIntercommunales', 'FinancesDepartementales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-376"
    descripteur: str = "finances locales"

class FinancesPubliques(BaseModel):
    terme_specifique: Union['FinancesLocales', 'ProprietePublique', 'DomainePublic', 'ComptabilitePublique', 'Monnaie', 'CommandePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1222"
    descripteur: str = "finances publiques"

class Administration(BaseModel):
    terme_specifique: Union['FinancesPubliques', 'Police', 'RegimeSeigneurial', 'Fiscalite', 'ProtectionCivile', 'AdministrationGenerale', 'DroitPublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1317"
    descripteur: str = "administration"
