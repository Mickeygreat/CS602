''' Demo of a for loop and while'''


for ch in "bentley":
    print(ch)

for var in range(1,10):
    print(var, end = " ")

var = 1
while var <= 10:
    print (var)
    var += 1


line = input("Please enter a sentence and I will output the words \
in the sentence, which are longer than 3 characters long\n")
for word in line.split():
    if (len(word) > 3) :
        print(word)


word = "Bentley"
for ch in word:
    print(ch, end = " ")
print()

for i in range (len(word)):
    print(word[i], end= " ")
print()

i = 0
while i < len(word):
    print(word[i], end = " ")
    i += 1
print()






    



