'''
Created on <Place the date you wrote your program>
CS 602 Assignment 3 Summer 2022
@author: <Mickey Yeh>
'''
# import required Python modules and dataset information
import BostonWeather
import datetime # to recognize and transfer date strings
import math

# Global variables
# Assign the data set to the reference variable called WEATHER
WEATHERDATA = BostonWeather.bostonweather #filename.theVariableYouCallTheData
# print(WEATHERDATA)
# A list that contains the number of days for each month.
# The first entry, 0, is a place holder. The first value, 31,
# is the number of days in the month of January.
daysInMonths = [0,31,28,31,30,31,30,31,31,30,31,30,31]

# A list that holds the string names for each month.
months = ["","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# A list that holds the string names for each day of the week.
weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# Variables that hold the column values for the Boston Weather data
highTempCol = 3  # High Temperature column
lowTempCol = 5   # Low Temperature column
aveHumCol = 7    # Average Humidity column
aveWindCol = 13  # Average Wind Speed column


#----------------------S T A R T----------------------#

# The main function will run the program. The
# main function is referred to as the driver program/function.
def main():
    # created to accept user input
    # while loop version
    while True:
        try:
            date = input("Enter a date between 1/1/2010 and 12/31/2017 in mm/dd/yyyy format:")
            datetime_object = datetime.datetime.strptime(date, "%m/%d/%Y")

        # prints out system detection of what is wrong
        except Exception as e:
            print(e)
        # except ValueError:
        #     print("Invalid date format.")

        # elif datetime_object.strftime("%m") < 0 or datetime_object.strftime("%m") > 0:
        #     print("Month needs to be between 1 and 12.")

        # if enter format matches in try, it comes here to check condition
        else:
            startDate = datetime.datetime.strptime("01/01/2010", "%m/%d/%Y")
            endDate = datetime.datetime(2017, 12, 31)

            if datetime_object >= startDate and datetime_object <= endDate:
                inputYear = int(datetime_object.strftime("%Y"))
                inputMonth = int(datetime_object.strftime("%m"))
                inputDay = int(datetime_object.strftime("%d"))
                print("="*67)

                # First Output
                # print("Weather Information For: ", datetime_object.strftime("%m/%d/%Y"))
                print("Weather Information For: ", months[inputMonth], dayString(inputDay) + ",", inputYear, "(is a", dayOfWeek(inputYear, inputMonth, inputDay) + ").")

                # Second Output
                # convert input date into integer seperately
                # while isLeap(inputYear) is True:
                if isLeap(inputYear) is True:
                    print(inputYear, "is a Leap Year")
                    # break
                else:
                    print(inputYear, "is not a Leap Year")

                # Third Output
                # dayOfYear = to show how many days of the year
                # dayOfYear = sum(daysInMonths[:inputMonth]) + inputDay
                # print(months[inputMonth], dayString(inputDay) + ",", inputYear, "is the", dayOfYear, "day of the year.")
                nDayInYear = dayInYear(inputYear, inputMonth, inputDay)
                print(months[inputMonth], dayString(inputDay) + ",", inputYear, "is the", dayString(nDayInYear), "day of the year.")

                # Fourth Output
                # How many days into Spring/Summer/Fall/Winter
                seasonInfo(inputYear, inputMonth, inputDay)

                print("="*67)
                break

            # 補一個 28日 30日的判斷

            else:
                print("Year needs to be between 2010 and 2017.")


    # # for loop version
    # startDate = datetime.datetime.strptime("01/01/2010", "%m/%d/%Y")
    # endDate = datetime.datetime(2017, 12, 31)
    # date = input("Enter a date between 1/1/2010 and 12/31/2017 in mm/dd/yyyy format:")
    # for _ in date:
    #     datetime_object = datetime.datetime.strptime(date, "%m/%d/%Y")
    #     inputYear = int(datetime_object.strftime("%Y"))
    #     inputMonth = int(datetime_object.strftime("%m"))
    #     inputDay = int(datetime_object.strftime("%d"))
    #
    #     if ValueError:
    #         print("Invalid date format.")
    #     elif inputYear < 2010 or inputYear > 2017:
    #         print("Year needs to be between 2010 and 2017.")
    #     elif inputMonth < 1 or inputMonth > 12:
    #         print("Month needs to be between 1 and 12.")
    #     elif isLeap(inputYear) == False and inputMonth == 2:
    #         print("The day number must be <= 28.")
    #     else:
    #         print("Invalid date format.")
    #         break
    #
    # print("="*67)
    # # First Output
    # # print("Weather Information For: ", datetime_object.strftime("%m/%d/%Y"))
    # print("Weather Information For: ", months[inputMonth], dayString(inputDay) + ",", inputYear, "(is a", dayOfWeek(inputYear, inputMonth, inputDay) + ").")
    #
    # # Second Output
    # # convert input date into integer seperately
    # if isLeap(inputYear) is True:
    #     print(inputYear, "is a Leap Year")
    #
    # else:
    #     print(inputYear, "is not a Leap Year")
    #
    # # Third Output
    # # dayOfYear = to show how many days of the year
    # # dayOfYear = sum(daysInMonths[:inputMonth]) + inputDay
    # # print(months[inputMonth], dayString(inputDay) + ",", inputYear, "is the", dayOfYear, "day of the year.")
    # nDayInYear = dayInYear(inputYear, inputMonth, inputDay)
    # print(months[inputMonth], dayString(inputDay) + ",", inputYear, "is the", dayString(nDayInYear), "day of the year.")
    #
    # # Fourth Output
    # # How many days into Spring/Summer/Fall/Winter
    # seasonInfo(inputYear, inputMonth, inputDay)
    #
    # print("="*67)





    # selected day info:
    i = 0
    a = 0

    for _ in WEATHERDATA:
        if WEATHERDATA[i][a] == inputYear:
            a+=1
            if WEATHERDATA[i][a] == inputMonth:
                a+=1
                if WEATHERDATA[i][a] == inputDay:
                        print("High Temperature:", str(WEATHERDATA[i][highTempCol]).rjust(22-17), "F")
                        print("Low Temperature:", str(WEATHERDATA[i][lowTempCol]).rjust(22-16), "F")
                        print("Average Humidity:", str(WEATHERDATA[i][aveHumCol]).rjust(22-17), "%")
                        print("Average Wind:", str(WEATHERDATA[i][aveWindCol]).rjust(22-13), "MPH")

                else:
                    i+=1
                    a=0
            else:
                i+=1
                a=0
        else:
            i+=1
    # don't show input year info
    # Compare High and Low Temperatures from Other Years
    print("-"*70)
    print("Compare High and Low Temperatures from Other Years")
    print("-"*70)

    selectedDateHighTemp = WEATHERDATA[findRowIndex(inputYear, inputMonth, inputDay)][highTempCol]
    selectedDateLowTemp = WEATHERDATA[findRowIndex(inputYear, inputMonth, inputDay)][lowTempCol]

    tempStartYear = 2010
    # row = findRowIndex(tempStartYear, inputMonth, inputDay)
    # weatherInfoHigh = WEATHERDATA[row][highTempCol]
    # weatherInfoLow = WEATHERDATA[row][lowTempCol]

    highTempRecord = []
    lowTempRecord = []

    for _ in WEATHERDATA:
        if tempStartYear < 2018 and tempStartYear != inputYear:
            # for non Feb.
            if inputMonth != 2:
                row = findRowIndex(tempStartYear, inputMonth, inputDay)
                weatherInfoHigh = WEATHERDATA[row][highTempCol]
                weatherInfoLow = WEATHERDATA[row][lowTempCol]
                print(str(inputMonth) + "/" + str(inputDay) + "/" + str(tempStartYear), "High Temp:", (str(weatherInfoHigh)+"F").rjust(3), ("(" + compareData(selectedDateHighTemp, weatherInfoHigh) + ")").ljust(5),
                  "Low Temp:".rjust(18), (str(weatherInfoLow)+"F").rjust(3), ("(" + compareData(selectedDateLowTemp, weatherInfoLow) + ")").ljust(5))
                tempStartYear+=1
                highTempRecord.append(weatherInfoHigh)
                lowTempRecord.append(weatherInfoLow)
            # for Feb. but not 29th
            elif inputMonth == 2 and inputDay != 29:
                row = findRowIndex(tempStartYear, inputMonth, inputDay)
                weatherInfoHigh = WEATHERDATA[row][highTempCol]
                weatherInfoLow = WEATHERDATA[row][lowTempCol]
                print(str(inputMonth) + "/" + str(inputDay) + "/" + str(tempStartYear), "High Temp:", (str(weatherInfoHigh)+"F").rjust(3), ("(" + compareData(selectedDateHighTemp, weatherInfoHigh) + ")").ljust(5),
                        "Low Temp:".rjust(18), (str(weatherInfoLow)+"F").rjust(3), ("(" + compareData(selectedDateLowTemp, weatherInfoLow) + ")").ljust(5))
                tempStartYear+=1
                highTempRecord.append(weatherInfoHigh)
                lowTempRecord.append(weatherInfoLow)
            # for leap year
            # elif tempStartYear+2 != inputYear:
            elif inputMonth == 2 and inputDay == 29:
                if tempStartYear % 4 != 0:
                    tempStartYear+=1
                else:
                    row = findRowIndex(tempStartYear, inputMonth, inputDay)
                    weatherInfoHigh = WEATHERDATA[row][highTempCol]
                    weatherInfoLow = WEATHERDATA[row][lowTempCol]
                    print(str(inputMonth) + "/" + str(inputDay) + "/" + str(tempStartYear), "High Temp:", (str(weatherInfoHigh)+"F").rjust(3), ("(" + compareData(selectedDateHighTemp, weatherInfoHigh) + ")").ljust(5),
                            "Low Temp:".rjust(18), (str(weatherInfoLow)+"F").rjust(3), ("(" + compareData(selectedDateLowTemp, weatherInfoLow) + ")").ljust(5))
                    tempStartYear+=4
                    highTempRecord.append(weatherInfoHigh)
                    lowTempRecord.append(weatherInfoLow)
            else:
                tempStartYear = 2016

        elif tempStartYear < 2018 and tempStartYear == inputYear:
            tempStartYear+=1
            # pass

        else:
            break

    highTempRecord.append(selectedDateHighTemp)
    lowTempRecord.append(selectedDateLowTemp)
    averageHighTemp = sum(highTempRecord)/len(highTempRecord)
    averageLowTemp = sum(lowTempRecord)/len(lowTempRecord)
    print()
    print("The average high temperature from 2010 - 2017 for all", str(inputMonth) + "/" + str(inputDay), "days:", str(math.floor(averageHighTemp)), "F")
    print("The average low temperature from 2010 - 2017 for all", str(inputMonth) + "/" + str(inputDay), "days:",  str(math.floor(averageLowTemp)), "F")
    print("The highest temperature from 2010 - 2017 on", str(inputMonth) + "/" + str(inputDay), "is", max(highTempRecord), "F")
    print("The lowest temperature from 2010 - 2017 on", str(inputMonth) + "/" + str(inputDay), "is", min(lowTempRecord), "F")

    # don't show input year info
    # Compare Average Humidity from Other Years
    print("-"*70)
    print("Compare Average Humidity from Other Years")
    print("-"*70)

    humidityStartYear = 2010
    selectedDateHumidity = WEATHERDATA[findRowIndex(inputYear, inputMonth, inputDay)][aveHumCol]
    # humidityRow = findRowIndex(humidityStartYear, inputMonth, inputDay)
    # humidityInfo = WEATHERDATA[humidityRow][aveHumCol]
    humidityRecord = []

    for _ in WEATHERDATA:
        # condtion for not including input year info
        if humidityStartYear < 2018 and humidityStartYear != inputYear:
            if inputMonth != 2:
                humidityRow = findRowIndex(humidityStartYear, inputMonth, inputDay)
                humidityInfo = WEATHERDATA[humidityRow][aveHumCol]
                print(str(inputMonth) + "/" + str(inputDay) + "/" + str(humidityStartYear), "Average Humidity:", str(humidityInfo).rjust(2), "%",
                      "(" + compareData(selectedDateHumidity, humidityInfo) + ")")
                humidityStartYear+=1
                humidityRecord.append(humidityInfo)
            elif inputMonth == 2 and inputDay != 29:
                humidityRow = findRowIndex(humidityStartYear, inputMonth, inputDay)
                humidityInfo = WEATHERDATA[humidityRow][aveHumCol]
                print(str(inputMonth) + "/" + str(inputDay) + "/" + str(humidityStartYear), "Average Humidity:", str(humidityInfo).rjust(2), "%",
                      "(" + compareData(selectedDateHumidity, humidityInfo) + ")")
                humidityStartYear+=1
                humidityRecord.append(humidityInfo)
            elif inputMonth == 2 and inputDay == 29:
                if humidityStartYear % 4 != 0:
                    humidityStartYear+=1
                else:
                    humidityRow = findRowIndex(humidityStartYear, inputMonth, inputDay)
                    humidityInfo = WEATHERDATA[humidityRow][aveHumCol]
                    print(str(inputMonth) + "/" + str(inputDay) + "/" + str(humidityStartYear), "Average Humidity:", str(humidityInfo).rjust(2), "%",
                        "(" + compareData(selectedDateHumidity, humidityInfo) + ")")
                    humidityStartYear += 4
                    humidityRecord.append(humidityInfo)
            else:
                humidityStartYear = 2016

        elif humidityStartYear < 2018 and humidityStartYear == inputYear:
            humidityStartYear+=1
            pass

        else:
            break

    humidityRecord.append(selectedDateHumidity)
    averageHumidity = sum(humidityRecord)/len(humidityRecord)
    print()
    print("The average humidity from 2010 - 2017 for all", str(inputMonth) + "/" + str(inputDay), "days:", str(math.floor(averageHumidity)) + "%")

    # don't show input year info
    # Compare Average Wind from Other Years
    print("-"*70)
    print("Compare Average Wind from Other Years")
    print("-"*70)

    windStartYear = 2010
    selectedDateHumidity = WEATHERDATA[findRowIndex(inputYear, inputMonth, inputDay)][aveWindCol]
    # windRow = findRowIndex(windStartYear, inputMonth, inputDay)
    # windInfo = WEATHERDATA[windRow][aveWindCol]
    windRecord = []

    for _ in WEATHERDATA:
        # condtion for not including input year info
        if windStartYear < 2018 and windStartYear != inputYear:
            if inputMonth != 2:
                windRow = findRowIndex(windStartYear, inputMonth, inputDay)
                windInfo = WEATHERDATA[windRow][aveWindCol]
                print(str(inputMonth) + "/" + str(inputDay) + "/" + str(windStartYear), "Average Wind:", str(windInfo).rjust(2), "MPH",
                      "(" + compareData(selectedDateHumidity, windInfo) + ")")
                windStartYear+=1
                windRecord.append(windInfo)
            elif inputMonth == 2 and inputDay != 29:
                windRow = findRowIndex(windStartYear, inputMonth, inputDay)
                windInfo = WEATHERDATA[windRow][aveWindCol]
                print(str(inputMonth) + "/" + str(inputDay) + "/" + str(windStartYear), "Average Wind:", str(windInfo).rjust(2), "MPH",
                      "(" + compareData(selectedDateHumidity, windInfo) + ")")
                windStartYear+=1
                windRecord.append(windInfo)
            elif inputMonth == 2 and inputDay == 29:
                if windStartYear % 4 != 0:
                    windStartYear+=1
                else:
                    windRow = findRowIndex(windStartYear, inputMonth, inputDay)
                    windInfo = WEATHERDATA[windRow][aveWindCol]
                    print(str(inputMonth) + "/" + str(inputDay) + "/" + str(windStartYear), "Average Wind:", str(windInfo).rjust(2), "MPH",
                        "(" + compareData(selectedDateHumidity, windInfo) + ")")
                    windStartYear += 4
                    windRecord.append(windInfo)
            else:
                windStartYear = 2016

        elif windStartYear < 2018 and windStartYear == inputYear:
            windStartYear+=1
            pass

        else:
            break

    windRecord.append(selectedDateHumidity)
    averageWind = sum(windRecord)/len(windRecord)
    print()
    print("The average wind from 2010 - 2017 for all", str(inputMonth) + "/" + str(inputDay), "days:", str(math.floor(averageWind)) + "MPH")



# a
def compareData(selectedDayVal, otherDayValue):
    difference = otherDayValue - selectedDayVal
    if difference >= 0 and len(str(difference))==2:
        return "+" + str(difference)
    elif difference >= 0 and len(str(difference))!=2:
        return " " + "+" + str(difference)
    elif difference < 0 and len(str(difference))==2:
        return " " + str(difference)
    else:
        return str(difference)


# b
def dayInYear(year, month, day):
    LeapYearDays = 1
    # dayOfYear = sum(daysInMonths[:month]) + inputDay + day
    if isLeap(year):
        # while to if
        if month > 2:
            dayOfYear = sum(daysInMonths[:month]) + day + LeapYearDays
            # break
        else:
            dayOfYear = sum(daysInMonths[:month]) + day

    else:
        dayOfYear = sum(daysInMonths[:month]) + day

    return dayOfYear


# c
def seasonInfo(year, month, day):
    # transfer integer to string
    date1 = str(month) + "/" + str(day) + "/" + str(year)
    # transfer to date format
    date2 = datetime.datetime.strptime(date1, "%m/%d/%Y").strftime("%m/%d")

    # Spring 3/19-6/19
    springStart = datetime.datetime.strptime('3/19', "%m/%d").strftime("%m/%d")
    springEnd = datetime.datetime.strptime('6/19', "%m/%d").strftime("%m/%d")
    # Summer 6/20-9/21
    summerStart = datetime.datetime.strptime('6/20', "%m/%d").strftime("%m/%d")
    summerEnd = datetime.datetime.strptime('9/21', "%m/%d").strftime("%m/%d")
    # Autumn 9/22-12/20
    autumnStart = datetime.datetime.strptime('9/22', "%m/%d").strftime("%m/%d")
    autumnEnd = datetime.datetime.strptime('12/20', "%m/%d").strftime("%m/%d")
    # Winter 12/21-3/18
    winterStart = datetime.datetime.strptime('12/21', "%m/%d").strftime("%m/%d")
    endOfYear = datetime.datetime.strptime('12/31', "%m/%d").strftime("%m/%d")
    startOfYear = datetime.datetime.strptime('1/1', "%m/%d").strftime("%m/%d")
    winterEnd = datetime.datetime.strptime('3/18', "%m/%d").strftime("%m/%d")

    # for leap year when month > 2
    leapDay = 0
    if isLeap(year):
        if month > 2:
            leapDay = 1
        else:
            leapDay = 0
    else:
        leapDay = 0

    if date2 >= springStart and date2 <= springEnd:
        nDayOfSeason = (sum(daysInMonths[3:int(month)]) + day) - 19 +1 # +1 is the first day
        # result = "is", nDayOfSeason, "day(s) into Spring."
        print(months[month], dayString(day),"is", nDayOfSeason, "day(s) into Spring.")
    elif date2 >= summerStart and date2 <= summerEnd:
        nDayOfSeason = (sum(daysInMonths[6:month]) + day) - 20 +1
        # result = "is", nDayOfSeason, "day(s) into Summer."
        print(months[month], dayString(day),"is", nDayOfSeason, "day(s) into Summer.")
    elif date2 >= autumnStart and date2 <= autumnEnd:
        nDayOfSeason = (sum(daysInMonths[9:month]) + day) - 22 +1
        # result = "is", nDayOfSeason, "day(s) into Autumn."
        print(months[month], dayString(day),"is", nDayOfSeason, "day(s) into Autumn.")
    elif date2 >= winterStart and date2 <= endOfYear:
        nDayOfSeason = day - 21 +1
        # result = "is", nDayOfSeason, "day(s) into Winter."
        print(months[month], dayString(day),"is", nDayOfSeason, "day(s) into Winter.")
    elif date2 >= startOfYear and date2 <= winterEnd:
        nDayOfSeason = (sum(daysInMonths[1:month]) + day) + 11 +leapDay +1 # +11 is the winter days in last december
        # result = "is", nDayOfSeason, "day(s) into Winter."
        print(months[month], dayString(day),"is", nDayOfSeason, "day(s) into Winter.")
    else:
        print()
    # return result


#d
def findRowIndex(year, month, day):
    x = 0
    y = 0
    # d = 0

    for _ in WEATHERDATA:
        if WEATHERDATA[x][y] == year:
            y+=1
            if WEATHERDATA[x][y] == month:
                y+=1
                if WEATHERDATA[x][y] == day:
                    return int(x)

                else:
                    x+=1
                    y=0
            else:
                x+=1
                y=0
        else:
            x+=1


# Function that determines if a year is a leap year
def isLeap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Function that creates the day string that is used to
# add the appropriate two character letters after the day number.
# Returns a formated string in the format: 1st, 2nd, 3rd, 4th, etc.
def dayString(day):
    # The below code determines what the last
    # digit is in the day number, by converting
    # the integer into a string and evaluating
    # the last character.
    stringDay = str(day)
    lastChar = stringDay[-1]

    # The code below evaluates the last
    # character to determine if its a 1, 2, 3,
    # or something else, and then assign the
    # appropriate character extension to the
    # day number value.
    if 10 < day < 20:
        day_string = stringDay + "th"
    elif lastChar == '1':
        day_string = stringDay + 'st'
    elif lastChar == '2':
        day_string = stringDay + 'nd'
    elif lastChar == '3':
        day_string = stringDay + 'rd'
    else:
        day_string = stringDay + 'th'
    return day_string

# Function that determines the week day string for
# any date provided. Uses the date function and
# the weekday function from the Python datetime
# module.
def dayOfWeek(year, month, day):
    selected_date = datetime.date(year, month, day)
    selected_date_day = selected_date.weekday()
    day_string = weekDays[selected_date_day]
    return day_string


#----------------------Moved to Top----------------------#
# # The main function will run the program. The
# # main function is referred to as the driver program/function.
# def main():
#
#     # these lines test the provided functions. remove them and
#     # replace with your code.
#     print('Main Program') # Remove this code line
#     print(dayString(2)) # Remove this code line
#     print(dayString(13)) # Remove this line
#     print(dayString(31)) # Remove this code line
#     print(dayString(235)) # Remove this code line
#     print(dayOfWeek(2020, 6, 12)) # Remove this code line
#     print(isLeap(2020)) # Remove this code line
#----------------------Moved to Top----------------------#


# This entry calls the main function that starts
# the running of the program.
main()
