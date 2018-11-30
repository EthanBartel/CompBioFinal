#!/usr/bin/env python

import datetime
import random 
import numpy as np

#classes for infections based on type, transmission, resistance, and virulence
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

def direct(self):
    for list in range(1):
        self.add_resist(0.03)
        self.add_trans(0.14)
        self.add_vir(0.06)
def indirect(self):
    for list in range(1):
        Virus.add_vir(0.07)
        Virus.add_trans(0.08)
        Virus.add_resist(0.05)
def vectors(self):
    for list in range(1):
        Virus.add_vir(0.12)
        Virus.add_trans(0.08)
        Virus.add_resist(0.06)

#setting base infections
Virus=infection(kind="Virus",transmission=[0.3],resistance=[0.2],virulence=[0.3])
Bacteria=infection(kind="Bacteria",transmission=[0.2],resistance=[0.2],virulence=[0.2])
Parasite=infection(kind="Parasite",transmission=[0.1],resistance=[0.3],virulence=[0.1])


#directory of continent selection options
continents = [
   dict(Name = "Asia", Population = "4,463,560,000"),
   dict(Name = "Africa", Population = "1,216,070,000"),
   dict(Name = "North America", Population = "579,768,000"),
   dict(Name = "South America", Population = "422,866,000"),
   dict(Name = "Australia", Population = "26,632,714"),
   dict(Name = "Europe", Population = "741,415,000"),
   ]

#Continent Classes
class continent:
    """Continent Class"""
    def __init__(self,name="",m=0,stdev=0,pop=0,state=0):
        self.name= name
        self.m = m
        self.stdev = stdev
        self.pop = pop
        self.state = state #Bool for infection state
    def chance(self):
        data=[]
        for number in range(20):
            data.append(random.gauss(self.m,self.stdev))
        chan=np.mean(data)
        return(chan)
    def infect(self):
        self.state=1
        


#Contructors for Continents
AS=continent(name="Asia",m=0.6,stdev=0.1,pop=4463560000)
AF=continent(name="Africa",m=0.35,stdev=0.1,pop=1216070000)
NA=continent(name="North America",m=0.55,stdev=0.1,pop=579768000)
SA=continent(name="South America",m=0.5,stdev=0.1,pop=422866000)
AU=continent(name="Australia",m=0.3,stdev=0.1,pop=26632714)
EU=continent(name="Europe",m=0.45,stdev=0.1,pop=741415000)


#find current date to print on bulletin 
current_date = datetime.datetime.strftime(datetime.date.today(), "%m-%d-%Y")   

#introduction of the game and User
print ("Welcome to CompBiol.Find(A+)'s Final Project")
user = input (('\n What is your name? ').title())
 # for later on in the game
#pick a country based from list of countries and populations
print ('-' * 55)
print ('\nChoose From Following Continents or Type Random\n')
print ("Continent".ljust(15),"Population\n")
for continent in continents:
    print (continent["Name"].ljust(15), continent["Population"]) #list of cont names for user

startcontinent = input (('\nWhat continent would you like to start in? ').title()) 

if startcontinent == 'Random': # random.sample can be used for more than one country later on
    startcontinent = random.choice(continents)
#input disease name 
diseasename = input (('\nWhat would you like to name your disease? ').title())

#start game... bulletin from user info, disease and start
print ('-' * 55)
print ('\nNews Bulletin'.ljust(45), current_date)
print ('-' * 55)
print ('An unknown disease named', diseasename, 'has struck', startcontinent, 'by storm.')
print ('Doctors and scientists will need to collaborate to find out more information about this disease.')
print ('-' * 55)

#Select options for Infection Type 
print ('\nSelect Your Infection Type: A, B, or C')
print ('\nA: VIRUSES- Fast Evolving, More Affected By Environment, Bonus To Infectivity')
print ('B: BACTERIA- Medium Evolving, Normally Affected By Environment, Bonus To Drug Resistance')
print ('C: PARASITES- Slow Evolving, Least Affected By Environment, Low Visibilty ')

infect = input('Selection:')
print ('-' * 55)

#Select options for transmittion factors
print ('\nSelect Your Transmission Factor: A, B, or C')
print ('\nA: DIRECT- This allows spread via direct contact')
print ('B: INDIRECT- This allows spread via indirect contact ex: water & airborne')
print ('C: VECTORS- This allows spread via carrier ex. rodents & insects')
factor = input('Selection:')
print ('-' * 55)

#Statements for Factor Choice
if factor=='A':
    for list in range(1):
        direct(Virus)
        direct(Bacteria)
        direct(Parasite)
if factor=='B':
    for list in range(1):
        indirect(Virus)
        indirect(Bacteria)
        indirect(Parasite)
if factor=='C':
    for list in range(1):
        vectors(Virus)
        vectors(Bacteria)
        vectors(Parasite)



#This will be our base class for different methods of infection
#It will include with inherit resistance rate


#when bool is 0 not infect when 1 it is infected 

#Boolean Infection
if (NA.chance())<(Virus.transmission[0]):
	NA.infect()
if (AS.chance())<(Virus.transmission[0]):
	AS.infect()
if (AF.chance())<(Virus.transmission[0]):
	AF.infect()
if (SA.chance())<(Virus.transmission[0]):
	SA.infect()
if (AU.chance())<(Virus.transmission[0]):
	AU.infect()
if (EU.chance())<(Virus.transmission[0]):
	EU.infect()


infect=[]
if AS.state is 1:
	infect.append("Asia")
if AF.state is 1:
	infect.append("Africa")
if NA.state is 1:
	infect.append("North America")
if SA.state is 1:
	infect.append("South America")
if AU.state is 1:
	infect.append("Australia")
if EU.state is 1:
	infect.append("Europe")

print ("You decimated the populations of these continients:")
print (infect)


#It will include their interactions with the environment (mode of transmission, drug interaction, etc.)

#Viruses will be the most virulent, then bacteria, then parasites

