'''
Play a game of Hangman

The game stops when either
1. user guesses the entire word, and then user is the winner, or
2. when user has proposed 6 letters not found in the word. In this case, the
program wins.
'''


word = "TEMPERATURE"  #change this to pick a different word 

template  = word[0] + "-"*(len(word) -2) + word[-1]

print( "Let's play a game of Hangman.\n\
I have picked a word that starts with letter T and ends with E.\n\
Here's the template in which each dash denotes a single letter:\n",
template)

wrongGuesses = 0
word = word.upper()

while wrongGuesses < 6 and "-" in template:
    
    guess = input("Please enter your next guess:").upper()
    if guess not in word:
        print("Incorrect. Letter", guess, "does not occur in this word.")
        wrongGuesses += 1
    else:
        print("Correct.")
      
        #update the template, by going through each position in word, 
        # if letter matches the guess, replace dash in that position with the guess
 
        for index in range(len(word)):
            if word[index] == guess:
                # new template consist of old, except this letter replaces - at index
                template = template[:index] + guess + template[index+1:]
        
        print(template)

if  "-" not in template:
    print("Congratulations, you won!")
else:
    print("You lost. The word is", word)