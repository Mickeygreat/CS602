#To assign the contents of this file to a variable in your program, use these 3 lines:
import Sentence_Text
import textwrap
import nltk
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

SENTENCE = Sentence_Text.sentence

# print(SENTENCE)

#Keep the symbolic constant SENTENCE intact and assign a new variable to its value when you process or manipulate the text.
s = SENTENCE
# PARAGRAPH = "".join(s)
# print(PARAGRAPH)

#Your program asks the user to enter a line width, a justification (left, right, or center),
# and a target word, and then provides the following analysis:


#============================ S T A R T ============================#

#Line Width & Seperation Line
while True:
    try:
      lw = int(input("Enter line width: ")) #line width input
    except ValueError:
      print("Please enter an integer from 30 to 80!!!")
      #better try again... Return to the start of the loop

    if lw < 30 or lw > 80:
      print("Please enter an integer from 30 to 80!!!")

    else:
      # lw is successfully parsed!
      # we're ready to exit the loop.
      break

if lw >= 30 and lw <= 80:
  split_line = ("=" * (lw+6)) # +8 to align text processing

else:
  print() #這樣可以跳過這行


#Justification
import textwrap

formatted_paragraph = textwrap.fill(s, lw)
split_line_paragraph = formatted_paragraph.splitlines() #to split formatted paragraphs into seperate lines
total_lines = len(split_line_paragraph) #to know how many lines

left = ("L", "l", "Left", "left", "LEFT")
right = ("R", "r", "Right", "right", "RIGHT")
center = ("C", "c", "Center", "center", "CENTER")

j = input("Enter justification ([L]eft/[R]ight/[C]enter): ")#.upper #justification input

# move down to make justification work
# for _ in j:
#   if _ in left:
#   # if i == "L" or i == "Left" or i == "l" or i == "left":
#     # l_just = textwrap.fill(s, lw).ljust(lw)
#     break
#
#   elif _ in right:
#   # elif i == "R" or i == "Right" or i == "r" or i == "right":
#     # r_just = textwrap.fill(s, lw).rjust(lw)
#     break
#
#   elif _ in center:
#   # elif i == "C" or i == "Center" or i == "c" or i == "center":
#     # c_just = textwrap.fill(s, lw).center(lw)
#     break
#
#   else:
#     print('Please enter letter "L" or "R" or "C" for corresponding justification!!!')


#Target Word
import re
import string

PUNC = string.punctuation

target_word = input("Enter target word: ") #target word input
sentenceList = re.findall(r"[\w']+|[.,!?;]", s) #[\w'] = apostrophes

# for word in range(len(sentenceList)):
#     if target_word.lower() == sentenceList[word]:
#         print("-->", sentenceList[word - 1], sentenceList[word].upper(), sentenceList[word + 1])



#Text Analysis
number = sum(c.isdigit() for c in s)

#find the 4-digit string in sentence #"(\d{4})" -> look for 4 digit string: ex:['2000','2002']
import re
year = len(re.findall("(\d{4})", s))
target = s.count(target_word)
letter = sum(c.isalpha() for c in s) #or len(SENTENCE)

#word count
words = s.split()
words_count = len(words)

#sentence count
sentence = s.split(".") # with "." includes "!" and "?" already :)

# import nltk
# nltk.download('punkt')
# from nltk.tokenize import sent_tokenize
# sentence = sent_tokenize(s)
sent_count = len(sentence)


avg_word_length = sum(len(word) for word in words) / len(words)
avg_sent_length = sum(len(sent) for sent in sentence) / len(sentence)

print(split_line)

# -9 to push printed numbers forwars
print("Digit Count: ", str(number).rjust(lw-13-9))
print("Year Count: ", str(year).rjust(lw-12-9))
print("Target Count: ", str(target).rjust(lw-14-9))
print("Character Count: ", str(letter).rjust(lw-17-9))
print("Word Count: ", str(words_count).rjust(lw-12-9))
print("Sentence Count: ", str(sent_count).rjust(lw-16-9))
print("Avg Word Length: ", str("{:.3f}".format(avg_word_length)).rjust(lw-13-9))
print("Avg Sent Length: ", str("{:.3f}".format(avg_sent_length)).rjust(lw-13-9))
#========================================================
print(split_line)

#Text Processing
import textwrap

formatted_paragraph = textwrap.fill(s, lw)
split_line_paragraph = formatted_paragraph.splitlines() #to split formatted paragraphs into seperate lines
total_lines = len(split_line_paragraph) #to know how many lines

line = 0
#============================ Fix the Justification ============================#
for line in range(total_lines):
  # r = len(list(split_line_paragraph[line]))

  if line <= total_lines:

    #這個從上面搬下來的！！！
    for _ in j: # justification cdoe will add white spaces for you!!! Nice :)
        if _ in j in left:
            # spaces = " " * (lw-r)
            # print(str(line+1).rjust(2), "|", split_line_paragraph[line], spaces, "|") #sequence(Number, |, sentence, Space before | to align it, |)
            print("{:>2}".format(line+1), "|", split_line_paragraph[line].ljust(lw) + "|")
            # "{:>2}".format() -> right justifies with a width of 2!!!
            line += 1

        elif _ in right:
            print("{:>2}".format(line+1), "|", split_line_paragraph[line].rjust(lw) + "|") #sequence(Number, |, sentence, Space before | to align it, |)
            line += 1

        elif _ in center:
            print("{:>2}".format(line+1), "|", split_line_paragraph[line].center(lw) + "|") #sequence(Number, |, sentence, Space before | to align it, |)
            line += 1

        else:
            # print('Please enter letter "L" or "R" or "C" for corresponding justification!!!')
            break

#========================================================
print(split_line)



for word in range(len(sentenceList)):
     # punctuation in front
     if target_word == sentenceList[word] and sentenceList[word - 1] in PUNC:
        print("-->", ">", sentenceList[word].upper(), sentenceList[word + 1])
     # punctuation at the back
     elif target_word == sentenceList[word] and sentenceList[word + 1] in PUNC:
        print("-->", sentenceList[word - 1], sentenceList[word].upper(), "<")
     elif target_word == sentenceList[word]:
        print("-->", sentenceList[word - 1], sentenceList[word].upper(), sentenceList[word + 1])


print(split_line)
