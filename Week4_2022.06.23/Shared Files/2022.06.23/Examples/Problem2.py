'''
Created on Sep 30, 2020
@author: ruded
'''


'''
Write a program that returns a new list by
eliminating the duplicate values in the original list
'''

# Read numbers as a string from the console
s = input("Enter numbers: ") 
items = s.split() # Extracts items from the string
numbers = [ eval(x) for x in items ] # Convert items to numbers
    
result = []
for element in numbers:
    if not (element in result): 
        result.append(element)
   
    
print("The distinct numbers are: ", end = ''); print(result)





