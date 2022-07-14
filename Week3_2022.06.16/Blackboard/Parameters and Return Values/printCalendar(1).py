'''
Created on May 30, 2021
@author: ruded
Program: printCalendar
'''

# [global x], global function equals accept everything outside def for x value

# stub for printMonth
def printMonth(year, month):
    printMonthTitle(year, month)
    printMonthBody(year, month)


# stub for readInput
def readInput():
    year = eval(input('Enter full year (e.g. 2021): '))
    month = eval(input('Enter month as a number between 1 and 12: '))
    return year, month


# stub for printMonthTitle
def printMonthTitle(year, month):
    print(f'        {getMonthName(month)} {year}')
    print('-' * 28)
    print(' Sun Mon Tue Wed Thu Fri Sat')


# stub for getMonthBody
def printMonthBody(year, month):
    startDay = getStartDay(year, month)
    numberOfDaysInMonth = getNumOfDaysInMonth(year, month)
    
    i = 0
    for i in range(0, startDay):
        print("   ", end=" ")
    for i in range(1, numberOfDaysInMonth + 1):
        print(format(i, "3d"), end=" ")
        if (i + startDay) % 7 == 0:
            print()


# stub for getMonthName
def getMonthName(month):
    if month == 1:
        monthName = "January"
    elif month == 2:
        monthName = "February"
    elif month == 3:
        monthName = "March"
    elif month == 4:
        monthName = "April"
    elif month == 5:
        monthName = "May"
    elif month == 6:
        monthName = "June"
    elif month == 7:
        monthName = "July"
    elif month == 8:
        monthName = "August"
    elif month == 9:
        monthName = "September"
    elif month == 10:
        monthName = "October"
    elif month == 11:
        monthName = "November"
    else:
        monthName = "December"
    return monthName


# stub for getStartDay
def getStartDay(year, month):
    START_DAY_FOR_JAN_1_1800 = 3
    
    totalNumberOfDays = getTotalNumOfDays(year, month)
    return (totalNumberOfDays + START_DAY_FOR_JAN_1_1800) % 7


# stub for getTotalNumOfDays
def getTotalNumOfDays(year, month):
    total = 0
    for i in range(1800, year):
        if isLeapYear(i):
            total = total + 366
        else:
            total = total + 365
            
    for i in range(1, month):
        total = total + getNumOfDaysInMonth(year, i)
        
    return total


# stub for getNumOfDaysInMonth
def getNumOfDaysInMonth(year, month):
    if (month == 1 or month == 3 or month == 5 or month == 7 or 
        month == 8 or month == 10 or month == 12):
        return 31
    
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28


# stub for isLeapYear
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


# stub for main
def main():
    y, m = readInput()
    printMonth(y, m)


main()

