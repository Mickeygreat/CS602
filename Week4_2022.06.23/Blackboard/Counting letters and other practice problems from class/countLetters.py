'''
Three solutins to the letter counting problem
'''



text = "Use a list to store letter counts."
counters= [0]*26 # a list of counters for each letter, from a to z in order

#go through each letter of english
#for letter in range('a', 'z')
for lettercode in range (ord('a'), ord('z') + 1):
    ch = chr(lettercode)
    #count how many of ch are in text
    lettercount =  text.lower().count (ch)
    print (ch, ord(ch) - ord('a') , lettercount)
    # update the appropriate counter value
    counters[ ord(ch) - ord('a')  ] = lettercount
    print (counters)

# Generate a printout of the results showing each letter as:
# a:2 
# b:3
# c:0, etc.
# go through all indices in the counters array,  
for i in range (len(counters)):
    letter = chr(i + ord('a')) 
    print (letter, ':', counters[i])

 
print (counters)



# Another approach - go through all letters of str
#  incrementing teh appropriate counter

str = 'THis is a sentence  .'
 
  
counters = [0] *26
for ch in str.lower():
    #ch is a letter
    if  ch.isalpha():
        ind =  ord (ch)- ord('a') #which index corresponds to letter ch
        #print(ch, ind )    
        counters[ ind ] += 1

print(counters)
 

#
# calculate how many times each letter occurs in text
#  storing the letter count in list letterCounters
#


text = "Don't trouble trouble until trouble troubles you."
letterCounters = [0]*26
textLower = text.lower()



## Go through letters from a to z, calculate how many times it occurs\

for  i  in  range(26):
    letter = chr (ord('a') + i)
    letterCounters[ i ] = textLower.count( letter )
    #print ('iteration number' , i  , letter, letterCounters[i] )



# prints each letter with its count value
print(letterCounters)
letterIndex = ord('a')
for lc in letterCounters:
    print ( chr(letterIndex)  , ':' ,  lc    )
    letterIndex += 1






