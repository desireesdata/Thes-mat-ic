from pydantic import BaseModel
from typing import Union, Literal

class Alcoolique(BaseModel):
    terme_specifique: Literal['Alcoolique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-412"
    descripteur: str = "alcoolique"

class HygieneSociale(BaseModel):
    terme_specifique: Union['Alcoolique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1163"
    descripteur: str = "hygiène sociale"

class ProduitCosmetique(BaseModel):
    terme_specifique: Literal['ProduitCosmetique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-728"
    descripteur: str = "produit cosmétique"

class SubstanceVeneneuse(BaseModel):
    terme_specifique: Literal['SubstanceVeneneuse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1028"
    descripteur: str = "substance vénéneuse"

class SpecialitePharmaceutique(BaseModel):
    terme_specifique: Literal['SpecialitePharmaceutique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-625"
    descripteur: str = "spécialité pharmaceutique"

class OfficinePharmaceutique(BaseModel):
    terme_specifique: Literal['OfficinePharmaceutique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1010"
    descripteur: str = "officine pharmaceutique"

class Pharmacie(BaseModel):
    terme_specifique: Union['OfficinePharmaceutique', 'SpecialitePharmaceutique', 'SubstanceVeneneuse', 'ProduitCosmetique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-337"
    descripteur: str = "pharmacie"

class LaboratoireDanalyse(BaseModel):
    terme_specifique: Literal['LaboratoireDanalyse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1265"
    descripteur: str = "laboratoire d'analyse"

class Vaccination(BaseModel):
    terme_specifique: Literal['Vaccination']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1085"
    descripteur: str = "vaccination"

class InstallationRadiologique(BaseModel):
    terme_specifique: Literal['InstallationRadiologique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-730"
    descripteur: str = "installation radiologique"

class TransfusionSanguine(BaseModel):
    terme_specifique: Literal['TransfusionSanguine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-279"
    descripteur: str = "transfusion sanguine"

class EtablissementMedicoSocial(BaseModel):
    terme_specifique: Literal['EtablissementMedicoSocial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-355"
    descripteur: str = "établissement médico social"

class TransportSanitaire(BaseModel):
    terme_specifique: Literal['TransportSanitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-635"
    descripteur: str = "transport sanitaire"

class OrganisationSanitaire(BaseModel):
    terme_specifique: Union['TransportSanitaire', 'EtablissementMedicoSocial', 'TransfusionSanguine', 'InstallationRadiologique', 'Vaccination', 'LaboratoireDanalyse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1423"
    descripteur: str = "organisation sanitaire"

class SoinsMedicaux(BaseModel):
    terme_specifique: Literal['SoinsMedicaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1498"
    descripteur: str = "soins médicaux"

class Sida(BaseModel):
    terme_specifique: Literal['Sida']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1308"
    descripteur: str = "sida"

class Toxicomanie(BaseModel):
    terme_specifique: Literal['Toxicomanie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1189"
    descripteur: str = "toxicomanie"

class Tabagisme(BaseModel):
    terme_specifique: Literal['Tabagisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-984"
    descripteur: str = "tabagisme"

class Alcoolisme(BaseModel):
    terme_specifique: Literal['Alcoolisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1270"
    descripteur: str = "alcoolisme"

class MaladieADeclarationObligatoire(BaseModel):
    terme_specifique: Literal['MaladieADeclarationObligatoire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-797"
    descripteur: str = "maladie à déclaration obligatoire"

class MaladieMentale(BaseModel):
    terme_specifique: Literal['MaladieMentale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-732"
    descripteur: str = "maladie mentale"

class Tuberculose(BaseModel):
    terme_specifique: Literal['Tuberculose']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-700"
    descripteur: str = "tuberculose"

class Epidemie(BaseModel):
    terme_specifique: Literal['Epidemie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-501"
    descripteur: str = "épidémie"

class Lepre(BaseModel):
    terme_specifique: Literal['Lepre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-322"
    descripteur: str = "lèpre"

class MaladieSexuellementTransmissible(BaseModel):
    terme_specifique: Literal['MaladieSexuellementTransmissible']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-214"
    descripteur: str = "maladie sexuellement transmissible"

class Cancer(BaseModel):
    terme_specifique: Literal['Cancer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-152"
    descripteur: str = "cancer"

class ActionSanitaire(BaseModel):
    terme_specifique: Union['Cancer', 'MaladieSexuellementTransmissible', 'Lepre', 'Epidemie', 'Tuberculose', 'MaladieMentale', 'MaladieADeclarationObligatoire', 'Alcoolisme', 'Tabagisme', 'Toxicomanie', 'Sida', 'SoinsMedicaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1319"
    descripteur: str = "action sanitaire"

class Accouchement(BaseModel):
    terme_specifique: Literal['Accouchement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-978"
    descripteur: str = "accouchement"

class Contraception(BaseModel):
    terme_specifique: Literal['Contraception']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-972"
    descripteur: str = "contraception"

class InterruptionVolontaireDeGrossesse(BaseModel):
    terme_specifique: Literal['InterruptionVolontaireDeGrossesse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-916"
    descripteur: str = "interruption volontaire de grossesse"

class MortaliteInfantile(BaseModel):
    terme_specifique: Literal['MortaliteInfantile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-541"
    descripteur: str = "mortalité infantile"

class AssistanteMaternelle(BaseModel):
    terme_specifique: Literal['AssistanteMaternelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1307"
    descripteur: str = "assistante maternelle"

class Creche(BaseModel):
    terme_specifique: Literal['Creche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-190"
    descripteur: str = "crèche"

class HalteGarderie(BaseModel):
    terme_specifique: Literal['HalteGarderie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-180"
    descripteur: str = "halte garderie"

class Puericultrice(BaseModel):
    terme_specifique: Literal['Puericultrice']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-134"
    descripteur: str = "puéricultrice"

class ProtectionMaternelleEtInfantile(BaseModel):
    terme_specifique: Union['Puericultrice', 'HalteGarderie', 'Creche', 'AssistanteMaternelle', 'MortaliteInfantile', 'InterruptionVolontaireDeGrossesse', 'Contraception', 'Accouchement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1094"
    descripteur: str = "protection maternelle et infantile"

class Hoteldieu(BaseModel):
    terme_specifique: Literal['Hoteldieu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1499"
    descripteur: str = "hôtel-dieu"

class EquipementMedicoChirurgical(BaseModel):
    terme_specifique: Literal['EquipementMedicoChirurgical']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-560"
    descripteur: str = "équipement médico chirurgical"

class Sanatorium(BaseModel):
    terme_specifique: Literal['Sanatorium']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-894"
    descripteur: str = "sanatorium"

class EtablissementPublicDhospitalisation(BaseModel):
    terme_specifique: Literal['EtablissementPublicDhospitalisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-329"
    descripteur: str = "établissement public d'hospitalisation"

class HopitalPsychiatrique(BaseModel):
    terme_specifique: Literal['HopitalPsychiatrique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1062"
    descripteur: str = "hôpital psychiatrique"

class Leproserie(BaseModel):
    terme_specifique: Literal['Leproserie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1263"
    descripteur: str = "léproserie"

class EtablissementSanitairePrive(BaseModel):
    terme_specifique: Literal['EtablissementSanitairePrive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1457"
    descripteur: str = "établissement sanitaire privé"

class PopulationHospitaliere(BaseModel):
    terme_specifique: Literal['PopulationHospitaliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-492"
    descripteur: str = "population hospitalière"

class ConstructionHospitaliere(BaseModel):
    terme_specifique: Literal['ConstructionHospitaliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-950"
    descripteur: str = "construction hospitalière"

class EtablissementDeSante(BaseModel):
    terme_specifique: Union['ConstructionHospitaliere', 'PopulationHospitaliere', 'EtablissementSanitairePrive', 'Leproserie', 'HopitalPsychiatrique', 'EtablissementPublicDhospitalisation', 'Sanatorium', 'EquipementMedicoChirurgical', 'Hoteldieu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-185"
    descripteur: str = "établissement de santé"

class SageFemme(BaseModel):
    terme_specifique: Literal['SageFemme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-806"
    descripteur: str = "sage femme"

class AuxiliaireMedical(BaseModel):
    terme_specifique: Literal['AuxiliaireMedical']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1032"
    descripteur: str = "auxiliaire médical"

class Pharmacien(BaseModel):
    terme_specifique: Literal['Pharmacien']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-365"
    descripteur: str = "pharmacien"

class ChirurgienDentiste(BaseModel):
    terme_specifique: Literal['ChirurgienDentiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-259"
    descripteur: str = "chirurgien dentiste"

class Medecin(BaseModel):
    terme_specifique: Literal['Medecin']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-89"
    descripteur: str = "médecin"

class MedecinHospitalier(BaseModel):
    terme_specifique: Literal['MedecinHospitalier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-777"
    descripteur: str = "médecin hospitalier"

class ProfessionMedicale(BaseModel):
    terme_specifique: Union['MedecinHospitalier', 'Medecin', 'ChirurgienDentiste', 'Pharmacien', 'AuxiliaireMedical', 'SageFemme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-672"
    descripteur: str = "profession médicale"

class Desinfection(BaseModel):
    terme_specifique: Literal['Desinfection']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-956"
    descripteur: str = "désinfection"

class Amiante(BaseModel):
    terme_specifique: Literal['Amiante']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-343"
    descripteur: str = "amiante"

class HygieneAlimentaire(BaseModel):
    terme_specifique: Literal['HygieneAlimentaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-565"
    descripteur: str = "hygiène alimentaire"

class Hygiene(BaseModel):
    terme_specifique: Union['HygieneAlimentaire', 'Amiante', 'Desinfection']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-748"
    descripteur: str = "hygiène"

class Thermoclimatisme(BaseModel):
    terme_specifique: Literal['Thermoclimatisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1268"
    descripteur: str = "thermoclimatisme"

class Sante(BaseModel):
    terme_specifique: Union['Thermoclimatisme', 'Hygiene', 'ProfessionMedicale', 'EtablissementDeSante', 'ProtectionMaternelleEtInfantile', 'ActionSanitaire', 'OrganisationSanitaire', 'Pharmacie', 'HygieneSociale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-344"
    descripteur: str = "santé"

class RestaurationCollective(BaseModel):
    terme_specifique: Literal['RestaurationCollective']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1479"
    descripteur: str = "restauration collective"

class EntrepriseDeTravailTemporaire(BaseModel):
    terme_specifique: Literal['EntrepriseDeTravailTemporaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1233"
    descripteur: str = "entreprise de travail temporaire"

class SyndicatProfessionnel(BaseModel):
    terme_specifique: Literal['SyndicatProfessionnel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-258"
    descripteur: str = "syndicat professionnel"

class ComiteDentreprise(BaseModel):
    terme_specifique: Literal['ComiteDentreprise']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1208"
    descripteur: str = "comité d'entreprise"

class DelegueDuPersonnel(BaseModel):
    terme_specifique: Literal['DelegueDuPersonnel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-650"
    descripteur: str = "délégué du personnel"

class ConflitDuTravail(BaseModel):
    terme_specifique: Literal['ConflitDuTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-886"
    descripteur: str = "conflit du travail"

class RelationsDuTravail(BaseModel):
    terme_specifique: Union['ConflitDuTravail', 'DelegueDuPersonnel', 'ComiteDentreprise', 'SyndicatProfessionnel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-847"
    descripteur: str = "relations du travail"

class TravailleurADomicile(BaseModel):
    terme_specifique: Literal['TravailleurADomicile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-907"
    descripteur: str = "travailleur à domicile"

class Concierge(BaseModel):
    terme_specifique: Literal['Concierge']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-517"
    descripteur: str = "concierge"

class EmployeDeMaison(BaseModel):
    terme_specifique: Literal['EmployeDeMaison']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-210"
    descripteur: str = "employé de maison"

class ProfessionParticuliere(BaseModel):
    terme_specifique: Union['EmployeDeMaison', 'Concierge', 'TravailleurADomicile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-480"
    descripteur: str = "profession particulière"

class AccidentDuTravail(BaseModel):
    terme_specifique: Literal['AccidentDuTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-682"
    descripteur: str = "accident du travail"

class MedecineDuTravail(BaseModel):
    terme_specifique: Literal['MedecineDuTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-841"
    descripteur: str = "médecine du travail"

class MaladieProfessionnelle(BaseModel):
    terme_specifique: Literal['MaladieProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-500"
    descripteur: str = "maladie professionnelle"

class MachineDangereuse(BaseModel):
    terme_specifique: Literal['MachineDangereuse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-176"
    descripteur: str = "machine dangereuse"

class SecuriteDuTravail(BaseModel):
    terme_specifique: Union['MachineDangereuse', 'MaladieProfessionnelle', 'MedecineDuTravail', 'AccidentDuTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1264"
    descripteur: str = "sécurité du travail"

class InteressementDesTravailleurs(BaseModel):
    terme_specifique: Literal['InteressementDesTravailleurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-111"
    descripteur: str = "intéressement des travailleurs"

class Ouvrier(BaseModel):
    terme_specifique: Literal['Ouvrier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-127"
    descripteur: str = "ouvrier"

class TravailDesEnfants(BaseModel):
    terme_specifique: Literal['TravailDesEnfants']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1100"
    descripteur: str = "travail des enfants"

class HoraireDeTravail(BaseModel):
    terme_specifique: Literal['HoraireDeTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-898"
    descripteur: str = "horaire de travail"

class TravailDeNuit(BaseModel):
    terme_specifique: Literal['TravailDeNuit']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1140"
    descripteur: str = "travail de nuit"

class CongesPayes(BaseModel):
    terme_specifique: Literal['CongesPayes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-405"
    descripteur: str = "congés payés"

class Remuneration(BaseModel):
    terme_specifique: Literal['Remuneration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-374"
    descripteur: str = "rémunération"

class ReposHebdomadaire(BaseModel):
    terme_specifique: Literal['ReposHebdomadaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-161"
    descripteur: str = "repos hebdomadaire"

class DureeDuTravail(BaseModel):
    terme_specifique: Literal['DureeDuTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-4"
    descripteur: str = "durée du travail"

class ConditionsDuTravail(BaseModel):
    terme_specifique: Union['DureeDuTravail', 'ReposHebdomadaire', 'Remuneration', 'CongesPayes', 'TravailDeNuit', 'HoraireDeTravail', 'TravailDesEnfants']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-861"
    descripteur: str = "conditions du travail"

class Travail(BaseModel):
    terme_specifique: Union['ConditionsDuTravail', 'Ouvrier', 'InteressementDesTravailleurs', 'SecuriteDuTravail', 'ProfessionParticuliere', 'RelationsDuTravail', 'EntrepriseDeTravailTemporaire', 'RestaurationCollective']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-536"
    descripteur: str = "travail"

class Dette(BaseModel):
    terme_specifique: Literal['Dette']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1030"
    descripteur: str = "dette"

class DroitDesObligations(BaseModel):
    terme_specifique: Union['Dette']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-819"
    descripteur: str = "droit des obligations"

class PatrimoinePrive(BaseModel):
    terme_specifique: Literal['PatrimoinePrive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-261"
    descripteur: str = "patrimoine privé"

class Succession(BaseModel):
    terme_specifique: Literal['Succession']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1494"
    descripteur: str = "succession"

class RegimeMatrimonial(BaseModel):
    terme_specifique: Literal['RegimeMatrimonial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-934"
    descripteur: str = "régime matrimonial"

class Emancipation(BaseModel):
    terme_specifique: Literal['Emancipation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-207"
    descripteur: str = "émancipation"

class EnfantNaturel(BaseModel):
    terme_specifique: Literal['EnfantNaturel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1284"
    descripteur: str = "enfant naturel"

class DroitDeLaFamille(BaseModel):
    terme_specifique: Union['EnfantNaturel', 'Emancipation', 'RegimeMatrimonial', 'Succession']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-489"
    descripteur: str = "droit de la famille"

class Bourgeoisie(BaseModel):
    terme_specifique: Literal['Bourgeoisie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-184"
    descripteur: str = "bourgeoisie"

class TiersEtat(BaseModel):
    terme_specifique: Literal['TiersEtat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-151"
    descripteur: str = "tiers état"

class Servage(BaseModel):
    terme_specifique: Literal['Servage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1181"
    descripteur: str = "servage"

class Proletariat(BaseModel):
    terme_specifique: Literal['Proletariat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-723"
    descripteur: str = "prolétariat"

class Esclavage(BaseModel):
    terme_specifique: Literal['Esclavage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1394"
    descripteur: str = "esclavage"

class Noblesse(BaseModel):
    terme_specifique: Literal['Noblesse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-446"
    descripteur: str = "noblesse"

class ConditionSociale(BaseModel):
    terme_specifique: Union['Noblesse', 'Esclavage', 'Proletariat', 'Servage', 'TiersEtat', 'Bourgeoisie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-103"
    descripteur: str = "condition sociale"

class ConditionDesPersonnesEtDesBiens(BaseModel):
    terme_specifique: Union['ConditionSociale', 'DroitDeLaFamille', 'PatrimoinePrive', 'DroitDesObligations']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-942"
    descripteur: str = "condition des personnes et des biens"

class AtelierDeCharite(BaseModel):
    terme_specifique: Literal['AtelierDeCharite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-783"
    descripteur: str = "atelier de charité"

class PopulationActive(BaseModel):
    terme_specifique: Literal['PopulationActive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-713"
    descripteur: str = "population active"

class Retraite(BaseModel):
    terme_specifique: Literal['Retraite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-929"
    descripteur: str = "retraité"

class CarriereProfessionnelle(BaseModel):
    terme_specifique: Literal['CarriereProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1146"
    descripteur: str = "carrière professionnelle"

class TravailClandestin(BaseModel):
    terme_specifique: Literal['TravailClandestin']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1344"
    descripteur: str = "travail clandestin"

class TravailleurFrontalier(BaseModel):
    terme_specifique: Literal['TravailleurFrontalier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1419"
    descripteur: str = "travailleur frontalier"

class LicenciementEconomique(BaseModel):
    terme_specifique: Literal['LicenciementEconomique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1277"
    descripteur: str = "licenciement économique"

class Licenciement(BaseModel):
    terme_specifique: Union['LicenciementEconomique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-611"
    descripteur: str = "licenciement"

class TraficDeMainDoeuvre(BaseModel):
    terme_specifique: Literal['TraficDeMainDoeuvre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-593"
    descripteur: str = "trafic de main d'oeuvre"

class TravailleurEtranger(BaseModel):
    terme_specifique: Union['TraficDeMainDoeuvre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-983"
    descripteur: str = "travailleur étranger"

class InsertionProfessionnelle(BaseModel):
    terme_specifique: Literal['InsertionProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-848"
    descripteur: str = "insertion professionnelle"

class CumulDemploi(BaseModel):
    terme_specifique: Literal['CumulDemploi']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-520"
    descripteur: str = "cumul d'emploi"

class ExamenProfessionnel(BaseModel):
    terme_specifique: Literal['ExamenProfessionnel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-414"
    descripteur: str = "examen professionnel"

class OffreDemploi(BaseModel):
    terme_specifique: Literal['OffreDemploi']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-234"
    descripteur: str = "offre d'emploi"

class EmploiReserve(BaseModel):
    terme_specifique: Literal['EmploiReserve']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1312"
    descripteur: str = "emploi réservé"

class TravailProtege(BaseModel):
    terme_specifique: Literal['TravailProtege']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-189"
    descripteur: str = "travail protégé"

class TravailleurHandicape(BaseModel):
    terme_specifique: Union['TravailProtege', 'EmploiReserve']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1027"
    descripteur: str = "travailleur handicapé"

class EmploiAide(BaseModel):
    terme_specifique: Literal['EmploiAide']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-144"
    descripteur: str = "emploi aidé"

class DemandeurDemploi(BaseModel):
    terme_specifique: Literal['DemandeurDemploi']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1194"
    descripteur: str = "demandeur d'emploi"

class ChomagePartiel(BaseModel):
    terme_specifique: Literal['ChomagePartiel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-137"
    descripteur: str = "chômage partiel"

class Chomage(BaseModel):
    terme_specifique: Union['ChomagePartiel', 'DemandeurDemploi']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-862"
    descripteur: str = "chômage"

class EmploiATempsPartiel(BaseModel):
    terme_specifique: Literal['EmploiATempsPartiel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-85"
    descripteur: str = "emploi à temps partiel"

class Stagiaire(BaseModel):
    terme_specifique: Literal['Stagiaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1292"
    descripteur: str = "stagiaire"

class OrganismeDeFormation(BaseModel):
    terme_specifique: Literal['OrganismeDeFormation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-927"
    descripteur: str = "organisme de formation"

class FormationQualifiante(BaseModel):
    terme_specifique: Literal['FormationQualifiante']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-509"
    descripteur: str = "formation qualifiante"

class Formateur(BaseModel):
    terme_specifique: Literal['Formateur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-583"
    descripteur: str = "formateur"

class FormationProfessionnelle(BaseModel):
    terme_specifique: Union['Formateur', 'FormationQualifiante', 'OrganismeDeFormation', 'Stagiaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1196"
    descripteur: str = "formation professionnelle"

class Emploi(BaseModel):
    terme_specifique: Union['FormationProfessionnelle', 'EmploiATempsPartiel', 'Chomage', 'EmploiAide', 'TravailleurHandicape', 'OffreDemploi', 'ExamenProfessionnel', 'CumulDemploi', 'InsertionProfessionnelle', 'TravailleurEtranger', 'Licenciement', 'TravailleurFrontalier', 'TravailClandestin', 'CarriereProfessionnelle', 'Retraite', 'PopulationActive', 'AtelierDeCharite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-696"
    descripteur: str = "emploi"

class InvalideDeGuerre(BaseModel):
    terme_specifique: Literal['InvalideDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1104"
    descripteur: str = "invalide de guerre"

class AdulteHandicape(BaseModel):
    terme_specifique: Literal['AdulteHandicape']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1301"
    descripteur: str = "adulte handicapé"

class InvalideDuTravail(BaseModel):
    terme_specifique: Literal['InvalideDuTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-719"
    descripteur: str = "invalide du travail"

class EnfantHandicape(BaseModel):
    terme_specifique: Literal['EnfantHandicape']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-82"
    descripteur: str = "enfant handicapé"

class PersonneHandicapee(BaseModel):
    terme_specifique: Union['EnfantHandicape', 'InvalideDuTravail', 'AdulteHandicape', 'InvalideDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1495"
    descripteur: str = "personne handicapée"

class InsertionSociale(BaseModel):
    terme_specifique: Literal['InsertionSociale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-987"
    descripteur: str = "insertion sociale"

class PrestationFamiliale(BaseModel):
    terme_specifique: Literal['PrestationFamiliale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-790"
    descripteur: str = "prestation familiale"

class PlacementFamilial(BaseModel):
    terme_specifique: Literal['PlacementFamilial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-591"
    descripteur: str = "placement familial"

class AssuranceVeuvage(BaseModel):
    terme_specifique: Literal['AssuranceVeuvage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-673"
    descripteur: str = "assurance veuvage"

class AssuranceInvalidite(BaseModel):
    terme_specifique: Literal['AssuranceInvalidite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1354"
    descripteur: str = "assurance invalidité"

class AssuranceDeces(BaseModel):
    terme_specifique: Literal['AssuranceDeces']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-291"
    descripteur: str = "assurance décès"

class AssuranceVieillesse(BaseModel):
    terme_specifique: Literal['AssuranceVieillesse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-192"
    descripteur: str = "assurance vieillesse"

class AssuranceMaladie(BaseModel):
    terme_specifique: Literal['AssuranceMaladie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1330"
    descripteur: str = "assurance maladie"

class AssuranceChomage(BaseModel):
    terme_specifique: Literal['AssuranceChomage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-779"
    descripteur: str = "assurance chômage"

class AssuranceMaternite(BaseModel):
    terme_specifique: Literal['AssuranceMaternite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1012"
    descripteur: str = "assurance maternité"

class AssuranceSociale(BaseModel):
    terme_specifique: Union['AssuranceMaternite', 'AssuranceChomage', 'AssuranceMaladie', 'AssuranceVieillesse', 'AssuranceDeces', 'AssuranceInvalidite', 'AssuranceVeuvage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-466"
    descripteur: str = "assurance sociale"

class CollectePublique(BaseModel):
    terme_specifique: Literal['CollectePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1171"
    descripteur: str = "collecte publique"

class Alphabetisation(BaseModel):
    terme_specifique: Literal['Alphabetisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-119"
    descripteur: str = "alphabétisation"

class ActionHumanitaire(BaseModel):
    terme_specifique: Union['Alphabetisation', 'CollectePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-544"
    descripteur: str = "action humanitaire"

class Adoption(BaseModel):
    terme_specifique: Literal['Adoption']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1281"
    descripteur: str = "adoption"

class Orphelinat(BaseModel):
    terme_specifique: Literal['Orphelinat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1217"
    descripteur: str = "orphelinat"

class ConseilDeFamille(BaseModel):
    terme_specifique: Literal['ConseilDeFamille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-843"
    descripteur: str = "conseil de famille"

class PupilleDeLEtat(BaseModel):
    terme_specifique: Literal['PupilleDeLEtat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-100"
    descripteur: str = "pupille de l'État"

class EnfantSecouru(BaseModel):
    terme_specifique: Literal['EnfantSecouru']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-99"
    descripteur: str = "enfant secouru"

class EnfantEnGarde(BaseModel):
    terme_specifique: Literal['EnfantEnGarde']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-467"
    descripteur: str = "enfant en garde"

class AideSocialeALenfance(BaseModel):
    terme_specifique: Union['EnfantEnGarde', 'EnfantSecouru', 'PupilleDeLEtat', 'ConseilDeFamille', 'Orphelinat', 'Adoption']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-852"
    descripteur: str = "aide sociale à l'enfance"

class AideSocialeFacultative(BaseModel):
    terme_specifique: Literal['AideSocialeFacultative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1249"
    descripteur: str = "aide sociale facultative"

class AllocationMilitaire(BaseModel):
    terme_specifique: Literal['AllocationMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1497"
    descripteur: str = "allocation militaire"

class AllocationLogement(BaseModel):
    terme_specifique: Literal['AllocationLogement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1496"
    descripteur: str = "allocation logement"

class PrestationDaideSocialeLegale(BaseModel):
    terme_specifique: Literal['PrestationDaideSocialeLegale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-742"
    descripteur: str = "prestation d'aide sociale légale"

class AideJudiciaire(BaseModel):
    terme_specifique: Literal['AideJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-371"
    descripteur: str = "aide judiciaire"

class StructureCommunaleDaideSociale(BaseModel):
    terme_specifique: Literal['StructureCommunaleDaideSociale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-357"
    descripteur: str = "structure communale d'aide sociale"

class AideMedicale(BaseModel):
    terme_specifique: Literal['AideMedicale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-53"
    descripteur: str = "aide médicale"

class AideSociale(BaseModel):
    terme_specifique: Union['AideMedicale', 'StructureCommunaleDaideSociale', 'AideJudiciaire', 'PrestationDaideSocialeLegale', 'AllocationLogement', 'AllocationMilitaire', 'AideSocialeFacultative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1168"
    descripteur: str = "aide sociale"

class OrganismeDeSecuriteSociale(BaseModel):
    terme_specifique: Literal['OrganismeDeSecuriteSociale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-230"
    descripteur: str = "organisme de sécurité sociale"

class SocieteMutualiste(BaseModel):
    terme_specifique: Literal['SocieteMutualiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-97"
    descripteur: str = "société mutualiste"

class SecuriteSociale(BaseModel):
    terme_specifique: Union['SocieteMutualiste', 'OrganismeDeSecuriteSociale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-432"
    descripteur: str = "sécurité sociale"

class Mendicite(BaseModel):
    terme_specifique: Literal['Mendicite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-420"
    descripteur: str = "mendicité"

class Indigent(BaseModel):
    terme_specifique: Literal['Indigent']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-678"
    descripteur: str = "indigent"

class ExclusionSociale(BaseModel):
    terme_specifique: Union['Indigent', 'Mendicite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-45"
    descripteur: str = "exclusion sociale"

class AssociationFamiliale(BaseModel):
    terme_specifique: Literal['AssociationFamiliale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-406"
    descripteur: str = "association familiale"

class AssociationSocioeducative(BaseModel):
    terme_specifique: Literal['AssociationSocioeducative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1096"
    descripteur: str = "association socioéducative"

class TravailleurSocial(BaseModel):
    terme_specifique: Literal['TravailleurSocial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-20"
    descripteur: str = "travailleur social"

class ActionSociale(BaseModel):
    terme_specifique: Union['TravailleurSocial', 'AssociationSocioeducative', 'AssociationFamiliale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-200"
    descripteur: str = "action sociale"

class ProtectionSociale(BaseModel):
    terme_specifique: Union['ActionSociale', 'ExclusionSociale', 'SecuriteSociale', 'AideSociale', 'AideSocialeALenfance', 'ActionHumanitaire', 'AssuranceSociale', 'PlacementFamilial', 'PrestationFamiliale', 'InsertionSociale', 'PersonneHandicapee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1299"
    descripteur: str = "protection sociale"

class Gitan(BaseModel):
    terme_specifique: Literal['Gitan']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1424"
    descripteur: str = "gitan"

class Rapatrie(BaseModel):
    terme_specifique: Literal['Rapatrie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1191"
    descripteur: str = "rapatrié"

class Demographie(BaseModel):
    terme_specifique: Literal['Demographie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1314"
    descripteur: str = "démographie"

class PopulationUrbaine(BaseModel):
    terme_specifique: Literal['PopulationUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1271"
    descripteur: str = "population urbaine"

class Harki(BaseModel):
    terme_specifique: Literal['Harki']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-910"
    descripteur: str = "harki"

class RecensementDePopulation(BaseModel):
    terme_specifique: Literal['RecensementDePopulation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-781"
    descripteur: str = "recensement de population"

class SansDomicileFixe(BaseModel):
    terme_specifique: Literal['SansDomicileFixe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-426"
    descripteur: str = "sans domicile fixe"

class Famille(BaseModel):
    terme_specifique: Literal['Famille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-411"
    descripteur: str = "famille"

class Nomade(BaseModel):
    terme_specifique: Literal['Nomade']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-339"
    descripteur: str = "nomade"

class Femme(BaseModel):
    terme_specifique: Literal['Femme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-312"
    descripteur: str = "femme"

class Juif(BaseModel):
    terme_specifique: Literal['Juif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-269"
    descripteur: str = "juif"

class PersonneAgee(BaseModel):
    terme_specifique: Literal['PersonneAgee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-404"
    descripteur: str = "personne âgée"

class Suicide(BaseModel):
    terme_specifique: Literal['Suicide']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-191"
    descripteur: str = "suicide"

class MigrationSaisonniere(BaseModel):
    terme_specifique: Literal['MigrationSaisonniere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-667"
    descripteur: str = "migration saisonnière"

class Famine(BaseModel):
    terme_specifique: Literal['Famine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-564"
    descripteur: str = "famine"

class Subsistances(BaseModel):
    terme_specifique: Union['Famine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1450"
    descripteur: str = "subsistances"

class Jeune(BaseModel):
    terme_specifique: Literal['Jeune']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-558"
    descripteur: str = "jeune"

class Enfant(BaseModel):
    terme_specifique: Literal['Enfant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-946"
    descripteur: str = "enfant"

class Emigration(BaseModel):
    terme_specifique: Literal['Emigration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-44"
    descripteur: str = "émigration"

class Naturalisation(BaseModel):
    terme_specifique: Literal['Naturalisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1240"
    descripteur: str = "naturalisation"

class Immigration(BaseModel):
    terme_specifique: Literal['Immigration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-815"
    descripteur: str = "immigration"

class Refugie(BaseModel):
    terme_specifique: Literal['Refugie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-106"
    descripteur: str = "réfugié"

class Etranger(BaseModel):
    terme_specifique: Union['Refugie', 'Immigration', 'Naturalisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-860"
    descripteur: str = "étranger"

class Mariage(BaseModel):
    terme_specifique: Literal['Mariage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1201"
    descripteur: str = "mariage"

class Naissance(BaseModel):
    terme_specifique: Literal['Naissance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-77"
    descripteur: str = "naissance"

class Deces(BaseModel):
    terme_specifique: Literal['Deces']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1348"
    descripteur: str = "décès"

class EtatCivil(BaseModel):
    terme_specifique: Union['Deces', 'Naissance', 'Mariage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1139"
    descripteur: str = "état civil"

class MigrationRurale(BaseModel):
    terme_specifique: Literal['MigrationRurale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1454"
    descripteur: str = "migration rurale"

class PopulationRurale(BaseModel):
    terme_specifique: Union['MigrationRurale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-764"
    descripteur: str = "population rurale"

class Population(BaseModel):
    terme_specifique: Union['PopulationRurale', 'EtatCivil', 'Etranger', 'Emigration', 'Enfant', 'Jeune', 'Subsistances', 'MigrationSaisonniere', 'Suicide', 'PersonneAgee', 'Juif', 'Femme', 'Nomade', 'Famille', 'SansDomicileFixe', 'RecensementDePopulation', 'Harki', 'PopulationUrbaine', 'Demographie', 'Rapatrie', 'Gitan']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1066"
    descripteur: str = "population"

class Societe(BaseModel):
    terme_specifique: Union['Population', 'ProtectionSociale', 'Emploi', 'ConditionDesPersonnesEtDesBiens', 'Travail', 'Sante']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-307"
    descripteur: str = "société"
