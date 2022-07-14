import random

"""
Find the largerst sequence of heads (starting at the right of the sequence).
Clever solution uses split to remove all of the sequences of Tails.
"""

def flip():
    if random.randint(1,2) == 1:
        return "H"
    else:
        return "T"

def flip_sequence(length= 50):
    seq = ""
    for i in range(length):
        seq += flip()
    return seq

def longest_heads(seq):
    longest_h = 0

    h_count =0
    pos = 0
    start_pos = 0
    for ch in seq:

       if ch == "H":
           h_count += 1
       else:
           if h_count >= longest_h:
                longest_h = h_count
                start_pos = pos - (longest_h)
                if start_pos < 0:
                    start_pos = 0
           h_count  = 0

       pos +=1
    return longest_h, start_pos

def main():
    length = 30  # 50 flips
    sequence = flip_sequence(length)
  #  sequence = "HHHHHTHHHHTT"
    longest_h, start_pos = longest_heads(sequence)
    print(f"found sequence of {longest_h} starting at {start_pos}")

    location_string = " " * start_pos + "^" * longest_h
    print(f"b[{location_string}] {start_pos}")
    print(longest_h, start_pos)
    print(sequence, "has ", longest_h, "consecutive heads:")
    print(location_string)

main()
