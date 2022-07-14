'''
Created on May 16, 2021
@author: ruded
'''
charString = '!#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz{|}~'
print('(Character) ASCii-Value')
stringLen = len(charString)
counter = 0
for i in range(stringLen):
    if counter > 10:
        counter = 0
        print()
    else:
        print(f'({charString[i]}) {ord(charString[i]):<3}', end='| ')
        counter += 1
print('(")', ord('"'), end='| ')        
print("(')", ord("'"))

print()
print('ASCii-Value (Character)')

counter = 0
for i in range(33, 127):
    if counter > 10:
        counter = 0
        print(f'{i} ({chr(i)})', end='| ')
        print()
    else:
        print(f'{i} ({chr(i)})', end='| ')
        counter += 1
