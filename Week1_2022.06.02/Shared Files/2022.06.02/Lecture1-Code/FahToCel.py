'''
Simple example program for the first class.
Converts temperature in degrees Fahrenheit to Celsius according 
to the formula TC = (TF -32)* 5/9
'''

print ("This program converts temperature in degrees Fahrenheit to degrees Celcius")

# convert from F to Celsius 

#fahStr = input('Please enter an integer number of degrees F ')
#print (fahStr, type(fahStr))
#fah = eval(fahStr) # evaluate the input string; will convert input string into a number

fah = float(input("Enter a number of degrees F: "))

celcius = (fah - 32) * 5 / 9
print(fah, type(fah))

#print it rounded to the closest int
print (fah, 'degrees F equals',  round(celcius), 'degrees C')



