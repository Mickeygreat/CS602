# string to number conversion

s = input ("enter a string of two numeric characters: ")
firstChar = s[0]
secondChar = s[1]

firstDigit = ord(firstChar) - ord('0')
secondDigit = ord(secondChar) - ord('0')

number = 10 * firstDigit + secondDigit
print("The number is", number)
print("The number plus 1 is ", number + 1)


