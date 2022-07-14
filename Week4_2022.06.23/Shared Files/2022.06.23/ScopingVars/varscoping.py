''' Examples demonstrating local/global scoping of variables
'''

x = 1
def f1():
    x = 2
    print("inside f1, x= ", x) #

print("before f1, x= ", x) #
f1()
print("after f1, x= ", x) #
exit()


x = 1
def increase():
    global x
    x =  x + 1
    print("inside increase, x = ", x)

print("before increase, x = ", x)
increase()
print("after increase, x = ", x)

