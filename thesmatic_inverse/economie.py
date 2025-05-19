from pydantic import BaseModel
from typing import Union, Literal

class EconomieDenergie(BaseModel):
    terme_specifique: Literal['EconomieDenergie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-452"
    descripteur: str = "économie d'énergie"

class EnergieNucleaire(BaseModel):
    terme_specifique: Literal['EnergieNucleaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1373"
    descripteur: str = "énergie nucléaire"

class EnergieEolienne(BaseModel):
    terme_specifique: Literal['EnergieEolienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1355"
    descripteur: str = "énergie éolienne"

class EnergieDeLaMer(BaseModel):
    terme_specifique: Literal['EnergieDeLaMer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-973"
    descripteur: str = "énergie de la mer"

class EnergieSolaire(BaseModel):
    terme_specifique: Literal['EnergieSolaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-775"
    descripteur: str = "énergie solaire"

class EnergieHydraulique(BaseModel):
    terme_specifique: Literal['EnergieHydraulique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-430"
    descripteur: str = "énergie hydraulique"

class EnergieGeothermique(BaseModel):
    terme_specifique: Literal['EnergieGeothermique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-92"
    descripteur: str = "énergie géothermique"

class EnergieRenouvelable(BaseModel):
    terme_specifique: Union['EnergieGeothermique', 'EnergieHydraulique', 'EnergieSolaire', 'EnergieDeLaMer', 'EnergieEolienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1315"
    descripteur: str = "énergie renouvelable"

class Biocarburant(BaseModel):
    terme_specifique: Literal['Biocarburant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1019"
    descripteur: str = "bio-carburant"

class CentraleThermique(BaseModel):
    terme_specifique: Literal['CentraleThermique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1441"
    descripteur: str = "centrale thermique"

class BarrageHydroelectrique(BaseModel):
    terme_specifique: Literal['BarrageHydroelectrique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1089"
    descripteur: str = "barrage hydroélectrique"

class CentraleNucleaire(BaseModel):
    terme_specifique: Literal['CentraleNucleaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1443"
    descripteur: str = "centrale nucléaire"

class ProductionElectrique(BaseModel):
    terme_specifique: Union['CentraleNucleaire', 'BarrageHydroelectrique', 'CentraleThermique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-457"
    descripteur: str = "production électrique"

class Energie(BaseModel):
    terme_specifique: Union['ProductionElectrique', 'Biocarburant', 'EnergieRenouvelable', 'EnergieNucleaire', 'EconomieDenergie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-166"
    descripteur: str = "énergie"

class CoutDeLaVie(BaseModel):
    terme_specifique: Literal['CoutDeLaVie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1466"
    descripteur: str = "coût de la vie"

class Prix(BaseModel):
    terme_specifique: Literal['Prix']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-568"
    descripteur: str = "prix"

class LabelDeQualite(BaseModel):
    terme_specifique: Literal['LabelDeQualite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1234"
    descripteur: str = "label de qualité"

class Concentration(BaseModel):
    terme_specifique: Literal['Concentration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1024"
    descripteur: str = "concentration"

class Entente(BaseModel):
    terme_specifique: Literal['Entente']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1204"
    descripteur: str = "entente"

class PoliceEconomique(BaseModel):
    terme_specifique: Union['Entente', 'Concentration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-939"
    descripteur: str = "police économique"

class DeveloppementDurable(BaseModel):
    terme_specifique: Literal['DeveloppementDurable']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-511"
    descripteur: str = "développement durable"

class ContratDePlan(BaseModel):
    terme_specifique: Literal['ContratDePlan']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-187"
    descripteur: str = "contrat de plan"

class Planification(BaseModel):
    terme_specifique: Union['ContratDePlan']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-129"
    descripteur: str = "planification"

class ZoneIndustrielle(BaseModel):
    terme_specifique: Literal['ZoneIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1431"
    descripteur: str = "zone industrielle"

class PolitiqueDeLaVille(BaseModel):
    terme_specifique: Literal['PolitiqueDeLaVille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1192"
    descripteur: str = "politique de la ville"

class ZoneDactivites(BaseModel):
    terme_specifique: Literal['ZoneDactivites']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-961"
    descripteur: str = "zone d'activités"

class VilleNouvelle(BaseModel):
    terme_specifique: Literal['VilleNouvelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1446"
    descripteur: str = "ville nouvelle"

class DecentralisationIndustrielle(BaseModel):
    terme_specifique: Literal['DecentralisationIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-182"
    descripteur: str = "décentralisation industrielle"

class PolitiqueDeLaMontagne(BaseModel):
    terme_specifique: Literal['PolitiqueDeLaMontagne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-52"
    descripteur: str = "politique de la montagne"

class AmenagementDuLittoral(BaseModel):
    terme_specifique: Literal['AmenagementDuLittoral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-399"
    descripteur: str = "aménagement du littoral"

class AmenagementDuTerritoire(BaseModel):
    terme_specifique: Union['AmenagementDuLittoral', 'PolitiqueDeLaMontagne', 'DecentralisationIndustrielle', 'VilleNouvelle', 'ZoneDactivites', 'PolitiqueDeLaVille', 'ZoneIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-554"
    descripteur: str = "aménagement du territoire"

class AidePubliqueAuxEntreprises(BaseModel):
    terme_specifique: Literal['AidePubliqueAuxEntreprises']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-920"
    descripteur: str = "aide publique aux entreprises"

class EconomieMontagnarde(BaseModel):
    terme_specifique: Literal['EconomieMontagnarde']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-116"
    descripteur: str = "économie montagnarde"

class ActionEconomique(BaseModel):
    terme_specifique: Union['EconomieMontagnarde', 'AidePubliqueAuxEntreprises', 'AmenagementDuTerritoire', 'Planification', 'DeveloppementDurable', 'PoliceEconomique', 'LabelDeQualite', 'Prix', 'CoutDeLaVie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-148"
    descripteur: str = "action économique"

class CreationDentreprise(BaseModel):
    terme_specifique: Literal['CreationDentreprise']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-938"
    descripteur: str = "création d'entreprise"

class SocieteDeconomieMixte(BaseModel):
    terme_specifique: Literal['SocieteDeconomieMixte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-701"
    descripteur: str = "société d'économie mixte"

class EntreprisePublique(BaseModel):
    terme_specifique: Literal['EntreprisePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-691"
    descripteur: str = "entreprise publique"

class EntrepriseIndustrielle(BaseModel):
    terme_specifique: Literal['EntrepriseIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-550"
    descripteur: str = "entreprise industrielle"

class SocieteDeServices(BaseModel):
    terme_specifique: Literal['SocieteDeServices']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-949"
    descripteur: str = "société de services"

class SocieteCommerciale(BaseModel):
    terme_specifique: Union['SocieteDeServices', 'EntrepriseIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1190"
    descripteur: str = "société commerciale"

class Commereant(BaseModel):
    terme_specifique: Literal['Commereant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-846"
    descripteur: str = "commerçant"

class CommereantEtranger(BaseModel):
    terme_specifique: Literal['CommereantEtranger']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-521"
    descripteur: str = "commerçant étranger"

class Artisan(BaseModel):
    terme_specifique: Literal['Artisan']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-810"
    descripteur: str = "artisan"

class ChefDentreprise(BaseModel):
    terme_specifique: Union['Artisan', 'CommereantEtranger', 'Commereant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1038"
    descripteur: str = "chef d'entreprise"

class SocieteCooperative(BaseModel):
    terme_specifique: Literal['SocieteCooperative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-817"
    descripteur: str = "société coopérative"

class CommissaireAuxComptes(BaseModel):
    terme_specifique: Literal['CommissaireAuxComptes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-445"
    descripteur: str = "commissaire aux comptes"

class ComptabiliteDentreprise(BaseModel):
    terme_specifique: Union['CommissaireAuxComptes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1294"
    descripteur: str = "comptabilité d'entreprise"

class BanqueMutualiste(BaseModel):
    terme_specifique: Literal['BanqueMutualiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1386"
    descripteur: str = "banque mutualiste"

class Preteur(BaseModel):
    terme_specifique: Literal['Preteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-622"
    descripteur: str = "prêteur"

class CaisseDepargne(BaseModel):
    terme_specifique: Literal['CaisseDepargne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-263"
    descripteur: str = "caisse d'épargne"

class EtablissementDeCredit(BaseModel):
    terme_specifique: Union['CaisseDepargne', 'Preteur', 'BanqueMutualiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-314"
    descripteur: str = "établissement de crédit"

class BauxCommerciaux(BaseModel):
    terme_specifique: Literal['BauxCommerciaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-844"
    descripteur: str = "baux commerciaux"

class EtablissementArtisanal(BaseModel):
    terme_specifique: Literal['EtablissementArtisanal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-596"
    descripteur: str = "établissement artisanal"

class MagasinCollectif(BaseModel):
    terme_specifique: Literal['MagasinCollectif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-118"
    descripteur: str = "magasin collectif"

class FondsDeCommerce(BaseModel):
    terme_specifique: Union['MagasinCollectif', 'EtablissementArtisanal', 'BauxCommerciaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1158"
    descripteur: str = "fonds de commerce"

class CompagnieDassurances(BaseModel):
    terme_specifique: Literal['CompagnieDassurances']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-513"
    descripteur: str = "compagnie d'assurances"

class EntrepriseEnDifficulte(BaseModel):
    terme_specifique: Literal['EntrepriseEnDifficulte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-724"
    descripteur: str = "entreprise en difficulté"

class SocieteCivileProfessionnelle(BaseModel):
    terme_specifique: Literal['SocieteCivileProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-27"
    descripteur: str = "société civile professionnelle"

class Corporation(BaseModel):
    terme_specifique: Literal['Corporation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1098"
    descripteur: str = "corporation"

class ChambreConsulaire(BaseModel):
    terme_specifique: Literal['ChambreConsulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-776"
    descripteur: str = "chambre consulaire"

class DelegueConsulaire(BaseModel):
    terme_specifique: Literal['DelegueConsulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-505"
    descripteur: str = "délégué consulaire"

class Compagnonnage(BaseModel):
    terme_specifique: Literal['Compagnonnage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-23"
    descripteur: str = "compagnonnage"

class OrganisationProfessionnelle(BaseModel):
    terme_specifique: Union['Compagnonnage', 'DelegueConsulaire', 'ChambreConsulaire', 'Corporation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1025"
    descripteur: str = "organisation professionnelle"

class Entreprise(BaseModel):
    terme_specifique: Union['OrganisationProfessionnelle', 'SocieteCivileProfessionnelle', 'EntrepriseEnDifficulte', 'CompagnieDassurances', 'FondsDeCommerce', 'EtablissementDeCredit', 'ComptabiliteDentreprise', 'SocieteCooperative', 'ChefDentreprise', 'SocieteCommerciale', 'EntreprisePublique', 'SocieteDeconomieMixte', 'CreationDentreprise']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-885"
    descripteur: str = "entreprise"

class DebitDeTabac(BaseModel):
    terme_specifique: Literal['DebitDeTabac']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1384"
    descripteur: str = "débit de tabac"

class Soldes(BaseModel):
    terme_specifique: Literal['Soldes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-947"
    descripteur: str = "soldes"

class VenteAuDeballage(BaseModel):
    terme_specifique: Union['Soldes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1101"
    descripteur: str = "vente au déballage"

class Brocanteur(BaseModel):
    terme_specifique: Literal['Brocanteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1351"
    descripteur: str = "brocanteur"

class PubliciteMensongere(BaseModel):
    terme_specifique: Literal['PubliciteMensongere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-711"
    descripteur: str = "publicité mensongère"

class FraudeCommerciale(BaseModel):
    terme_specifique: Union['PubliciteMensongere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-932"
    descripteur: str = "fraude commerciale"

class AgentDeChange(BaseModel):
    terme_specifique: Literal['AgentDeChange']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-516"
    descripteur: str = "agent de change"

class Affichage(BaseModel):
    terme_specifique: Literal['Affichage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-931"
    descripteur: str = "affichage"

class Publicite(BaseModel):
    terme_specifique: Union['Affichage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-490"
    descripteur: str = "publicité"

class VoyageurRepresentantPlacier(BaseModel):
    terme_specifique: Literal['VoyageurRepresentantPlacier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-851"
    descripteur: str = "voyageur représentant placier"

class GrandeSurfaceCommerciale(BaseModel):
    terme_specifique: Literal['GrandeSurfaceCommerciale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1155"
    descripteur: str = "grande surface commerciale"

class ManifestationCommerciale(BaseModel):
    terme_specifique: Literal['ManifestationCommerciale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-470"
    descripteur: str = "manifestation commerciale"

class CommerceDeDetail(BaseModel):
    terme_specifique: Literal['CommerceDeDetail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-431"
    descripteur: str = "commerce de détail"

class MarcheDinteretNational(BaseModel):
    terme_specifique: Literal['MarcheDinteretNational']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-941"
    descripteur: str = "marché d'intérêt national"

class MarcheEnGros(BaseModel):
    terme_specifique: Union['MarcheDinteretNational']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-785"
    descripteur: str = "marché en gros"

class CommerceExterieur(BaseModel):
    terme_specifique: Literal['CommerceExterieur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-456"
    descripteur: str = "commerce extérieur"

class Colporteur(BaseModel):
    terme_specifique: Literal['Colporteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1385"
    descripteur: str = "colporteur"

class MarchandForain(BaseModel):
    terme_specifique: Literal['MarchandForain']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1078"
    descripteur: str = "marchand forain"

class MarcheDeDetail(BaseModel):
    terme_specifique: Union['MarchandForain', 'Colporteur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-274"
    descripteur: str = "marché de détail"

class AgentDassurances(BaseModel):
    terme_specifique: Literal['AgentDassurances']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1363"
    descripteur: str = "agent d'assurances"

class EcoleDeConduite(BaseModel):
    terme_specifique: Literal['EcoleDeConduite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1141"
    descripteur: str = "école de conduite"

class DetectivePrive(BaseModel):
    terme_specifique: Literal['DetectivePrive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-733"
    descripteur: str = "détective privé"

class Coiffeur(BaseModel):
    terme_specifique: Literal['Coiffeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-587"
    descripteur: str = "coiffeur"

class AgentDeSecurite(BaseModel):
    terme_specifique: Literal['AgentDeSecurite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-248"
    descripteur: str = "agent de sécurité"

class Services(BaseModel):
    terme_specifique: Union['AgentDeSecurite', 'Coiffeur', 'DetectivePrive', 'EcoleDeConduite', 'AgentDassurances']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-801"
    descripteur: str = "services"

class Epicerie(BaseModel):
    terme_specifique: Literal['Epicerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1063"
    descripteur: str = "épicerie"

class Boulangerie(BaseModel):
    terme_specifique: Literal['Boulangerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1178"
    descripteur: str = "boulangerie"

class Boucherie(BaseModel):
    terme_specifique: Literal['Boucherie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-644"
    descripteur: str = "boucherie"

class DebitDeBoissons(BaseModel):
    terme_specifique: Literal['DebitDeBoissons']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-826"
    descripteur: str = "débit de boissons"

class CommerceAlimentaire(BaseModel):
    terme_specifique: Union['DebitDeBoissons', 'Boucherie', 'Boulangerie', 'Epicerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-869"
    descripteur: str = "commerce alimentaire"

class CourtierDeMarchandises(BaseModel):
    terme_specifique: Literal['CourtierDeMarchandises']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-220"
    descripteur: str = "courtier de marchandises"

class Poidsetmesures(BaseModel):
    terme_specifique: Literal['Poidsetmesures']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-135"
    descripteur: str = "poids-et-mesures"

class Armurier(BaseModel):
    terme_specifique: Literal['Armurier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-108"
    descripteur: str = "armurier"

class AssociationDeConsommateurs(BaseModel):
    terme_specifique: Literal['AssociationDeConsommateurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-98"
    descripteur: str = "association de consommateurs"

class Consommation(BaseModel):
    terme_specifique: Union['AssociationDeConsommateurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-581"
    descripteur: str = "consommation"

class Libraire(BaseModel):
    terme_specifique: Literal['Libraire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-397"
    descripteur: str = "libraire"

class Editeur(BaseModel):
    terme_specifique: Literal['Editeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1212"
    descripteur: str = "éditeur"

class Imprimeur(BaseModel):
    terme_specifique: Literal['Imprimeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-752"
    descripteur: str = "imprimeur"

class MetiersDuLivre(BaseModel):
    terme_specifique: Union['Imprimeur', 'Editeur', 'Libraire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-88"
    descripteur: str = "métiers du livre"

class MagasinGeneral(BaseModel):
    terme_specifique: Literal['MagasinGeneral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-65"
    descripteur: str = "magasin général"

class VenteAuxEncheres(BaseModel):
    terme_specifique: Literal['VenteAuxEncheres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-13"
    descripteur: str = "vente aux enchères"

class Commerce(BaseModel):
    terme_specifique: Union['VenteAuxEncheres', 'MagasinGeneral', 'MetiersDuLivre', 'Consommation', 'Armurier', 'Poidsetmesures', 'CourtierDeMarchandises', 'CommerceAlimentaire', 'Services', 'MarcheDeDetail', 'CommerceExterieur', 'MarcheEnGros', 'CommerceDeDetail', 'ManifestationCommerciale', 'GrandeSurfaceCommerciale', 'VoyageurRepresentantPlacier', 'Publicite', 'AgentDeChange', 'FraudeCommerciale', 'Brocanteur', 'VenteAuDeballage', 'DebitDeTabac']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1248"
    descripteur: str = "commerce"

class Artisanat(BaseModel):
    terme_specifique: Literal['Artisanat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1467"
    descripteur: str = "artisanat"

class Metallurgie(BaseModel):
    terme_specifique: Literal['Metallurgie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-913"
    descripteur: str = "métallurgie"

class Poterie(BaseModel):
    terme_specifique: Literal['Poterie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/0e632b89-9db1-4903-a388-358ba80de079"
    descripteur: str = "poterie"

class Pyrotechnie(BaseModel):
    terme_specifique: Literal['Pyrotechnie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/389242ac-8cc8-4cd7-87f0-e722c00a7b9d"
    descripteur: str = "pyrotechnie"

class Tuilerie(BaseModel):
    terme_specifique: Literal['Tuilerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/0f56930a-b6e1-4526-abf7-d6dc2044801a"
    descripteur: str = "tuilerie"

class Briqueterie(BaseModel):
    terme_specifique: Literal['Briqueterie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/9ba975ce-cf1d-4296-b41c-56feb24b44c1"
    descripteur: str = "briqueterie"

class IndustrieDuFeu(BaseModel):
    terme_specifique: Union['Briqueterie', 'Tuilerie', 'Pyrotechnie', 'Poterie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1267"
    descripteur: str = "industrie du feu"

class IndustrieDuVerre(BaseModel):
    terme_specifique: Literal['IndustrieDuVerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-873"
    descripteur: str = "industrie du verre"

class IndustrieSpatiale(BaseModel):
    terme_specifique: Literal['IndustrieSpatiale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1116"
    descripteur: str = "industrie spatiale"

class Manufacture(BaseModel):
    terme_specifique: Literal['Manufacture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1402"
    descripteur: str = "manufacture"

class BatimentIndustriel(BaseModel):
    terme_specifique: Union['Manufacture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-315"
    descripteur: str = "bâtiment industriel"

class IndustrieChimique(BaseModel):
    terme_specifique: Literal['IndustrieChimique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1145"
    descripteur: str = "industrie chimique"

class ConstructionAeronautique(BaseModel):
    terme_specifique: Literal['ConstructionAeronautique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-272"
    descripteur: str = "construction aéronautique"

class ConstructionAutomobile(BaseModel):
    terme_specifique: Literal['ConstructionAutomobile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1374"
    descripteur: str = "construction automobile"

class IndustrieMecanique(BaseModel):
    terme_specifique: Union['ConstructionAutomobile', 'ConstructionAeronautique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-849"
    descripteur: str = "industrie mécanique"

class IndustrieAgroalimentaire(BaseModel):
    terme_specifique: Literal['IndustrieAgroalimentaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-244"
    descripteur: str = "industrie agroalimentaire"

class GazNaturel(BaseModel):
    terme_specifique: Literal['GazNaturel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1023"
    descripteur: str = "gaz naturel"

class Minerai(BaseModel):
    terme_specifique: Literal['Minerai']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-268"
    descripteur: str = "minerai"

class Houille(BaseModel):
    terme_specifique: Literal['Houille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-94"
    descripteur: str = "houille"

class Hydrocarbure(BaseModel):
    terme_specifique: Literal['Hydrocarbure']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-647"
    descripteur: str = "hydrocarbure"

class MatierePremiere(BaseModel):
    terme_specifique: Union['Hydrocarbure', 'Houille', 'Minerai', 'GazNaturel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1326"
    descripteur: str = "matière première"

class ComposantElectronique(BaseModel):
    terme_specifique: Literal['ComposantElectronique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-236"
    descripteur: str = "composant électronique"

class IndustrieElectronique(BaseModel):
    terme_specifique: Union['ComposantElectronique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-81"
    descripteur: str = "industrie électronique"

class IndustrieTextile(BaseModel):
    terme_specifique: Literal['IndustrieTextile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-203"
    descripteur: str = "industrie textile"

class ConstructionNavale(BaseModel):
    terme_specifique: Literal['ConstructionNavale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-964"
    descripteur: str = "construction navale"

class IndustrieMaritime(BaseModel):
    terme_specifique: Union['ConstructionNavale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-59"
    descripteur: str = "industrie maritime"

class ExploitationMiniere(BaseModel):
    terme_specifique: Literal['ExploitationMiniere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1455"
    descripteur: str = "exploitation minière"

class ProspectionPetroliere(BaseModel):
    terme_specifique: Literal['ProspectionPetroliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-535"
    descripteur: str = "prospection pétrolière"

class MineurDeFond(BaseModel):
    terme_specifique: Literal['MineurDeFond']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1052"
    descripteur: str = "mineur de fond"

class RechercheMiniere(BaseModel):
    terme_specifique: Literal['RechercheMiniere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-173"
    descripteur: str = "recherche minière"

class Carriere(BaseModel):
    terme_specifique: Literal['Carriere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-19"
    descripteur: str = "carrière"

class IndustrieExtractive(BaseModel):
    terme_specifique: Union['Carriere', 'RechercheMiniere', 'MineurDeFond', 'ProspectionPetroliere', 'ExploitationMiniere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-481"
    descripteur: str = "industrie extractive"

class IndustrieDuCuir(BaseModel):
    terme_specifique: Literal['IndustrieDuCuir']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-10"
    descripteur: str = "industrie du cuir"

class IndustriePapetiere(BaseModel):
    terme_specifique: Literal['IndustriePapetiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-845"
    descripteur: str = "industrie papetière"

class IndustrieDuBois(BaseModel):
    terme_specifique: Union['IndustriePapetiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-497"
    descripteur: str = "industrie du bois"

class Industrie(BaseModel):
    terme_specifique: Union['IndustrieDuBois', 'IndustrieDuCuir', 'IndustrieExtractive', 'IndustrieMaritime', 'IndustrieTextile', 'IndustrieElectronique', 'MatierePremiere', 'IndustrieAgroalimentaire', 'IndustrieMecanique', 'IndustrieChimique', 'BatimentIndustriel', 'IndustrieSpatiale', 'IndustrieDuVerre', 'IndustrieDuFeu', 'Metallurgie', 'Artisanat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-527"
    descripteur: str = "industrie"

class Economie(BaseModel):
    terme_specifique: Union['Industrie', 'Commerce', 'Entreprise', 'ActionEconomique', 'Energie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-543"
    descripteur: str = "économie"
