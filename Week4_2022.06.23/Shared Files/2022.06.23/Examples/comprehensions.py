'''

Practice on list comprehensions
@author: DRUDE
'''

a = []
for x in 'abc':
    a.append(x)
print(a)

a = [x for x in 'abc']
print(a)
b = [x for x in 'A little knowledge is a dangerous thing. '.split() if len (x) <= 3]
print(b)
c = [[x] for x in range (5, 10)]
print(c)
d = [[0 for col in range(3)] for row in range(5)]
print(d)
e = [[row for col in range(3)] for row in range(5)]
print(e)
# write using a for loop

e = []
for row in range(5):
    exp = []
    for col in range(3):
       exp.append(row)        
    print(exp)
    e.append(exp)

print(e)

# Other comprehensions
f = [  [ col for col in range (1, 4) ] for row in range(4) ] 
print(f)

g = [  [ col for col in range (1, row) ] for row in range(4) ] 
print(g)

h1 = [ [ col for col in range (1, row) ] for row in range(2, 7)  ] 
h2 = [ [ col + 1 for col in range (row + 1) ] for row in range(5)  ] 
print (h1)
print (h2)

# print (a,b,c,d,e, sep = '\n------------\n')
# 
# 
punctuation = [x for x in "-Hello!. ??" if x in [".", "!", ",", ":", ";", "?", "-"]]
print(punctuation)

# Another way
Str = input('Type in your string:')
punctuation1 = [x for x in Str if x.isalnum() == False and x.isspace() == False]
punctuation2 = [x for x in Str if  not x.isalnum() and not x.isspace() ]
punctuation3 = [x for x in Str if  not (x.isalnum() or x.isspace()) ]
punctuation4 = [x for x in Str if  x.isalnum() == x.isspace() == False ]

print(punctuation1)
print(punctuation2)
print(punctuation3)
print(punctuation4)
