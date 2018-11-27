#!/usr/bin/python
#Math for Final 
import numpy as np
import random 

mean = 0.5
stdev = 0.2   # 99.73% chance the sample will fall in your desired range
chance = [random.gauss(mean, stdev)]
data = []

for number in range(20):
	data.append(random.gauss(mean, stdev))

chance = np.mean(data)

if transmission >= chance:
	print ("Test Postitive")
elif transmission < chance:
	print ("Test Negative")