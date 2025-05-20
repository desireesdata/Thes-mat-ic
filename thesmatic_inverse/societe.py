from pydantic import BaseModel
from typing import Union, Literal

class Alcoolique(BaseModel):
    sous_descripteur: Literal['Alcoolique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-412"
    descripteur: str = "alcoolique"

class HygieneSociale(BaseModel):
    sous_descripteur: Union['Alcoolique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1163"
    descripteur: str = "hygiène sociale"

class ProduitCosmetique(BaseModel):
    sous_descripteur: Literal['ProduitCosmetique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-728"
    descripteur: str = "produit cosmétique"

class SubstanceVeneneuse(BaseModel):
    sous_descripteur: Literal['SubstanceVeneneuse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1028"
    descripteur: str = "substance vénéneuse"

class SpecialitePharmaceutique(BaseModel):
    sous_descripteur: Literal['SpecialitePharmaceutique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-625"
    descripteur: str = "spécialité pharmaceutique"

class OfficinePharmaceutique(BaseModel):
    sous_descripteur: Literal['OfficinePharmaceutique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1010"
    descripteur: str = "officine pharmaceutique"

class Pharmacie(BaseModel):
    sous_descripteur: Union['OfficinePharmaceutique', 'SpecialitePharmaceutique', 'SubstanceVeneneuse', 'ProduitCosmetique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-337"
    descripteur: str = "pharmacie"

class LaboratoireDanalyse(BaseModel):
    sous_descripteur: Literal['LaboratoireDanalyse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1265"
    descripteur: str = "laboratoire d'analyse"

class Vaccination(BaseModel):
    sous_descripteur: Literal['Vaccination']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1085"
    descripteur: str = "vaccination"

class InstallationRadiologique(BaseModel):
    sous_descripteur: Literal['InstallationRadiologique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-730"
    descripteur: str = "installation radiologique"

class TransfusionSanguine(BaseModel):
    sous_descripteur: Literal['TransfusionSanguine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-279"
    descripteur: str = "transfusion sanguine"

class EtablissementMedicoSocial(BaseModel):
    sous_descripteur: Literal['EtablissementMedicoSocial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-355"
    descripteur: str = "établissement médico social"

class TransportSanitaire(BaseModel):
    sous_descripteur: Literal['TransportSanitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-635"
    descripteur: str = "transport sanitaire"

class OrganisationSanitaire(BaseModel):
    sous_descripteur: Union['TransportSanitaire', 'EtablissementMedicoSocial', 'TransfusionSanguine', 'InstallationRadiologique', 'Vaccination', 'LaboratoireDanalyse'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1423"
    descripteur: str = "organisation sanitaire"

class SoinsMedicaux(BaseModel):
    sous_descripteur: Literal['SoinsMedicaux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1498"
    descripteur: str = "soins médicaux"

class Sida(BaseModel):
    sous_descripteur: Literal['Sida']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1308"
    descripteur: str = "sida"

class Toxicomanie(BaseModel):
    sous_descripteur: Literal['Toxicomanie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1189"
    descripteur: str = "toxicomanie"

class Tabagisme(BaseModel):
    sous_descripteur: Literal['Tabagisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-984"
    descripteur: str = "tabagisme"

class Alcoolisme(BaseModel):
    sous_descripteur: Literal['Alcoolisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1270"
    descripteur: str = "alcoolisme"

class MaladieADeclarationObligatoire(BaseModel):
    sous_descripteur: Literal['MaladieADeclarationObligatoire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-797"
    descripteur: str = "maladie à déclaration obligatoire"

class MaladieMentale(BaseModel):
    sous_descripteur: Literal['MaladieMentale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-732"
    descripteur: str = "maladie mentale"

class Tuberculose(BaseModel):
    sous_descripteur: Literal['Tuberculose']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-700"
    descripteur: str = "tuberculose"

class Epidemie(BaseModel):
    sous_descripteur: Literal['Epidemie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-501"
    descripteur: str = "épidémie"

class Lepre(BaseModel):
    sous_descripteur: Literal['Lepre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-322"
    descripteur: str = "lèpre"

class MaladieSexuellementTransmissible(BaseModel):
    sous_descripteur: Literal['MaladieSexuellementTransmissible']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-214"
    descripteur: str = "maladie sexuellement transmissible"

class Cancer(BaseModel):
    sous_descripteur: Literal['Cancer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-152"
    descripteur: str = "cancer"

class ActionSanitaire(BaseModel):
    sous_descripteur: Union['Cancer', 'MaladieSexuellementTransmissible', 'Lepre', 'Epidemie', 'Tuberculose', 'MaladieMentale', 'MaladieADeclarationObligatoire', 'Alcoolisme', 'Tabagisme', 'Toxicomanie', 'Sida', 'SoinsMedicaux'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1319"
    descripteur: str = "action sanitaire"

class Accouchement(BaseModel):
    sous_descripteur: Literal['Accouchement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-978"
    descripteur: str = "accouchement"

class Contraception(BaseModel):
    sous_descripteur: Literal['Contraception']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-972"
    descripteur: str = "contraception"

class InterruptionVolontaireDeGrossesse(BaseModel):
    sous_descripteur: Literal['InterruptionVolontaireDeGrossesse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-916"
    descripteur: str = "interruption volontaire de grossesse"

class MortaliteInfantile(BaseModel):
    sous_descripteur: Literal['MortaliteInfantile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-541"
    descripteur: str = "mortalité infantile"

class AssistanteMaternelle(BaseModel):
    sous_descripteur: Literal['AssistanteMaternelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1307"
    descripteur: str = "assistante maternelle"

class Creche(BaseModel):
    sous_descripteur: Literal['Creche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-190"
    descripteur: str = "crèche"

class HalteGarderie(BaseModel):
    sous_descripteur: Literal['HalteGarderie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-180"
    descripteur: str = "halte garderie"

class Puericultrice(BaseModel):
    sous_descripteur: Literal['Puericultrice']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-134"
    descripteur: str = "puéricultrice"

class ProtectionMaternelleEtInfantile(BaseModel):
    sous_descripteur: Union['Puericultrice', 'HalteGarderie', 'Creche', 'AssistanteMaternelle', 'MortaliteInfantile', 'InterruptionVolontaireDeGrossesse', 'Contraception', 'Accouchement'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1094"
    descripteur: str = "protection maternelle et infantile"

class Hoteldieu(BaseModel):
    sous_descripteur: Literal['Hoteldieu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1499"
    descripteur: str = "hôtel-dieu"

class EquipementMedicoChirurgical(BaseModel):
    sous_descripteur: Literal['EquipementMedicoChirurgical']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-560"
    descripteur: str = "équipement médico chirurgical"

class Sanatorium(BaseModel):
    sous_descripteur: Literal['Sanatorium']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-894"
    descripteur: str = "sanatorium"

class EtablissementPublicDhospitalisation(BaseModel):
    sous_descripteur: Literal['EtablissementPublicDhospitalisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-329"
    descripteur: str = "établissement public d'hospitalisation"

class HopitalPsychiatrique(BaseModel):
    sous_descripteur: Literal['HopitalPsychiatrique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1062"
    descripteur: str = "hôpital psychiatrique"

class Leproserie(BaseModel):
    sous_descripteur: Literal['Leproserie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1263"
    descripteur: str = "léproserie"

class EtablissementSanitairePrive(BaseModel):
    sous_descripteur: Literal['EtablissementSanitairePrive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1457"
    descripteur: str = "établissement sanitaire privé"

class PopulationHospitaliere(BaseModel):
    sous_descripteur: Literal['PopulationHospitaliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-492"
    descripteur: str = "population hospitalière"

class ConstructionHospitaliere(BaseModel):
    sous_descripteur: Literal['ConstructionHospitaliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-950"
    descripteur: str = "construction hospitalière"

class EtablissementDeSante(BaseModel):
    sous_descripteur: Union['ConstructionHospitaliere', 'PopulationHospitaliere', 'EtablissementSanitairePrive', 'Leproserie', 'HopitalPsychiatrique', 'EtablissementPublicDhospitalisation', 'Sanatorium', 'EquipementMedicoChirurgical', 'Hoteldieu'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-185"
    descripteur: str = "établissement de santé"

class SageFemme(BaseModel):
    sous_descripteur: Literal['SageFemme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-806"
    descripteur: str = "sage femme"

class AuxiliaireMedical(BaseModel):
    sous_descripteur: Literal['AuxiliaireMedical']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1032"
    descripteur: str = "auxiliaire médical"

class Pharmacien(BaseModel):
    sous_descripteur: Literal['Pharmacien']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-365"
    descripteur: str = "pharmacien"

class ChirurgienDentiste(BaseModel):
    sous_descripteur: Literal['ChirurgienDentiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-259"
    descripteur: str = "chirurgien dentiste"

class Medecin(BaseModel):
    sous_descripteur: Literal['Medecin']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-89"
    descripteur: str = "médecin"

class MedecinHospitalier(BaseModel):
    sous_descripteur: Literal['MedecinHospitalier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-777"
    descripteur: str = "médecin hospitalier"

class ProfessionMedicale(BaseModel):
    sous_descripteur: Union['MedecinHospitalier', 'Medecin', 'ChirurgienDentiste', 'Pharmacien', 'AuxiliaireMedical', 'SageFemme'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-672"
    descripteur: str = "profession médicale"

class Desinfection(BaseModel):
    sous_descripteur: Literal['Desinfection']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-956"
    descripteur: str = "désinfection"

class Amiante(BaseModel):
    sous_descripteur: Literal['Amiante']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-343"
    descripteur: str = "amiante"

class HygieneAlimentaire(BaseModel):
    sous_descripteur: Literal['HygieneAlimentaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-565"
    descripteur: str = "hygiène alimentaire"

class Hygiene(BaseModel):
    sous_descripteur: Union['HygieneAlimentaire', 'Amiante', 'Desinfection'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-748"
    descripteur: str = "hygiène"

class Thermoclimatisme(BaseModel):
    sous_descripteur: Literal['Thermoclimatisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1268"
    descripteur: str = "thermoclimatisme"

class Sante(BaseModel):
    sous_descripteur: Union['Thermoclimatisme', 'Hygiene', 'ProfessionMedicale', 'EtablissementDeSante', 'ProtectionMaternelleEtInfantile', 'ActionSanitaire', 'OrganisationSanitaire', 'Pharmacie', 'HygieneSociale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-344"
    descripteur: str = "santé"

class RestaurationCollective(BaseModel):
    sous_descripteur: Literal['RestaurationCollective']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1479"
    descripteur: str = "restauration collective"

class EntrepriseDeTravailTemporaire(BaseModel):
    sous_descripteur: Literal['EntrepriseDeTravailTemporaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1233"
    descripteur: str = "entreprise de travail temporaire"

class SyndicatProfessionnel(BaseModel):
    sous_descripteur: Literal['SyndicatProfessionnel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-258"
    descripteur: str = "syndicat professionnel"

class ComiteDentreprise(BaseModel):
    sous_descripteur: Literal['ComiteDentreprise']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1208"
    descripteur: str = "comité d'entreprise"

class DelegueDuPersonnel(BaseModel):
    sous_descripteur: Literal['DelegueDuPersonnel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-650"
    descripteur: str = "délégué du personnel"

class ConflitDuTravail(BaseModel):
    sous_descripteur: Literal['ConflitDuTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-886"
    descripteur: str = "conflit du travail"

class RelationsDuTravail(BaseModel):
    sous_descripteur: Union['ConflitDuTravail', 'DelegueDuPersonnel', 'ComiteDentreprise', 'SyndicatProfessionnel'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-847"
    descripteur: str = "relations du travail"

class TravailleurADomicile(BaseModel):
    sous_descripteur: Literal['TravailleurADomicile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-907"
    descripteur: str = "travailleur à domicile"

class Concierge(BaseModel):
    sous_descripteur: Literal['Concierge']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-517"
    descripteur: str = "concierge"

class EmployeDeMaison(BaseModel):
    sous_descripteur: Literal['EmployeDeMaison']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-210"
    descripteur: str = "employé de maison"

class ProfessionParticuliere(BaseModel):
    sous_descripteur: Union['EmployeDeMaison', 'Concierge', 'TravailleurADomicile'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-480"
    descripteur: str = "profession particulière"

class AccidentDuTravail(BaseModel):
    sous_descripteur: Literal['AccidentDuTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-682"
    descripteur: str = "accident du travail"

class MedecineDuTravail(BaseModel):
    sous_descripteur: Literal['MedecineDuTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-841"
    descripteur: str = "médecine du travail"

class MaladieProfessionnelle(BaseModel):
    sous_descripteur: Literal['MaladieProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-500"
    descripteur: str = "maladie professionnelle"

class MachineDangereuse(BaseModel):
    sous_descripteur: Literal['MachineDangereuse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-176"
    descripteur: str = "machine dangereuse"

class SecuriteDuTravail(BaseModel):
    sous_descripteur: Union['MachineDangereuse', 'MaladieProfessionnelle', 'MedecineDuTravail', 'AccidentDuTravail'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1264"
    descripteur: str = "sécurité du travail"

class InteressementDesTravailleurs(BaseModel):
    sous_descripteur: Literal['InteressementDesTravailleurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-111"
    descripteur: str = "intéressement des travailleurs"

class Ouvrier(BaseModel):
    sous_descripteur: Literal['Ouvrier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-127"
    descripteur: str = "ouvrier"

class TravailDesEnfants(BaseModel):
    sous_descripteur: Literal['TravailDesEnfants']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1100"
    descripteur: str = "travail des enfants"

class HoraireDeTravail(BaseModel):
    sous_descripteur: Literal['HoraireDeTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-898"
    descripteur: str = "horaire de travail"

class TravailDeNuit(BaseModel):
    sous_descripteur: Literal['TravailDeNuit']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1140"
    descripteur: str = "travail de nuit"

class CongesPayes(BaseModel):
    sous_descripteur: Literal['CongesPayes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-405"
    descripteur: str = "congés payés"

class Remuneration(BaseModel):
    sous_descripteur: Literal['Remuneration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-374"
    descripteur: str = "rémunération"

class ReposHebdomadaire(BaseModel):
    sous_descripteur: Literal['ReposHebdomadaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-161"
    descripteur: str = "repos hebdomadaire"

class DureeDuTravail(BaseModel):
    sous_descripteur: Literal['DureeDuTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-4"
    descripteur: str = "durée du travail"

class ConditionsDuTravail(BaseModel):
    sous_descripteur: Union['DureeDuTravail', 'ReposHebdomadaire', 'Remuneration', 'CongesPayes', 'TravailDeNuit', 'HoraireDeTravail', 'TravailDesEnfants'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-861"
    descripteur: str = "conditions du travail"

class Travail(BaseModel):
    sous_descripteur: Union['ConditionsDuTravail', 'Ouvrier', 'InteressementDesTravailleurs', 'SecuriteDuTravail', 'ProfessionParticuliere', 'RelationsDuTravail', 'EntrepriseDeTravailTemporaire', 'RestaurationCollective'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-536"
    descripteur: str = "travail"

class Dette(BaseModel):
    sous_descripteur: Literal['Dette']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1030"
    descripteur: str = "dette"

class DroitDesObligations(BaseModel):
    sous_descripteur: Union['Dette'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-819"
    descripteur: str = "droit des obligations"

class PatrimoinePrive(BaseModel):
    sous_descripteur: Literal['PatrimoinePrive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-261"
    descripteur: str = "patrimoine privé"

class Succession(BaseModel):
    sous_descripteur: Literal['Succession']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1494"
    descripteur: str = "succession"

class RegimeMatrimonial(BaseModel):
    sous_descripteur: Literal['RegimeMatrimonial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-934"
    descripteur: str = "régime matrimonial"

class Emancipation(BaseModel):
    sous_descripteur: Literal['Emancipation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-207"
    descripteur: str = "émancipation"

class EnfantNaturel(BaseModel):
    sous_descripteur: Literal['EnfantNaturel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1284"
    descripteur: str = "enfant naturel"

class DroitDeLaFamille(BaseModel):
    sous_descripteur: Union['EnfantNaturel', 'Emancipation', 'RegimeMatrimonial', 'Succession'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-489"
    descripteur: str = "droit de la famille"

class Bourgeoisie(BaseModel):
    sous_descripteur: Literal['Bourgeoisie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-184"
    descripteur: str = "bourgeoisie"

class TiersEtat(BaseModel):
    sous_descripteur: Literal['TiersEtat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-151"
    descripteur: str = "tiers état"

class Servage(BaseModel):
    sous_descripteur: Literal['Servage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1181"
    descripteur: str = "servage"

class Proletariat(BaseModel):
    sous_descripteur: Literal['Proletariat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-723"
    descripteur: str = "prolétariat"

class Esclavage(BaseModel):
    sous_descripteur: Literal['Esclavage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1394"
    descripteur: str = "esclavage"

class Noblesse(BaseModel):
    sous_descripteur: Literal['Noblesse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-446"
    descripteur: str = "noblesse"

class ConditionSociale(BaseModel):
    sous_descripteur: Union['Noblesse', 'Esclavage', 'Proletariat', 'Servage', 'TiersEtat', 'Bourgeoisie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-103"
    descripteur: str = "condition sociale"

class ConditionDesPersonnesEtDesBiens(BaseModel):
    sous_descripteur: Union['ConditionSociale', 'DroitDeLaFamille', 'PatrimoinePrive', 'DroitDesObligations'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-942"
    descripteur: str = "condition des personnes et des biens"

class AtelierDeCharite(BaseModel):
    sous_descripteur: Literal['AtelierDeCharite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-783"
    descripteur: str = "atelier de charité"

class PopulationActive(BaseModel):
    sous_descripteur: Literal['PopulationActive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-713"
    descripteur: str = "population active"

class Retraite(BaseModel):
    sous_descripteur: Literal['Retraite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-929"
    descripteur: str = "retraité"

class CarriereProfessionnelle(BaseModel):
    sous_descripteur: Literal['CarriereProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1146"
    descripteur: str = "carrière professionnelle"

class TravailClandestin(BaseModel):
    sous_descripteur: Literal['TravailClandestin']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1344"
    descripteur: str = "travail clandestin"

class TravailleurFrontalier(BaseModel):
    sous_descripteur: Literal['TravailleurFrontalier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1419"
    descripteur: str = "travailleur frontalier"

class LicenciementEconomique(BaseModel):
    sous_descripteur: Literal['LicenciementEconomique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1277"
    descripteur: str = "licenciement économique"

class Licenciement(BaseModel):
    sous_descripteur: Union['LicenciementEconomique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-611"
    descripteur: str = "licenciement"

class TraficDeMainDoeuvre(BaseModel):
    sous_descripteur: Literal['TraficDeMainDoeuvre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-593"
    descripteur: str = "trafic de main d'oeuvre"

class TravailleurEtranger(BaseModel):
    sous_descripteur: Union['TraficDeMainDoeuvre'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-983"
    descripteur: str = "travailleur étranger"

class InsertionProfessionnelle(BaseModel):
    sous_descripteur: Literal['InsertionProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-848"
    descripteur: str = "insertion professionnelle"

class CumulDemploi(BaseModel):
    sous_descripteur: Literal['CumulDemploi']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-520"
    descripteur: str = "cumul d'emploi"

class ExamenProfessionnel(BaseModel):
    sous_descripteur: Literal['ExamenProfessionnel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-414"
    descripteur: str = "examen professionnel"

class OffreDemploi(BaseModel):
    sous_descripteur: Literal['OffreDemploi']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-234"
    descripteur: str = "offre d'emploi"

class EmploiReserve(BaseModel):
    sous_descripteur: Literal['EmploiReserve']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1312"
    descripteur: str = "emploi réservé"

class TravailProtege(BaseModel):
    sous_descripteur: Literal['TravailProtege']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-189"
    descripteur: str = "travail protégé"

class TravailleurHandicape(BaseModel):
    sous_descripteur: Union['TravailProtege', 'EmploiReserve'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1027"
    descripteur: str = "travailleur handicapé"

class EmploiAide(BaseModel):
    sous_descripteur: Literal['EmploiAide']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-144"
    descripteur: str = "emploi aidé"

class DemandeurDemploi(BaseModel):
    sous_descripteur: Literal['DemandeurDemploi']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1194"
    descripteur: str = "demandeur d'emploi"

class ChomagePartiel(BaseModel):
    sous_descripteur: Literal['ChomagePartiel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-137"
    descripteur: str = "chômage partiel"

class Chomage(BaseModel):
    sous_descripteur: Union['ChomagePartiel', 'DemandeurDemploi'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-862"
    descripteur: str = "chômage"

class EmploiATempsPartiel(BaseModel):
    sous_descripteur: Literal['EmploiATempsPartiel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-85"
    descripteur: str = "emploi à temps partiel"

class Stagiaire(BaseModel):
    sous_descripteur: Literal['Stagiaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1292"
    descripteur: str = "stagiaire"

class OrganismeDeFormation(BaseModel):
    sous_descripteur: Literal['OrganismeDeFormation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-927"
    descripteur: str = "organisme de formation"

class FormationQualifiante(BaseModel):
    sous_descripteur: Literal['FormationQualifiante']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-509"
    descripteur: str = "formation qualifiante"

class Formateur(BaseModel):
    sous_descripteur: Literal['Formateur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-583"
    descripteur: str = "formateur"

class FormationProfessionnelle(BaseModel):
    sous_descripteur: Union['Formateur', 'FormationQualifiante', 'OrganismeDeFormation', 'Stagiaire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1196"
    descripteur: str = "formation professionnelle"

class Emploi(BaseModel):
    sous_descripteur: Union['FormationProfessionnelle', 'EmploiATempsPartiel', 'Chomage', 'EmploiAide', 'TravailleurHandicape', 'OffreDemploi', 'ExamenProfessionnel', 'CumulDemploi', 'InsertionProfessionnelle', 'TravailleurEtranger', 'Licenciement', 'TravailleurFrontalier', 'TravailClandestin', 'CarriereProfessionnelle', 'Retraite', 'PopulationActive', 'AtelierDeCharite'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-696"
    descripteur: str = "emploi"

class InvalideDeGuerre(BaseModel):
    sous_descripteur: Literal['InvalideDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1104"
    descripteur: str = "invalide de guerre"

class AdulteHandicape(BaseModel):
    sous_descripteur: Literal['AdulteHandicape']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1301"
    descripteur: str = "adulte handicapé"

class InvalideDuTravail(BaseModel):
    sous_descripteur: Literal['InvalideDuTravail']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-719"
    descripteur: str = "invalide du travail"

class EnfantHandicape(BaseModel):
    sous_descripteur: Literal['EnfantHandicape']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-82"
    descripteur: str = "enfant handicapé"

class PersonneHandicapee(BaseModel):
    sous_descripteur: Union['EnfantHandicape', 'InvalideDuTravail', 'AdulteHandicape', 'InvalideDeGuerre'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1495"
    descripteur: str = "personne handicapée"

class InsertionSociale(BaseModel):
    sous_descripteur: Literal['InsertionSociale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-987"
    descripteur: str = "insertion sociale"

class PrestationFamiliale(BaseModel):
    sous_descripteur: Literal['PrestationFamiliale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-790"
    descripteur: str = "prestation familiale"

class PlacementFamilial(BaseModel):
    sous_descripteur: Literal['PlacementFamilial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-591"
    descripteur: str = "placement familial"

class AssuranceVeuvage(BaseModel):
    sous_descripteur: Literal['AssuranceVeuvage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-673"
    descripteur: str = "assurance veuvage"

class AssuranceInvalidite(BaseModel):
    sous_descripteur: Literal['AssuranceInvalidite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1354"
    descripteur: str = "assurance invalidité"

class AssuranceDeces(BaseModel):
    sous_descripteur: Literal['AssuranceDeces']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-291"
    descripteur: str = "assurance décès"

class AssuranceVieillesse(BaseModel):
    sous_descripteur: Literal['AssuranceVieillesse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-192"
    descripteur: str = "assurance vieillesse"

class AssuranceMaladie(BaseModel):
    sous_descripteur: Literal['AssuranceMaladie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1330"
    descripteur: str = "assurance maladie"

class AssuranceChomage(BaseModel):
    sous_descripteur: Literal['AssuranceChomage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-779"
    descripteur: str = "assurance chômage"

class AssuranceMaternite(BaseModel):
    sous_descripteur: Literal['AssuranceMaternite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1012"
    descripteur: str = "assurance maternité"

class AssuranceSociale(BaseModel):
    sous_descripteur: Union['AssuranceMaternite', 'AssuranceChomage', 'AssuranceMaladie', 'AssuranceVieillesse', 'AssuranceDeces', 'AssuranceInvalidite', 'AssuranceVeuvage'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-466"
    descripteur: str = "assurance sociale"

class CollectePublique(BaseModel):
    sous_descripteur: Literal['CollectePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1171"
    descripteur: str = "collecte publique"

class Alphabetisation(BaseModel):
    sous_descripteur: Literal['Alphabetisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-119"
    descripteur: str = "alphabétisation"

class ActionHumanitaire(BaseModel):
    sous_descripteur: Union['Alphabetisation', 'CollectePublique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-544"
    descripteur: str = "action humanitaire"

class Adoption(BaseModel):
    sous_descripteur: Literal['Adoption']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1281"
    descripteur: str = "adoption"

class Orphelinat(BaseModel):
    sous_descripteur: Literal['Orphelinat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1217"
    descripteur: str = "orphelinat"

class ConseilDeFamille(BaseModel):
    sous_descripteur: Literal['ConseilDeFamille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-843"
    descripteur: str = "conseil de famille"

class PupilleDeLEtat(BaseModel):
    sous_descripteur: Literal['PupilleDeLEtat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-100"
    descripteur: str = "pupille de l'État"

class EnfantSecouru(BaseModel):
    sous_descripteur: Literal['EnfantSecouru']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-99"
    descripteur: str = "enfant secouru"

class EnfantEnGarde(BaseModel):
    sous_descripteur: Literal['EnfantEnGarde']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-467"
    descripteur: str = "enfant en garde"

class AideSocialeALenfance(BaseModel):
    sous_descripteur: Union['EnfantEnGarde', 'EnfantSecouru', 'PupilleDeLEtat', 'ConseilDeFamille', 'Orphelinat', 'Adoption'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-852"
    descripteur: str = "aide sociale à l'enfance"

class AideSocialeFacultative(BaseModel):
    sous_descripteur: Literal['AideSocialeFacultative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1249"
    descripteur: str = "aide sociale facultative"

class AllocationMilitaire(BaseModel):
    sous_descripteur: Literal['AllocationMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1497"
    descripteur: str = "allocation militaire"

class AllocationLogement(BaseModel):
    sous_descripteur: Literal['AllocationLogement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1496"
    descripteur: str = "allocation logement"

class PrestationDaideSocialeLegale(BaseModel):
    sous_descripteur: Literal['PrestationDaideSocialeLegale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-742"
    descripteur: str = "prestation d'aide sociale légale"

class AideJudiciaire(BaseModel):
    sous_descripteur: Literal['AideJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-371"
    descripteur: str = "aide judiciaire"

class StructureCommunaleDaideSociale(BaseModel):
    sous_descripteur: Literal['StructureCommunaleDaideSociale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-357"
    descripteur: str = "structure communale d'aide sociale"

class AideMedicale(BaseModel):
    sous_descripteur: Literal['AideMedicale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-53"
    descripteur: str = "aide médicale"

class AideSociale(BaseModel):
    sous_descripteur: Union['AideMedicale', 'StructureCommunaleDaideSociale', 'AideJudiciaire', 'PrestationDaideSocialeLegale', 'AllocationLogement', 'AllocationMilitaire', 'AideSocialeFacultative'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1168"
    descripteur: str = "aide sociale"

class OrganismeDeSecuriteSociale(BaseModel):
    sous_descripteur: Literal['OrganismeDeSecuriteSociale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-230"
    descripteur: str = "organisme de sécurité sociale"

class SocieteMutualiste(BaseModel):
    sous_descripteur: Literal['SocieteMutualiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-97"
    descripteur: str = "société mutualiste"

class SecuriteSociale(BaseModel):
    sous_descripteur: Union['SocieteMutualiste', 'OrganismeDeSecuriteSociale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-432"
    descripteur: str = "sécurité sociale"

class Mendicite(BaseModel):
    sous_descripteur: Literal['Mendicite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-420"
    descripteur: str = "mendicité"

class Indigent(BaseModel):
    sous_descripteur: Literal['Indigent']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-678"
    descripteur: str = "indigent"

class ExclusionSociale(BaseModel):
    sous_descripteur: Union['Indigent', 'Mendicite'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-45"
    descripteur: str = "exclusion sociale"

class AssociationFamiliale(BaseModel):
    sous_descripteur: Literal['AssociationFamiliale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-406"
    descripteur: str = "association familiale"

class AssociationSocioeducative(BaseModel):
    sous_descripteur: Literal['AssociationSocioeducative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1096"
    descripteur: str = "association socioéducative"

class TravailleurSocial(BaseModel):
    sous_descripteur: Literal['TravailleurSocial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-20"
    descripteur: str = "travailleur social"

class ActionSociale(BaseModel):
    sous_descripteur: Union['TravailleurSocial', 'AssociationSocioeducative', 'AssociationFamiliale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-200"
    descripteur: str = "action sociale"

class ProtectionSociale(BaseModel):
    sous_descripteur: Union['ActionSociale', 'ExclusionSociale', 'SecuriteSociale', 'AideSociale', 'AideSocialeALenfance', 'ActionHumanitaire', 'AssuranceSociale', 'PlacementFamilial', 'PrestationFamiliale', 'InsertionSociale', 'PersonneHandicapee'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1299"
    descripteur: str = "protection sociale"

class Gitan(BaseModel):
    sous_descripteur: Literal['Gitan']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1424"
    descripteur: str = "gitan"

class Rapatrie(BaseModel):
    sous_descripteur: Literal['Rapatrie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1191"
    descripteur: str = "rapatrié"

class Demographie(BaseModel):
    sous_descripteur: Literal['Demographie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1314"
    descripteur: str = "démographie"

class PopulationUrbaine(BaseModel):
    sous_descripteur: Literal['PopulationUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1271"
    descripteur: str = "population urbaine"

class Harki(BaseModel):
    sous_descripteur: Literal['Harki']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-910"
    descripteur: str = "harki"

class RecensementDePopulation(BaseModel):
    sous_descripteur: Literal['RecensementDePopulation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-781"
    descripteur: str = "recensement de population"

class SansDomicileFixe(BaseModel):
    sous_descripteur: Literal['SansDomicileFixe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-426"
    descripteur: str = "sans domicile fixe"

class Famille(BaseModel):
    sous_descripteur: Literal['Famille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-411"
    descripteur: str = "famille"

class Nomade(BaseModel):
    sous_descripteur: Literal['Nomade']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-339"
    descripteur: str = "nomade"

class Femme(BaseModel):
    sous_descripteur: Literal['Femme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-312"
    descripteur: str = "femme"

class Juif(BaseModel):
    sous_descripteur: Literal['Juif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-269"
    descripteur: str = "juif"

class PersonneAgee(BaseModel):
    sous_descripteur: Literal['PersonneAgee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-404"
    descripteur: str = "personne âgée"

class Suicide(BaseModel):
    sous_descripteur: Literal['Suicide']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-191"
    descripteur: str = "suicide"

class MigrationSaisonniere(BaseModel):
    sous_descripteur: Literal['MigrationSaisonniere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-667"
    descripteur: str = "migration saisonnière"

class Famine(BaseModel):
    sous_descripteur: Literal['Famine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-564"
    descripteur: str = "famine"

class Subsistances(BaseModel):
    sous_descripteur: Union['Famine'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1450"
    descripteur: str = "subsistances"

class Jeune(BaseModel):
    sous_descripteur: Literal['Jeune']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-558"
    descripteur: str = "jeune"

class Enfant(BaseModel):
    sous_descripteur: Literal['Enfant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-946"
    descripteur: str = "enfant"

class Emigration(BaseModel):
    sous_descripteur: Literal['Emigration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-44"
    descripteur: str = "émigration"

class Naturalisation(BaseModel):
    sous_descripteur: Literal['Naturalisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1240"
    descripteur: str = "naturalisation"

class Immigration(BaseModel):
    sous_descripteur: Literal['Immigration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-815"
    descripteur: str = "immigration"

class Refugie(BaseModel):
    sous_descripteur: Literal['Refugie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-106"
    descripteur: str = "réfugié"

class Etranger(BaseModel):
    sous_descripteur: Union['Refugie', 'Immigration', 'Naturalisation'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-860"
    descripteur: str = "étranger"

class Mariage(BaseModel):
    sous_descripteur: Literal['Mariage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1201"
    descripteur: str = "mariage"

class Naissance(BaseModel):
    sous_descripteur: Literal['Naissance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-77"
    descripteur: str = "naissance"

class Deces(BaseModel):
    sous_descripteur: Literal['Deces']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1348"
    descripteur: str = "décès"

class EtatCivil(BaseModel):
    sous_descripteur: Union['Deces', 'Naissance', 'Mariage'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1139"
    descripteur: str = "état civil"

class MigrationRurale(BaseModel):
    sous_descripteur: Literal['MigrationRurale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1454"
    descripteur: str = "migration rurale"

class PopulationRurale(BaseModel):
    sous_descripteur: Union['MigrationRurale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-764"
    descripteur: str = "population rurale"

class Population(BaseModel):
    sous_descripteur: Union['PopulationRurale', 'EtatCivil', 'Etranger', 'Emigration', 'Enfant', 'Jeune', 'Subsistances', 'MigrationSaisonniere', 'Suicide', 'PersonneAgee', 'Juif', 'Femme', 'Nomade', 'Famille', 'SansDomicileFixe', 'RecensementDePopulation', 'Harki', 'PopulationUrbaine', 'Demographie', 'Rapatrie', 'Gitan'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1066"
    descripteur: str = "population"

class Societe(BaseModel):
    sous_descripteur: Union['Population', 'ProtectionSociale', 'Emploi', 'ConditionDesPersonnesEtDesBiens', 'Travail', 'Sante'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-307"
    descripteur: str = "société"
