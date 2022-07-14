"""
String Methods with Loops
"""

sentence ="She sells sea shells by the sea shore."

words = sentence.split()
for w in words:
    print(w)
print()



#  deconstruct a date, which can have various length month, day, or years
#date = "6/9/2022"
date = "10/12/22"
first_slash = date.find("/")
last_slash = date.rfind("/")

month = int(date[:first_slash])
day = int(date[first_slash+1:last_slash])
year = int(date[last_slash+1:])
print(month, day, year)

# print only positions of 'e's

pos_e = sentence.find("e")
while pos_e != -1:
    print(pos_e)
    pos_e = sentence.find("e", pos_e+1)
print()

# in operator

VOWELS = "aeiou"
for ch in  sentence.lower():
    if ch in VOWELS:
        print(ch, "is a vowel")
    else:
        print(ch, "is a consonant")

# how can we improve this?


