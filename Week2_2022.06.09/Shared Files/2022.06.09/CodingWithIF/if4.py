# write a program to have the user enter 3 numbers and print a message
# saying if the third number is between the first and the second
# the program should work regardless of whether the first is greater or less than the second

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
b = int(input(f"Enter a number in between {n1} and {n2}:"))

if (n1 < b and b < n2) or (n1 > b and b > n2):
    print(f"{b} is between {n1} and {n2}")
else:
    print(f"{b} is not between {n1} and {n2}")

# this also works

if (n1 < b < n2) or (n1 > b > n2):
    print(f"{b} is between {n1} and {n2}")
else:
    print(f"{b} is not between {n1} and {n2}")