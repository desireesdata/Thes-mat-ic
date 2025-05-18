from pydantic import BaseModel
from typing import Union, Literal
                
class Communications(BaseModel):
    terme_specifique: Union['Transport', 'Messagerie']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-503"
    descripteur: str = "communications"
class Transport(BaseModel):
    terme_specifique: Union['CirculationRoutiere', 'ChauffeurDeTaxi', 'TransportFerroviaire', 'Port', 'VehiculeAutomobile', 'TransportMultimodal', 'TransportMaritime', 'BateauDePlaisance', 'TransportEnCommun', 'Automobiliste', 'Aeronef', 'BateauDeNavigationInterieure', 'TransportFluvial', 'Navire', 'TransportADosDhomme', 'TransportAerien', 'TransportParAnimal', 'VehiculeADeuxRoues', 'TransportRoutier', 'Pilote', 'Aerodrome', 'CirculationUrbaine', 'Gare']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-548"
    descripteur: str = "transport"
class CirculationRoutiere(BaseModel):
    terme_specifique: Union['SignalisationRoutiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1050"
    descripteur: str = "circulation routière"
class SignalisationRoutiere(BaseModel):
    terme_specifique: Literal['SignalisationRoutiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1076"
    descripteur: str = "signalisation routière"
class ChauffeurDeTaxi(BaseModel):
    terme_specifique: Literal['ChauffeurDeTaxi']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-617"
    descripteur: str = "chauffeur de taxi"
class TransportFerroviaire(BaseModel):
    terme_specifique: Union['LigneDeCheminDeFer', 'LiaisonFerreeInternationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-164"
    descripteur: str = "transport ferroviaire"
class LigneDeCheminDeFer(BaseModel):
    terme_specifique: Literal['LigneDeCheminDeFer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-139"
    descripteur: str = "ligne de chemin de fer"
class LiaisonFerreeInternationale(BaseModel):
    terme_specifique: Literal['LiaisonFerreeInternationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-493"
    descripteur: str = "liaison ferrée internationale"
class Port(BaseModel):
    terme_specifique: Union['InfrastructurePortuaire', 'PortDePeche', 'PortMaritime', 'Docker', 'PortDeCommerce', 'PortFluvial', 'PortDePlaisance', 'OfficierDePort']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-231"
    descripteur: str = "port"
class InfrastructurePortuaire(BaseModel):
    terme_specifique: Literal['InfrastructurePortuaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-277"
    descripteur: str = "infrastructure portuaire"
class PortDePeche(BaseModel):
    terme_specifique: Literal['PortDePeche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-156"
    descripteur: str = "port de pêche"
class PortMaritime(BaseModel):
    terme_specifique: Literal['PortMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-597"
    descripteur: str = "port maritime"
class Docker(BaseModel):
    terme_specifique: Literal['Docker']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1434"
    descripteur: str = "docker"
class PortDeCommerce(BaseModel):
    terme_specifique: Literal['PortDeCommerce']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-567"
    descripteur: str = "port de commerce"
class PortFluvial(BaseModel):
    terme_specifique: Literal['PortFluvial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-948"
    descripteur: str = "port fluvial"
class PortDePlaisance(BaseModel):
    terme_specifique: Literal['PortDePlaisance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1253"
    descripteur: str = "port de plaisance"
class OfficierDePort(BaseModel):
    terme_specifique: Literal['OfficierDePort']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-928"
    descripteur: str = "officier de port"
class VehiculeAutomobile(BaseModel):
    terme_specifique: Literal['VehiculeAutomobile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-50"
    descripteur: str = "véhicule automobile"
class TransportMultimodal(BaseModel):
    terme_specifique: Union['Ferroutage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-745"
    descripteur: str = "transport multimodal"
class Ferroutage(BaseModel):
    terme_specifique: Literal['Ferroutage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-178"
    descripteur: str = "ferroutage"
class TransportMaritime(BaseModel):
    terme_specifique: Union['SignalisationMaritime', 'LigneMaritime', 'MarinDeCommerce', 'ArmementMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1090"
    descripteur: str = "transport maritime"
class SignalisationMaritime(BaseModel):
    terme_specifique: Literal['SignalisationMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-951"
    descripteur: str = "signalisation maritime"
class LigneMaritime(BaseModel):
    terme_specifique: Literal['LigneMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-196"
    descripteur: str = "ligne maritime"
class MarinDeCommerce(BaseModel):
    terme_specifique: Literal['MarinDeCommerce']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-642"
    descripteur: str = "marin de commerce"
class ArmementMaritime(BaseModel):
    terme_specifique: Literal['ArmementMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1332"
    descripteur: str = "armement maritime"
class BateauDePlaisance(BaseModel):
    terme_specifique: Literal['BateauDePlaisance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-217"
    descripteur: str = "bateau de plaisance"
class TransportEnCommun(BaseModel):
    terme_specifique: Union['UsagerDesTransports']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1273"
    descripteur: str = "transport en commun"
class UsagerDesTransports(BaseModel):
    terme_specifique: Literal['UsagerDesTransports']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-816"
    descripteur: str = "usager des transports"
class Automobiliste(BaseModel):
    terme_specifique: Literal['Automobiliste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-267"
    descripteur: str = "automobiliste"
class Aeronef(BaseModel):
    terme_specifique: Literal['Aeronef']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1406"
    descripteur: str = "aéronef"
class BateauDeNavigationInterieure(BaseModel):
    terme_specifique: Literal['BateauDeNavigationInterieure']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1256"
    descripteur: str = "bateau de navigation intérieure"
class TransportFluvial(BaseModel):
    terme_specifique: Literal['TransportFluvial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-679"
    descripteur: str = "transport fluvial"
class Navire(BaseModel):
    terme_specifique: Literal['Navire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-328"
    descripteur: str = "navire"
class TransportADosDhomme(BaseModel):
    terme_specifique: Literal['TransportADosDhomme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-440"
    descripteur: str = "transport à dos d'homme"
class TransportAerien(BaseModel):
    terme_specifique: Union['ServitudeAeronautique', 'NavigationAerienne', 'LigneAerienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1329"
    descripteur: str = "transport aérien"
class ServitudeAeronautique(BaseModel):
    terme_specifique: Literal['ServitudeAeronautique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-479"
    descripteur: str = "servitude aéronautique"
class NavigationAerienne(BaseModel):
    terme_specifique: Literal['NavigationAerienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-859"
    descripteur: str = "navigation aérienne"
class LigneAerienne(BaseModel):
    terme_specifique: Literal['LigneAerienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1236"
    descripteur: str = "ligne aérienne"
class TransportParAnimal(BaseModel):
    terme_specifique: Union['AnimalDeBat', 'VehiculeATractionAnimale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-488"
    descripteur: str = "transport par animal"
class AnimalDeBat(BaseModel):
    terme_specifique: Literal['AnimalDeBat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-573"
    descripteur: str = "animal de bât"
class VehiculeATractionAnimale(BaseModel):
    terme_specifique: Literal['VehiculeATractionAnimale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-955"
    descripteur: str = "véhicule à traction animale"
class VehiculeADeuxRoues(BaseModel):
    terme_specifique: Literal['VehiculeADeuxRoues']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1257"
    descripteur: str = "véhicule à deux roues"
class TransportRoutier(BaseModel):
    terme_specifique: Union['LiaisonRoutiereInternationale', 'PoidsLourd']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-883"
    descripteur: str = "transport routier"
class LiaisonRoutiereInternationale(BaseModel):
    terme_specifique: Literal['LiaisonRoutiereInternationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-705"
    descripteur: str = "liaison routière internationale"
class PoidsLourd(BaseModel):
    terme_specifique: Literal['PoidsLourd']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1003"
    descripteur: str = "poids lourd"
class Pilote(BaseModel):
    terme_specifique: Literal['Pilote']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-627"
    descripteur: str = "pilote"
class Aerodrome(BaseModel):
    terme_specifique: Literal['Aerodrome']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1022"
    descripteur: str = "aérodrome"
class CirculationUrbaine(BaseModel):
    terme_specifique: Literal['CirculationUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1427"
    descripteur: str = "circulation urbaine"
class Gare(BaseModel):
    terme_specifique: Literal['Gare']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1428"
    descripteur: str = "gare"
class Messagerie(BaseModel):
    terme_specifique: Union['PigeonVoyageur', 'Telecommunications', 'Telediffusion', 'SystemeDinformation', 'Poste', 'Radiodiffusion', 'ServiceRadioElectrique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-915"
    descripteur: str = "messagerie"
class PigeonVoyageur(BaseModel):
    terme_specifique: Literal['PigeonVoyageur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-518"
    descripteur: str = "pigeon voyageur"
class Telecommunications(BaseModel):
    terme_specifique: Union['Telematique', 'ReseauDinformation', 'Telegraphe', 'Telex', 'Telephone']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1327"
    descripteur: str = "télécommunications"
class Telematique(BaseModel):
    terme_specifique: Literal['Telematique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-95"
    descripteur: str = "télématique"
class ReseauDinformation(BaseModel):
    terme_specifique: Literal['ReseauDinformation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-413"
    descripteur: str = "réseau d'information"
class Telegraphe(BaseModel):
    terme_specifique: Literal['Telegraphe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-486"
    descripteur: str = "télégraphe"
class Telex(BaseModel):
    terme_specifique: Literal['Telex']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-768"
    descripteur: str = "télex"
class Telephone(BaseModel):
    terme_specifique: Literal['Telephone']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1187"
    descripteur: str = "téléphone"
class Telediffusion(BaseModel):
    terme_specifique: Union['SocieteDeTelediffusionPrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-228"
    descripteur: str = "télédiffusion"
class SocieteDeTelediffusionPrivee(BaseModel):
    terme_specifique: Literal['SocieteDeTelediffusionPrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-219"
    descripteur: str = "société de télédiffusion privée"
class SystemeDinformation(BaseModel):
    terme_specifique: Union['LogicielInformatique', 'MaterielInformatique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-903"
    descripteur: str = "système d'information"
class LogicielInformatique(BaseModel):
    terme_specifique: Literal['LogicielInformatique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-482"
    descripteur: str = "logiciel informatique"
class MaterielInformatique(BaseModel):
    terme_specifique: Literal['MaterielInformatique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1426"
    descripteur: str = "matériel informatique"
class Poste(BaseModel):
    terme_specifique: Union['ServiceFinancierDeLaPoste', 'DistributionPostale', 'TriPostal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1184"
    descripteur: str = "poste"
class ServiceFinancierDeLaPoste(BaseModel):
    terme_specifique: Literal['ServiceFinancierDeLaPoste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1082"
    descripteur: str = "service financier de la poste"
class DistributionPostale(BaseModel):
    terme_specifique: Literal['DistributionPostale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-547"
    descripteur: str = "distribution postale"
class TriPostal(BaseModel):
    terme_specifique: Literal['TriPostal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1416"
    descripteur: str = "tri postal"
class Radiodiffusion(BaseModel):
    terme_specifique: Union['StationDeRadiodiffusionPrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-592"
    descripteur: str = "radiodiffusion"
class StationDeRadiodiffusionPrivee(BaseModel):
    terme_specifique: Literal['StationDeRadiodiffusionPrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1336"
    descripteur: str = "station de radiodiffusion privée"
class ServiceRadioElectrique(BaseModel):
    terme_specifique: Union['ServitudeRadioElectrique', 'AppareilRadioElectrique', 'StationRadioElectriquePrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-945"
    descripteur: str = "service radio électrique"
class ServitudeRadioElectrique(BaseModel):
    terme_specifique: Literal['ServitudeRadioElectrique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1008"
    descripteur: str = "servitude radio électrique"
class AppareilRadioElectrique(BaseModel):
    terme_specifique: Literal['AppareilRadioElectrique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-692"
    descripteur: str = "appareil radio électrique"
class StationRadioElectriquePrivee(BaseModel):
    terme_specifique: Literal['StationRadioElectriquePrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1445"
    descripteur: str = "station radio électrique privée"
