'''
Created on Sep 30, 2020
@author: ruded
'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given
for row in range(0, len(matrix)): 
    for column in range(0, len(matrix[row])): 
        print(matrix[row][column], end = " ")  
    print() # Print a newline
print()


for row in range(0, len(matrix)):
    total1 = 0
    for column in range(0, len(matrix[row])): 
        total1 += matrix[row][column]
    print("Sum for row " + str(row) + " is " + str(total1))
print()
  
total = 0
for column in range(0, len(matrix[0])): 
    for row in range(0, len(matrix)): 
        total += matrix[row][column]
    print("Sum for column " + str(column) + " is " + str(total))
    

