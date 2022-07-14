'''
Created on Oct 7, 2019

@author: ruded
'''
import csv

pList = []
f = open('president_heights_weights.csv')
for row in csv.reader(f):
    pList.append(row)

cont = input()
print(pList) # entire matrix

cont = input()
print(pList[0]) # single list in matrix

cont = input()
print(pList[0][1]) # single entry in a list in the matrix
print('\n')
#Read it all out element by element
for row in range(0, len(pList)): 
    for column in range(0, len(pList[row])): 
        print(pList[row][column], end = " ")  
    print() # Print a newline