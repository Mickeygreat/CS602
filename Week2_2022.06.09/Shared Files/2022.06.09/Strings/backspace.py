"""
Backspace character and Format Strings for Variable Names
"""

print("abcdef\bghijk")

s = "abc\b"
print (s)
print(len(s))
name= "mark"

print (f"My name is {name.capitalize()}")
print (f"My name is {name.upper()}")

print (f"{name =}")   # Python 3.8 or later!
print ("name ='" + name + "'" )
print (f"name= {name}")
