from pydantic import BaseModel, Field
from typing import Union, Literal

class OeuvreDeGuerre(BaseModel):
    sous_descripteur: Literal['OeuvreDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1020"
    descripteur: str = "oeuvre de guerre"

class Abri(BaseModel):
    sous_descripteur: Literal['Abri']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1195"
    descripteur: str = "abri"

class DefensePassive(BaseModel):
    sous_descripteur: Union['Abri'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-989"
    descripteur: str = "défense passive"

class TravailContraint(BaseModel):
    sous_descripteur: Literal['TravailContraint']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-979"
    descripteur: str = "travail contraint"

class PrisonnierDeGuerre(BaseModel):
    sous_descripteur: Literal['PrisonnierDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-563"
    descripteur: str = "prisonnier de guerre"

class ChantierDeLaJeunesse(BaseModel):
    sous_descripteur: Literal['ChantierDeLaJeunesse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-699"
    descripteur: str = "chantier de la jeunesse"

class AutoriteDoccupation(BaseModel):
    sous_descripteur: Literal['AutoriteDoccupation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1202"
    descripteur: str = "autorité d'occupation"

class Collaboration(BaseModel):
    sous_descripteur: Literal['Collaboration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-830"
    descripteur: str = "collaboration"

class Resistance(BaseModel):
    sous_descripteur: Literal['Resistance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1231"
    descripteur: str = "résistance"

class Epuration(BaseModel):
    sous_descripteur: Literal['Epuration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-494"
    descripteur: str = "épuration"

class OccupationEtrangere(BaseModel):
    sous_descripteur: Union['Epuration', 'Resistance', 'Collaboration', 'AutoriteDoccupation'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-788"
    descripteur: str = "occupation étrangère"

class BienSinistre(BaseModel):
    sous_descripteur: Literal['BienSinistre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1255"
    descripteur: str = "bien sinistré"

class BienSpolie(BaseModel):
    sous_descripteur: Literal['BienSpolie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-725"
    descripteur: str = "bien spolié"

class DommagesDeGuerre(BaseModel):
    sous_descripteur: Union['BienSpolie', 'BienSinistre'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1453"
    descripteur: str = "dommages de guerre"

class ForcesAlliees(BaseModel):
    sous_descripteur: Literal['ForcesAlliees']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-402"
    descripteur: str = "forces alliées"

class MortPourLaFrance(BaseModel):
    sous_descripteur: Literal['MortPourLaFrance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1484"
    descripteur: str = "mort pour la France"

class VeuveDeGuerre(BaseModel):
    sous_descripteur: Literal['VeuveDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-969"
    descripteur: str = "veuve de guerre"

class Deporte(BaseModel):
    sous_descripteur: Literal['Deporte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-680"
    descripteur: str = "déporté"

class PupilleDeLaNation(BaseModel):
    sous_descripteur: Literal['PupilleDeLaNation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1399"
    descripteur: str = "pupille de la nation"

class VictimeDeGuerre(BaseModel):
    sous_descripteur: Union['PupilleDeLaNation', 'Deporte', 'VeuveDeGuerre', 'MortPourLaFrance'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-879"
    descripteur: str = "victime de guerre"

class AncienCombattant(BaseModel):
    sous_descripteur: Literal['AncienCombattant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-352"
    descripteur: str = "ancien combattant"

class InternementAdministratif(BaseModel):
    sous_descripteur: Literal['InternementAdministratif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1279"
    descripteur: str = "internement administratif"

class CampDinternement(BaseModel):
    sous_descripteur: Union['InternementAdministratif'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-324"
    descripteur: str = "camp d'internement"

class MarcheNoir(BaseModel):
    sous_descripteur: Literal['MarcheNoir']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-756"
    descripteur: str = "marché noir"

class Rationnement(BaseModel):
    sous_descripteur: Literal['Rationnement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1150"
    descripteur: str = "rationnement"

class Ravitaillement(BaseModel):
    sous_descripteur: Union['Rationnement', 'MarcheNoir'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-146"
    descripteur: str = "ravitaillement"

class Bombardement(BaseModel):
    sous_descripteur: Literal['Bombardement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-120"
    descripteur: str = "bombardement"

class RefugieDeGuerre(BaseModel):
    sous_descripteur: Literal['RefugieDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1243"
    descripteur: str = "réfugié de guerre"

class OperationMilitaire(BaseModel):
    sous_descripteur: Literal['OperationMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-8"
    descripteur: str = "opération militaire"

class Guerre(BaseModel):
    sous_descripteur: Union['OperationMilitaire', 'RefugieDeGuerre', 'Bombardement', 'Ravitaillement', 'CampDinternement', 'AncienCombattant', 'VictimeDeGuerre', 'ForcesAlliees', 'DommagesDeGuerre', 'OccupationEtrangere', 'ChantierDeLaJeunesse', 'PrisonnierDeGuerre', 'TravailContraint', 'DefensePassive', 'OeuvreDeGuerre'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1341"
    descripteur: str = "guerre"

class AideAuDeveloppement(BaseModel):
    sous_descripteur: Literal['AideAuDeveloppement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1485"
    descripteur: str = "aide au développement"

class RelationsEuropeennes(BaseModel):
    sous_descripteur: Literal['RelationsEuropeennes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-957"
    descripteur: str = "relations européennes"

class Diplomate(BaseModel):
    sous_descripteur: Literal['Diplomate']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1442"
    descripteur: str = "diplomate"

class RepresentationDiplomatique(BaseModel):
    sous_descripteur: Union['Diplomate'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-831"
    descripteur: str = "représentation diplomatique"

class OrganisationInternationale(BaseModel):
    sous_descripteur: Literal['OrganisationInternationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-612"
    descripteur: str = "organisation internationale"

class Independance(BaseModel):
    sous_descripteur: Literal['Independance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-808"
    descripteur: str = "indépendance"

class Colonisation(BaseModel):
    sous_descripteur: Literal['Colonisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-384"
    descripteur: str = "colonisation"

class Colonie(BaseModel):
    sous_descripteur: Union['Colonisation', 'Independance'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1069"
    descripteur: str = "colonie"

class AnnexionDeTerritoire(BaseModel):
    sous_descripteur: Literal['AnnexionDeTerritoire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-577"
    descripteur: str = "annexion de territoire"

class Blocus(BaseModel):
    sous_descripteur: Literal['Blocus']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-959"
    descripteur: str = "blocus"

class Frontiere(BaseModel):
    sous_descripteur: Union['Blocus', 'AnnexionDeTerritoire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-341"
    descripteur: str = "frontière"

class Francophonie(BaseModel):
    sous_descripteur: Literal['Francophonie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-15"
    descripteur: str = "francophonie"

class RelationsInternationales(BaseModel):
    sous_descripteur: Union['Francophonie', 'Frontiere', 'Colonie', 'OrganisationInternationale', 'RepresentationDiplomatique', 'RelationsEuropeennes', 'AideAuDeveloppement'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-974"
    descripteur: str = "relations internationales"

class ManoeuvreMilitaire(BaseModel):
    sous_descripteur: Literal['ManoeuvreMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1483"
    descripteur: str = "manoeuvre militaire"

class PoliceMilitaire(BaseModel):
    sous_descripteur: Literal['PoliceMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-966"
    descripteur: str = "police militaire"

class Mobilisation(BaseModel):
    sous_descripteur: Literal['Mobilisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1293"
    descripteur: str = "mobilisation"

class MilicesProvinciales(BaseModel):
    sous_descripteur: Literal['MilicesProvinciales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1280"
    descripteur: str = "milices provinciales"

class MilicesBourgeoises(BaseModel):
    sous_descripteur: Literal['MilicesBourgeoises']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-571"
    descripteur: str = "milices bourgeoises"

class GardeNationale(BaseModel):
    sous_descripteur: Literal['GardeNationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-519"
    descripteur: str = "garde nationale"

class Milices(BaseModel):
    sous_descripteur: Union['GardeNationale', 'MilicesBourgeoises', 'MilicesProvinciales'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-770"
    descripteur: str = "milices"

class GensDeGuerre(BaseModel):
    sous_descripteur: Literal['GensDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1286"
    descripteur: str = "gens de guerre"

class EcoleMilitaire(BaseModel):
    sous_descripteur: Literal['EcoleMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1006"
    descripteur: str = "école militaire"

class Demisolde(BaseModel):
    sous_descripteur: Literal['Demisolde']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-579"
    descripteur: str = "demi-solde"

class OfficierMilitaire(BaseModel):
    sous_descripteur: Literal['OfficierMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-247"
    descripteur: str = "officier militaire"

class Militaire(BaseModel):
    sous_descripteur: Union['OfficierMilitaire', 'Demisolde', 'EcoleMilitaire', 'GensDeGuerre'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1103"
    descripteur: str = "militaire"

class ArmeeDeLair(BaseModel):
    sous_descripteur: Literal['ArmeeDeLair']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1352"
    descripteur: str = "armée de l'air"

class ArmeeDeTerre(BaseModel):
    sous_descripteur: Literal['ArmeeDeTerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-977"
    descripteur: str = "armée de terre"

class LegionEtrangere(BaseModel):
    sous_descripteur: Literal['LegionEtrangere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-455"
    descripteur: str = "légion étrangère"

class Marine(BaseModel):
    sous_descripteur: Literal['Marine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-122"
    descripteur: str = "marine"

class Armee(BaseModel):
    sous_descripteur: Union['Marine', 'LegionEtrangere', 'ArmeeDeTerre', 'ArmeeDeLair'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-551"
    descripteur: str = "armée"

class RemonteMilitaire(BaseModel):
    sous_descripteur: Literal['RemonteMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1465"
    descripteur: str = "remonte militaire"

class ServiceSanitaireMilitaire(BaseModel):
    sous_descripteur: Literal['ServiceSanitaireMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-905"
    descripteur: str = "service sanitaire militaire"

class Etatmajor(BaseModel):
    sous_descripteur: Literal['Etatmajor']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-506"
    descripteur: str = "état-major"

class RequisitionsMilitaires(BaseModel):
    sous_descripteur: Literal['RequisitionsMilitaires']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1321"
    descripteur: str = "réquisitions militaires"

class EquipementMilitaire(BaseModel):
    sous_descripteur: Literal['EquipementMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-744"
    descripteur: str = "équipement militaire"

class RavitaillementMilitaire(BaseModel):
    sous_descripteur: Literal['RavitaillementMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-121"
    descripteur: str = "ravitaillement militaire"

class OrganisationDeLarmee(BaseModel):
    sous_descripteur: Union['RavitaillementMilitaire', 'EquipementMilitaire', 'RequisitionsMilitaires', 'Etatmajor', 'ServiceSanitaireMilitaire', 'RemonteMilitaire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-167"
    descripteur: str = "organisation de l'armée"

class ServiceCivique(BaseModel):
    sous_descripteur: Literal['ServiceCivique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-359"
    descripteur: str = "service civique"

class Enrolement(BaseModel):
    sous_descripteur: Literal['Enrolement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1039"
    descripteur: str = "enrôlement"

class Conscription(BaseModel):
    sous_descripteur: Literal['Conscription']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1408"
    descripteur: str = "conscription"

class RecrutementMilitaire(BaseModel):
    sous_descripteur: Union['Conscription', 'Enrolement'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-872"
    descripteur: str = "recrutement militaire"

class BaseAerienne(BaseModel):
    sous_descripteur: Literal['BaseAerienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1397"
    descripteur: str = "base aérienne"

class Arsenal(BaseModel):
    sous_descripteur: Literal['Arsenal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1119"
    descripteur: str = "arsenal"

class Caserne(BaseModel):
    sous_descripteur: Literal['Caserne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-823"
    descripteur: str = "caserne"

class CimetiereMilitaire(BaseModel):
    sous_descripteur: Literal['CimetiereMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-799"
    descripteur: str = "cimetière militaire"

class Fortification(BaseModel):
    sous_descripteur: Literal['Fortification']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-427"
    descripteur: str = "fortification"

class TerrainMilitaire(BaseModel):
    sous_descripteur: Literal['TerrainMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-358"
    descripteur: str = "terrain militaire"

class GenieMilitaire(BaseModel):
    sous_descripteur: Literal['GenieMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-12"
    descripteur: str = "génie militaire"

class InfrastructureMilitaire(BaseModel):
    sous_descripteur: Union['GenieMilitaire', 'TerrainMilitaire', 'Fortification', 'CimetiereMilitaire', 'Caserne', 'Arsenal', 'BaseAerienne'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-912"
    descripteur: str = "infrastructure militaire"

class DefenseDuTerritoire(BaseModel):
    sous_descripteur: Union['InfrastructureMilitaire', 'RecrutementMilitaire', 'ServiceCivique', 'OrganisationDeLarmee', 'Armee', 'Militaire', 'Milices', 'Mobilisation', 'PoliceMilitaire', 'ManoeuvreMilitaire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-250"
    descripteur: str = "défense du territoire"

class Exterieur(BaseModel):
    sous_descripteur: Union['DefenseDuTerritoire', 'RelationsInternationales', 'Guerre'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-150"
    descripteur: str = "extérieur"
