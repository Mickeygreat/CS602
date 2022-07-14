'''
Created on Oct 7, 2019

@author: ruded
'''
import csv

pList = []
f = open('president_heights_weights.csv')
for row in csv.reader(f):
    pList.append(row)

cont = input("Continue 1:")
print(pList) # entire matrix

cont = input("Continue 2:")
print(pList[0]) # single list in matrix

cont = input("Continue 3:")
print(pList[0][1]) # single entry in a list in the matrix
print('\n')
#Read it all out element by element
for row in range(0, len(pList)): 
    for column in range(0, len(pList[row])): 
        print(pList[row][column], end = " ")  
    print() # Print a newline
###
print() # Print a newline
print("Alternative Solution:")
for pres in pList:
    for column in range(0, len(pres)):
        print(pres[column], end = " ")
    print() # Print a newline
