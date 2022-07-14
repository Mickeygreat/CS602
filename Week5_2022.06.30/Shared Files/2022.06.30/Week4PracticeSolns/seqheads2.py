"""
flip a coin and find the largest sequence of heads
"""
NFLIPS =50
import random
def flip():
    n = random.randint(1,2)
    if n == 1:
        flip ="H"
    else:
        flip = "T"
    return flip

seq = ""

for i in range(NFLIPS):
   coin = flip()
   seq += coin

print (seq)
head_groups = seq.split("T")   # this is kinda sneaky
print(head_groups)
lengths = [len(h) for h in head_groups]
print(lengths)
mx = max(lengths)
# mx = lengths[0]
# for item in lengths:
#     if item> mx:
#         mx = item


start = seq.index(mx*"H")
print("Max sequence is" , mx, "starting at", start)

arrows = start*" "+mx*"^"
print(seq)
print(arrows)
