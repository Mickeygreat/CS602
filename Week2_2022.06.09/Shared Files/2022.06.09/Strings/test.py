'''
Name:  Mark Frydenberg
Description:  Next Letter
'''
ch = input("Enter a letter:").strip()
code = ord(ch)
print(f"{ch} has ascii value {code}")

num = int(input("Enter a number between 33 and 126: "))
ch = chr(num)
print(f"{ch} has ascii value {num}")

nextLetter = chr(ord(ch) +1)
print ("next letter is ", nextLetter)



