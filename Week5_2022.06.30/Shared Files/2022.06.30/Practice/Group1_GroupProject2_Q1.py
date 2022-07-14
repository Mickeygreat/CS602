"""
[Question 1]
Enter a string; remove all upper case letters, vowels, and digits.
Print the result.
"""

import re #to remove capital letters


string = input("Enter a String:")

vowels = ('a', 'e', 'i', 'o', 'u')
digits = ("1234567890")


# using loop and in
# to remove numeric digits, vowels, and capital letters from string
string2 = ""
for i in string:
  if i not in digits:
    if i not in vowels:
      string2 += i


#(re.sub(r'[A-Z]', '',string)) = remove capital letters
print(re.sub(r'[A-Z]', '',string2))
