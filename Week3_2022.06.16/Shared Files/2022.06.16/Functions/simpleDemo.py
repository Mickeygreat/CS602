'''
Created on Sep 25, 2018
Simplest function definition and function calls
@author: root
'''


# The following is a function definition
# This function has no parameters and no return value
def printHelloWorld():
    print ('Hello, world')
    print ("Goodbye, cruel world!")

 # call the above function three times
printHelloWorld()
printHelloWorld()
printHelloWorld()


#---------------------------------------------
#Function takes a single parameter; returns no value
def printHello (name):
    print ('Hello,' , name , '!')



printHello('Tamara')
printHello('Mark')

aname = input('Greetings! what is your name?')
printHello(aname)
print(aname)


--------------------------------------------------------
Function takes a single parameter, returns a single value

def helloString (name):
    result = 'Hello, ' + name + '!'
    return result

#helloString("Cathy") doesn't do anything

greetingString =  helloString('Cathy')
print(greetingString)
print(helloString("Jackie"))

def helloString2 (name='David'):   # default parameter

    result = 'Hello, ' + name + '!'
    return result

def main():
    greetingString = helloString2()
    print(greetingString)
    greetingString = helloString2('Cathy')
    print(greetingString)
    #
main()


