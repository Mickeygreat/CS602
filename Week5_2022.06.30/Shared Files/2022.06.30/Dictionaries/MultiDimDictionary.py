'''
Created on Jun 13, 2021
Multi-Dimensional Dictionary Example
@author: ruded
'''
from win32com.servers import dictionary
'''
Create a multi-dimensional Dictionary
'''
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)
input('\nHit Enter...\n')

'''
Access elements in a multi-dimensional Dictionary
'''
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
print()
print(people.get(2).get('name'))
print(people.get(2).get('age'))
print(people.get(2).get('sex'))
input('\nHit Enter...\n')

'''
Add an element to a multi-dimensional Dictionary
'''
people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people[3])
print(people)
input('\nHit Enter...\n')

'''
Add another element to a multi-dimensional dictionary
'''
people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])
print(people)
input('\nHit Enter...\n')

'''
Delete elements from a multi-dimensional dictionary
'''
# del people[3]['married']
# del people[4]['married']

returnValue1 = people.get(3).pop('married')
print('Married: ', returnValue1)
print(people.get(3))
returnValue2 = people.get(4).pop('married')
print('Married: ', returnValue2)
print(people.get(4))
input('\nHit Enter...\n')

'''
Delete dictionary from a multi-dimensional dictionary
'''
# del people[3], people[4]

subDictionary1 = people.pop(3)
subDictionary2 = people.pop(4)
print('Removed from people dictionary, New Dictionary 1:', subDictionary1)
print('Removed from people dictionary, New Dictionary 2:', subDictionary2)
print('people dictionary:\n', people)
input('\nHit Enter...\n')

'''
Iterate through a multi-dimensional dictionary
'''
for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])
        
