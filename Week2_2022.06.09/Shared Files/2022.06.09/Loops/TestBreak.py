sum = 0
number = 0

while number < 20:
    number += 1
    sum += number
    if sum >= 100: 
        break

print("The number is", number)
print("The sum is", sum)

# does the word an e?
word = input("Enter a string: ").lower()

contains_e = False
for ch in word:
    if ch == "e":
        contains_e = True
        break
print(f"{word} contains_e: {contains_e}")

# without a break

contains_e = False
i = 0
while i < len(word) and not contains_e:
    ch = word[i]
    if ch == "e":
        contains_e = True
    i += 1
print(f"{word} contains_e: {contains_e}")
