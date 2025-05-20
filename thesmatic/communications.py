from pydantic import BaseModel, Field
from typing import Union, Literal
                
class Communications(BaseModel):
    sous_descripteur: Union['Transport', 'Messagerie'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-503"
    descripteur: str = "communications"
class Transport(BaseModel):
    sous_descripteur: Union['CirculationRoutiere', 'ChauffeurDeTaxi', 'TransportFerroviaire', 'Port', 'VehiculeAutomobile', 'TransportMultimodal', 'TransportMaritime', 'BateauDePlaisance', 'TransportEnCommun', 'Automobiliste', 'Aeronef', 'BateauDeNavigationInterieure', 'TransportFluvial', 'Navire', 'TransportADosDhomme', 'TransportAerien', 'TransportParAnimal', 'VehiculeADeuxRoues', 'TransportRoutier', 'Pilote', 'Aerodrome', 'CirculationUrbaine', 'Gare'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-548"
    descripteur: str = "transport"
class CirculationRoutiere(BaseModel):
    sous_descripteur: Union['SignalisationRoutiere'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1050"
    descripteur: str = "circulation routière"
class SignalisationRoutiere(BaseModel):
    sous_descripteur: Literal['SignalisationRoutiere']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1076"
    descripteur: str = "signalisation routière"
class ChauffeurDeTaxi(BaseModel):
    sous_descripteur: Literal['ChauffeurDeTaxi']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-617"
    descripteur: str = "chauffeur de taxi"
class TransportFerroviaire(BaseModel):
    sous_descripteur: Union['LigneDeCheminDeFer', 'LiaisonFerreeInternationale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-164"
    descripteur: str = "transport ferroviaire"
class LigneDeCheminDeFer(BaseModel):
    sous_descripteur: Literal['LigneDeCheminDeFer']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-139"
    descripteur: str = "ligne de chemin de fer"
class LiaisonFerreeInternationale(BaseModel):
    sous_descripteur: Literal['LiaisonFerreeInternationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-493"
    descripteur: str = "liaison ferrée internationale"
class Port(BaseModel):
    sous_descripteur: Union['InfrastructurePortuaire', 'PortDePeche', 'PortMaritime', 'Docker', 'PortDeCommerce', 'PortFluvial', 'PortDePlaisance', 'OfficierDePort'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-231"
    descripteur: str = "port"
class InfrastructurePortuaire(BaseModel):
    sous_descripteur: Literal['InfrastructurePortuaire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-277"
    descripteur: str = "infrastructure portuaire"
class PortDePeche(BaseModel):
    sous_descripteur: Literal['PortDePeche']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-156"
    descripteur: str = "port de pêche"
class PortMaritime(BaseModel):
    sous_descripteur: Literal['PortMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-597"
    descripteur: str = "port maritime"
class Docker(BaseModel):
    sous_descripteur: Literal['Docker']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1434"
    descripteur: str = "docker"
class PortDeCommerce(BaseModel):
    sous_descripteur: Literal['PortDeCommerce']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-567"
    descripteur: str = "port de commerce"
class PortFluvial(BaseModel):
    sous_descripteur: Literal['PortFluvial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-948"
    descripteur: str = "port fluvial"
class PortDePlaisance(BaseModel):
    sous_descripteur: Literal['PortDePlaisance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1253"
    descripteur: str = "port de plaisance"
class OfficierDePort(BaseModel):
    sous_descripteur: Literal['OfficierDePort']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-928"
    descripteur: str = "officier de port"
class VehiculeAutomobile(BaseModel):
    sous_descripteur: Literal['VehiculeAutomobile']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-50"
    descripteur: str = "véhicule automobile"
class TransportMultimodal(BaseModel):
    sous_descripteur: Union['Ferroutage'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-745"
    descripteur: str = "transport multimodal"
class Ferroutage(BaseModel):
    sous_descripteur: Literal['Ferroutage']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-178"
    descripteur: str = "ferroutage"
class TransportMaritime(BaseModel):
    sous_descripteur: Union['SignalisationMaritime', 'LigneMaritime', 'MarinDeCommerce', 'ArmementMaritime'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1090"
    descripteur: str = "transport maritime"
class SignalisationMaritime(BaseModel):
    sous_descripteur: Literal['SignalisationMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-951"
    descripteur: str = "signalisation maritime"
class LigneMaritime(BaseModel):
    sous_descripteur: Literal['LigneMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-196"
    descripteur: str = "ligne maritime"
class MarinDeCommerce(BaseModel):
    sous_descripteur: Literal['MarinDeCommerce']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-642"
    descripteur: str = "marin de commerce"
class ArmementMaritime(BaseModel):
    sous_descripteur: Literal['ArmementMaritime']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1332"
    descripteur: str = "armement maritime"
class BateauDePlaisance(BaseModel):
    sous_descripteur: Literal['BateauDePlaisance']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-217"
    descripteur: str = "bateau de plaisance"
class TransportEnCommun(BaseModel):
    sous_descripteur: Union['UsagerDesTransports'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1273"
    descripteur: str = "transport en commun"
class UsagerDesTransports(BaseModel):
    sous_descripteur: Literal['UsagerDesTransports']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-816"
    descripteur: str = "usager des transports"
class Automobiliste(BaseModel):
    sous_descripteur: Literal['Automobiliste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-267"
    descripteur: str = "automobiliste"
class Aeronef(BaseModel):
    sous_descripteur: Literal['Aeronef']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1406"
    descripteur: str = "aéronef"
class BateauDeNavigationInterieure(BaseModel):
    sous_descripteur: Literal['BateauDeNavigationInterieure']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1256"
    descripteur: str = "bateau de navigation intérieure"
class TransportFluvial(BaseModel):
    sous_descripteur: Literal['TransportFluvial']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-679"
    descripteur: str = "transport fluvial"
class Navire(BaseModel):
    sous_descripteur: Literal['Navire']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-328"
    descripteur: str = "navire"
class TransportADosDhomme(BaseModel):
    sous_descripteur: Literal['TransportADosDhomme']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-440"
    descripteur: str = "transport à dos d'homme"
class TransportAerien(BaseModel):
    sous_descripteur: Union['ServitudeAeronautique', 'NavigationAerienne', 'LigneAerienne'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1329"
    descripteur: str = "transport aérien"
class ServitudeAeronautique(BaseModel):
    sous_descripteur: Literal['ServitudeAeronautique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-479"
    descripteur: str = "servitude aéronautique"
class NavigationAerienne(BaseModel):
    sous_descripteur: Literal['NavigationAerienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-859"
    descripteur: str = "navigation aérienne"
class LigneAerienne(BaseModel):
    sous_descripteur: Literal['LigneAerienne']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1236"
    descripteur: str = "ligne aérienne"
class TransportParAnimal(BaseModel):
    sous_descripteur: Union['AnimalDeBat', 'VehiculeATractionAnimale'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-488"
    descripteur: str = "transport par animal"
class AnimalDeBat(BaseModel):
    sous_descripteur: Literal['AnimalDeBat']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-573"
    descripteur: str = "animal de bât"
class VehiculeATractionAnimale(BaseModel):
    sous_descripteur: Literal['VehiculeATractionAnimale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-955"
    descripteur: str = "véhicule à traction animale"
class VehiculeADeuxRoues(BaseModel):
    sous_descripteur: Literal['VehiculeADeuxRoues']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1257"
    descripteur: str = "véhicule à deux roues"
class TransportRoutier(BaseModel):
    sous_descripteur: Union['LiaisonRoutiereInternationale', 'PoidsLourd'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-883"
    descripteur: str = "transport routier"
class LiaisonRoutiereInternationale(BaseModel):
    sous_descripteur: Literal['LiaisonRoutiereInternationale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-705"
    descripteur: str = "liaison routière internationale"
class PoidsLourd(BaseModel):
    sous_descripteur: Literal['PoidsLourd']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1003"
    descripteur: str = "poids lourd"
class Pilote(BaseModel):
    sous_descripteur: Literal['Pilote']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-627"
    descripteur: str = "pilote"
class Aerodrome(BaseModel):
    sous_descripteur: Literal['Aerodrome']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1022"
    descripteur: str = "aérodrome"
class CirculationUrbaine(BaseModel):
    sous_descripteur: Literal['CirculationUrbaine']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1427"
    descripteur: str = "circulation urbaine"
class Gare(BaseModel):
    sous_descripteur: Literal['Gare']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1428"
    descripteur: str = "gare"
class Messagerie(BaseModel):
    sous_descripteur: Union['PigeonVoyageur', 'Telecommunications', 'Telediffusion', 'SystemeDinformation', 'Poste', 'Radiodiffusion', 'ServiceRadioElectrique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-915"
    descripteur: str = "messagerie"
class PigeonVoyageur(BaseModel):
    sous_descripteur: Literal['PigeonVoyageur']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-518"
    descripteur: str = "pigeon voyageur"
class Telecommunications(BaseModel):
    sous_descripteur: Union['Telematique', 'ReseauDinformation', 'Telegraphe', 'Telex', 'Telephone'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1327"
    descripteur: str = "télécommunications"
class Telematique(BaseModel):
    sous_descripteur: Literal['Telematique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-95"
    descripteur: str = "télématique"
class ReseauDinformation(BaseModel):
    sous_descripteur: Literal['ReseauDinformation']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-413"
    descripteur: str = "réseau d'information"
class Telegraphe(BaseModel):
    sous_descripteur: Literal['Telegraphe']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-486"
    descripteur: str = "télégraphe"
class Telex(BaseModel):
    sous_descripteur: Literal['Telex']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-768"
    descripteur: str = "télex"
class Telephone(BaseModel):
    sous_descripteur: Literal['Telephone']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1187"
    descripteur: str = "téléphone"
class Telediffusion(BaseModel):
    sous_descripteur: Union['SocieteDeTelediffusionPrivee'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-228"
    descripteur: str = "télédiffusion"
class SocieteDeTelediffusionPrivee(BaseModel):
    sous_descripteur: Literal['SocieteDeTelediffusionPrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-219"
    descripteur: str = "société de télédiffusion privée"
class SystemeDinformation(BaseModel):
    sous_descripteur: Union['LogicielInformatique', 'MaterielInformatique'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-903"
    descripteur: str = "système d'information"
class LogicielInformatique(BaseModel):
    sous_descripteur: Literal['LogicielInformatique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-482"
    descripteur: str = "logiciel informatique"
class MaterielInformatique(BaseModel):
    sous_descripteur: Literal['MaterielInformatique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1426"
    descripteur: str = "matériel informatique"
class Poste(BaseModel):
    sous_descripteur: Union['ServiceFinancierDeLaPoste', 'DistributionPostale', 'TriPostal'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1184"
    descripteur: str = "poste"
class ServiceFinancierDeLaPoste(BaseModel):
    sous_descripteur: Literal['ServiceFinancierDeLaPoste']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1082"
    descripteur: str = "service financier de la poste"
class DistributionPostale(BaseModel):
    sous_descripteur: Literal['DistributionPostale']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-547"
    descripteur: str = "distribution postale"
class TriPostal(BaseModel):
    sous_descripteur: Literal['TriPostal']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1416"
    descripteur: str = "tri postal"
class Radiodiffusion(BaseModel):
    sous_descripteur: Union['StationDeRadiodiffusionPrivee'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-592"
    descripteur: str = "radiodiffusion"
class StationDeRadiodiffusionPrivee(BaseModel):
    sous_descripteur: Literal['StationDeRadiodiffusionPrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1336"
    descripteur: str = "station de radiodiffusion privée"
class ServiceRadioElectrique(BaseModel):
    sous_descripteur: Union['ServitudeRadioElectrique', 'AppareilRadioElectrique', 'StationRadioElectriquePrivee'] = Field(description="Choisir entre les différentes options, sauf si le descripteur est suffisamment pertinent") 
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-945"
    descripteur: str = "service radio électrique"
class ServitudeRadioElectrique(BaseModel):
    sous_descripteur: Literal['ServitudeRadioElectrique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1008"
    descripteur: str = "servitude radio électrique"
class AppareilRadioElectrique(BaseModel):
    sous_descripteur: Literal['AppareilRadioElectrique']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-692"
    descripteur: str = "appareil radio électrique"
class StationRadioElectriquePrivee(BaseModel):
    sous_descripteur: Literal['StationRadioElectriquePrivee']
    ark: str = "http://data.culture.fr/thesaurus/resource/ark:/67717/T1-1445"
    descripteur: str = "station radio électrique privée"
