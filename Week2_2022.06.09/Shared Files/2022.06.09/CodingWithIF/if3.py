# leap year test
# using nested conditions with if

# A leap year is exactly divisible by 4 except for century years
# (years ending with 00). The century year is a leap year only
# if it is perfectly divisible by 400.

year = int(input("Enter a year: "))

# To get year (integer input) from the user
# year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(f"{year} is a leap year")
       else:
           print(f"{year} is not a leap year")
   else:
       print(f"{year} is a leap year")
else:
   print(f"{year} is not a leap year")
