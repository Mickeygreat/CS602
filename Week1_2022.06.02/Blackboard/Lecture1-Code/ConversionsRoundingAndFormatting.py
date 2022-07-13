'''
Created on Aug 27, 2018 @author: TBABAIAN
# Conversion, rounding, etc 
#  datatype(val) produces val as a datatype
'''

import math  #import mathematical funcitons from the math package

val = 7.540638
print ('val = ', val, ', int(val) = ' , int(val))
print (' round(val)=', round(val))
print (' round(val,1)=', round(val,1))    
print (' round(val,2)=', round(val,2))
print (' round(val,3)=', round(val,3))        


print ('\nstr(val) = ', str(val), 
        'math.ceil(val)=', math.ceil(val),
        ', math.floor(val) = ' , math.floor(val))

val = 5
print('(str(val).zfill(3)) -->', str(val).zfill(2))

print()
str = '4.5'
print (float(str)+1 )

