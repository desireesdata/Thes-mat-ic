from pydantic import BaseModel
from typing import Union, Literal

class OeuvreDeGuerre(BaseModel):
    terme_specifique: Literal['OeuvreDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1020"
    descripteur: str = "oeuvre de guerre"

class Abri(BaseModel):
    terme_specifique: Literal['Abri']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1195"
    descripteur: str = "abri"

class DefensePassive(BaseModel):
    terme_specifique: Union['Abri']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-989"
    descripteur: str = "défense passive"

class TravailContraint(BaseModel):
    terme_specifique: Literal['TravailContraint']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-979"
    descripteur: str = "travail contraint"

class PrisonnierDeGuerre(BaseModel):
    terme_specifique: Literal['PrisonnierDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-563"
    descripteur: str = "prisonnier de guerre"

class ChantierDeLaJeunesse(BaseModel):
    terme_specifique: Literal['ChantierDeLaJeunesse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-699"
    descripteur: str = "chantier de la jeunesse"

class AutoriteDoccupation(BaseModel):
    terme_specifique: Literal['AutoriteDoccupation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1202"
    descripteur: str = "autorité d'occupation"

class Collaboration(BaseModel):
    terme_specifique: Literal['Collaboration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-830"
    descripteur: str = "collaboration"

class Resistance(BaseModel):
    terme_specifique: Literal['Resistance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1231"
    descripteur: str = "résistance"

class Epuration(BaseModel):
    terme_specifique: Literal['Epuration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-494"
    descripteur: str = "épuration"

class OccupationEtrangere(BaseModel):
    terme_specifique: Union['Epuration', 'Resistance', 'Collaboration', 'AutoriteDoccupation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-788"
    descripteur: str = "occupation étrangère"

class BienSinistre(BaseModel):
    terme_specifique: Literal['BienSinistre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1255"
    descripteur: str = "bien sinistré"

class BienSpolie(BaseModel):
    terme_specifique: Literal['BienSpolie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-725"
    descripteur: str = "bien spolié"

class DommagesDeGuerre(BaseModel):
    terme_specifique: Union['BienSpolie', 'BienSinistre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1453"
    descripteur: str = "dommages de guerre"

class ForcesAlliees(BaseModel):
    terme_specifique: Literal['ForcesAlliees']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-402"
    descripteur: str = "forces alliées"

class MortPourLaFrance(BaseModel):
    terme_specifique: Literal['MortPourLaFrance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1484"
    descripteur: str = "mort pour la France"

class VeuveDeGuerre(BaseModel):
    terme_specifique: Literal['VeuveDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-969"
    descripteur: str = "veuve de guerre"

class Deporte(BaseModel):
    terme_specifique: Literal['Deporte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-680"
    descripteur: str = "déporté"

class PupilleDeLaNation(BaseModel):
    terme_specifique: Literal['PupilleDeLaNation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1399"
    descripteur: str = "pupille de la nation"

class VictimeDeGuerre(BaseModel):
    terme_specifique: Union['PupilleDeLaNation', 'Deporte', 'VeuveDeGuerre', 'MortPourLaFrance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-879"
    descripteur: str = "victime de guerre"

class AncienCombattant(BaseModel):
    terme_specifique: Literal['AncienCombattant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-352"
    descripteur: str = "ancien combattant"

class InternementAdministratif(BaseModel):
    terme_specifique: Literal['InternementAdministratif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1279"
    descripteur: str = "internement administratif"

class CampDinternement(BaseModel):
    terme_specifique: Union['InternementAdministratif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-324"
    descripteur: str = "camp d'internement"

class MarcheNoir(BaseModel):
    terme_specifique: Literal['MarcheNoir']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-756"
    descripteur: str = "marché noir"

class Rationnement(BaseModel):
    terme_specifique: Literal['Rationnement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1150"
    descripteur: str = "rationnement"

class Ravitaillement(BaseModel):
    terme_specifique: Union['Rationnement', 'MarcheNoir']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-146"
    descripteur: str = "ravitaillement"

class Bombardement(BaseModel):
    terme_specifique: Literal['Bombardement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-120"
    descripteur: str = "bombardement"

class RefugieDeGuerre(BaseModel):
    terme_specifique: Literal['RefugieDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1243"
    descripteur: str = "réfugié de guerre"

class OperationMilitaire(BaseModel):
    terme_specifique: Literal['OperationMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-8"
    descripteur: str = "opération militaire"

class Guerre(BaseModel):
    terme_specifique: Union['OperationMilitaire', 'RefugieDeGuerre', 'Bombardement', 'Ravitaillement', 'CampDinternement', 'AncienCombattant', 'VictimeDeGuerre', 'ForcesAlliees', 'DommagesDeGuerre', 'OccupationEtrangere', 'ChantierDeLaJeunesse', 'PrisonnierDeGuerre', 'TravailContraint', 'DefensePassive', 'OeuvreDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1341"
    descripteur: str = "guerre"

class AideAuDeveloppement(BaseModel):
    terme_specifique: Literal['AideAuDeveloppement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1485"
    descripteur: str = "aide au développement"

class RelationsEuropeennes(BaseModel):
    terme_specifique: Literal['RelationsEuropeennes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-957"
    descripteur: str = "relations européennes"

class Diplomate(BaseModel):
    terme_specifique: Literal['Diplomate']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1442"
    descripteur: str = "diplomate"

class RepresentationDiplomatique(BaseModel):
    terme_specifique: Union['Diplomate']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-831"
    descripteur: str = "représentation diplomatique"

class OrganisationInternationale(BaseModel):
    terme_specifique: Literal['OrganisationInternationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-612"
    descripteur: str = "organisation internationale"

class Independance(BaseModel):
    terme_specifique: Literal['Independance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-808"
    descripteur: str = "indépendance"

class Colonisation(BaseModel):
    terme_specifique: Literal['Colonisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-384"
    descripteur: str = "colonisation"

class Colonie(BaseModel):
    terme_specifique: Union['Colonisation', 'Independance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1069"
    descripteur: str = "colonie"

class AnnexionDeTerritoire(BaseModel):
    terme_specifique: Literal['AnnexionDeTerritoire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-577"
    descripteur: str = "annexion de territoire"

class Blocus(BaseModel):
    terme_specifique: Literal['Blocus']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-959"
    descripteur: str = "blocus"

class Frontiere(BaseModel):
    terme_specifique: Union['Blocus', 'AnnexionDeTerritoire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-341"
    descripteur: str = "frontière"

class Francophonie(BaseModel):
    terme_specifique: Literal['Francophonie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-15"
    descripteur: str = "francophonie"

class RelationsInternationales(BaseModel):
    terme_specifique: Union['Francophonie', 'Frontiere', 'Colonie', 'OrganisationInternationale', 'RepresentationDiplomatique', 'RelationsEuropeennes', 'AideAuDeveloppement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-974"
    descripteur: str = "relations internationales"

class ManoeuvreMilitaire(BaseModel):
    terme_specifique: Literal['ManoeuvreMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1483"
    descripteur: str = "manoeuvre militaire"

class PoliceMilitaire(BaseModel):
    terme_specifique: Literal['PoliceMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-966"
    descripteur: str = "police militaire"

class Mobilisation(BaseModel):
    terme_specifique: Literal['Mobilisation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1293"
    descripteur: str = "mobilisation"

class MilicesProvinciales(BaseModel):
    terme_specifique: Literal['MilicesProvinciales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1280"
    descripteur: str = "milices provinciales"

class MilicesBourgeoises(BaseModel):
    terme_specifique: Literal['MilicesBourgeoises']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-571"
    descripteur: str = "milices bourgeoises"

class GardeNationale(BaseModel):
    terme_specifique: Literal['GardeNationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-519"
    descripteur: str = "garde nationale"

class Milices(BaseModel):
    terme_specifique: Union['GardeNationale', 'MilicesBourgeoises', 'MilicesProvinciales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-770"
    descripteur: str = "milices"

class GensDeGuerre(BaseModel):
    terme_specifique: Literal['GensDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1286"
    descripteur: str = "gens de guerre"

class EcoleMilitaire(BaseModel):
    terme_specifique: Literal['EcoleMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1006"
    descripteur: str = "école militaire"

class Demisolde(BaseModel):
    terme_specifique: Literal['Demisolde']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-579"
    descripteur: str = "demi-solde"

class OfficierMilitaire(BaseModel):
    terme_specifique: Literal['OfficierMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-247"
    descripteur: str = "officier militaire"

class Militaire(BaseModel):
    terme_specifique: Union['OfficierMilitaire', 'Demisolde', 'EcoleMilitaire', 'GensDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1103"
    descripteur: str = "militaire"

class ArmeeDeLair(BaseModel):
    terme_specifique: Literal['ArmeeDeLair']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1352"
    descripteur: str = "armée de l'air"

class ArmeeDeTerre(BaseModel):
    terme_specifique: Literal['ArmeeDeTerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-977"
    descripteur: str = "armée de terre"

class LegionEtrangere(BaseModel):
    terme_specifique: Literal['LegionEtrangere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-455"
    descripteur: str = "légion étrangère"

class Marine(BaseModel):
    terme_specifique: Literal['Marine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-122"
    descripteur: str = "marine"

class Armee(BaseModel):
    terme_specifique: Union['Marine', 'LegionEtrangere', 'ArmeeDeTerre', 'ArmeeDeLair']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-551"
    descripteur: str = "armée"

class RemonteMilitaire(BaseModel):
    terme_specifique: Literal['RemonteMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1465"
    descripteur: str = "remonte militaire"

class ServiceSanitaireMilitaire(BaseModel):
    terme_specifique: Literal['ServiceSanitaireMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-905"
    descripteur: str = "service sanitaire militaire"

class Etatmajor(BaseModel):
    terme_specifique: Literal['Etatmajor']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-506"
    descripteur: str = "état-major"

class RequisitionsMilitaires(BaseModel):
    terme_specifique: Literal['RequisitionsMilitaires']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1321"
    descripteur: str = "réquisitions militaires"

class EquipementMilitaire(BaseModel):
    terme_specifique: Literal['EquipementMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-744"
    descripteur: str = "équipement militaire"

class RavitaillementMilitaire(BaseModel):
    terme_specifique: Literal['RavitaillementMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-121"
    descripteur: str = "ravitaillement militaire"

class OrganisationDeLarmee(BaseModel):
    terme_specifique: Union['RavitaillementMilitaire', 'EquipementMilitaire', 'RequisitionsMilitaires', 'Etatmajor', 'ServiceSanitaireMilitaire', 'RemonteMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-167"
    descripteur: str = "organisation de l'armée"

class ServiceCivique(BaseModel):
    terme_specifique: Literal['ServiceCivique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-359"
    descripteur: str = "service civique"

class Enrolement(BaseModel):
    terme_specifique: Literal['Enrolement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1039"
    descripteur: str = "enrôlement"

class Conscription(BaseModel):
    terme_specifique: Literal['Conscription']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1408"
    descripteur: str = "conscription"

class RecrutementMilitaire(BaseModel):
    terme_specifique: Union['Conscription', 'Enrolement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-872"
    descripteur: str = "recrutement militaire"

class BaseAerienne(BaseModel):
    terme_specifique: Literal['BaseAerienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1397"
    descripteur: str = "base aérienne"

class Arsenal(BaseModel):
    terme_specifique: Literal['Arsenal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1119"
    descripteur: str = "arsenal"

class Caserne(BaseModel):
    terme_specifique: Literal['Caserne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-823"
    descripteur: str = "caserne"

class CimetiereMilitaire(BaseModel):
    terme_specifique: Literal['CimetiereMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-799"
    descripteur: str = "cimetière militaire"

class Fortification(BaseModel):
    terme_specifique: Literal['Fortification']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-427"
    descripteur: str = "fortification"

class TerrainMilitaire(BaseModel):
    terme_specifique: Literal['TerrainMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-358"
    descripteur: str = "terrain militaire"

class GenieMilitaire(BaseModel):
    terme_specifique: Literal['GenieMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-12"
    descripteur: str = "génie militaire"

class InfrastructureMilitaire(BaseModel):
    terme_specifique: Union['GenieMilitaire', 'TerrainMilitaire', 'Fortification', 'CimetiereMilitaire', 'Caserne', 'Arsenal', 'BaseAerienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-912"
    descripteur: str = "infrastructure militaire"

class DefenseDuTerritoire(BaseModel):
    terme_specifique: Union['InfrastructureMilitaire', 'RecrutementMilitaire', 'ServiceCivique', 'OrganisationDeLarmee', 'Armee', 'Militaire', 'Milices', 'Mobilisation', 'PoliceMilitaire', 'ManoeuvreMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-250"
    descripteur: str = "défense du territoire"

class Exterieur(BaseModel):
    terme_specifique: Union['DefenseDuTerritoire', 'RelationsInternationales', 'Guerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-150"
    descripteur: str = "extérieur"
