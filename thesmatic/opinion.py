from pydantic import BaseModel
from typing import Union, Literal
                
class Opinion(BaseModel):
    terme_specifique: Union['ViePublique', 'ViePolitique', 'MouvementDidees', 'VieReligieuse', 'Election', 'CroyancesEtSciencesParalleles']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-906"
    descripteur: str = "opinion"
class ViePublique(BaseModel):
    terme_specifique: Union['Association', 'Donsetlegs', 'SocieteRevolutionnaire', 'CeremoniePublique', 'Presse', 'RelationsPubliques', 'SocieteSecrete', 'Personnalite', 'SymboliqueOfficielle', 'Censure', 'OpinionPublique', 'Jumelage', 'Propagande', 'Secte', 'Commemoration', 'BaptemeCivil', 'DistinctionHonorifique', 'Armoiries', 'ManifestationPublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1174"
    descripteur: str = "vie publique"
class Association(BaseModel):
    terme_specifique: Union['Fondation', 'AssociationReconnueDutilitePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-760"
    descripteur: str = "association"
class Fondation(BaseModel):
    terme_specifique: Literal['Fondation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1379"
    descripteur: str = "fondation"
class AssociationReconnueDutilitePublique(BaseModel):
    terme_specifique: Literal['AssociationReconnueDutilitePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-997"
    descripteur: str = "association reconnue d'utilité publique"
class Donsetlegs(BaseModel):
    terme_specifique: Literal['Donsetlegs']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-838"
    descripteur: str = "dons-et-legs"
class SocieteRevolutionnaire(BaseModel):
    terme_specifique: Literal['SocieteRevolutionnaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-16"
    descripteur: str = "société révolutionnaire"
class CeremoniePublique(BaseModel):
    terme_specifique: Union['VisiteOfficielle', 'EntreeSolennelle', 'PrierePublique', 'ReceptionOfficielle', 'Inauguration', 'CeremonieMilitaire', 'DeuilPublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-21"
    descripteur: str = "cérémonie publique"
class VisiteOfficielle(BaseModel):
    terme_specifique: Literal['VisiteOfficielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-606"
    descripteur: str = "visite officielle"
class EntreeSolennelle(BaseModel):
    terme_specifique: Literal['EntreeSolennelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-936"
    descripteur: str = "entrée solennelle"
class PrierePublique(BaseModel):
    terme_specifique: Literal['PrierePublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1310"
    descripteur: str = "prière publique"
class ReceptionOfficielle(BaseModel):
    terme_specifique: Literal['ReceptionOfficielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-194"
    descripteur: str = "réception officielle"
class Inauguration(BaseModel):
    terme_specifique: Literal['Inauguration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1335"
    descripteur: str = "inauguration"
class CeremonieMilitaire(BaseModel):
    terme_specifique: Literal['CeremonieMilitaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1486"
    descripteur: str = "cérémonie militaire"
class DeuilPublic(BaseModel):
    terme_specifique: Literal['DeuilPublic']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1488"
    descripteur: str = "deuil public"
class Presse(BaseModel):
    terme_specifique: Union['ReporterPhotographe', 'DepotLegal', 'Journaliste', 'PublicationInterne', 'PresseRegionale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-140"
    descripteur: str = "presse"
class ReporterPhotographe(BaseModel):
    terme_specifique: Literal['ReporterPhotographe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-576"
    descripteur: str = "reporter photographe"
class DepotLegal(BaseModel):
    terme_specifique: Literal['DepotLegal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-813"
    descripteur: str = "dépôt légal"
class Journaliste(BaseModel):
    terme_specifique: Literal['Journaliste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1186"
    descripteur: str = "journaliste"
class PublicationInterne(BaseModel):
    terme_specifique: Literal['PublicationInterne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-968"
    descripteur: str = "publication interne"
class PresseRegionale(BaseModel):
    terme_specifique: Literal['PresseRegionale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1358"
    descripteur: str = "presse régionale"
class RelationsPubliques(BaseModel):
    terme_specifique: Union['InterventionDelu', 'CommunicationInstitutionnelle', 'RelationsAvecLesUsagers']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1388"
    descripteur: str = "relations publiques"
class InterventionDelu(BaseModel):
    terme_specifique: Literal['InterventionDelu']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-685"
    descripteur: str = "intervention d'élu"
class CommunicationInstitutionnelle(BaseModel):
    terme_specifique: Literal['CommunicationInstitutionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-308"
    descripteur: str = "communication institutionnelle"
class RelationsAvecLesUsagers(BaseModel):
    terme_specifique: Literal['RelationsAvecLesUsagers']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-761"
    descripteur: str = "relations avec les usagers"
class SocieteSecrete(BaseModel):
    terme_specifique: Union['FrancMaeon']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-370"
    descripteur: str = "société secrète"
class FrancMaeon(BaseModel):
    terme_specifique: Literal['FrancMaeon']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-361"
    descripteur: str = "franc maçon"
class Personnalite(BaseModel):
    terme_specifique: Literal['Personnalite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-473"
    descripteur: str = "personnalité"
class SymboliqueOfficielle(BaseModel):
    terme_specifique: Union['CostumeOfficiel', 'HymneNational', 'Drapeau', 'FeteNationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1126"
    descripteur: str = "symbolique officielle"
class CostumeOfficiel(BaseModel):
    terme_specifique: Literal['CostumeOfficiel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-515"
    descripteur: str = "costume officiel"
class HymneNational(BaseModel):
    terme_specifique: Literal['HymneNational']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-660"
    descripteur: str = "hymne national"
class Drapeau(BaseModel):
    terme_specifique: Literal['Drapeau']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-757"
    descripteur: str = "drapeau"
class FeteNationale(BaseModel):
    terme_specifique: Literal['FeteNationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1125"
    descripteur: str = "fête nationale"
class Censure(BaseModel):
    terme_specifique: Literal['Censure']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-528"
    descripteur: str = "censure"
class OpinionPublique(BaseModel):
    terme_specifique: Literal['OpinionPublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-681"
    descripteur: str = "opinion publique"
class Jumelage(BaseModel):
    terme_specifique: Literal['Jumelage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-753"
    descripteur: str = "jumelage"
class Propagande(BaseModel):
    terme_specifique: Literal['Propagande']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1274"
    descripteur: str = "propagande"
class Secte(BaseModel):
    terme_specifique: Literal['Secte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-818"
    descripteur: str = "secte"
class Commemoration(BaseModel):
    terme_specifique: Literal['Commemoration']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-953"
    descripteur: str = "commémoration"
class BaptemeCivil(BaseModel):
    terme_specifique: Literal['BaptemeCivil']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1124"
    descripteur: str = "baptême civil"
class DistinctionHonorifique(BaseModel):
    terme_specifique: Literal['DistinctionHonorifique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1200"
    descripteur: str = "distinction honorifique"
class Armoiries(BaseModel):
    terme_specifique: Literal['Armoiries']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1478"
    descripteur: str = "armoiries"
class ManifestationPublique(BaseModel):
    terme_specifique: Union['ReunionPublique', 'ManifestationDeProtestation', 'MouvementPopulaire', 'ManifestationAntinationale', 'ManifestationDadhesionAuRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1489"
    descripteur: str = "manifestation publique"
class ReunionPublique(BaseModel):
    terme_specifique: Literal['ReunionPublique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-891"
    descripteur: str = "réunion publique"
class ManifestationDeProtestation(BaseModel):
    terme_specifique: Literal['ManifestationDeProtestation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-796"
    descripteur: str = "manifestation de protestation"
class MouvementPopulaire(BaseModel):
    terme_specifique: Literal['MouvementPopulaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1153"
    descripteur: str = "mouvement populaire"
class ManifestationAntinationale(BaseModel):
    terme_specifique: Literal['ManifestationAntinationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1490"
    descripteur: str = "manifestation antinationale"
class ManifestationDadhesionAuRegime(BaseModel):
    terme_specifique: Literal['ManifestationDadhesionAuRegime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1491"
    descripteur: str = "manifestation d'adhésion au régime"
class ViePolitique(BaseModel):
    terme_specifique: Union['ActeDopposition', 'PartiPolitique', 'MouvementPolitiqueEtSocietal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-22"
    descripteur: str = "vie politique"
class ActeDopposition(BaseModel):
    terme_specifique: Union['ChansonSubversive', 'ProposSubversif', 'Clandestinite', 'EcritSubversif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-727"
    descripteur: str = "acte d'opposition"
class ChansonSubversive(BaseModel):
    terme_specifique: Literal['ChansonSubversive']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-18"
    descripteur: str = "chanson subversive"
class ProposSubversif(BaseModel):
    terme_specifique: Literal['ProposSubversif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-249"
    descripteur: str = "propos subversif"
class Clandestinite(BaseModel):
    terme_specifique: Literal['Clandestinite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-382"
    descripteur: str = "clandestinité"
class EcritSubversif(BaseModel):
    terme_specifique: Literal['EcritSubversif']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-729"
    descripteur: str = "écrit subversif"
class PartiPolitique(BaseModel):
    terme_specifique: Union['MilitantPolitique', 'CongresPolitique', 'Dissident']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1169"
    descripteur: str = "parti politique"
class MilitantPolitique(BaseModel):
    terme_specifique: Literal['MilitantPolitique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-78"
    descripteur: str = "militant politique"
class CongresPolitique(BaseModel):
    terme_specifique: Literal['CongresPolitique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-363"
    descripteur: str = "congrès politique"
class Dissident(BaseModel):
    terme_specifique: Literal['Dissident']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-821"
    descripteur: str = "dissident"
class MouvementPolitiqueEtSocietal(BaseModel):
    terme_specifique: Union['MouvementLanque', 'Fascisme', 'Centrisme', 'Republicanisme', 'Socialisme', 'Anticapitalisme', 'Anarchisme', 'Nationalisme', 'MouvementEcologiste', 'Colonialisme', 'Communisme', 'Gaullisme', 'MouvementRegionaliste', 'MouvementEtudiant', 'Clericalisme', 'MouvementOuvrier', 'Liberalisme', 'Radicalisme', 'ExtremeDroite', 'ExtremeGauche', 'Royalisme', 'Bonapartisme', 'MouvementFeministe', 'MouvementAutonomiste', 'MouvementHomosexuel', 'MouvementPacifiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-87"
    descripteur: str = "mouvement politique et sociétal"
class MouvementLanque(BaseModel):
    terme_specifique: Literal['MouvementLanque']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-70"
    descripteur: str = "mouvement laïque"
class Fascisme(BaseModel):
    terme_specifique: Literal['Fascisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-919"
    descripteur: str = "fascisme"
class Centrisme(BaseModel):
    terme_specifique: Literal['Centrisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-110"
    descripteur: str = "centrisme"
class Republicanisme(BaseModel):
    terme_specifique: Literal['Republicanisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-170"
    descripteur: str = "républicanisme"
class Socialisme(BaseModel):
    terme_specifique: Literal['Socialisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1021"
    descripteur: str = "socialisme"
class Anticapitalisme(BaseModel):
    terme_specifique: Literal['Anticapitalisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-288"
    descripteur: str = "anticapitalisme"
class Anarchisme(BaseModel):
    terme_specifique: Literal['Anarchisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-634"
    descripteur: str = "anarchisme"
class Nationalisme(BaseModel):
    terme_specifique: Literal['Nationalisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1278"
    descripteur: str = "nationalisme"
class MouvementEcologiste(BaseModel):
    terme_specifique: Literal['MouvementEcologiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1177"
    descripteur: str = "mouvement écologiste"
class Colonialisme(BaseModel):
    terme_specifique: Literal['Colonialisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-538"
    descripteur: str = "colonialisme"
class Communisme(BaseModel):
    terme_specifique: Literal['Communisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-526"
    descripteur: str = "communisme"
class Gaullisme(BaseModel):
    terme_specifique: Literal['Gaullisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-605"
    descripteur: str = "gaullisme"
class MouvementRegionaliste(BaseModel):
    terme_specifique: Literal['MouvementRegionaliste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-720"
    descripteur: str = "mouvement régionaliste"
class MouvementEtudiant(BaseModel):
    terme_specifique: Literal['MouvementEtudiant']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1339"
    descripteur: str = "mouvement étudiant"
class Clericalisme(BaseModel):
    terme_specifique: Literal['Clericalisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-197"
    descripteur: str = "cléricalisme"
class MouvementOuvrier(BaseModel):
    terme_specifique: Literal['MouvementOuvrier']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-391"
    descripteur: str = "mouvement ouvrier"
class Liberalisme(BaseModel):
    terme_specifique: Literal['Liberalisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-266"
    descripteur: str = "libéralisme"
class Radicalisme(BaseModel):
    terme_specifique: Literal['Radicalisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1390"
    descripteur: str = "radicalisme"
class ExtremeDroite(BaseModel):
    terme_specifique: Literal['ExtremeDroite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1322"
    descripteur: str = "extrême droite"
class ExtremeGauche(BaseModel):
    terme_specifique: Literal['ExtremeGauche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1207"
    descripteur: str = "extrême gauche"
class Royalisme(BaseModel):
    terme_specifique: Literal['Royalisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-229"
    descripteur: str = "royalisme"
class Bonapartisme(BaseModel):
    terme_specifique: Literal['Bonapartisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-174"
    descripteur: str = "bonapartisme"
class MouvementFeministe(BaseModel):
    terme_specifique: Literal['MouvementFeministe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1218"
    descripteur: str = "mouvement féministe"
class MouvementAutonomiste(BaseModel):
    terme_specifique: Literal['MouvementAutonomiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-803"
    descripteur: str = "mouvement autonomiste"
class MouvementHomosexuel(BaseModel):
    terme_specifique: Literal['MouvementHomosexuel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-115"
    descripteur: str = "mouvement homosexuel"
class MouvementPacifiste(BaseModel):
    terme_specifique: Literal['MouvementPacifiste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-318"
    descripteur: str = "mouvement pacifiste"
class MouvementDidees(BaseModel):
    terme_specifique: Union['VieIntellectuelle', 'Philosophie', 'Tolerance', 'DroitsDeLhomme', 'Atheisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-33"
    descripteur: str = "mouvement d'idées"
class VieIntellectuelle(BaseModel):
    terme_specifique: Literal['VieIntellectuelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-896"
    descripteur: str = "vie intellectuelle"
class Philosophie(BaseModel):
    terme_specifique: Literal['Philosophie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-143"
    descripteur: str = "philosophie"
class Tolerance(BaseModel):
    terme_specifique: Union['PersecutionReligieuse', 'Antisemitisme', 'Racisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-453"
    descripteur: str = "tolérance"
class PersecutionReligieuse(BaseModel):
    terme_specifique: Literal['PersecutionReligieuse']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-181"
    descripteur: str = "persécution religieuse"
class Antisemitisme(BaseModel):
    terme_specifique: Literal['Antisemitisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1297"
    descripteur: str = "antisémitisme"
class Racisme(BaseModel):
    terme_specifique: Literal['Racisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-496"
    descripteur: str = "racisme"
class DroitsDeLhomme(BaseModel):
    terme_specifique: Literal['DroitsDeLhomme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1239"
    descripteur: str = "droits de l'homme"
class Atheisme(BaseModel):
    terme_specifique: Literal['Atheisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1247"
    descripteur: str = "athéisme"
class VieReligieuse(BaseModel):
    terme_specifique: Union['PratiqueReligieuse', 'AssociationCultuelle', 'InstitutionEcclesiastique', 'ManifestationAntireligieuse', 'VieSpirituelle', 'Presbytere', 'Culte', 'MinistreDuCulte', 'EdificeCultuel', 'TemporelEcclesiastique', 'Heresie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-804"
    descripteur: str = "vie religieuse"
class PratiqueReligieuse(BaseModel):
    terme_specifique: Union['Pelerinage', 'ServiceReligieux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-128"
    descripteur: str = "pratique religieuse"
class Pelerinage(BaseModel):
    terme_specifique: Literal['Pelerinage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1492"
    descripteur: str = "pèlerinage"
class ServiceReligieux(BaseModel):
    terme_specifique: Literal['ServiceReligieux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1493"
    descripteur: str = "service religieux"
class AssociationCultuelle(BaseModel):
    terme_specifique: Union['Congregation', 'Confrerie', 'SocieteDeCharite', 'Tiersordre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-74"
    descripteur: str = "association cultuelle"
class Congregation(BaseModel):
    terme_specifique: Literal['Congregation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-633"
    descripteur: str = "congrégation"
class Confrerie(BaseModel):
    terme_specifique: Literal['Confrerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-58"
    descripteur: str = "confrérie"
class SocieteDeCharite(BaseModel):
    terme_specifique: Literal['SocieteDeCharite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1391"
    descripteur: str = "société de charité"
class Tiersordre(BaseModel):
    terme_specifique: Literal['Tiersordre']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-917"
    descripteur: str = "tiers-ordre"
class InstitutionEcclesiastique(BaseModel):
    terme_specifique: Union['CirconscriptionEcclesiastique', 'AssembleeGeneraleDuClerge', 'InstitutionMonastique', 'Inquisition', 'FabriqueDeglise', 'AdministrationDiocesaine', 'SeminaireReligieux', 'Papaute', 'Missions', 'Concile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-793"
    descripteur: str = "institution ecclésiastique"
class CirconscriptionEcclesiastique(BaseModel):
    terme_specifique: Literal['CirconscriptionEcclesiastique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-66"
    descripteur: str = "circonscription ecclésiastique"
class AssembleeGeneraleDuClerge(BaseModel):
    terme_specifique: Literal['AssembleeGeneraleDuClerge']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-407"
    descripteur: str = "assemblée générale du clergé"
class InstitutionMonastique(BaseModel):
    terme_specifique: Literal['InstitutionMonastique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-529"
    descripteur: str = "institution monastique"
class Inquisition(BaseModel):
    terme_specifique: Literal['Inquisition']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-539"
    descripteur: str = "inquisition"
class FabriqueDeglise(BaseModel):
    terme_specifique: Literal['FabriqueDeglise']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-811"
    descripteur: str = "fabrique d'église"
class AdministrationDiocesaine(BaseModel):
    terme_specifique: Literal['AdministrationDiocesaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1053"
    descripteur: str = "administration diocésaine"
class SeminaireReligieux(BaseModel):
    terme_specifique: Literal['SeminaireReligieux']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-967"
    descripteur: str = "séminaire religieux"
class Papaute(BaseModel):
    terme_specifique: Literal['Papaute']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-918"
    descripteur: str = "papauté"
class Missions(BaseModel):
    terme_specifique: Literal['Missions']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1291"
    descripteur: str = "missions"
class Concile(BaseModel):
    terme_specifique: Literal['Concile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1183"
    descripteur: str = "concile"
class ManifestationAntireligieuse(BaseModel):
    terme_specifique: Union['Impiete']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-485"
    descripteur: str = "manifestation antireligieuse"
class Impiete(BaseModel):
    terme_specifique: Literal['Impiete']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-69"
    descripteur: str = "impiété"
class VieSpirituelle(BaseModel):
    terme_specifique: Union['Miracle', 'Mysticisme', 'Spiritualite', 'Theologie', 'LivreSaint']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1210"
    descripteur: str = "vie spirituelle"
class Miracle(BaseModel):
    terme_specifique: Literal['Miracle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-165"
    descripteur: str = "miracle"
class Mysticisme(BaseModel):
    terme_specifique: Literal['Mysticisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-530"
    descripteur: str = "mysticisme"
class Spiritualite(BaseModel):
    terme_specifique: Literal['Spiritualite']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-552"
    descripteur: str = "spiritualité"
class Theologie(BaseModel):
    terme_specifique: Literal['Theologie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1197"
    descripteur: str = "théologie"
class LivreSaint(BaseModel):
    terme_specifique: Literal['LivreSaint']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1305"
    descripteur: str = "livre saint"
class Presbytere(BaseModel):
    terme_specifique: Literal['Presbytere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-257"
    descripteur: str = "presbytère"
class Culte(BaseModel):
    terme_specifique: Union['Judansme', 'Hindouisme', 'Islam', 'Chamanisme', 'Catholicisme', 'ReligionOrthodoxe', 'Bouddhisme', 'Protestantisme', 'Taonsme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1179"
    descripteur: str = "culte"
class Judansme(BaseModel):
    terme_specifique: Literal['Judansme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-281"
    descripteur: str = "judaïsme"
class Hindouisme(BaseModel):
    terme_specifique: Literal['Hindouisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-303"
    descripteur: str = "hindouisme"
class Islam(BaseModel):
    terme_specifique: Literal['Islam']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-636"
    descripteur: str = "islam"
class Chamanisme(BaseModel):
    terme_specifique: Literal['Chamanisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-716"
    descripteur: str = "chamanisme"
class Catholicisme(BaseModel):
    terme_specifique: Literal['Catholicisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-740"
    descripteur: str = "catholicisme"
class ReligionOrthodoxe(BaseModel):
    terme_specifique: Literal['ReligionOrthodoxe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-980"
    descripteur: str = "religion orthodoxe"
class Bouddhisme(BaseModel):
    terme_specifique: Literal['Bouddhisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1175"
    descripteur: str = "bouddhisme"
class Protestantisme(BaseModel):
    terme_specifique: Literal['Protestantisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1367"
    descripteur: str = "protestantisme"
class Taonsme(BaseModel):
    terme_specifique: Literal['Taonsme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1401"
    descripteur: str = "taoïsme"
class MinistreDuCulte(BaseModel):
    terme_specifique: Literal['MinistreDuCulte']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-424"
    descripteur: str = "ministre du culte"
class EdificeCultuel(BaseModel):
    terme_specifique: Literal['EdificeCultuel']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-820"
    descripteur: str = "édifice cultuel"
class TemporelEcclesiastique(BaseModel):
    terme_specifique: Literal['TemporelEcclesiastique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-864"
    descripteur: str = "temporel ecclésiastique"
class Heresie(BaseModel):
    terme_specifique: Literal['Heresie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1369"
    descripteur: str = "hérésie"
class Election(BaseModel):
    terme_specifique: Union['ElectionSociale', 'Elu', 'ElectionPolitique', 'CampagneElectorale', 'Electeur', 'DecoupageElectoral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1152"
    descripteur: str = "élection"
class ElectionSociale(BaseModel):
    terme_specifique: Union['ElectionProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1214"
    descripteur: str = "élection sociale"
class ElectionProfessionnelle(BaseModel):
    terme_specifique: Literal['ElectionProfessionnelle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1061"
    descripteur: str = "élection professionnelle"
class Elu(BaseModel):
    terme_specifique: Union['PresidentDuConseilRegional', 'ConseillerRegional', 'Maire', 'ConseillerMunicipal', 'Parlementaire', 'PresidentDuConseilGeneral', 'ConseillerGeneral', 'ConseillerDarrondissement', 'Echevin', 'PresidentDetablissementPublicDeCooperationIntercommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-868"
    descripteur: str = "élu"
class PresidentDuConseilRegional(BaseModel):
    terme_specifique: Literal['PresidentDuConseilRegional']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-54"
    descripteur: str = "président du conseil régional"
class ConseillerRegional(BaseModel):
    terme_specifique: Literal['ConseillerRegional']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1382"
    descripteur: str = "conseiller régional"
class Maire(BaseModel):
    terme_specifique: Literal['Maire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1251"
    descripteur: str = "maire"
class ConseillerMunicipal(BaseModel):
    terme_specifique: Literal['ConseillerMunicipal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1188"
    descripteur: str = "conseiller municipal"
class Parlementaire(BaseModel):
    terme_specifique: Literal['Parlementaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-902"
    descripteur: str = "parlementaire"
class PresidentDuConseilGeneral(BaseModel):
    terme_specifique: Literal['PresidentDuConseilGeneral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1250"
    descripteur: str = "président du conseil général"
class ConseillerGeneral(BaseModel):
    terme_specifique: Literal['ConseillerGeneral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-721"
    descripteur: str = "conseiller général"
class ConseillerDarrondissement(BaseModel):
    terme_specifique: Literal['ConseillerDarrondissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-438"
    descripteur: str = "conseiller d'arrondissement"
class Echevin(BaseModel):
    terme_specifique: Literal['Echevin']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-512"
    descripteur: str = "échevin"
class PresidentDetablissementPublicDeCooperationIntercommunale(BaseModel):
    terme_specifique: Literal['PresidentDetablissementPublicDeCooperationIntercommunale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-893"
    descripteur: str = "président d'établissement public de coopération intercommunale"
class ElectionPolitique(BaseModel):
    terme_specifique: Union['ElectionRegionale', 'ElectionCantonale', 'ElectionMunicipale', 'ElectionEuropeenne', 'ElectionPresidentielle', 'ElectionSenatoriale', 'Referendum', 'ElectionAuConseilDarrondissement', 'ElectionLegislative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-107"
    descripteur: str = "élection politique"
class ElectionRegionale(BaseModel):
    terme_specifique: Literal['ElectionRegionale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1081"
    descripteur: str = "élection régionale"
class ElectionCantonale(BaseModel):
    terme_specifique: Literal['ElectionCantonale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-923"
    descripteur: str = "élection cantonale"
class ElectionMunicipale(BaseModel):
    terme_specifique: Literal['ElectionMunicipale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-171"
    descripteur: str = "élection municipale"
class ElectionEuropeenne(BaseModel):
    terme_specifique: Literal['ElectionEuropeenne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-870"
    descripteur: str = "élection européenne"
class ElectionPresidentielle(BaseModel):
    terme_specifique: Literal['ElectionPresidentielle']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-624"
    descripteur: str = "élection présidentielle"
class ElectionSenatoriale(BaseModel):
    terme_specifique: Literal['ElectionSenatoriale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1383"
    descripteur: str = "élection sénatoriale"
class Referendum(BaseModel):
    terme_specifique: Literal['Referendum']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-321"
    descripteur: str = "référendum"
class ElectionAuConseilDarrondissement(BaseModel):
    terme_specifique: Literal['ElectionAuConseilDarrondissement']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-401"
    descripteur: str = "élection au conseil d'arrondissement"
class ElectionLegislative(BaseModel):
    terme_specifique: Literal['ElectionLegislative']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1254"
    descripteur: str = "élection législative"
class CampagneElectorale(BaseModel):
    terme_specifique: Literal['CampagneElectorale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-177"
    descripteur: str = "campagne électorale"
class Electeur(BaseModel):
    terme_specifique: Union['DroitsCiviques', 'CollegeElectoral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-450"
    descripteur: str = "électeur"
class DroitsCiviques(BaseModel):
    terme_specifique: Literal['DroitsCiviques']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-911"
    descripteur: str = "droits civiques"
class CollegeElectoral(BaseModel):
    terme_specifique: Literal['CollegeElectoral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-675"
    descripteur: str = "collège électoral"
class DecoupageElectoral(BaseModel):
    terme_specifique: Literal['DecoupageElectoral']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-459"
    descripteur: str = "découpage électoral"
class CroyancesEtSciencesParalleles(BaseModel):
    terme_specifique: Union['SciencesParalleles', 'CroyancesPopulaires', 'Magie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1439"
    descripteur: str = "croyances et sciences parallèles"
class SciencesParalleles(BaseModel):
    terme_specifique: Union['Esoterisme', 'Astrologie', 'Alchimie', 'Graphologie', 'Spiritisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-172"
    descripteur: str = "sciences parallèles"
class Esoterisme(BaseModel):
    terme_specifique: Literal['Esoterisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-39"
    descripteur: str = "ésotérisme"
class Astrologie(BaseModel):
    terme_specifique: Literal['Astrologie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1111"
    descripteur: str = "astrologie"
class Alchimie(BaseModel):
    terme_specifique: Literal['Alchimie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-784"
    descripteur: str = "alchimie"
class Graphologie(BaseModel):
    terme_specifique: Literal['Graphologie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-386"
    descripteur: str = "graphologie"
class Spiritisme(BaseModel):
    terme_specifique: Literal['Spiritisme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-901"
    descripteur: str = "spiritisme"
class CroyancesPopulaires(BaseModel):
    terme_specifique: Union['Mythe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1015"
    descripteur: str = "croyances populaires"
class Mythe(BaseModel):
    terme_specifique: Literal['Mythe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1046"
    descripteur: str = "mythe"
class Magie(BaseModel):
    terme_specifique: Union['Sorcellerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1364"
    descripteur: str = "magie"
class Sorcellerie(BaseModel):
    terme_specifique: Literal['Sorcellerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-836"
    descripteur: str = "sorcellerie"
