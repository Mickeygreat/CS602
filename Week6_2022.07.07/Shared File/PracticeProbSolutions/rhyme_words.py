import string
import pprint as pp



def main():

  g = string.punctuation
  f = open("rhyme.txt",'r')
  s = f.read()  # read f into a long string

  s = s.lower()
  # remove all punc
  for ch in s:
    if ch in g:
      s = s.replace(ch, "")

  #word list
  words = s.split()

  # construct dict by frequency
  word_dict = {}
  for word in words:
    if word not in word_dict:
      word_dict[word] = 1
    else:
      word_dict[word] = word_dict.get(word) + 1


  for key,val in word_dict.items():
    print(f'{key:<13}{val:>13}')
  print(f'\n{"Alphabetical":^26}')
  for key in sorted (word_dict):
    print(f'{key:<13}{word_dict[key]:>13}')

  print(f'\n{"Sort By Frequency":^26}')

   # there are probably better ways to do this, but thi swokrs!
  d_words = word_dict.copy()
  d_words_sorted_by_freq = []
  while d_words != {}:
      key_list, val_list = list(d_words.keys()), list(d_words.values())
      min_val = min(val_list)
      position = val_list.index(min_val)
      d_words_sorted_by_freq.insert(0, (key_list[position], val_list[position]))
            # creates the list with highest freq first, use append() if you want it in increasing order
      d_words.pop(key_list[position])


  for k, v in d_words_sorted_by_freq:
       print(f'{k:<13}{v:>13}')

main()
