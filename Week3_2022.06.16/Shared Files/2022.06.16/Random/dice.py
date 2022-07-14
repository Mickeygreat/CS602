'''
Random Dice Rolling (for loops)

'''

import random


count = 0
boxcars = 0
for roll in range(100):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 == d2:
        count += 1
        print(d1,d2)
    if d1 + d2 == 12:
        boxcars += 1
#      print("Both dice match!")

print("Total number of doubles: ", count)
print("Total number of boxcars:  ", boxcars)
