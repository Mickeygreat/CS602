"""
guessing game uses while loop
"""
import math
import random
print ("Guessing Game.")

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0
"""
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print(f"Congratulations! You've got it in {count} tries!")
        break
"""
# rewrite to avoid the break and while... true

MAX_GUESSES = 10
userNumber = int(input("Enter your guess: "))
while count <= MAX_GUESSES and userNumber != myNumber:
    count += 1

    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    userNumber = int(input("Enter your guess: "))

if userNumber == myNumber:
    print(f"Congratulations! You've got it in {count} tries!")
else:
    print("Sorry, the number was", myNumber)
