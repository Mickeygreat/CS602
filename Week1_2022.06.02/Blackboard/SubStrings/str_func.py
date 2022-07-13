"""
String Methods
"""
sentence = "Today is Wednesday."
print (sentence.split())
print(1, "myfile.txt".split('.'))
s = "banana bread"

print(2, s.count("an"))
print(3, s.endswith('d'))
print(4, s.find("an",3))
print(5, s.find("an"))
print(6, s.find("an",4))

print(7, f"Uppercase: {s.upper()}\t Lowercase:  {s.lower()}")
print(8, f"Capitalize:  {s.capitalize()}\t Title case: {s.title()}")

print(9, s.find("an", s.find("an")+1))
print(10, "*".join(s))
print(11, s.isalpha())
print(12, s.isdigit())
print(13, s.split(" "))
print(14, s.startswith("ban"))
print(15, s.replace("banana","pumpkin"))
print(16, s.replace("a","@"))
print(16, s.replace("a","@",2))
s = s.center(30)
print(17, f"|{s}|")
s = s.strip()
print(18, f"|{s}|")

