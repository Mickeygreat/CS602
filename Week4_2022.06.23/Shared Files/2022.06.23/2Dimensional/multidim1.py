'''
Created on Sept 30, 2019
@author: ruded
'''
matrix = [] # Create an empty list
numberOfRows = eval(input("Enter the number of rows: "))
numberOfColumns = eval(input("Enter the number of columns: "))

for row in range(0, numberOfRows): 
    matrix.append([]) # Add an empty new row 
    for column in range(0, numberOfColumns): 
        value = eval(input("Enter a number and press Enter: "))
        matrix[row].append(value) 

print(matrix)  

for row in range(0, len(matrix)): 
    for column in range(0, len(matrix[row])): 
        print(matrix[row][column], end = " ")  
    print() # Print a newline
