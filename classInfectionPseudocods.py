#!/usr/bin/env/ python

class infection
	"""Base Class for Infections"""
	def __init__(self,kind="",transmission=0,resistance=0,virulence=0)
	self.kind = kind
	self.transmission = transmission
	self.resistance = resistance
	self.virulence = virulence

Virus=infection(name="Virus",transmission=0.3,resistance=0.1,virulence=0.3)
Bacteria=infection(name="Bacteria",transmission=0.2,resistance=0.2,virulence=0.2)
Parasite=infection(name="Parasite",transmission=0.1,resistance=0.3,virulence=0.1)

#This will be our base class for different methods of infection
#It will include with inherit resistance rate

#viruses- fastest evolving, more affected by environment, bonus to infectivity
#bacteria- medium evol., normally affected by environ., bonus to drug resistance
#parasites- slow evoluntion, least affected by environ, low visibilty


#Each type of infection will have it's own transmission rate

#select for transmisttion
#rodent-rats, mice, squirrels, and other rodents 
#insect- mosquitos and other blood-sucking insects
#waterborne-spread through water>can infect water facilities, requires moisture)
#airborne- allows virus to spread though air

#It will include their interactions with the environment (mode of transmission, drug interaction, etc.)

#Viruses will be the most virulent, then bacteria, then parasites
