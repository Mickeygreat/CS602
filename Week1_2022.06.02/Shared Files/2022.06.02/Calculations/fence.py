"""
Class: CS602
Name: Mark
Description:  Calculate the cost of a fence given its
              length and width and the cost per foot.
"""
COST_PER_FOOT = 3.95

length = int(input("What's the length? "))
width = int(input("What's the width? "))

# perform the calculation

perim = 2 * (length + width)

print ("The perimeter of the fence is ", perim)

cost = COST_PER_FOOT * perim
print(f"The cost of the fence is ${cost:8.2f}")
