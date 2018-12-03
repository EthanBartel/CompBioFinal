#!/usr/bin/python

class infection:
    """Base Class for Infections"""
    def __init__(self,kind="",transmission=0,resistance=0,virulence=0):
        self.kind = kind
        self.transmission = transmission
        self.resistance = resistance
        self.virulence = virulence
    def add_trans(self,trans):
        self.transmission.append(trans)
        self.transmission.append(sum(self.transmission))
        self.transmission.pop(0)
        self.transmission.pop(0)
    def add_resist(self,resist):
        self.resistance.append(resist)
        self.resistance.append(sum(self.resistance))
        self.resistance.pop(0)
        self.resistance.pop(0)
    def add_vir(self,vir):
        self.virulence.append(vir)
        self.virulence.append(sum(self.virulence))
        self.virulence.pop(0)
        self.virulence.pop(0)

def air(self):
    for list in range(1):
        self.add_resist(0.04)
        self.add_trans(0.15)
        self.add_vir(0.08)
def water(self):
    for list in range(1):
        Virus.add_vir(0.09)
        Virus.add_trans(0.12)
        Virus.add_resist(0.06)
def rat(self):
    for list in range(1):
        Virus.add_vir(0.13)
        Virus.add_trans(0.08)
        Virus.add_resist(0.05)
def bug(self):
    for list in range(1):
        Virus.add_vir(0.11)
        Virus.add_trans(0.05)
        Virus.add_resist(0.09)

Virus=infection(kind="Virus",transmission=[0.3],resistance=[0.1],virulence=[0.3])
Bacteria=infection(kind="Bacteria",transmission=[0.2],resistance=[0.2],virulence=[0.2])
Parasite=infection(kind="Parasite",transmission=[0.1],resistance=[0.3],virulence=[0.1])

print("Please select your transmission vector: \n A) Airborne - allows virus to spread though air. \n B) Waterborne - spread through water>can infect water facilities, requires moisture. \n C) Rodent - rats, mice, squirrels, and other rodents. \n D) Insect - mosquitos and other blood-sucking insects")
print("Please select A/B/C/D:\n ")
vector=input()
if vector=='A':
    for list in range(1):
        air(Virus)
if vector=='B':
    for list in range(1):
        water(Virus)
if vector=='C':
    for list in range(1):
        rat(Virus)
if vector=='D':
    for list in range(1):
        bug(Virus)
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

