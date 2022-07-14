# String Indices
print('String Indices')
fruit = 'banana'
letter = fruit[1]
print(letter)
letter = fruit[4]
print(letter)
#letter = fruit[6]
print(letter)

# strings are immutable

#fruit[0] = 'm'
print(fruit)

fruit = 'm' + fruit[1:]
print(fruit)
