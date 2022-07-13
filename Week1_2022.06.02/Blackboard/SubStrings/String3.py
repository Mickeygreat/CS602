s ='Snowy Wednesday'
print(1, s[0:5])
print(2, s[6:13])
print(3, s[:3])
print(4, s[3:])

# step is 2
print(5, s[0::2])

#start at string length, end at position 0, move with step -1
print(6, s[len(s)::-1])

print(7, s[::-1])
print(8, s[::])
