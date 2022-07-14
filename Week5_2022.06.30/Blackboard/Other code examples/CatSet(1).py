'''
Created on Oct 28, 2019
@author: ruded
'''

# Use the input file called files-small2 for
# use with this code example

import os
from pygments.unistring import cats

def initDataStructures(filesLocation):
    
    catIDict, catADict = processCatFiles(filesLocation)
    
    return catIDict, catADict
    
def processCatFiles(filesLocation):
    files = os.listdir(os.path.join(os.getcwd(), filesLocation))
    catFiles = [f for f in files]
    
    intDict = {}
    actDict = {}
    
    for file in catFiles:
        
        with open(os.path.join(os.getcwd(), filesLocation, file), 'r') as cf:
            iCode =  cf.readline().strip()[0:]
            if iCode[0] == 'I':
                print (file, '--', iCode)
                catIntSet = { line.strip() for line in cf }                
                cf.close()

                if iCode not in intDict:
                    intDict [iCode] = catIntSet
                else: 
                    intDict [iCode] = intDict[iCode] | catIntSet
            else:
                print (file, '--', iCode)
                catActSet = { line.strip() for line in cf }                
                cf.close()

                if iCode not in actDict:
                    actDict [iCode] = catActSet
                else: 
                    actDict [iCode] = actDict[iCode] | catActSet
    return intDict, actDict
    
def main():
    subfolder= input('Please enter the name of the sub-folder with files: ')
    
    catsIntDict, catsActDict = initDataStructures(subfolder)
    
    allcats = set()
    for cats in catsActDict.values():
        allcats = allcats.union(cats)
            
    print('All Cats: Count: {} > {}'.format(len(allcats), sorted(allcats)))
    print('Cat Intelligence Dictionary > {}'.format(catsIntDict))
    print('Cat Activity Dictionary > {}'.format(catsActDict))
    
    allIntCats = set()
    for cats in catsIntDict.keys():
        if cats == 'I4':
            allIntCats = allIntCats.union(catsIntDict.get(cats))
            
    allActCats = set()
    for cats in catsActDict.keys():
        if cats == 'A5':
            allActCats = allActCats.union(catsActDict.get(cats))
            
    print('Cats with intelligence = 5 > {}'.format(allIntCats))
    print('Cats with activity = 5 > {}'.format(allActCats))
    print('The intersection is > {}'.format(allActCats.intersection(allIntCats)))
    
main()