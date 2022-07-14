'''
list testing
'''

mylist = []
for i in range(0,10):
    if i % 4 == 0:
         mylist.append(i*2)

print(mylist)

# list comprehension

list2 = [ i * 2  for i in range(0,10) if i % 4 == 0]
print(list2)

people = ['Ed','Jojo','Colin','Connor','Andreas']

# process based on value

for person in people:
    print(person)

# process based on position
print()
for i in range(len(people)):
    print(people[i])

print(people[-1])
print (people[3:])
print(people[1:3])
list3 = people+ list2
print(list3)
list4 = [0]* 10
print(list4)
zoom = [['Ed','Jojo','Colin'],
        ['Connor','Andreas','Ruby'],
        ['Brad','Xuewen','Harrison']]
print(zoom)
brad = zoom[2][0]
print(brad)

for row in zoom:
    for person in row:
        print(f"{person:10s}", end= " ")
    print()

list5 = list4.copy()
print (list4, list5)
print(people)
people.sort()
print(people)
people.append("Ahmed")
print(people)
people.insert(3, "Connor")
print(people)
x = people.index("Connor")
print(x)
cCount = people.count("Connor")
print(cCount)
people.pop(1)
print(people)
del people[4]
print(people)
