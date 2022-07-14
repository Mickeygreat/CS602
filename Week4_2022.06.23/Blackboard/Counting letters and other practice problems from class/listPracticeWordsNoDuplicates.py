'''
1. Given a text-storing string, produce a sorted 
list of words in it that includes each word
only once. Deal with punctuation the best way you can.
'''
#ADDING Strategy As we move trhough the list, add word into a new list,
# but only if it's not already there 

str = 'don\'t trouble trouble until trouble troubles you'
wordsLst = str.split()
newList = []
for word in wordsLst:
    if word not in newList:
        newList.append(word)

newList.sort()
print (newList)



