from pydantic import BaseModel
from typing import Union, Literal

class VenteJudiciaire(BaseModel):
    sous_descripteur: Literal['VenteJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1285"
    descripteur: str = "vente judiciaire"

class ClassementSansSuite(BaseModel):
    sous_descripteur: Literal['ClassementSansSuite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1037"
    descripteur: str = "classement sans suite"

class Saisie(BaseModel):
    sous_descripteur: Literal['Saisie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-924"
    descripteur: str = "saisie"

class Nonlieu(BaseModel):
    sous_descripteur: Literal['Nonlieu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-880"
    descripteur: str = "non-lieu"

class Appel(BaseModel):
    sous_descripteur: Literal['Appel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-828"
    descripteur: str = "appel"

class Extradition(BaseModel):
    sous_descripteur: Literal['Extradition']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-477"
    descripteur: str = "extradition"

class Acquittement(BaseModel):
    sous_descripteur: Literal['Acquittement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-429"
    descripteur: str = "acquittement"

class AssignationAResidence(BaseModel):
    sous_descripteur: Literal['AssignationAResidence']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1432"
    descripteur: str = "assignation à résidence"

class PeineCorporelle(BaseModel):
    sous_descripteur: Literal['PeineCorporelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1447"
    descripteur: str = "peine corporelle"

class PeineCapitale(BaseModel):
    sous_descripteur: Literal['PeineCapitale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1009"
    descripteur: str = "peine capitale"

class PeineDeSubstitution(BaseModel):
    sous_descripteur: Literal['PeineDeSubstitution']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-746"
    descripteur: str = "peine de substitution"

class TravauxForces(BaseModel):
    sous_descripteur: Literal['TravauxForces']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-758"
    descripteur: str = "travaux forcés"

class Galeres(BaseModel):
    sous_descripteur: Literal['Galeres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-613"
    descripteur: str = "galères"

class Amende(BaseModel):
    sous_descripteur: Literal['Amende']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-388"
    descripteur: str = "amende"

class Bannissement(BaseModel):
    sous_descripteur: Literal['Bannissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-345"
    descripteur: str = "bannissement"

class ReclusionCriminelle(BaseModel):
    sous_descripteur: Literal['ReclusionCriminelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-270"
    descripteur: str = "réclusion criminelle"

class Peine(BaseModel):
    sous_descripteur: Union['ReclusionCriminelle', 'Bannissement', 'Amende', 'Galeres', 'TravauxForces', 'PeineDeSubstitution', 'PeineCapitale', 'PeineCorporelle', 'AssignationAResidence'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-615"
    descripteur: str = "peine"

class Grace(BaseModel):
    sous_descripteur: Literal['Grace']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-822"
    descripteur: str = "grâce"

class LiberationConditionnelle(BaseModel):
    sous_descripteur: Literal['LiberationConditionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1162"
    descripteur: str = "libération conditionnelle"

class Amnistie(BaseModel):
    sous_descripteur: Literal['Amnistie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-408"
    descripteur: str = "amnistie"

class Rehabilitation(BaseModel):
    sous_descripteur: Literal['Rehabilitation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-392"
    descripteur: str = "réhabilitation"

class Probation(BaseModel):
    sous_descripteur: Literal['Probation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-26"
    descripteur: str = "probation"

class ApplicationDesPeines(BaseModel):
    sous_descripteur: Union['Probation', 'Rehabilitation', 'Amnistie', 'LiberationConditionnelle', 'Grace'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-996"
    descripteur: str = "application des peines"

class DecisionDeJustice(BaseModel):
    sous_descripteur: Union['ApplicationDesPeines', 'Peine', 'Acquittement', 'Extradition', 'Appel', 'Nonlieu', 'Saisie', 'ClassementSansSuite', 'VenteJudiciaire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1242"
    descripteur: str = "décision de justice"

class Contravention(BaseModel):
    sous_descripteur: Literal['Contravention']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1381"
    descripteur: str = "contravention"

class QualificationCriminelle(BaseModel):
    sous_descripteur: Literal['QualificationCriminelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1084"
    descripteur: str = "qualification criminelle"

class Delinquance(BaseModel):
    sous_descripteur: Literal['Delinquance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1458"
    descripteur: str = "délinquance"

class VictimeDinfraction(BaseModel):
    sous_descripteur: Literal['VictimeDinfraction']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1014"
    descripteur: str = "victime d'infraction"

class QualificationCorrectionnelle(BaseModel):
    sous_descripteur: Literal['QualificationCorrectionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-331"
    descripteur: str = "qualification correctionnelle"

class JuryDassises(BaseModel):
    sous_descripteur: Literal['JuryDassises']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-264"
    descripteur: str = "jury d'assises"

class Criminalite(BaseModel):
    sous_descripteur: Literal['Criminalite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-235"
    descripteur: str = "criminalité"

class Avortement(BaseModel):
    sous_descripteur: Literal['Avortement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1421"
    descripteur: str = "avortement"

class CoupsEtBlessures(BaseModel):
    sous_descripteur: Literal['CoupsEtBlessures']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1392"
    descripteur: str = "coups et blessures"

class AbusDeFonction(BaseModel):
    sous_descripteur: Literal['AbusDeFonction']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1224"
    descripteur: str = "abus de fonction"

class Vol(BaseModel):
    sous_descripteur: Literal['Vol']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1164"
    descripteur: str = "vol"

class FauxEnEcriture(BaseModel):
    sous_descripteur: Literal['FauxEnEcriture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1156"
    descripteur: str = "faux en écriture"

class Meurtre(BaseModel):
    sous_descripteur: Literal['Meurtre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1080"
    descripteur: str = "meurtre"

class AtteinteAPapiersPublics(BaseModel):
    sous_descripteur: Literal['AtteinteAPapiersPublics']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1048"
    descripteur: str = "atteinte à papiers publics"

class DegradationDeBiens(BaseModel):
    sous_descripteur: Literal['DegradationDeBiens']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-992"
    descripteur: str = "dégradation de biens"

class PriseDotage(BaseModel):
    sous_descripteur: Literal['PriseDotage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1436"
    descripteur: str = "prise d'otage"

class AtteinteALaDigniteDesPersonnes(BaseModel):
    sous_descripteur: Literal['AtteinteALaDigniteDesPersonnes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-877"
    descripteur: str = "atteinte à la dignité des personnes"

class FauxMonnayage(BaseModel):
    sous_descripteur: Literal['FauxMonnayage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-759"
    descripteur: str = "faux monnayage"

class OutrageAuxMoeurs(BaseModel):
    sous_descripteur: Literal['OutrageAuxMoeurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-751"
    descripteur: str = "outrage aux moeurs"

class DelitDusage(BaseModel):
    sous_descripteur: Literal['DelitDusage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-659"
    descripteur: str = "délit d'usage"

class CrimeDeGuerre(BaseModel):
    sous_descripteur: Literal['CrimeDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-619"
    descripteur: str = "crime de guerre"

class AbandonDenfant(BaseModel):
    sous_descripteur: Literal['AbandonDenfant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-588"
    descripteur: str = "abandon d'enfant"

class Bigamie(BaseModel):
    sous_descripteur: Literal['Bigamie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-557"
    descripteur: str = "bigamie"

class InfractionEconomique(BaseModel):
    sous_descripteur: Literal['InfractionEconomique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-809"
    descripteur: str = "infraction économique"

class AssociationDeMalfaiteurs(BaseModel):
    sous_descripteur: Literal['AssociationDeMalfaiteurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-504"
    descripteur: str = "association de malfaiteurs"

class AtteinteALordrePublic(BaseModel):
    sous_descripteur: Literal['AtteinteALordrePublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-707"
    descripteur: str = "atteinte à l'ordre public"

class InfractionMaritime(BaseModel):
    sous_descripteur: Literal['InfractionMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-394"
    descripteur: str = "infraction maritime"

class FauxTemoignage(BaseModel):
    sous_descripteur: Literal['FauxTemoignage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-364"
    descripteur: str = "faux témoignage"

class Terrorisme(BaseModel):
    sous_descripteur: Literal['Terrorisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-320"
    descripteur: str = "terrorisme"

class Corruption(BaseModel):
    sous_descripteur: Literal['Corruption']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-316"
    descripteur: str = "corruption"

class Escroquerie(BaseModel):
    sous_descripteur: Literal['Escroquerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-296"
    descripteur: str = "escroquerie"

class AbandonDeFamille(BaseModel):
    sous_descripteur: Literal['AbandonDeFamille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-215"
    descripteur: str = "abandon de famille"

class AgressionSexuelle(BaseModel):
    sous_descripteur: Literal['AgressionSexuelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-142"
    descripteur: str = "agression sexuelle"

class InfractionMilitaire(BaseModel):
    sous_descripteur: Literal['InfractionMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-61"
    descripteur: str = "infraction militaire"

class IncendieVolontaire(BaseModel):
    sous_descripteur: Literal['IncendieVolontaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-25"
    descripteur: str = "incendie volontaire"

class AtteinteALaSureteDeLEtat(BaseModel):
    sous_descripteur: Literal['AtteinteALaSureteDeLEtat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-301"
    descripteur: str = "atteinte à la sûreté de l'État"

class CrimesEtDelits(BaseModel):
    sous_descripteur: Union['AtteinteALaSureteDeLEtat', 'IncendieVolontaire', 'InfractionMilitaire', 'AgressionSexuelle', 'AbandonDeFamille', 'Escroquerie', 'Corruption', 'Terrorisme', 'FauxTemoignage', 'InfractionMaritime', 'AtteinteALordrePublic', 'AssociationDeMalfaiteurs', 'InfractionEconomique', 'Bigamie', 'AbandonDenfant', 'CrimeDeGuerre', 'DelitDusage', 'OutrageAuxMoeurs', 'FauxMonnayage', 'AtteinteALaDigniteDesPersonnes', 'PriseDotage', 'DegradationDeBiens', 'AtteinteAPapiersPublics', 'Meurtre', 'FauxEnEcriture', 'Vol', 'AbusDeFonction', 'CoupsEtBlessures', 'Avortement'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1403"
    descripteur: str = "crimes et délits"

class JusticePenale(BaseModel):
    sous_descripteur: Union['CrimesEtDelits', 'Criminalite', 'JuryDassises', 'QualificationCorrectionnelle', 'VictimeDinfraction', 'Delinquance', 'QualificationCriminelle', 'Contravention'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-525"
    descripteur: str = "justice pénale"

class JusticeSeigneuriale(BaseModel):
    sous_descripteur: Literal['JusticeSeigneuriale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-970"
    descripteur: str = "justice seigneuriale"

class JusticeRoyale(BaseModel):
    sous_descripteur: Literal['JusticeRoyale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-569"
    descripteur: str = "justice royale"

class JusticeMunicipale(BaseModel):
    sous_descripteur: Literal['JusticeMunicipale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-212"
    descripteur: str = "justice municipale"

class JusticeMilitaire(BaseModel):
    sous_descripteur: Literal['JusticeMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1487"
    descripteur: str = "justice militaire"

class Juridiction(BaseModel):
    sous_descripteur: Union['JusticeMilitaire', 'JusticeMunicipale', 'JusticeRoyale', 'JusticeSeigneuriale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1132"
    descripteur: str = "juridiction"

class Expert(BaseModel):
    sous_descripteur: Literal['Expert']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-534"
    descripteur: str = "expert"

class Greffier(BaseModel):
    sous_descripteur: Literal['Greffier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-882"
    descripteur: str = "greffier"

class Avocat(BaseModel):
    sous_descripteur: Literal['Avocat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-994"
    descripteur: str = "avocat"

class Conciliateur(BaseModel):
    sous_descripteur: Literal['Conciliateur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1323"
    descripteur: str = "conciliateur"

class AgentDePoliceJudiciaire(BaseModel):
    sous_descripteur: Literal['AgentDePoliceJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-629"
    descripteur: str = "agent de police judiciaire"

class OfficierDePoliceJudiciaire(BaseModel):
    sous_descripteur: Literal['OfficierDePoliceJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1226"
    descripteur: str = "officier de police judiciaire"

class SyndicDeFaillite(BaseModel):
    sous_descripteur: Literal['SyndicDeFaillite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-163"
    descripteur: str = "syndic de faillite"

class MediateurDeJustice(BaseModel):
    sous_descripteur: Literal['MediateurDeJustice']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-109"
    descripteur: str = "médiateur de justice"

class ConseilJuridique(BaseModel):
    sous_descripteur: Literal['ConseilJuridique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-104"
    descripteur: str = "conseil juridique"

class AdministrateurJudiciaire(BaseModel):
    sous_descripteur: Literal['AdministrateurJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-224"
    descripteur: str = "administrateur judiciaire"

class AuxiliaireDeJustice(BaseModel):
    sous_descripteur: Union['AdministrateurJudiciaire', 'ConseilJuridique', 'MediateurDeJustice', 'SyndicDeFaillite', 'OfficierDePoliceJudiciaire', 'AgentDePoliceJudiciaire', 'Conciliateur', 'Avocat', 'Greffier', 'Expert'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-487"
    descripteur: str = "auxiliaire de justice"

class Magistrat(BaseModel):
    sous_descripteur: Literal['Magistrat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1366"
    descripteur: str = "magistrat"

class JugeDePaix(BaseModel):
    sous_descripteur: Literal['JugeDePaix']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-795"
    descripteur: str = "juge de paix"

class OfficierDeJusticeDAncienRegime(BaseModel):
    sous_descripteur: Literal['OfficierDeJusticeDAncienRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-409"
    descripteur: str = "officier de justice d'Ancien Régime"

class JugeConsulaire(BaseModel):
    sous_descripteur: Literal['JugeConsulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-372"
    descripteur: str = "juge consulaire"

class JugeAdministratif(BaseModel):
    sous_descripteur: Literal['JugeAdministratif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-313"
    descripteur: str = "juge administratif"

class Prudhomme(BaseModel):
    sous_descripteur: Literal['Prudhomme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-51"
    descripteur: str = "prud'homme"

class Juge(BaseModel):
    sous_descripteur: Union['Prudhomme', 'JugeAdministratif', 'JugeConsulaire', 'OfficierDeJusticeDAncienRegime', 'JugeDePaix', 'Magistrat'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-767"
    descripteur: str = "juge"

class HuissierDeJustice(BaseModel):
    sous_descripteur: Literal['HuissierDeJustice']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-390"
    descripteur: str = "huissier de justice"

class GreffierDeCommerce(BaseModel):
    sous_descripteur: Literal['GreffierDeCommerce']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-878"
    descripteur: str = "greffier de commerce"

class Avoue(BaseModel):
    sous_descripteur: Literal['Avoue']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1166"
    descripteur: str = "avoué"

class Notaire(BaseModel):
    sous_descripteur: Literal['Notaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-60"
    descripteur: str = "notaire"

class CommissairePriseur(BaseModel):
    sous_descripteur: Literal['CommissairePriseur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1137"
    descripteur: str = "commissaire priseur"

class OfficierMinisteriel(BaseModel):
    sous_descripteur: Union['CommissairePriseur', 'Notaire', 'Avoue', 'GreffierDeCommerce', 'HuissierDeJustice'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-101"
    descripteur: str = "officier ministériel"

class OrganisationJudiciaire(BaseModel):
    sous_descripteur: Union['OfficierMinisteriel', 'Juge', 'AuxiliaireDeJustice', 'Juridiction'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-158"
    descripteur: str = "organisation judiciaire"

class IncapableMajeur(BaseModel):
    sous_descripteur: Literal['IncapableMajeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1118"
    descripteur: str = "incapable majeur"

class TutelleAuxPrestationsSociales(BaseModel):
    sous_descripteur: Literal['TutelleAuxPrestationsSociales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-717"
    descripteur: str = "tutelle aux prestations sociales"

class TutelleJudiciaire(BaseModel):
    sous_descripteur: Union['TutelleAuxPrestationsSociales', 'IncapableMajeur'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1176"
    descripteur: str = "tutelle judiciaire"

class AffairePrudhomale(BaseModel):
    sous_descripteur: Literal['AffairePrudhomale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-839"
    descripteur: str = "affaire prud'homale"

class AffaireFamiliale(BaseModel):
    sous_descripteur: Literal['AffaireFamiliale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-533"
    descripteur: str = "affaire familiale"

class AffaireCivile(BaseModel):
    sous_descripteur: Union['AffaireFamiliale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-666"
    descripteur: str = "affaire civile"

class EducationSurveillee(BaseModel):
    sous_descripteur: Literal['EducationSurveillee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1444"
    descripteur: str = "éducation surveillée"

class MineurDelinquant(BaseModel):
    sous_descripteur: Literal['MineurDelinquant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1072"
    descripteur: str = "mineur délinquant"

class AssistanceEducative(BaseModel):
    sous_descripteur: Literal['AssistanceEducative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-336"
    descripteur: str = "assistance éducative"

class MineurSurveille(BaseModel):
    sous_descripteur: Literal['MineurSurveille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-566"
    descripteur: str = "mineur surveillé"

class ProtectionJudiciaireDeLaJeunesse(BaseModel):
    sous_descripteur: Union['MineurSurveille', 'AssistanceEducative', 'MineurDelinquant', 'EducationSurveillee'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-824"
    descripteur: str = "protection judiciaire de la jeunesse"

class ContentieuxElectoral(BaseModel):
    sous_descripteur: Literal['ContentieuxElectoral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-169"
    descripteur: str = "contentieux électoral"

class ContentieuxFiscal(BaseModel):
    sous_descripteur: Literal['ContentieuxFiscal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-193"
    descripteur: str = "contentieux fiscal"

class ContentieuxAdministratif(BaseModel):
    sous_descripteur: Union['ContentieuxFiscal', 'ContentieuxElectoral'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1154"
    descripteur: str = "contentieux administratif"

class ContentieuxDeLaSecuriteSociale(BaseModel):
    sous_descripteur: Literal['ContentieuxDeLaSecuriteSociale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-46"
    descripteur: str = "contentieux de la sécurité sociale"

class IdentiteCommerciale(BaseModel):
    sous_descripteur: Literal['IdentiteCommerciale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-524"
    descripteur: str = "identité commerciale"

class SureteMobiliere(BaseModel):
    sous_descripteur: Literal['SureteMobiliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1283"
    descripteur: str = "sûreté mobilière"

class ProprieteIndustrielle(BaseModel):
    sous_descripteur: Literal['ProprieteIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-68"
    descripteur: str = "propriété industrielle"

class EnregistrementJudiciaire(BaseModel):
    sous_descripteur: Union['ProprieteIndustrielle', 'SureteMobiliere', 'IdentiteCommerciale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-369"
    descripteur: str = "enregistrement judiciaire"

class Faillite(BaseModel):
    sous_descripteur: Literal['Faillite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1232"
    descripteur: str = "faillite"

class RedressementJudiciaire(BaseModel):
    sous_descripteur: Literal['RedressementJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-42"
    descripteur: str = "redressement judiciaire"

class AffaireCommerciale(BaseModel):
    sous_descripteur: Union['RedressementJudiciaire', 'Faillite'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-460"
    descripteur: str = "affaire commerciale"

class JusticeCivile(BaseModel):
    sous_descripteur: Union['AffaireCommerciale', 'EnregistrementJudiciaire', 'ContentieuxDeLaSecuriteSociale', 'ContentieuxAdministratif', 'ProtectionJudiciaireDeLaJeunesse', 'AffaireCivile', 'AffairePrudhomale', 'TutelleJudiciaire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-892"
    descripteur: str = "justice civile"

class TravailPenitentiaire(BaseModel):
    sous_descripteur: Literal['TravailPenitentiaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1148"
    descripteur: str = "travail pénitentiaire"

class Evasion(BaseModel):
    sous_descripteur: Literal['Evasion']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1275"
    descripteur: str = "évasion"

class Incarceration(BaseModel):
    sous_descripteur: Literal['Incarceration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-855"
    descripteur: str = "incarcération"

class PopulationPenitentiaire(BaseModel):
    sous_descripteur: Union['Incarceration', 'Evasion'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-737"
    descripteur: str = "population pénitentiaire"

class EtablissementPenitentiaire(BaseModel):
    sous_descripteur: Literal['EtablissementPenitentiaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-674"
    descripteur: str = "établissement pénitentiaire"

class EnseignementPenitentiaire(BaseModel):
    sous_descripteur: Literal['EnseignementPenitentiaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-609"
    descripteur: str = "enseignement pénitentiaire"

class MedecinePenitentiaire(BaseModel):
    sous_descripteur: Literal['MedecinePenitentiaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-702"
    descripteur: str = "médecine pénitentiaire"

class Mutinerie(BaseModel):
    sous_descripteur: Literal['Mutinerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-216"
    descripteur: str = "mutinerie"

class DisciplinePenitentiaire(BaseModel):
    sous_descripteur: Union['Mutinerie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-80"
    descripteur: str = "discipline pénitentiaire"

class VisiteurDePrison(BaseModel):
    sous_descripteur: Literal['VisiteurDePrison']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-2"
    descripteur: str = "visiteur de prison"

class ConditionPenitentiaire(BaseModel):
    sous_descripteur: Union['VisiteurDePrison', 'DisciplinePenitentiaire', 'MedecinePenitentiaire', 'EnseignementPenitentiaire', 'EtablissementPenitentiaire', 'PopulationPenitentiaire', 'TravailPenitentiaire'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1117"
    descripteur: str = "condition pénitentiaire"

class Justice(BaseModel):
    sous_descripteur: Union['ConditionPenitentiaire', 'JusticeCivile', 'OrganisationJudiciaire', 'JusticePenale', 'DecisionDeJustice'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-483"
    descripteur: str = "justice"
