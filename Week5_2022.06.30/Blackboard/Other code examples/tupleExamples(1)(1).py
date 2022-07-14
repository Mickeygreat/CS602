'''
Created on Oct 31, 2019

@author: ruded
'''
t = 3, 'foo'
print(t)

t = tuple('abcdef')
print(t)

e = () # empty tuple
print(e)

s = 'hi' # s is a variable holding a string
print(s)

s = 'hi', #s is a tuple 
print(s)

#Sequence packing/unpacking
a = 45, 'g', 456.6
print(a)
b, c, d = a
print(b, c, d)

# Slicing
t = tuple('abcdef')
print(t)
print(t[1:5:2])
print(t[:-3])
print(t[4:])

# tuples cannot be chnaged, they are
# immutable, however a mutable object
# in a tuple can be changed
tu = 5, 'foo', [3,4,5]
print(tu)

# causes an error
tu[0] = 6

# this is OK
tu[2][0] = 1000
print(tu)
