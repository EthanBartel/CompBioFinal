#!/usr/bin/env python

import datetime
import random 

countries = [
   dict(Name = "China", Population = "1,363,560,000"),
   dict(Name = "India", Population = "1,242,070,000"),
   dict(Name = "United States", Population = "317,768,000"),
   dict(Name = "Indonesia", Population = "249,866,000"),
   dict(Name = "Brazil", Population = "201,032,714"),
   dict(Name = "Pakistan", Population = "186,015,000"),
   dict(Name = "Nigeria", Population = "173,615,000"),
   dict(Name = "Bangladesh", Population = "152,518,015"),
   dict(Name = "Russia", Population = "143,700,000"),
   dict(Name = "Japan", Population = "127,120,000"),
   dict(Name = "Mexico", Population = "119,713,203"),
   dict(Name = "Philippines", Population = "99,329,000"),
   dict(Name = "Vietnam", Population = "89,708,900"),
   dict(Name = "Egypt", Population = "86,188,600"),
   dict(Name = "Germany", Population = "80,716,000"),
   dict(Name = "Iran", Population = "77,315,000"),
   dict(Name = "Turkey", Population = "76,667,864"),
   dict(Name = "Thailand", Population = "65,926,261"),
   dict(Name = "France", Population = "65,844,000"),
   dict(Name = "United Kingdom", Population = "63,705,000"),
   dict(Name = "Italy", Population = "59,996,777"),
   dict(Name = "South Africa", Population = "52,981,991"),
   dict(Name = "South Korea", Population = "50,219,669"),
   dict(Name = "Colombia", Population = "47,522,000"),
   dict(Name = "Spain", Population = "46,609,700"),
   dict(Name = "Ukraine", Population = "45,410,071"),
   dict(Name = "Kenya", Population = "44,354,000"),
   dict(Name = "Argentina", Population = "40,117,096"),
   dict(Name = "Poland", Population = "38,502,396"),
   dict(Name = "Sudan", Population = "37,964,000"),
   dict(Name = "Uganda", Population = "35,357,000"),
   dict(Name = "Canada", Population = "35,344,962"),
   dict(Name = "Iraq", Population = "34,035,000"),
   ]

current_date = datetime.datetime.strftime(datetime.date.today(), "%m-%d-%Y")   

#introduction of the game and User
print ("Welcome to Caroline's and Ethan's Final Project")
user = input (('\n What is your name? ').title())
 # for later on in the game
#pick a country based from list of countries and populations
print ('\nCountries to choose from are\n')
print ("Country".ljust(15),"Population\n")
for country in countries:
    print (country["Name"].ljust(15), country["Population"])
startcountry = input (('\nWhat country would you like to start in? ').title()) 

if startcountry == 'Random': # random.sample can be used for more than one country later on
    startcountry = random.choice(countries)
#input disease name 
diseasename = input (('\nWhat would you like to name your disease? ').title())

#start game... bulletin from with info on disease and start
print ('\nNews Bulletin'.ljust(45), current_date)
print ('-' * 55)
print ('An unknown disease named', diseasename, 'has struck', startcountry, 'by storm.')
print ('Doctors and scientists will need to collaborate to find out more information about this disease.')
