'''
Name:  Mark Frydenberg
File: Examples of ord and chr functions
Description:
'''



lower = input("enter a lowercase letter: ")
upper = chr(ord(lower)-ord('a')+ord('A'))
print (lower, upper)

digitch = input ("enter a digit: ")
digit = ord(digitch) - ord('0')
print (digitch, digit)

# enter three digit characters and calculate the number

hundreds = int(input ("hundreds: "))
tens = int(input ("tens: "))
ones = int(input ("ones:"))

number = 100 * hundreds + 10 * tens + ones

print ("number = ", number)
