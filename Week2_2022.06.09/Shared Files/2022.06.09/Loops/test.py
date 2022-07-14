startWithVowel = 0

previous = ''
current = input("Enter word: ")

if current[0].upper() in 'AEIOUY':
    startWithVowel += 1
    print (current , 'starts with a vowel')

while previous.lower() <= current.lower() :

    previous = current
    #read another word
    current = input("Enter word:")
    if current[0].upper() in 'AEIOUY':
        startWithVowel += 1
        print (current , 'starts with a vowel')

print ('startWithVowel = ', startWithVowel)
