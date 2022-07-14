''' program solves the two problems on speech comparison from Handout 8.'''


import os
import os.path
import stopwords



def wordFreq ( cleanfilename):
    ''' Construct word frequencies dictionary from words in file 
    cleanfilename, minus the stopwords in stopwords.py.
    Return the dictionary. '''
    
    STOPWORDS = stopwords.STOPWORDS
    
    wfdict = {}
    with open(cleanfilename, 'r') as infile:
        for line in infile:
            for word in line.split():
                if word not in STOPWORDS:
                    #print (word)
                    if word in wfdict:
                        wfdict[word] += 1;
                    else: 
                        wfdict[word] = 1;
                
        infile.close()
    return wfdict


def itemvalue (key_value_tuple):
    ''' Helper function for sorting dictionary items.
    Returns the second element from a tuple'''
    return key_value_tuple[1] # the value part


def main(): 
    
    #First construct a dictionary with word frequencies for each speech 
    # (note, this is not needed for question 1, but can be used nevertheless)    
  
    dictA = wordFreq(os.path.join(os.getcwd(), 'files','clean-presADB.txt'))
    dictB = wordFreq(os.path.join(os.getcwd(), 'files','clean-presKH.txt'))
    print (len(dictA), len(dictB))
    
    print("1. Common words are: ")
    common = sorted(dictA.keys() & dictB.keys()) 
    numCommon =   len (common)
    print ( 'there are ', numCommon, 'non-stop words that are used in both speeches' )
    print( 'That is ', format(numCommon/len(dictA) * 100,'.1f')  ,
           '% of words of the fist speech and ' , 
           format(numCommon/len(dictB) * 100, '.1f'), '% of second.')
    
    print("\n2. Most frequent words in each speech: ")
    
    #get list of items from dictionaries sorted by value from most frequent to least freq.
    lstA = sorted(dictA.items(), key=itemvalue, reverse = True)
    lstB = sorted(dictB.items(), key=itemvalue, reverse = True)
        
    topTenA =  lstA[:10]
    topTenB =  lstB[:10]

    print ('top 10 A---------------------\n', topTenA)
    print ('top 10 B---------------------\n', topTenB)
    
    topTenAwords = {pair[0] for pair in topTenA }
    topTenBwords = {pair[0] for pair in topTenB }
    
    print ("\nAmong the top 10 , there are common words. They are: ")
    
    commonFrequent = topTenAwords & topTenBwords
    print (commonFrequent)
    print ('only A ',  topTenAwords - commonFrequent)
    print ('only B ',  topTenBwords - commonFrequent)
    
main()