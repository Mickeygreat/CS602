'''
Created on Sep 30, 2020
@author: ruded
'''


'''
Given the following list called lst, what is the list after applying each of 
the following statements?
'''
lst = [20, 5, 0, 33, 1, 16]
print(lst)

lst.append(40)
lst.insert(1, 55)
lst.extend([7, 44])
lst.remove(1)
lst.pop(1)
lst.pop()
lst.sort()

lst.reverse()

cont = input()
print(lst)

'''
What is the return value
of each of the following
'''
cont = input()
lst = [20, 5, 0, 33, 1, 16]
print(lst)

cont = input()
print(lst.index(1))
cont = input()
print(lst.count(1))
cont = input()
print(len(lst))
cont = input()
print(max(lst))
cont = input()
print(min(lst))
cont = input()
print(sum(lst))

cont = input()

'''
What is the return value of each
of the following statements
'''
list1 = [25, 44, 22, 76, 91, 10]
print(list1)
cont = input()

a = [x for x in list1 if x > 30]
cont = input()
print('a = ', end = ''); print(a)
cont = input()

b = [x for x in range(0, 10, 2)]
cont = input()
print('b = ', end = ''); print(b)
