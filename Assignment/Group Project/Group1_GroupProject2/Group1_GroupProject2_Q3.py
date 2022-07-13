"""
[Question 3]
Hangman. Try writing the hangman game as described on page 4 and 5 of the handout from lecture 4.
(See course documents from June 9).
"""


print("Let's play a game of Hangman.")
print("Now it's your turn to guess a letter.\n")

secretword = "NOTEBOOK"

lettersguessed = ""

failurecount = 6

while failurecount > 0:
  guess = input("Please enter your next guess: ").upper()
  if guess in secretword:
      print(f"Correct.")
  else:
      failurecount -= 1
      print(f"Incorrect. Letter {guess} does not occur in this word.\n")

  lettersguessed += guess
  wronglettercount = 0

  for letter in secretword:
    if letter in lettersguessed:
        print(f"{letter}", end = " ")
    else:
        print("-", end = " ")
        wronglettercount += 1
  print("\n")

  if wronglettercount == 0:
    print(f"Congratulations! The word is: {secretword.upper()}. You Won!\n")
    break

else:
  print (f"You lost this game. The word is {secretword.upper()}.\n")
