# if statements

x = int(input("Enter a number: "))

if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")

# check for negatives

if x < 0:
    print(f"The number {x} is negative.")
print("This line is always printed")

# what's wrong here?

if x < 0:
  print(f"The number {x} is negative.")
else:
    if x >0:
        print(f"The number {x} is positive.")
    else:
        print("The number is zero.")

if x < 0:
   print(f"The number {x} is negative.")
elif x >0:
   print(f"The number {x} is positive.")
else:
   print("The number is zero.")
