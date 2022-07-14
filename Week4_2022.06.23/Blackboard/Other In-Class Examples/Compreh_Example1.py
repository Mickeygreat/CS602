'''
Created on Sep 30, 2020
@author: ruded
'''
a = [5 for x in 'abc']
cont = input()
print('a = ', end = ''); print(a)

b = [x  for x in 'A little knowledge is a dangerous thing. '.split() if len(x) <= 3] 
cont = input()
print('b = ', end = ''); print(b)

c = [[x] for x in range(5,10)]
cont = input()
print('c = ', end = ''); print(c)

d = [[0 for col in range(3)] for row in range(5)]
cont = input()
print('d = ', end = ''); print(d)

e = [[row for col in range(3)] for row in range(5)]
cont = input()
print('e = ', end = ''); print(e)

cont = input()
string1 = 'This is a test! Is Dave, an instructor? To be or not to be, that is the question? test 1,2,3.'
print('\n' + string1)
f = [x for x in string1 if x in '.?,!']
cont = input()
print('f = ', end = ''); print(f)