persons = [['Alice', 25, 'blonde'],
           ['Bob', 33, 'black'],
           ['Ann', 18, 'purple']]

persons_dict = {}
for x in persons:
    persons_dict[x[0]] = x[1:]
print(persons_dict)

# as a _dictionary_ comprehension
persons_dict = {}
persons_dict = {x[0]: x[1:] for x in persons}
print(persons_dict)
# {'Alice': [25, 'blonde'],
#  'Bob': [33, 'black'],
#  'Ann': [18, 'purple']}
