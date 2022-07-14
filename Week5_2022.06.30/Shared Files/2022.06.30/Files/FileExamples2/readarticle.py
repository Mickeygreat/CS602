"""
read a text file
"""
myfile = open("article.txt", "r")

text = myfile.read()
print(text)
search_word = input("enter a search word: ").lower()

search_word_count = 0
words = text.split()
for w in words:
    if search_word in w.lower():
        search_word_count +=1
print(search_word, " appears", search_word_count, "times")
