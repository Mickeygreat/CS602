"""
Move words from a string to a list to a set to a list again.
"""

sentence = "one fish two fish red fish blue fish"
words = sentence.split()

word_set = set()  # the empty set
for w in words:
    word_set.add(w)

print(word_set)

for w in word_set:
    print(w)
# these are unordered

# print (word_set[2])  can't do this!

unique_list = [ w for w in word_set]
print(unique_list)
unique_list.sort()
print(unique_list)
