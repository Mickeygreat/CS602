"""
Class: CS602
Name: Mark
Description:  Calculate the cost of a round fence given its
              radius and the cost per foot.
"""
import math

COST_PER_FOOT = 3.25

radius = float(input("What's the radius? "))


# perform the calculation

circumf = 2 * math.pi * radius

print ("The circumference of the fence is ", circumf)

cost = COST_PER_FOOT * circumf
print(f"The cost of the fence is ${cost:0.2f}", cost)
