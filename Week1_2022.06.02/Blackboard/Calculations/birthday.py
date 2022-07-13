"""
Class: CS602
Name: Mark
Description: (Birthday candles)

"""


SYMBOL = "!"  # SYMBOL is a symbolic constant
SONG_LINE = "Happy Birthday to you!"

# enter first name and age
first_name = input("first name: ")
age = int(input("age: "))

# multi-line statement

song = SONG_LINE + "\n" +  SONG_LINE + "\n"+ \
       "Happy Birthday, Dear " + first_name +"!" + "\n" + \
       SONG_LINE + "\n"

print(song)

# calculate candles and print message
candles = age * SYMBOL
print(candles)





