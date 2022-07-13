import Sentence_Text
SENTENCE = Sentence_Text.sentence
s = SENTENCE
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
left = ("L", "l", "Left", "left", "LEFT")
right = ("R", "r", "Right", "right", "RIGHT")
center = ("C", "c", "Center", "center", "CENTER")

just = input("Enter justification ([L]eft/[R]ight/[C]enter): ")#.upper #justification input



#Target Word
import re
import string

PUNC = string.punctuation

target_word = input("Enter target word: ") #target word input
sentenceList = re.findall(r"[\w']+|[.,!?;]", s) #[\w'] = apostrophes


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
curr_line = "" # turns into a string
#curr_line = [] # turns into a list
curr_line_width = 0
line = 0

for word in range(len(words)-1): #list indices must be integers or slices, not str
  curr_line_width = curr_line_width + len(words[word])

  if (curr_line_width + len(words[word])) < lw:
    curr_line_width = curr_line_width + 1 # +1 is the space before next word
    curr_line = curr_line + words[word]
    curr_line = curr_line + " " # put in a space before next word

  elif (curr_line_width + len(words[word+1])) > lw:
      for _ in just: # justification code will add white spaces for you!!! Nice :)
        if _ in left:
          print("{:>2}".format(line+1), "|", curr_line.ljust(lw) + "|")
          line += 1 # neew line number
          curr_line_width = 0 # reset for next new line
          curr_line = "" # reset for next new line

        elif _ in right:
          print("{:>2}".format(line+1), "|", curr_line.rjust(lw) + "|")
          line += 1 # neew line number
          curr_line_width = 0 # reset for next new line
          curr_line = "" # reset for next new line

        elif _ in center:
          print("{:>2}".format(line+1), "|", curr_line.center(lw) + "|")
          line += 1 # neew line number
          curr_line_width = 0 # reset for next new line
          curr_line = "" # reset for next new line

        else:
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
