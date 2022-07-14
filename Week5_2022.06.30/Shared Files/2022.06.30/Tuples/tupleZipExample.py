'''
Created on Oct 31, 2019

@author: ruded
'''

# Iterating over a zipped sequences

city = ['Boston', 'Paris', 'Lagos']
area = [11700, 17174, 2706] #sq km
population = [4628910, 12405426, 21000000]

# 1 with a loop - this is not the Python way!

city_info1 = []
for i in range(len(city)):
    city_info1.append( (city[i], area[i], population[i]))
print(city_info1, "\n")

# 2 with a list comprehension

city_info2 = [(city[i], area[i], population[i]) for i in range (len(city))]
print(city_info2, "\n")

# 3 with zip

city_info3 =  zip(city, area, population)
print(city_info3)
print(list(zip(city, area, population)))

for ci, a, pop in city_info3:
    print('Population Density of ', ci, 'is', round(pop/a, 1))
