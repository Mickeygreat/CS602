print("--- PASS ---")
for letter in 'Python':
    if letter == 'h':
        pass  # this line doesn't do anything except hold place for code coming later
        print('This is a pass')
    print('Current letter is',letter)
print("---BREAK---")

for letter in 'Python':
    if letter == 'h':
        break
        print('This is a break')
    print('Current letter is',letter)
print("-CONTINUE-")
for letter in 'Python':
    if letter == 'h':
        continue
        print('This is a continue')
    print('Current letter is',letter)
