''' program solves the two problems on speech comparison from Handout 8.
    using inauguration speeches from Donald Trump and Joe Biden'''

import stopwords
import pprint as pp
import string
pp = pp.PrettyPrinter(indent=4)

def wordFreq (cleanfilename):
    ''' Construct word frequencies dictionary from words in file 
    cleanfilename, minus the stopwords in stopwords.py.
    Return the dictionary. '''
    
    STOPWORDS = stopwords.STOPWORDS # a file of words we don't want to include

    PUNC = string.punctuation
    wfdict = {}
    with open(cleanfilename, 'r', encoding="utf8") as infile:
        for line in infile:
            print(line)
            for word in line.split():

                if word[-1] in PUNC:
                    word = word[:-1]
                if word.lower() not in STOPWORDS:
                    #print (word)
                    if word in wfdict:
                        wfdict[word] += 1
                    else: 
                        wfdict[word] = 1
                
        infile.close()
    return wfdict


def itemvalue (key_value_tuple):
    ''' Helper function for sorting dictionary items.
    Returns the second element from a tuple'''
    return key_value_tuple[1] # the value part


def main(): 

    FILE1 = "adblake.txt"
    FILE2 = "chrite.txt"
    #First construct a dictionary with word frequencies for each speech 
    # (note, this is not needed for question 1, but can be used nevertheless)    
  
    dictA = wordFreq(FILE1)
    pp.pprint(dictA)
    dictB = wordFreq(FILE2)
    pp.pprint(dictB)
    print (len(dictA), len(dictB))



    print("1. Common words are: ")
    common = sorted(dictA.keys() & dictB.keys()) 
    numCommon =  len (common)
    print ( 'there are ', numCommon, 'non-stop words that are used in both speeches' )
    print( f'That is {numCommon/len(dictA) * 100:.1f} % of words of the first speech ', FILE1)
    print( f'and {numCommon/len(dictB) * 100: .1f} % of second.', FILE2)
    
    print("\n2. Most frequent words in each speech: ")
    
    #get list of items from dictionaries sorted by value from most frequent to least freq.
    lstA = sorted(dictA.items(), key=itemvalue, reverse = True)
    lstB = sorted(dictB.items(), key=itemvalue, reverse = True)
        
    topTenA =  lstA[:10]
    topTenB =  lstB[:10]

    print (FILE1, 'top 10 A---------------------\n')
    pp.pprint(topTenA)
    print (FILE2, 'top 10 B---------------------\n')
    pp.pprint(topTenB)

    topTenAwords = {pair[0] for pair in topTenA }
    topTenBwords = {pair[0] for pair in topTenB }
    
    print ("\nAmong the top 10 , there are common words. They are: ")
    
    commonFrequent = topTenAwords & topTenBwords
    print (commonFrequent)
    print ('only A ', FILE1,  topTenAwords - commonFrequent)
    print ('only B ', FILE2,  topTenBwords - commonFrequent)

    done = False
    while not done:
        word = input("Enter a word to see how many times it was said: ")
        if word != "":
            if word in dictA.keys():
                aCount = dictA[word]
            else:
                aCount = 0
            if word in dictB.keys():
                bCount = dictB[word]
            else:
                bCount = 0
            print(f"{FILE1}\t {word}\t {aCount}")
            print(f"{FILE2}\t {word}\t {bCount}")
        else:
            done = True



main()
