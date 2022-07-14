''' example of if statements
'''
# number = int(input("Numeric Grade?"))
#
# if number > 100  or number <0 :
#    grade = "Error" #error!
# elif number >= 95:
#     grade = "A"
# elif number >= 90:
#     grade = "A-"
# elif number >= 87:
#     grade = "B+"
# elif number >= 84:
#     grade = "B"
# elif number >= 80:
#     grade = "B-"
# else:
#     grade = "F"
#
# if grade == "F":
#     print ("Your grade is Failing")
# elif grade == "Error":
#     print("Error in data.")
# else:
#     print(f"Your grade is {grade}")


''' example of if statements
'''
number = int(input("Numeric Grade?"))

if number > 100  or number <0 :
   grade = "Error" #error!
elif number >= 80:
    grade = "B-"
elif number >= 84:
    grade = "B"
elif number >= 87:
    grade = "B+"
elif number >= 90:
    grade = "A-"
elif number >= 94:
    grade = "A"
else:
    grade = "F"

if grade == "F":
    print ("Your grade is Failing")
elif grade == "Error":
    print("Error in data.")
else:
    print(f"Your grade is {grade}")
