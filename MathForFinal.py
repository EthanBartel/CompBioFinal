#!/usr/bin/python
#Math for Final 
import numpy as np
import random 
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
            chance=np.mean(data)
        print(np.mean(chance))
    def infect(self):
        self.state=1
#Contructors for Continents
AS=continent(name="Asia",m=0.6,stdev=0.1,pop=4463560000)
AF=continent(name="Africa",m=0.5,stdev=0.1,pop=1216070000)
NA=continent(name="North America",m=0.6,stdev=0.1,pop=579768000)
SA=continent(name="South America",m=0.5,stdev=0.1,pop=422866000)
AU=continent(name="Australia",m=0.65,stdev=0.1,pop=26632714)
EU=continent(name="Europe",m=0.5,stdev=0.1,pop=741415000)

#Boolean Infection
if (NA.chance())<(Virus.transmission)
    NA.infect()
if (AS.chance())<(Virus.transmission)
    AS.infect()
if (AF.chance())<(Virus.transmission)
    AF.infect()
if (SA.chance())<(Virus.transmission)
    SA.infect()
if (AU.chance())<(Virus.transmission)
    AU.infect()
if (EU.chance())<(Virus.transmission)
    EU.infect()
