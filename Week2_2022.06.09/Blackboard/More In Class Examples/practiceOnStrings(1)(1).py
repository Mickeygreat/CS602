'''
Created on Sep 6, 2018
@author: TBABAIAN
PRactice problems from handout 2 in reverse order
'''

str1 = 'Brevity is the soul of wit'
words = str1.split()
posFSpace = str1.find(' ')
posLSpace = str1.rfind(" ")
middle = str1[posFSpace: posLSpace].strip();
print (words[0].upper() , middle, words[-1].upper())

str2 = 'blackboard'
posA = str2.find('a')
twoLetters = str2[posA + 1:posA + 3].upper()
newstr = str2[:posA + 1] + twoLetters + str[posA + 3:]
print (newstr)

str3 = "Hi, my name is Tamara"
newstr = str3.replace(' ', '-')
print (newstr)

str4 = 'Some text ( and some more in parens)  is included here. '
posLeft = str4.find('(')
posRight = str4.find(')')
print (str4[posLeft + 1:posRight].strip())

str5 = 'WooHoo'
print(str5[len(str5) // 2:])

word = 'Bentley'
upperLetters = (word[0] + word[-1]).upper()
print(upperLetters)

str6 = '9856784433'
phoneWIthDashes = str6[:3] + '-' + str6[3:6] + '-' + str6[6:]
print(phoneWIthDashes)

