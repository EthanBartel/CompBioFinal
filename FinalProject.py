#!/usr/bin/env python

import datetime
import random 

#directory of continent selection options
continents = [
   dict(Name = "Asia", Population = "4,463,560,000"),
   dict(Name = "Africa", Population = "1,216,070,000"),
   dict(Name = "North America", Population = "579,768,000"),
   dict(Name = "South America", Population = "422,866,000"),
   dict(Name = "Australia", Population = "26,632,714"),
   dict(Name = "Europe", Population = "741,415,000"),
   ]

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
