"""
formatting in columns
"""

LINE = "="*50

item1 = 1053
description1 = "Air Fryer Toaster Oven"
price1 = 179.95

item2 = 4058
description2 = "Food Processor"
price2 = 79.99

item3 = 9422
description3 = "Blender"
price3 = 45.25

print(LINE + "\n" + \
      "Welcome to the Appliance Store.\n "
      + LINE +"\n")

print(f"{item1}\t{description1}\t${price1:>0.2f}")
print(f"{item2}\t{description2}\t${price2:>0.2f}")
print(f"{item3}\t{description3}\t${price3:>0.2f}")
print()
print(f"{item1}\t{description1:25s}\t${price1:>6.2f}")
print(f"{item2}\t{description2:25s}\t${price2:>6.2f}")
print(f"{item3}\t{description3:25s}\t${price3:>6.2f}")
