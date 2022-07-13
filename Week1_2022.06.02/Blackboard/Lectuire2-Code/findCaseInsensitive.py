# -*- coding: utf-8 -*-
'''
Find a substring in a string in a case-insensitive manner, 
e.g. looking for **keyword** "DAY", 'day', 'Day', 'DAy' 
in **sentence** "what a wonderful day it is today".

PROBLEM: find/rfind  search and return a position,
 but only when the lettercases match.

The trick is to convert both sentence and keyword
 to the same lettercase, then do the search. 
 If we need to preserve the orginal form of sentence
  and keyword, we can store converted versions of
   both in new variables.
'''

sentence =  "What a wonderful day it is today!"
keyword = input ("enter a word and I will locate it inside sentence \n" + sentence)

#create lowercase versions of both keyword and sentence
sentenceLower = sentence.lower()
keywordLower = keyword.lower()
print ('Converted to lowercase', keywordLower, "\"" +sentenceLower + "\"")


#locate the first occurrance of keywordLower inside sentenceLower
posOfKeywrd = sentenceLower.find(keywordLower)
print(posOfKeywrd)