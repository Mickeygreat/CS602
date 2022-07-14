'''
Created on Sep 9, 2020
@author: ruded
'''
s = 'this is a string that contains many sub strings of words.'
print(s.split())
print(s.count('string'))
print(s.count('string', 8, 20))

s1 = 'Hello, welcome to my world.'
print(s1.endswith('my world.'))
print(s1.endswith('my world', 5, 11))

print(s1.startswith('Hello'))

x = s1.find("we", 5, 10)
print(x)

x1 = s.rfind("string", 16, 50)
print(x1)

print('Py' in 'Python')

print(s1.swapcase())
print(s.title())
print(s.capitalize())

s2 = s1.replace('welcome', 'goodbye')
print(s2)
