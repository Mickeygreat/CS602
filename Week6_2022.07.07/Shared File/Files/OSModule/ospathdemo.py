'''
Created on Oct 2, 2018
Demo of the os.path package functions
@author: TBABAIAN
'''

import os
print("Current path: ")
orig_path = os.getcwd()#'C:\\Users'
#path = input ("Please enter a path to a folder")
print (orig_path)
path = input("Press ENTER to use this path or type another one: ")
if path == "":
    path = orig_path

print('Examine content of ', path)
print (os.path.getsize(path))

allfiles = os.listdir(path)
print(allfiles)
# print if an element of a folder is a folder or a file  
for item in allfiles:
    print (item, 'is a', end = ' ')
    itemFullPath = os.path.join(path, item)
    if os.path.isdir(itemFullPath):
        print('folder') 
    elif os.path.isfile(itemFullPath):
        print('file')
    else:
        print(' neither ')
        


# generate all file extensions for a given folder in a list using a comprehension
folder = path
print('\n collect all extensions of files in ', folder)

extensions = [  os.path.splitext(item) [1]  for item in  os.listdir(folder)  
                                            if  os.path.isfile(item)         
              ]
print (extensions)
nonEmptyExtensions = [ x  for x in extensions if x!=''  ]

print (nonEmptyExtensions)
