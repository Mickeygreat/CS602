'''
Created on Oct 28, 2019
@author: ruded
'''

# Use the input file called files-small1 to
# use with this code example

import os

def initDataStructures(filesLocation):
    
    catDict = processCatFiles(filesLocation)
    dogDict = processDogFiles(filesLocation)
    
    return catDict, dogDict
    
def processCatFiles(filesLocation):
    files = os.listdir(os.path.join(os.getcwd(), filesLocation))
    catFiles = [f for f in files if f if f.startswith ('cat')]
    
    cDict = {}
    
    for file in catFiles:
        with open(os.path.join(os.getcwd(), filesLocation, file), 'r') as cf:
            fileType = cf.readline().strip()
            print (file, '--', fileType)
            for line in cf:
                catCode, catName = line.strip().split(' ', 1)
                cDict [catCode.strip()] = catName.strip().title();
        cf.close()
    return cDict

def processDogFiles(filesLocation):
    files = os.listdir(os.path.join(os.getcwd(), filesLocation))
    dogFiles = [f for f in files if f if f.startswith ('dog')]
    
    dDict = {}
    
    for file in dogFiles:
        with open(os.path.join(os.getcwd(), filesLocation, file), 'r') as df:
            fileType = df.readline().strip()
            print (file, '--', fileType)
            for line in df:
                dogCode, dogName = line.strip().split(' ', 1)
                dDict [dogCode.strip()] = dogName.strip().title();
        df.close()
    return dDict    
def main():
    subfolder= input('Please enter the name of the sub-folder with files: ')
    
    catsDict, dogsDict = initDataStructures(subfolder)
    print(catsDict)
    print(dogsDict)
    print(catsDict.get('C8'))
    print(dogsDict.get('D7'))
    
main()

