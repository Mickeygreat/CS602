'''
Created on Nov 1, 2019
@author: ruded
setExamples
'''
s = {1,2,3}
s.add(1)
print(s)
# s[2] = 4 # exception is thrown
a ={2,3,40,50}
print(a)

print(s.intersection(a))
print(s & a)

print(s.difference(a))
print(s - a)

print(s.union(a))
print(s | a)

print(s.symmetric_difference(a))
print(s ^ a)

s.clear()
a.clear()
print(s, a)