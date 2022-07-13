# Python program to demonstrate
# the str.format() method

# using format option in a simple string
print("{}, A computer science portal for geeks." .format("GeeksforGeeks"))

# using format option for a
# value stored in a variable
string = "This article is written in {}"
print (string.format("Python"))

# formatting a string using a numeric constant
print("Hello, I am {} years old !".format(18))

#formatting numbers
print('\nGeeks {0:2d}, Python {1:.2f}'.format(12,0.546))
print('Geeks {0:2d}, Python {1:2f}'.format(12,0.546))
print('Geeks {0:2d}, Python {1:8.2f}'.format(12,0.546))
print('Geeks {0:2d}, Python {1:>.2f}'.format(12,0.546))

print('\nWhat not to do')
#print('\nGeeks {d}'.format(12), 'Python {.2f}'.format(0.546))
