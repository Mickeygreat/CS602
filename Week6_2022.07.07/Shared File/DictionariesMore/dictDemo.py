'''
Created on Oct 21, 2018
Demo of dictionary sorting
'''

names = { 'Harry Potter':753, 'Albus Dumbledore':119, 'Tamara Babaian': 15 }


print ('-------ordered alphabetically by key values ----')
keysSortedLst = sorted(names.keys())
print(keysSortedLst)
# display names and values one per line in SORTED ORDER by key
   
for key  in  keysSortedLst:
    print(key, ' has value ' , names[key])
    
print ('-------ordered by LENGTH of key values ----')
keysSortedLst = sorted(names.keys(), key = len)
print(keysSortedLst)
# display names and values one per line in SORTED ORDER by key
   
for key  in  keysSortedLst:
    print(key, ' has value ' , names[key])

 
def valueFromKeyValueTuple(key_value_tuple):
    return key_value_tuple[1] 

# print names in order of last names 
print ('-------ordered by last names ----')
 
def lastName(FnameLnameStr ): 
    lastName = FnameLnameStr.split()[1]
    return lastName
 
keysSortedByLName = sorted(names.keys(), key = lastName)
for item in keysSortedByLName:
    print (item, ' has value', names[item])
    
print ('-------ordered by the values, descending----')
keysSortedByValue = sorted(names.items(), key = valueFromKeyValueTuple,
                            reverse = True)
print(keysSortedByValue)

for item in keysSortedByValue:
   print (item[0], ' has value', item[1])





