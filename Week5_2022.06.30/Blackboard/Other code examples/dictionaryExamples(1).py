'''
Created on Nov 1, 2019
@author: ruded
Dictionary Examples
'''
names = {'Courtney':753, 'Alexis':119, 'Steven':279}
print(names)
print(names.keys())
print(names.values())
print()

print('John' in names)
print('Alexis' in names)
names['Steven'] = 35
print(names)
names['Mark'] = 463
print(names.get('susan'))
print(names.get('Alexis'))

for key, val in names.items():
    print(key, val)
    
for val in names:
    print(names[val])
    
print(len(names))

names.pop('Courtney')
print(names)

keySortedList = sorted(names.items())
print(keySortedList)

def itemValue(tuple):
    return tuple[1]

valueSortedList = sorted(names.items(), key = itemValue)
print(valueSortedList)

names.clear()
print(names)