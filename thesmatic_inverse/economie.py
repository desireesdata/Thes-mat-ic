from pydantic import BaseModel, Field
from typing import Union, Literal

class EconomieDenergie(BaseModel):
    sous_descripteur: Literal['EconomieDenergie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-452"
    descripteur: str = "économie d'énergie"

class EnergieNucleaire(BaseModel):
    sous_descripteur: Literal['EnergieNucleaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1373"
    descripteur: str = "énergie nucléaire"

class EnergieEolienne(BaseModel):
    sous_descripteur: Literal['EnergieEolienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1355"
    descripteur: str = "énergie éolienne"

class EnergieDeLaMer(BaseModel):
    sous_descripteur: Literal['EnergieDeLaMer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-973"
    descripteur: str = "énergie de la mer"

class EnergieSolaire(BaseModel):
    sous_descripteur: Literal['EnergieSolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-775"
    descripteur: str = "énergie solaire"

class EnergieHydraulique(BaseModel):
    sous_descripteur: Literal['EnergieHydraulique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-430"
    descripteur: str = "énergie hydraulique"

class EnergieGeothermique(BaseModel):
    sous_descripteur: Literal['EnergieGeothermique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-92"
    descripteur: str = "énergie géothermique"

class EnergieRenouvelable(BaseModel):
    sous_descripteur: Union['EnergieGeothermique', 'EnergieHydraulique', 'EnergieSolaire', 'EnergieDeLaMer', 'EnergieEolienne'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1315"
    descripteur: str = "énergie renouvelable"

class Biocarburant(BaseModel):
    sous_descripteur: Literal['Biocarburant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1019"
    descripteur: str = "bio-carburant"

class CentraleThermique(BaseModel):
    sous_descripteur: Literal['CentraleThermique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1441"
    descripteur: str = "centrale thermique"

class BarrageHydroelectrique(BaseModel):
    sous_descripteur: Literal['BarrageHydroelectrique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1089"
    descripteur: str = "barrage hydroélectrique"

class CentraleNucleaire(BaseModel):
    sous_descripteur: Literal['CentraleNucleaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1443"
    descripteur: str = "centrale nucléaire"

class ProductionElectrique(BaseModel):
    sous_descripteur: Union['CentraleNucleaire', 'BarrageHydroelectrique', 'CentraleThermique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-457"
    descripteur: str = "production électrique"

class Energie(BaseModel):
    sous_descripteur: Union['ProductionElectrique', 'Biocarburant', 'EnergieRenouvelable', 'EnergieNucleaire', 'EconomieDenergie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-166"
    descripteur: str = "énergie"

class CoutDeLaVie(BaseModel):
    sous_descripteur: Literal['CoutDeLaVie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1466"
    descripteur: str = "coût de la vie"

class Prix(BaseModel):
    sous_descripteur: Literal['Prix']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-568"
    descripteur: str = "prix"

class LabelDeQualite(BaseModel):
    sous_descripteur: Literal['LabelDeQualite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1234"
    descripteur: str = "label de qualité"

class Concentration(BaseModel):
    sous_descripteur: Literal['Concentration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1024"
    descripteur: str = "concentration"

class Entente(BaseModel):
    sous_descripteur: Literal['Entente']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1204"
    descripteur: str = "entente"

class PoliceEconomique(BaseModel):
    sous_descripteur: Union['Entente', 'Concentration'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-939"
    descripteur: str = "police économique"

class DeveloppementDurable(BaseModel):
    sous_descripteur: Literal['DeveloppementDurable']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-511"
    descripteur: str = "développement durable"

class ContratDePlan(BaseModel):
    sous_descripteur: Literal['ContratDePlan']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-187"
    descripteur: str = "contrat de plan"

class Planification(BaseModel):
    sous_descripteur: Union['ContratDePlan'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-129"
    descripteur: str = "planification"

class ZoneIndustrielle(BaseModel):
    sous_descripteur: Literal['ZoneIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1431"
    descripteur: str = "zone industrielle"

class PolitiqueDeLaVille(BaseModel):
    sous_descripteur: Literal['PolitiqueDeLaVille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1192"
    descripteur: str = "politique de la ville"

class ZoneDactivites(BaseModel):
    sous_descripteur: Literal['ZoneDactivites']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-961"
    descripteur: str = "zone d'activités"

class VilleNouvelle(BaseModel):
    sous_descripteur: Literal['VilleNouvelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1446"
    descripteur: str = "ville nouvelle"

class DecentralisationIndustrielle(BaseModel):
    sous_descripteur: Literal['DecentralisationIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-182"
    descripteur: str = "décentralisation industrielle"

class PolitiqueDeLaMontagne(BaseModel):
    sous_descripteur: Literal['PolitiqueDeLaMontagne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-52"
    descripteur: str = "politique de la montagne"

class AmenagementDuLittoral(BaseModel):
    sous_descripteur: Literal['AmenagementDuLittoral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-399"
    descripteur: str = "aménagement du littoral"

class AmenagementDuTerritoire(BaseModel):
    sous_descripteur: Union['AmenagementDuLittoral', 'PolitiqueDeLaMontagne', 'DecentralisationIndustrielle', 'VilleNouvelle', 'ZoneDactivites', 'PolitiqueDeLaVille', 'ZoneIndustrielle'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-554"
    descripteur: str = "aménagement du territoire"

class AidePubliqueAuxEntreprises(BaseModel):
    sous_descripteur: Literal['AidePubliqueAuxEntreprises']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-920"
    descripteur: str = "aide publique aux entreprises"

class EconomieMontagnarde(BaseModel):
    sous_descripteur: Literal['EconomieMontagnarde']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-116"
    descripteur: str = "économie montagnarde"

class ActionEconomique(BaseModel):
    sous_descripteur: Union['EconomieMontagnarde', 'AidePubliqueAuxEntreprises', 'AmenagementDuTerritoire', 'Planification', 'DeveloppementDurable', 'PoliceEconomique', 'LabelDeQualite', 'Prix', 'CoutDeLaVie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-148"
    descripteur: str = "action économique"

class CreationDentreprise(BaseModel):
    sous_descripteur: Literal['CreationDentreprise']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-938"
    descripteur: str = "création d'entreprise"

class SocieteDeconomieMixte(BaseModel):
    sous_descripteur: Literal['SocieteDeconomieMixte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-701"
    descripteur: str = "société d'économie mixte"

class EntreprisePublique(BaseModel):
    sous_descripteur: Literal['EntreprisePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-691"
    descripteur: str = "entreprise publique"

class EntrepriseIndustrielle(BaseModel):
    sous_descripteur: Literal['EntrepriseIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-550"
    descripteur: str = "entreprise industrielle"

class SocieteDeServices(BaseModel):
    sous_descripteur: Literal['SocieteDeServices']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-949"
    descripteur: str = "société de services"

class SocieteCommerciale(BaseModel):
    sous_descripteur: Union['SocieteDeServices', 'EntrepriseIndustrielle'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1190"
    descripteur: str = "société commerciale"

class Commereant(BaseModel):
    sous_descripteur: Literal['Commereant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-846"
    descripteur: str = "commerçant"

class CommereantEtranger(BaseModel):
    sous_descripteur: Literal['CommereantEtranger']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-521"
    descripteur: str = "commerçant étranger"

class Artisan(BaseModel):
    sous_descripteur: Literal['Artisan']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-810"
    descripteur: str = "artisan"

class ChefDentreprise(BaseModel):
    sous_descripteur: Union['Artisan', 'CommereantEtranger', 'Commereant'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1038"
    descripteur: str = "chef d'entreprise"

class SocieteCooperative(BaseModel):
    sous_descripteur: Literal['SocieteCooperative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-817"
    descripteur: str = "société coopérative"

class CommissaireAuxComptes(BaseModel):
    sous_descripteur: Literal['CommissaireAuxComptes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-445"
    descripteur: str = "commissaire aux comptes"

class ComptabiliteDentreprise(BaseModel):
    sous_descripteur: Union['CommissaireAuxComptes'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1294"
    descripteur: str = "comptabilité d'entreprise"

class BanqueMutualiste(BaseModel):
    sous_descripteur: Literal['BanqueMutualiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1386"
    descripteur: str = "banque mutualiste"

class Preteur(BaseModel):
    sous_descripteur: Literal['Preteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-622"
    descripteur: str = "prêteur"

class CaisseDepargne(BaseModel):
    sous_descripteur: Literal['CaisseDepargne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-263"
    descripteur: str = "caisse d'épargne"

class EtablissementDeCredit(BaseModel):
    sous_descripteur: Union['CaisseDepargne', 'Preteur', 'BanqueMutualiste'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-314"
    descripteur: str = "établissement de crédit"

class BauxCommerciaux(BaseModel):
    sous_descripteur: Literal['BauxCommerciaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-844"
    descripteur: str = "baux commerciaux"

class EtablissementArtisanal(BaseModel):
    sous_descripteur: Literal['EtablissementArtisanal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-596"
    descripteur: str = "établissement artisanal"

class MagasinCollectif(BaseModel):
    sous_descripteur: Literal['MagasinCollectif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-118"
    descripteur: str = "magasin collectif"

class FondsDeCommerce(BaseModel):
    sous_descripteur: Union['MagasinCollectif', 'EtablissementArtisanal', 'BauxCommerciaux'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1158"
    descripteur: str = "fonds de commerce"

class CompagnieDassurances(BaseModel):
    sous_descripteur: Literal['CompagnieDassurances']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-513"
    descripteur: str = "compagnie d'assurances"

class EntrepriseEnDifficulte(BaseModel):
    sous_descripteur: Literal['EntrepriseEnDifficulte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-724"
    descripteur: str = "entreprise en difficulté"

class SocieteCivileProfessionnelle(BaseModel):
    sous_descripteur: Literal['SocieteCivileProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-27"
    descripteur: str = "société civile professionnelle"

class Corporation(BaseModel):
    sous_descripteur: Literal['Corporation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1098"
    descripteur: str = "corporation"

class ChambreConsulaire(BaseModel):
    sous_descripteur: Literal['ChambreConsulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-776"
    descripteur: str = "chambre consulaire"

class DelegueConsulaire(BaseModel):
    sous_descripteur: Literal['DelegueConsulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-505"
    descripteur: str = "délégué consulaire"

class Compagnonnage(BaseModel):
    sous_descripteur: Literal['Compagnonnage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-23"
    descripteur: str = "compagnonnage"

class OrganisationProfessionnelle(BaseModel):
    sous_descripteur: Union['Compagnonnage', 'DelegueConsulaire', 'ChambreConsulaire', 'Corporation'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1025"
    descripteur: str = "organisation professionnelle"

class Entreprise(BaseModel):
    sous_descripteur: Union['OrganisationProfessionnelle', 'SocieteCivileProfessionnelle', 'EntrepriseEnDifficulte', 'CompagnieDassurances', 'FondsDeCommerce', 'EtablissementDeCredit', 'ComptabiliteDentreprise', 'SocieteCooperative', 'ChefDentreprise', 'SocieteCommerciale', 'EntreprisePublique', 'SocieteDeconomieMixte', 'CreationDentreprise'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-885"
    descripteur: str = "entreprise"

class DebitDeTabac(BaseModel):
    sous_descripteur: Literal['DebitDeTabac']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1384"
    descripteur: str = "débit de tabac"

class Soldes(BaseModel):
    sous_descripteur: Literal['Soldes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-947"
    descripteur: str = "soldes"

class VenteAuDeballage(BaseModel):
    sous_descripteur: Union['Soldes'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1101"
    descripteur: str = "vente au déballage"

class Brocanteur(BaseModel):
    sous_descripteur: Literal['Brocanteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1351"
    descripteur: str = "brocanteur"

class PubliciteMensongere(BaseModel):
    sous_descripteur: Literal['PubliciteMensongere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-711"
    descripteur: str = "publicité mensongère"

class FraudeCommerciale(BaseModel):
    sous_descripteur: Union['PubliciteMensongere'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-932"
    descripteur: str = "fraude commerciale"

class AgentDeChange(BaseModel):
    sous_descripteur: Literal['AgentDeChange']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-516"
    descripteur: str = "agent de change"

class Affichage(BaseModel):
    sous_descripteur: Literal['Affichage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-931"
    descripteur: str = "affichage"

class Publicite(BaseModel):
    sous_descripteur: Union['Affichage'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-490"
    descripteur: str = "publicité"

class VoyageurRepresentantPlacier(BaseModel):
    sous_descripteur: Literal['VoyageurRepresentantPlacier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-851"
    descripteur: str = "voyageur représentant placier"

class GrandeSurfaceCommerciale(BaseModel):
    sous_descripteur: Literal['GrandeSurfaceCommerciale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1155"
    descripteur: str = "grande surface commerciale"

class ManifestationCommerciale(BaseModel):
    sous_descripteur: Literal['ManifestationCommerciale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-470"
    descripteur: str = "manifestation commerciale"

class CommerceDeDetail(BaseModel):
    sous_descripteur: Literal['CommerceDeDetail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-431"
    descripteur: str = "commerce de détail"

class MarcheDinteretNational(BaseModel):
    sous_descripteur: Literal['MarcheDinteretNational']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-941"
    descripteur: str = "marché d'intérêt national"

class MarcheEnGros(BaseModel):
    sous_descripteur: Union['MarcheDinteretNational'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-785"
    descripteur: str = "marché en gros"

class CommerceExterieur(BaseModel):
    sous_descripteur: Literal['CommerceExterieur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-456"
    descripteur: str = "commerce extérieur"

class Colporteur(BaseModel):
    sous_descripteur: Literal['Colporteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1385"
    descripteur: str = "colporteur"

class MarchandForain(BaseModel):
    sous_descripteur: Literal['MarchandForain']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1078"
    descripteur: str = "marchand forain"

class MarcheDeDetail(BaseModel):
    sous_descripteur: Union['MarchandForain', 'Colporteur'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-274"
    descripteur: str = "marché de détail"

class AgentDassurances(BaseModel):
    sous_descripteur: Literal['AgentDassurances']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1363"
    descripteur: str = "agent d'assurances"

class EcoleDeConduite(BaseModel):
    sous_descripteur: Literal['EcoleDeConduite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1141"
    descripteur: str = "école de conduite"

class DetectivePrive(BaseModel):
    sous_descripteur: Literal['DetectivePrive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-733"
    descripteur: str = "détective privé"

class Coiffeur(BaseModel):
    sous_descripteur: Literal['Coiffeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-587"
    descripteur: str = "coiffeur"

class AgentDeSecurite(BaseModel):
    sous_descripteur: Literal['AgentDeSecurite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-248"
    descripteur: str = "agent de sécurité"

class Services(BaseModel):
    sous_descripteur: Union['AgentDeSecurite', 'Coiffeur', 'DetectivePrive', 'EcoleDeConduite', 'AgentDassurances'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-801"
    descripteur: str = "services"

class Epicerie(BaseModel):
    sous_descripteur: Literal['Epicerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1063"
    descripteur: str = "épicerie"

class Boulangerie(BaseModel):
    sous_descripteur: Literal['Boulangerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1178"
    descripteur: str = "boulangerie"

class Boucherie(BaseModel):
    sous_descripteur: Literal['Boucherie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-644"
    descripteur: str = "boucherie"

class DebitDeBoissons(BaseModel):
    sous_descripteur: Literal['DebitDeBoissons']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-826"
    descripteur: str = "débit de boissons"

class CommerceAlimentaire(BaseModel):
    sous_descripteur: Union['DebitDeBoissons', 'Boucherie', 'Boulangerie', 'Epicerie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-869"
    descripteur: str = "commerce alimentaire"

class CourtierDeMarchandises(BaseModel):
    sous_descripteur: Literal['CourtierDeMarchandises']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-220"
    descripteur: str = "courtier de marchandises"

class Poidsetmesures(BaseModel):
    sous_descripteur: Literal['Poidsetmesures']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-135"
    descripteur: str = "poids-et-mesures"

class Armurier(BaseModel):
    sous_descripteur: Literal['Armurier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-108"
    descripteur: str = "armurier"

class AssociationDeConsommateurs(BaseModel):
    sous_descripteur: Literal['AssociationDeConsommateurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-98"
    descripteur: str = "association de consommateurs"

class Consommation(BaseModel):
    sous_descripteur: Union['AssociationDeConsommateurs'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-581"
    descripteur: str = "consommation"

class Libraire(BaseModel):
    sous_descripteur: Literal['Libraire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-397"
    descripteur: str = "libraire"

class Editeur(BaseModel):
    sous_descripteur: Literal['Editeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1212"
    descripteur: str = "éditeur"

class Imprimeur(BaseModel):
    sous_descripteur: Literal['Imprimeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-752"
    descripteur: str = "imprimeur"

class MetiersDuLivre(BaseModel):
    sous_descripteur: Union['Imprimeur', 'Editeur', 'Libraire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-88"
    descripteur: str = "métiers du livre"

class MagasinGeneral(BaseModel):
    sous_descripteur: Literal['MagasinGeneral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-65"
    descripteur: str = "magasin général"

class VenteAuxEncheres(BaseModel):
    sous_descripteur: Literal['VenteAuxEncheres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-13"
    descripteur: str = "vente aux enchères"

class Commerce(BaseModel):
    sous_descripteur: Union['VenteAuxEncheres', 'MagasinGeneral', 'MetiersDuLivre', 'Consommation', 'Armurier', 'Poidsetmesures', 'CourtierDeMarchandises', 'CommerceAlimentaire', 'Services', 'MarcheDeDetail', 'CommerceExterieur', 'MarcheEnGros', 'CommerceDeDetail', 'ManifestationCommerciale', 'GrandeSurfaceCommerciale', 'VoyageurRepresentantPlacier', 'Publicite', 'AgentDeChange', 'FraudeCommerciale', 'Brocanteur', 'VenteAuDeballage', 'DebitDeTabac'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1248"
    descripteur: str = "commerce"

class Artisanat(BaseModel):
    sous_descripteur: Literal['Artisanat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1467"
    descripteur: str = "artisanat"

class Metallurgie(BaseModel):
    sous_descripteur: Literal['Metallurgie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-913"
    descripteur: str = "métallurgie"

class Poterie(BaseModel):
    sous_descripteur: Literal['Poterie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/0e632b89-9db1-4903-a388-358ba80de079"
    descripteur: str = "poterie"

class Pyrotechnie(BaseModel):
    sous_descripteur: Literal['Pyrotechnie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/389242ac-8cc8-4cd7-87f0-e722c00a7b9d"
    descripteur: str = "pyrotechnie"

class Tuilerie(BaseModel):
    sous_descripteur: Literal['Tuilerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/0f56930a-b6e1-4526-abf7-d6dc2044801a"
    descripteur: str = "tuilerie"

class Briqueterie(BaseModel):
    sous_descripteur: Literal['Briqueterie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/9ba975ce-cf1d-4296-b41c-56feb24b44c1"
    descripteur: str = "briqueterie"

class IndustrieDuFeu(BaseModel):
    sous_descripteur: Union['Briqueterie', 'Tuilerie', 'Pyrotechnie', 'Poterie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1267"
    descripteur: str = "industrie du feu"

class IndustrieDuVerre(BaseModel):
    sous_descripteur: Literal['IndustrieDuVerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-873"
    descripteur: str = "industrie du verre"

class IndustrieSpatiale(BaseModel):
    sous_descripteur: Literal['IndustrieSpatiale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1116"
    descripteur: str = "industrie spatiale"

class Manufacture(BaseModel):
    sous_descripteur: Literal['Manufacture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1402"
    descripteur: str = "manufacture"

class BatimentIndustriel(BaseModel):
    sous_descripteur: Union['Manufacture'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-315"
    descripteur: str = "bâtiment industriel"

class IndustrieChimique(BaseModel):
    sous_descripteur: Literal['IndustrieChimique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1145"
    descripteur: str = "industrie chimique"

class ConstructionAeronautique(BaseModel):
    sous_descripteur: Literal['ConstructionAeronautique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-272"
    descripteur: str = "construction aéronautique"

class ConstructionAutomobile(BaseModel):
    sous_descripteur: Literal['ConstructionAutomobile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1374"
    descripteur: str = "construction automobile"

class IndustrieMecanique(BaseModel):
    sous_descripteur: Union['ConstructionAutomobile', 'ConstructionAeronautique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-849"
    descripteur: str = "industrie mécanique"

class IndustrieAgroalimentaire(BaseModel):
    sous_descripteur: Literal['IndustrieAgroalimentaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-244"
    descripteur: str = "industrie agroalimentaire"

class GazNaturel(BaseModel):
    sous_descripteur: Literal['GazNaturel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1023"
    descripteur: str = "gaz naturel"

class Minerai(BaseModel):
    sous_descripteur: Literal['Minerai']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-268"
    descripteur: str = "minerai"

class Houille(BaseModel):
    sous_descripteur: Literal['Houille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-94"
    descripteur: str = "houille"

class Hydrocarbure(BaseModel):
    sous_descripteur: Literal['Hydrocarbure']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-647"
    descripteur: str = "hydrocarbure"

class MatierePremiere(BaseModel):
    sous_descripteur: Union['Hydrocarbure', 'Houille', 'Minerai', 'GazNaturel'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1326"
    descripteur: str = "matière première"

class ComposantElectronique(BaseModel):
    sous_descripteur: Literal['ComposantElectronique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-236"
    descripteur: str = "composant électronique"

class IndustrieElectronique(BaseModel):
    sous_descripteur: Union['ComposantElectronique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-81"
    descripteur: str = "industrie électronique"

class IndustrieTextile(BaseModel):
    sous_descripteur: Literal['IndustrieTextile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-203"
    descripteur: str = "industrie textile"

class ConstructionNavale(BaseModel):
    sous_descripteur: Literal['ConstructionNavale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-964"
    descripteur: str = "construction navale"

class IndustrieMaritime(BaseModel):
    sous_descripteur: Union['ConstructionNavale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-59"
    descripteur: str = "industrie maritime"

class ExploitationMiniere(BaseModel):
    sous_descripteur: Literal['ExploitationMiniere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1455"
    descripteur: str = "exploitation minière"

class ProspectionPetroliere(BaseModel):
    sous_descripteur: Literal['ProspectionPetroliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-535"
    descripteur: str = "prospection pétrolière"

class MineurDeFond(BaseModel):
    sous_descripteur: Literal['MineurDeFond']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1052"
    descripteur: str = "mineur de fond"

class RechercheMiniere(BaseModel):
    sous_descripteur: Literal['RechercheMiniere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-173"
    descripteur: str = "recherche minière"

class Carriere(BaseModel):
    sous_descripteur: Literal['Carriere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-19"
    descripteur: str = "carrière"

class IndustrieExtractive(BaseModel):
    sous_descripteur: Union['Carriere', 'RechercheMiniere', 'MineurDeFond', 'ProspectionPetroliere', 'ExploitationMiniere'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-481"
    descripteur: str = "industrie extractive"

class IndustrieDuCuir(BaseModel):
    sous_descripteur: Literal['IndustrieDuCuir']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-10"
    descripteur: str = "industrie du cuir"

class IndustriePapetiere(BaseModel):
    sous_descripteur: Literal['IndustriePapetiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-845"
    descripteur: str = "industrie papetière"

class IndustrieDuBois(BaseModel):
    sous_descripteur: Union['IndustriePapetiere'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-497"
    descripteur: str = "industrie du bois"

class Industrie(BaseModel):
    sous_descripteur: Union['IndustrieDuBois', 'IndustrieDuCuir', 'IndustrieExtractive', 'IndustrieMaritime', 'IndustrieTextile', 'IndustrieElectronique', 'MatierePremiere', 'IndustrieAgroalimentaire', 'IndustrieMecanique', 'IndustrieChimique', 'BatimentIndustriel', 'IndustrieSpatiale', 'IndustrieDuVerre', 'IndustrieDuFeu', 'Metallurgie', 'Artisanat'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-527"
    descripteur: str = "industrie"

class Economie(BaseModel):
    sous_descripteur: Union['Industrie', 'Commerce', 'Entreprise', 'ActionEconomique', 'Energie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-543"
    descripteur: str = "économie"
