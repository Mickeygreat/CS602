"""
[Question 2]
Given a sentence and a keyword that appears inside the sentence of the text (it will not be the first or the last word of any sentence), find the keyword and the two words that surround it in the sentence. Display the word and the surrounding words.

For example, given the following sentence (entered without line breaks): Guido Van Rossum once said that Python is an experiment in how much freedom programmers need and I certainly agree with this statement.

and keyword freedom, the program should output much FREEDOM programmers

For keyword Python, the output should be that PYTHON is

For an added challenge, make sure to make the program case-insensitive (i.e. treat python and Python as the same) and find the whole word and not a part of it (i.e., when looking for keyword an, don’t find it in the word Van)

Develop the program by

- identifying the INPUT, OUTPUT and PROGRAM DATA,

- outlining the algorithm and creating test cases,

- implementing the algorithm,

- testing and debugging your code.

Note: Program 2 has requirements which are very similar to this group assignment, so try working on this before you begin Program #2.
"""

sentence = """Guido Van Rossum once said that Python is an experiment in how much freedom programmers need and I certainly agree with this statement."""

keyword = input("Input keyword from sentence: ")
sentenceList = sentence.lower().split(" ")

for word in range(len(sentenceList)):
  if keyword.lower() == sentenceList[word]:
    print(sentenceList[word - 1], sentenceList[word].upper(), sentenceList[word + 1])
