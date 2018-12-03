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

#functions for adding factor choices
def direct(self):
    for list in range(1):
        self.add_resist(0.03)
        self.add_trans(0.14)
        self.add_vir(0.07)
def indirect(self):
    for list in range(1):
        self.add_vir(0.08)
        self.add_trans(0.09)
        self.add_resist(0.07)
def vectors(self):
    for list in range(1):
        self.add_vir(0.12)
        self.add_trans(0.08)
        self.add_resist(0.07)

#setting base infections
Virus=infection(kind="Virus",transmission=[0.3],resistance=[0.2],virulence=[0.3])
Bacteria=infection(kind="Bacteria",transmission=[0.2],resistance=[0.2],virulence=[0.2])
Parasite=infection(kind="Parasite",transmission=[0.1],resistance=[0.3],virulence=[0.1])


#dictionary for continent selection options
continents = [
   dict(Name = "Asia", Population = "4,463,560,000"),
   dict(Name = "Africa", Population = "1,216,070,000"),
   dict(Name = "North America", Population = "579,768,000"),
   dict(Name = "South America", Population = "422,866,000"),
   dict(Name = "Australia", Population = "26,632,714"),
   dict(Name = "Europe", Population = "741,415,000"),
   ]

#Continent Classe
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
AS=continent(name="Asia",m=0.65,stdev=0.1,pop=4463560000)
AF=continent(name="Africa",m=0.40,stdev=0.1,pop=1216070000)
NA=continent(name="North America",m=0.6,stdev=0.1,pop=579768000)
SA=continent(name="South America",m=0.5,stdev=0.1,pop=422866000)
AU=continent(name="Australia",m=0.35,stdev=0.1,pop=26632714)
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
input ("Press enter to continue...")
print ('-' * 55)


#Select options for Infection Type 
print ('\nSelect Your Infection Type: A, B, or C')
print ('\nA: VIRUSES- Fast Evolving, More Affected By Environment, Bonus To Infectivity')
print ('B: BACTERIA- Medium Evolving, Normally Affected By Environment, Bonus To Drug Resistance')
print ('C: PARASITES- Slow Evolving, Least Affected By Environment, Low Visibilty ')

infect = input('Selection:')
infect=infect.upper()
print ('-' * 55)

#Select options for transmittion factors
print ('\nSelect Your Transmission Factor: A, B, or C')
print ('\nA: DIRECT- This allows spread via direct contact')
print ('B: INDIRECT- This allows spread via indirect contact ex: water & airborne')
print ('C: VECTORS- This allows spread via carrier ex. rodents & insects')
factor = input('Selection:')
factor=factor.upper()
print ('-' * 55)


infected=[]
death=[]
if startcontinent=="Asia":
	AS.infect()
if startcontinent=="North America":
	NA.infect()
if startcontinent=="South America":
	SA.infect()
if startcontinent=="Australia":
	AU.infect()
if startcontinent=="Africa":
	AF.infect()
if startcontinent=="Europe":
	EU.infect()

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
if infect=='A':
	if (NA.chance())<(Virus.transmission[0]):
		NA.infect()
		for list in range(1):
			deathNA=(Virus.virulence[0])*(NA.pop)
			death.append(deathNA)
	if (AS.chance())<(Virus.transmission[0]):
		AS.infect()
		for list in range(1):
			deathAS=(Virus.virulence[0])*(AS.pop)
			death.append(deathAS)
	if (AF.chance())<(Virus.transmission[0]):
	    AF.infect()
	    for list in range(1):
	    	deathAF=(Virus.virulence[0]*AF.pop)
	    	death.append(deathAF)
	if (SA.chance())<(Virus.transmission[0]):
	    SA.infect()
	    for list in range(1):
	    	deathSA=(Virus.virulence[0]*SA.pop)
	    	death.append(deathSA)
	if (AU.chance())<(Virus.transmission[0]):
		AU.infect()
		for list in range(1):
			deathAU=(Virus.virulence[0]*AU.pop)
			death.append(deathAU)
	if (EU.chance())<(Virus.transmission[0]):
		EU.infect()
		for list in range(1):
			deathEU=(Virus.virulence[0]*EU.pop)
			death.append(deathEU)

