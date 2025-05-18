from pydantic import BaseModel
from typing import Union, Literal
                
class Justice(BaseModel):
    terme_specifique: Union['ConditionPenitentiaire', 'JusticeCivile', 'OrganisationJudiciaire', 'JusticePenale', 'DecisionDeJustice']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-483"
    descripteur: str = "justice"
class ConditionPenitentiaire(BaseModel):
    terme_specifique: Union['VisiteurDePrison', 'DisciplinePenitentiaire', 'MedecinePenitentiaire', 'EnseignementPenitentiaire', 'EtablissementPenitentiaire', 'PopulationPenitentiaire', 'TravailPenitentiaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1117"
    descripteur: str = "condition pénitentiaire"
class VisiteurDePrison(BaseModel):
    terme_specifique: Literal['VisiteurDePrison']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-2"
    descripteur: str = "visiteur de prison"
class DisciplinePenitentiaire(BaseModel):
    terme_specifique: Union['Mutinerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-80"
    descripteur: str = "discipline pénitentiaire"
class Mutinerie(BaseModel):
    terme_specifique: Literal['Mutinerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-216"
    descripteur: str = "mutinerie"
class MedecinePenitentiaire(BaseModel):
    terme_specifique: Literal['MedecinePenitentiaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-702"
    descripteur: str = "médecine pénitentiaire"
class EnseignementPenitentiaire(BaseModel):
    terme_specifique: Literal['EnseignementPenitentiaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-609"
    descripteur: str = "enseignement pénitentiaire"
class EtablissementPenitentiaire(BaseModel):
    terme_specifique: Literal['EtablissementPenitentiaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-674"
    descripteur: str = "établissement pénitentiaire"
class PopulationPenitentiaire(BaseModel):
    terme_specifique: Union['Incarceration', 'Evasion']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-737"
    descripteur: str = "population pénitentiaire"
class Incarceration(BaseModel):
    terme_specifique: Literal['Incarceration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-855"
    descripteur: str = "incarcération"
class Evasion(BaseModel):
    terme_specifique: Literal['Evasion']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1275"
    descripteur: str = "évasion"
class TravailPenitentiaire(BaseModel):
    terme_specifique: Literal['TravailPenitentiaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1148"
    descripteur: str = "travail pénitentiaire"
class JusticeCivile(BaseModel):
    terme_specifique: Union['AffaireCommerciale', 'EnregistrementJudiciaire', 'ContentieuxDeLaSecuriteSociale', 'ContentieuxAdministratif', 'ProtectionJudiciaireDeLaJeunesse', 'AffaireCivile', 'AffairePrudhomale', 'TutelleJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-892"
    descripteur: str = "justice civile"
class AffaireCommerciale(BaseModel):
    terme_specifique: Union['RedressementJudiciaire', 'Faillite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-460"
    descripteur: str = "affaire commerciale"
class RedressementJudiciaire(BaseModel):
    terme_specifique: Literal['RedressementJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-42"
    descripteur: str = "redressement judiciaire"
class Faillite(BaseModel):
    terme_specifique: Literal['Faillite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1232"
    descripteur: str = "faillite"
class EnregistrementJudiciaire(BaseModel):
    terme_specifique: Union['ProprieteIndustrielle', 'SureteMobiliere', 'IdentiteCommerciale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-369"
    descripteur: str = "enregistrement judiciaire"
class ProprieteIndustrielle(BaseModel):
    terme_specifique: Literal['ProprieteIndustrielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-68"
    descripteur: str = "propriété industrielle"
class SureteMobiliere(BaseModel):
    terme_specifique: Literal['SureteMobiliere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1283"
    descripteur: str = "sûreté mobilière"
class IdentiteCommerciale(BaseModel):
    terme_specifique: Literal['IdentiteCommerciale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-524"
    descripteur: str = "identité commerciale"
class ContentieuxDeLaSecuriteSociale(BaseModel):
    terme_specifique: Literal['ContentieuxDeLaSecuriteSociale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-46"
    descripteur: str = "contentieux de la sécurité sociale"
class ContentieuxAdministratif(BaseModel):
    terme_specifique: Union['ContentieuxFiscal', 'ContentieuxElectoral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1154"
    descripteur: str = "contentieux administratif"
class ContentieuxFiscal(BaseModel):
    terme_specifique: Literal['ContentieuxFiscal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-193"
    descripteur: str = "contentieux fiscal"
class ContentieuxElectoral(BaseModel):
    terme_specifique: Literal['ContentieuxElectoral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-169"
    descripteur: str = "contentieux électoral"
class ProtectionJudiciaireDeLaJeunesse(BaseModel):
    terme_specifique: Union['MineurSurveille', 'AssistanceEducative', 'MineurDelinquant', 'EducationSurveillee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-824"
    descripteur: str = "protection judiciaire de la jeunesse"
class MineurSurveille(BaseModel):
    terme_specifique: Literal['MineurSurveille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-566"
    descripteur: str = "mineur surveillé"
class AssistanceEducative(BaseModel):
    terme_specifique: Literal['AssistanceEducative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-336"
    descripteur: str = "assistance éducative"
class MineurDelinquant(BaseModel):
    terme_specifique: Literal['MineurDelinquant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1072"
    descripteur: str = "mineur délinquant"
class EducationSurveillee(BaseModel):
    terme_specifique: Literal['EducationSurveillee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1444"
    descripteur: str = "éducation surveillée"
class AffaireCivile(BaseModel):
    terme_specifique: Union['AffaireFamiliale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-666"
    descripteur: str = "affaire civile"
class AffaireFamiliale(BaseModel):
    terme_specifique: Literal['AffaireFamiliale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-533"
    descripteur: str = "affaire familiale"
class AffairePrudhomale(BaseModel):
    terme_specifique: Literal['AffairePrudhomale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-839"
    descripteur: str = "affaire prud'homale"
class TutelleJudiciaire(BaseModel):
    terme_specifique: Union['TutelleAuxPrestationsSociales', 'IncapableMajeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1176"
    descripteur: str = "tutelle judiciaire"
class TutelleAuxPrestationsSociales(BaseModel):
    terme_specifique: Literal['TutelleAuxPrestationsSociales']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-717"
    descripteur: str = "tutelle aux prestations sociales"
class IncapableMajeur(BaseModel):
    terme_specifique: Literal['IncapableMajeur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1118"
    descripteur: str = "incapable majeur"
class OrganisationJudiciaire(BaseModel):
    terme_specifique: Union['OfficierMinisteriel', 'Juge', 'AuxiliaireDeJustice', 'Juridiction']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-158"
    descripteur: str = "organisation judiciaire"
class OfficierMinisteriel(BaseModel):
    terme_specifique: Union['CommissairePriseur', 'Notaire', 'Avoue', 'GreffierDeCommerce', 'HuissierDeJustice']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-101"
    descripteur: str = "officier ministériel"
class CommissairePriseur(BaseModel):
    terme_specifique: Literal['CommissairePriseur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1137"
    descripteur: str = "commissaire priseur"
class Notaire(BaseModel):
    terme_specifique: Literal['Notaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-60"
    descripteur: str = "notaire"
class Avoue(BaseModel):
    terme_specifique: Literal['Avoue']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1166"
    descripteur: str = "avoué"
class GreffierDeCommerce(BaseModel):
    terme_specifique: Literal['GreffierDeCommerce']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-878"
    descripteur: str = "greffier de commerce"
class HuissierDeJustice(BaseModel):
    terme_specifique: Literal['HuissierDeJustice']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-390"
    descripteur: str = "huissier de justice"
class Juge(BaseModel):
    terme_specifique: Union['Prudhomme', 'JugeAdministratif', 'JugeConsulaire', 'OfficierDeJusticeDAncienRegime', 'JugeDePaix', 'Magistrat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-767"
    descripteur: str = "juge"
class Prudhomme(BaseModel):
    terme_specifique: Literal['Prudhomme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-51"
    descripteur: str = "prud'homme"
class JugeAdministratif(BaseModel):
    terme_specifique: Literal['JugeAdministratif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-313"
    descripteur: str = "juge administratif"
class JugeConsulaire(BaseModel):
    terme_specifique: Literal['JugeConsulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-372"
    descripteur: str = "juge consulaire"
class OfficierDeJusticeDAncienRegime(BaseModel):
    terme_specifique: Literal['OfficierDeJusticeDAncienRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-409"
    descripteur: str = "officier de justice d'Ancien Régime"
class JugeDePaix(BaseModel):
    terme_specifique: Literal['JugeDePaix']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-795"
    descripteur: str = "juge de paix"
class Magistrat(BaseModel):
    terme_specifique: Literal['Magistrat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1366"
    descripteur: str = "magistrat"
class AuxiliaireDeJustice(BaseModel):
    terme_specifique: Union['AdministrateurJudiciaire', 'ConseilJuridique', 'MediateurDeJustice', 'SyndicDeFaillite', 'OfficierDePoliceJudiciaire', 'AgentDePoliceJudiciaire', 'Conciliateur', 'Avocat', 'Greffier', 'Expert']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-487"
    descripteur: str = "auxiliaire de justice"
class AdministrateurJudiciaire(BaseModel):
    terme_specifique: Literal['AdministrateurJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-224"
    descripteur: str = "administrateur judiciaire"
class ConseilJuridique(BaseModel):
    terme_specifique: Literal['ConseilJuridique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-104"
    descripteur: str = "conseil juridique"
class MediateurDeJustice(BaseModel):
    terme_specifique: Literal['MediateurDeJustice']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-109"
    descripteur: str = "médiateur de justice"
class SyndicDeFaillite(BaseModel):
    terme_specifique: Literal['SyndicDeFaillite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-163"
    descripteur: str = "syndic de faillite"
class OfficierDePoliceJudiciaire(BaseModel):
    terme_specifique: Literal['OfficierDePoliceJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1226"
    descripteur: str = "officier de police judiciaire"
class AgentDePoliceJudiciaire(BaseModel):
    terme_specifique: Literal['AgentDePoliceJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-629"
    descripteur: str = "agent de police judiciaire"
class Conciliateur(BaseModel):
    terme_specifique: Literal['Conciliateur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1323"
    descripteur: str = "conciliateur"
class Avocat(BaseModel):
    terme_specifique: Literal['Avocat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-994"
    descripteur: str = "avocat"
class Greffier(BaseModel):
    terme_specifique: Literal['Greffier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-882"
    descripteur: str = "greffier"
class Expert(BaseModel):
    terme_specifique: Literal['Expert']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-534"
    descripteur: str = "expert"
class Juridiction(BaseModel):
    terme_specifique: Union['JusticeMilitaire', 'JusticeMunicipale', 'JusticeRoyale', 'JusticeSeigneuriale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1132"
    descripteur: str = "juridiction"
class JusticeMilitaire(BaseModel):
    terme_specifique: Literal['JusticeMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1487"
    descripteur: str = "justice militaire"
class JusticeMunicipale(BaseModel):
    terme_specifique: Literal['JusticeMunicipale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-212"
    descripteur: str = "justice municipale"
class JusticeRoyale(BaseModel):
    terme_specifique: Literal['JusticeRoyale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-569"
    descripteur: str = "justice royale"
class JusticeSeigneuriale(BaseModel):
    terme_specifique: Literal['JusticeSeigneuriale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-970"
    descripteur: str = "justice seigneuriale"
class JusticePenale(BaseModel):
    terme_specifique: Union['CrimesEtDelits', 'Criminalite', 'JuryDassises', 'QualificationCorrectionnelle', 'VictimeDinfraction', 'Delinquance', 'QualificationCriminelle', 'Contravention']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-525"
    descripteur: str = "justice pénale"
class CrimesEtDelits(BaseModel):
    terme_specifique: Union['AtteinteALaSureteDeLEtat', 'IncendieVolontaire', 'InfractionMilitaire', 'AgressionSexuelle', 'AbandonDeFamille', 'Escroquerie', 'Corruption', 'Terrorisme', 'FauxTemoignage', 'InfractionMaritime', 'AtteinteALordrePublic', 'AssociationDeMalfaiteurs', 'InfractionEconomique', 'Bigamie', 'AbandonDenfant', 'CrimeDeGuerre', 'DelitDusage', 'OutrageAuxMoeurs', 'FauxMonnayage', 'AtteinteALaDigniteDesPersonnes', 'PriseDotage', 'DegradationDeBiens', 'AtteinteAPapiersPublics', 'Meurtre', 'FauxEnEcriture', 'Vol', 'AbusDeFonction', 'CoupsEtBlessures', 'Avortement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1403"
    descripteur: str = "crimes et délits"
class AtteinteALaSureteDeLEtat(BaseModel):
    terme_specifique: Literal['AtteinteALaSureteDeLEtat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-301"
    descripteur: str = "atteinte à la sûreté de l'État"
class IncendieVolontaire(BaseModel):
    terme_specifique: Literal['IncendieVolontaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-25"
    descripteur: str = "incendie volontaire"
class InfractionMilitaire(BaseModel):
    terme_specifique: Literal['InfractionMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-61"
    descripteur: str = "infraction militaire"
class AgressionSexuelle(BaseModel):
    terme_specifique: Literal['AgressionSexuelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-142"
    descripteur: str = "agression sexuelle"
class AbandonDeFamille(BaseModel):
    terme_specifique: Literal['AbandonDeFamille']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-215"
    descripteur: str = "abandon de famille"
class Escroquerie(BaseModel):
    terme_specifique: Literal['Escroquerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-296"
    descripteur: str = "escroquerie"
class Corruption(BaseModel):
    terme_specifique: Literal['Corruption']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-316"
    descripteur: str = "corruption"
class Terrorisme(BaseModel):
    terme_specifique: Literal['Terrorisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-320"
    descripteur: str = "terrorisme"
class FauxTemoignage(BaseModel):
    terme_specifique: Literal['FauxTemoignage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-364"
    descripteur: str = "faux témoignage"
class InfractionMaritime(BaseModel):
    terme_specifique: Literal['InfractionMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-394"
    descripteur: str = "infraction maritime"
class AtteinteALordrePublic(BaseModel):
    terme_specifique: Literal['AtteinteALordrePublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-707"
    descripteur: str = "atteinte à l'ordre public"
class AssociationDeMalfaiteurs(BaseModel):
    terme_specifique: Literal['AssociationDeMalfaiteurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-504"
    descripteur: str = "association de malfaiteurs"
class InfractionEconomique(BaseModel):
    terme_specifique: Literal['InfractionEconomique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-809"
    descripteur: str = "infraction économique"
class Bigamie(BaseModel):
    terme_specifique: Literal['Bigamie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-557"
    descripteur: str = "bigamie"
class AbandonDenfant(BaseModel):
    terme_specifique: Literal['AbandonDenfant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-588"
    descripteur: str = "abandon d'enfant"
class CrimeDeGuerre(BaseModel):
    terme_specifique: Literal['CrimeDeGuerre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-619"
    descripteur: str = "crime de guerre"
class DelitDusage(BaseModel):
    terme_specifique: Literal['DelitDusage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-659"
    descripteur: str = "délit d'usage"
class OutrageAuxMoeurs(BaseModel):
    terme_specifique: Literal['OutrageAuxMoeurs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-751"
    descripteur: str = "outrage aux moeurs"
class FauxMonnayage(BaseModel):
    terme_specifique: Literal['FauxMonnayage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-759"
    descripteur: str = "faux monnayage"
class AtteinteALaDigniteDesPersonnes(BaseModel):
    terme_specifique: Literal['AtteinteALaDigniteDesPersonnes']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-877"
    descripteur: str = "atteinte à la dignité des personnes"
class PriseDotage(BaseModel):
    terme_specifique: Literal['PriseDotage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1436"
    descripteur: str = "prise d'otage"
class DegradationDeBiens(BaseModel):
    terme_specifique: Literal['DegradationDeBiens']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-992"
    descripteur: str = "dégradation de biens"
class AtteinteAPapiersPublics(BaseModel):
    terme_specifique: Literal['AtteinteAPapiersPublics']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1048"
    descripteur: str = "atteinte à papiers publics"
class Meurtre(BaseModel):
    terme_specifique: Literal['Meurtre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1080"
    descripteur: str = "meurtre"
class FauxEnEcriture(BaseModel):
    terme_specifique: Literal['FauxEnEcriture']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1156"
    descripteur: str = "faux en écriture"
class Vol(BaseModel):
    terme_specifique: Literal['Vol']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1164"
    descripteur: str = "vol"
class AbusDeFonction(BaseModel):
    terme_specifique: Literal['AbusDeFonction']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1224"
    descripteur: str = "abus de fonction"
class CoupsEtBlessures(BaseModel):
    terme_specifique: Literal['CoupsEtBlessures']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1392"
    descripteur: str = "coups et blessures"
class Avortement(BaseModel):
    terme_specifique: Literal['Avortement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1421"
    descripteur: str = "avortement"
class Criminalite(BaseModel):
    terme_specifique: Literal['Criminalite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-235"
    descripteur: str = "criminalité"
class JuryDassises(BaseModel):
    terme_specifique: Literal['JuryDassises']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-264"
    descripteur: str = "jury d'assises"
class QualificationCorrectionnelle(BaseModel):
    terme_specifique: Literal['QualificationCorrectionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-331"
    descripteur: str = "qualification correctionnelle"
class VictimeDinfraction(BaseModel):
    terme_specifique: Literal['VictimeDinfraction']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1014"
    descripteur: str = "victime d'infraction"
class Delinquance(BaseModel):
    terme_specifique: Literal['Delinquance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1458"
    descripteur: str = "délinquance"
class QualificationCriminelle(BaseModel):
    terme_specifique: Literal['QualificationCriminelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1084"
    descripteur: str = "qualification criminelle"
class Contravention(BaseModel):
    terme_specifique: Literal['Contravention']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1381"
    descripteur: str = "contravention"
class DecisionDeJustice(BaseModel):
    terme_specifique: Union['ApplicationDesPeines', 'Peine', 'Acquittement', 'Extradition', 'Appel', 'Nonlieu', 'Saisie', 'ClassementSansSuite', 'VenteJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1242"
    descripteur: str = "décision de justice"
class ApplicationDesPeines(BaseModel):
    terme_specifique: Union['Probation', 'Rehabilitation', 'Amnistie', 'LiberationConditionnelle', 'Grace']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-996"
    descripteur: str = "application des peines"
class Probation(BaseModel):
    terme_specifique: Literal['Probation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-26"
    descripteur: str = "probation"
class Rehabilitation(BaseModel):
    terme_specifique: Literal['Rehabilitation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-392"
    descripteur: str = "réhabilitation"
class Amnistie(BaseModel):
    terme_specifique: Literal['Amnistie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-408"
    descripteur: str = "amnistie"
class LiberationConditionnelle(BaseModel):
    terme_specifique: Literal['LiberationConditionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1162"
    descripteur: str = "libération conditionnelle"
class Grace(BaseModel):
    terme_specifique: Literal['Grace']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-822"
    descripteur: str = "grâce"
class Peine(BaseModel):
    terme_specifique: Union['ReclusionCriminelle', 'Bannissement', 'Amende', 'Galeres', 'TravauxForces', 'PeineDeSubstitution', 'PeineCapitale', 'PeineCorporelle', 'AssignationAResidence']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-615"
    descripteur: str = "peine"
class ReclusionCriminelle(BaseModel):
    terme_specifique: Literal['ReclusionCriminelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-270"
    descripteur: str = "réclusion criminelle"
class Bannissement(BaseModel):
    terme_specifique: Literal['Bannissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-345"
    descripteur: str = "bannissement"
class Amende(BaseModel):
    terme_specifique: Literal['Amende']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-388"
    descripteur: str = "amende"
class Galeres(BaseModel):
    terme_specifique: Literal['Galeres']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-613"
    descripteur: str = "galères"
class TravauxForces(BaseModel):
    terme_specifique: Literal['TravauxForces']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-758"
    descripteur: str = "travaux forcés"
class PeineDeSubstitution(BaseModel):
    terme_specifique: Literal['PeineDeSubstitution']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-746"
    descripteur: str = "peine de substitution"
class PeineCapitale(BaseModel):
    terme_specifique: Literal['PeineCapitale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1009"
    descripteur: str = "peine capitale"
class PeineCorporelle(BaseModel):
    terme_specifique: Literal['PeineCorporelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1447"
    descripteur: str = "peine corporelle"
class AssignationAResidence(BaseModel):
    terme_specifique: Literal['AssignationAResidence']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1432"
    descripteur: str = "assignation à résidence"
class Acquittement(BaseModel):
    terme_specifique: Literal['Acquittement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-429"
    descripteur: str = "acquittement"
class Extradition(BaseModel):
    terme_specifique: Literal['Extradition']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-477"
    descripteur: str = "extradition"
class Appel(BaseModel):
    terme_specifique: Literal['Appel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-828"
    descripteur: str = "appel"
class Nonlieu(BaseModel):
    terme_specifique: Literal['Nonlieu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-880"
    descripteur: str = "non-lieu"
class Saisie(BaseModel):
    terme_specifique: Literal['Saisie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-924"
    descripteur: str = "saisie"
class ClassementSansSuite(BaseModel):
    terme_specifique: Literal['ClassementSansSuite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1037"
    descripteur: str = "classement sans suite"
class VenteJudiciaire(BaseModel):
    terme_specifique: Literal['VenteJudiciaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1285"
    descripteur: str = "vente judiciaire"
