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
#It will include viruses, bacteria, parasites
#Each type of infection will have it's own transmission rate
#It will include their interactions with the environment (mode of transmission, drug interaction, etc.)
#Viruses will be the most virulent, then bacteria, then parasites
