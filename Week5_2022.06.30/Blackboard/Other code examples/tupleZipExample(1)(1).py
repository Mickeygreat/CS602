'''
Created on Oct 31, 2019

@author: ruded
'''

# Iterating over a zipped sequences
city = ['Boston', 'Paris', 'Lagos']
area = [11700, 17174, 2706] #sq km
population = [4628910, 12405426, 21000000]

for ci, a, pop in zip(city, area, population):
    print('Population Density of ', ci, 'is', round(pop/a, 1))