if infect=='B':
	if (NA.chance())<(Bacteria.transmission[0]):
		NA.infect()
		for list in range(1):
			deathNA=(Bacteria.virulence[0])*(NA.pop)
			death.append(deathNA)
	if (AS.chance())<(Bacteria.transmission[0]):
		AS.infect()
		for list in range(1):
			deathAS=(Bacteria.virulence[0])*(AS.pop)
			death.append(deathAS)
	if (AF.chance())<(Bacteria.transmission[0]):
		AF.infect()
		for list in range(1):
			deathAF=(Bacteria.virulence[0]*AF.pop)
			death.append(deathAF)
	if (SA.chance())<(Bacteria.transmission[0]):
		SA.infect()
		for list in range(1):
			deathSA=(Bacteria.virulence[0]*SA.pop)
			death.append(deathSA)
	if (AU.chance())<(Bacteria.transmission[0]):
		AU.infect()
		for list in range(1):
			deathAU=(Bacteria.virulence[0]*AU.pop)
			death.append(deathAU)
	if (EU.chance())<(Bacteria.transmission[0]):
		EU.infect()
		for list in range(1):
			deathEU=(Bacteria.virulence[0]*EU.pop)
			death.append(deathEU)
if infect=='C':
	if (NA.chance())<(Parasite.transmission[0]):
		NA.infect()
		for list in range(1):
			deathNA=(Parasite.virulence[0])*(NA.pop)
			death.append(deathNA)
	if (AS.chance())<(Parasite.transmission[0]):
		AS.infect()
		for list in range(1):
			deathAS=(Parasite.virulence[0])*(AS.pop)
			death.append(deathAS)
	if (AF.chance())<(Parasite.transmission[0]):
		AF.infect()
		for list in range(1):
			deathAF=(Parasite.virulence[0]*AF.pop)
			death.append(deathAF)
	if (SA.chance())<(Parasite.transmission[0]):
		SA.infect()
		for list in range(1):
			deathSA=(Parasite.virulence[0]*SA.pop)
			death.append(deathSA)
	if (AU.chance())<(Parasite.transmission[0]):
		AU.infect()
		for list in range(1):
			deathAU=(Parasite.virulence[0]*AU.pop)
			death.append(deathAU)
	if (EU.chance())<(Parasite.transmission[0]):
		EU.infect()
		for list in range(1):
			deathEU=(Parasite.virulence[0]*EU.pop)
			death.append(deathEU)

if NA.state is 1:
	for list in range(1):
	    infected.append("North America")
	    # death.extend(deathNA)
if AS.state is 1:
	for list in range(1):
	    infected.append("Asia")
		# death.extend(deathAS)
if AF.state is 1:
	for list in range(1):
		infected.append("Africa")
		# death.extend(deathAF)
if SA.state is 1:
	for list in range(1):
		infected.append("South America")
		# death.extend(deathSA)
if AU.state is 1:
	for list in range(1):
		infected.append("Australia")
		# death.extend(deathAU)
if EU.state is 1:
	for list in range(1):
		infected.append("Europe")
		# death.extend(deathEU)

print ('-' * 55)
death=sum(death)
death=round(death)
print (user, "and",diseasename, "have decimated the populations of these continients:")
print (infected)
if len(infected)==0:
	print("None.", user, "has failed to infect the world.") 
print("You are responsible for the deaths of", death,"people across these continients.")
print ('-' * 55)

print ('-' * 55)

#It will include their interactions with the environment (mode of transmission, drug interaction, etc.)

#Viruses will be the most virulent, then bacteria, then parasites

