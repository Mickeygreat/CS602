"""
CS 602 Summer 2022
Social Security Data:  Baby Names Data Analysis

WRITE YOUR NAME HERE: Mickey Yeh
"""
import os
import pprint as pp
import matplotlib.pyplot as plt
import numpy as np

DEBUG = False #set to True for verbose output

FIRST_N = 200  # how many names to read from each file
DIRNAME = 'data'
EXT = '.txt'
SEPARATOR = "-"*10


############# HELPERS

def new_section(number):
    if DEBUG:
        input("Press enter to continue.")
    print("\n" + SEPARATOR + str(number) + SEPARATOR + "\n")

def show_names_in_columns(names, ncols=5):

    count = 0
    for name in names:
        count += 1
        print(f"{name:10s}", end=" ")
        if count % ncols == 0:
            print()
    print()


# scanning the directory to get required files
def get_data():
    f_name_data_dict = {}
    m_name_data_dict = {}

    for file_f in os.scandir(DIRNAME):
        num_f = 0
        num_m = 0
        if file_f.path.endswith(EXT):
            with open(file_f, "r") as myfile:
                year = int(myfile.name.split(".")[0][-4:])
                # to check if year == year on file name
                # print(myfile.name)
                while num_f < FIRST_N or num_m < FIRST_N:
                    words = myfile.readline().strip().split(",")
                    if words[1] == "F":
                        num_f += 1
                        if num_f > FIRST_N:
                            continue  # Skip the appending process if the number of female names is larger than 200
                        if words[0] not in f_name_data_dict:
                            f_name_data_dict[words[0]] = {year: int(words[2])}
                        elif words[0] in f_name_data_dict:
                            f_name_data_dict[words[0]][year] = int(words[2])

                    if words[1] == "M":
                        if words[0] not in m_name_data_dict:
                            m_name_data_dict[words[0]] = {year: int(words[2])}
                        elif words[0] in m_name_data_dict:
                            m_name_data_dict[words[0]][year] = int(words[2])
                        num_m += 1

    return m_name_data_dict, f_name_data_dict



####  1
def find_names_of_length_x(nchars, name_data_dict):

    name_list = [name for name in name_data_dict if len(name) == nchars]
    name_list.sort()

    return name_list

def show_names_of_length(gender, n_chars, name_data_dict):
    result = find_names_of_length_x(n_chars, name_data_dict)
    print(f"{len(result)} {gender} name(s) have {n_chars} letters. ")
    show_names_in_columns(result, 10)

#### 2

def find_longest_name_length(name_data_dict):

    # built-in function max(): a key argument to find the longest string in a list/dict/etc.
    longest_key = max(name_data_dict, key=len)
    # to change the longest name into length of name
    length = len(longest_key)

    return length

def show_longest_length(gender, name_data_dict):
    longest = find_longest_name_length(name_data_dict)
    print(f"The longest {gender} names have {longest} letters:")
    show_names_of_length(gender, longest, name_data_dict)

#### 3


def search_names_containing(search, name_data_dict):
    # write this using a list comprehension. watch the video of the course recording for the answer!
    name_list = [key for key in name_data_dict if search in key.lower()]
    name_list.sort()

    return name_list

def show_names_containing(gender, search_string, name_data_dict):
    result = search_names_containing(search_string, name_data_dict)
    print(f"{len(result)} {gender} name(s) contain {search_string}.")
    show_names_in_columns(result)

####  4

def find_names_as_both( m_name_data_dict, f_name_data_dict):
    """
    return a list of both male and female names
    """
    both_names = [names for names in m_name_data_dict if names in f_name_data_dict]

    return both_names


#### 5

def is_name_becoming_popular(years, year_freq_dict):

    # return True if the name has had increasing popularity during the years specified
    year1, year2, year3 = years

    for name in year_freq_dict.keys():
        if year1 in year_freq_dict.keys() and year2 in year_freq_dict.keys() and year3 in year_freq_dict.keys():
            if year_freq_dict[year1] < year_freq_dict[year2] < year_freq_dict[year3]:
                increasing = True

            else:
                increasing = False

        else:
            increasing = False

        return increasing


def show_incr_popular_names(gender, years, name_data_dict):

    print(f"\nThese {gender} names increase in popularity from 2000-2020:")
    popular_names = []
    for name in name_data_dict.keys():
        year_freq_dict = name_data_dict[name]
        if is_name_becoming_popular(years, year_freq_dict):
            popular_names.append(name)

    popular_names.sort()
    # REQUIRED: rewrite the code segment above as a list comprehension
    print("=" * 55)
    # REQUIRED: write the code to display the output as shown in the sample
    for trend_names in popular_names:
        print(trend_names.ljust(13), "2000: ", str(name_data_dict[trend_names][2000]).rjust(6),
              " 2010: ", str(name_data_dict[trend_names][2010]).rjust(6),
              " 2020: ", str(name_data_dict[trend_names][2020]).rjust(6))

    print("=" * 55)



#### 6

def find_top_names_in_year(year, name_data_dict, number):

    top_name_freq_list = []   # will be a list of tuples
    for name6 in name_data_dict.keys():
        # if year in name_data_dict[name6][year]:  # ERROR! # argument of type 'int' is not iterable # occurs when we use the membership test operators (in and not in) with an integer value
        if year in name_data_dict[name6].keys():
            # to get the value count of the name in wanted year
            value = name_data_dict[name6][year]
            if len(top_name_freq_list) < 10:
                top_name_freq_list.append((name6, value))
                # sort the list of tuples
                # reverse = None (Sorts in Ascending order)
                # key is set to sort using second element
                # sublist lambda has been used
                # sorted(name_data_dict, key=lambda x: (name_data_dict[x][year])) # not correct! this is sorting a dictionary
                top_name_freq_list.sort(key=lambda x: x[1])  # sort by second element in the tuple
            # elif len(top_name_freq_list) >= 10:
            else:
                # get name from list and search count for wanted year to compare
                if name_data_dict[top_name_freq_list[0][0]][year] < name_data_dict[name6][year]:
                    top_name_freq_list[0] = (name6, value)
                    top_name_freq_list.sort(key=lambda x: x[1])
        else:
            pass

    return top_name_freq_list


def show_top_names_in_year(gender, year, name_data_dict, number=10):

    top_list = find_top_names_in_year(year, name_data_dict, number)
    title = f"Finding top {number} {gender} names for {year}:"
    print(title)
    pp.pprint(top_list)
    print()

    # CHARTS: call pie_chart here
    top_list_name = []
    top_list_data = []
    i = 0
    x = 0
    for _ in top_list:
        top_list_name.append(top_list[i][0])
        i += 1

    for _ in top_list:
        top_list_data.append(top_list[x][1])
        x += 1

    print(top_list_name)
    print(top_list_data)

    # chart name/ data/ labels
    pie_chart(f"Finding top {number} {gender} names for {year}:", top_list_data, top_list_name)

#### 7
def find_names_in_one_year(year, name_data_dict):
    names_in_one_decade = []
    for name7 in name_data_dict.keys():
        if len(name_data_dict[name7]) == 1 and year in name_data_dict[name7].keys():
            names_in_one_decade.append(name7)
        # else:
        #     pass

    names_in_one_decade.sort()

    bar_chart_x = []
    bar_chart_y = []
    i = 0
    for name in names_in_one_decade:
        if i < 10:
            bar_chart_x.append(name)
            i += 1
        else:
            break

    for name in bar_chart_x:
        bar_chart_y.append(name_data_dict[name][year])

    # print(bar_chart_x)
    # print(bar_chart_y)

    if str(name_data_dict) == 'f' or 'F':
        gender = "Female"
    else:
        gender = "Male"

    bar_chart(f"{gender} names popular in {year}", bar_chart_x, bar_chart_x, bar_chart_y, "", "Popularity", "b")

    return names_in_one_decade



#### 8
def find_frequency_for_all_years(name, years, name_data_dict):

    freq_data = []
    # for name8 in name_data_dict.keys():
    # for name8 in name:
    if name in name_data_dict.keys():
        # for year in name_data_dict[name8].keys():
        for year in years:
        # while years[-1] < 2020:
            # if years in name_data_dict[name].keys():  # error! # unhashable type: 'list' # need to change from list to Tuple!!
            # if name8 in name_data_dict.keys():
            if year in tuple(name_data_dict[name].keys()):
                freq_data.append(name_data_dict[name][year])
            else:
                freq_data.append(0)

    return freq_data


def show_frequency_for_all_years(names, years, name_data_dict):
    for name in names:
        # for year in years:
        freq_data = find_frequency_for_all_years(name, years, name_data_dict)
        print(f"{name:10s}", freq_data)

        # CHARTS:  Call the line_chart function here.
        line_chart(f"Frequency of {name} across all years", years, years, freq_data, "Years", "Frequency", chart_color='green')

############## Chart Functions

def bar_chart(title, x_axis_data, x_axis_labels, y_axis_data, x_axis_title, y_axis_title, chart_color='blue'):

    # plt.style.use('_mpl-gallery')
    # make data:
    x = x_axis_data
    y = y_axis_data
    plt.figure(1, [10, 5])  # to control the screen size of chart output
    # plot
    plt.bar(x, y, color=chart_color,
            width=0.8)  # default is 0.8
    # Add title and axis names
    plt.title(title)
    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)

    plt.show()

def line_chart(title, x_axis_data, x_axis_labels, y_axis_data, x_axis_title, y_axis_title, chart_color='green'):

    x_axis = x_axis_data
    y_axis = y_axis_data
    plt.figure(1, [9, 4])  # to control the screen size of chart output
    plt.xticks(x_axis_labels)

    plt.plot(x_axis, y_axis, color=chart_color)
    plt.title(title)
    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)

    plt.show()

def pie_chart(title, axis_data, axis_labels):

    y = np.array(axis_data)
    mylabels = axis_labels
    myexplode = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2]  # len of myexplode has to = to number of items

    plt.pie(y, labels=mylabels, autopct='%.1f%%', explode=myexplode)
    plt.title(title)

    plt.show()

def main():
    m_name_data_dict, f_name_data_dict = get_data()

    if DEBUG:
        print("########################  MALE NAMES AND DATA  ########################")
        print("\n\n\n\n")
        pp.pprint(m_name_data_dict)
        print("\n\n\n\n")
        print("######################## FEMALE NAMES AND DATA ########################")
        print("\n\n\n\n")
        pp.pprint(f_name_data_dict)
        print("\n\n\n\n")

    new_section(1)
    print("\n1 a Finding Male Names with 7 letters:")
    show_names_of_length("male", 7, m_name_data_dict)

    print("\n1 b Finding Female Names with 10 letters:")
    show_names_of_length("female", 10, f_name_data_dict)

    new_section(2)

    print("\n2 a Finding the longest male name(s) in the data:")
    show_longest_length("male", m_name_data_dict)

    print("\n2 b Finding the longest female name(s) in the data:")
    show_longest_length("female", f_name_data_dict)

    new_section(3)

    search_string = "cha"
    print(f"\n3 a Finding male names that contain {search_string}:")
    show_names_containing("male", search_string, m_name_data_dict)

    print(f"\n3 b Finding female names that contain {search_string}:")
    show_names_containing("female", search_string, f_name_data_dict)

    new_section(4)

    print("\n5 Names designated both male and female:")
    result = find_names_as_both(m_name_data_dict, f_name_data_dict)
    show_names_in_columns(result)

    new_section(5)
    print("\n5 a Finding male names increasing in popularity 2000-2020")
    show_incr_popular_names("male", [2000,2010,2020], m_name_data_dict)

    print("\n5 b Finding female names increasing in popularity 2000-2020")
    show_incr_popular_names("female", [2000,2010,2020], f_name_data_dict)

    new_section(6)


    print("\n6 a Top Male Names by year:")
    show_top_names_in_year("male", 1920, m_name_data_dict)
    show_top_names_in_year("male", 2020, m_name_data_dict)

    print("\n6 b Top Female Names by year:")
    show_top_names_in_year("female", 1900, f_name_data_dict, number=5)
    show_top_names_in_year("female", 2000, f_name_data_dict, number=5)

    new_section(7)

    print("\n7 a Showing all male names popular only in 2020:")
    names = find_names_in_one_year(2020, m_name_data_dict)
    show_names_in_columns(names, 8)

    print("\n7 b Showing all female names popular only in 1880:")
    names = find_names_in_one_year(1880, f_name_data_dict)
    show_names_in_columns(names)

    # CHARTS: Set up the data to call bar_chart here on the first ten names returned


    new_section(8)

    print("\n8 Names and Frequencies for Decades Between 1880 and 2020:")
    names = ["Taylor", "Elizabeth", "Catherine", "Mary"]
    years = [1880 + x * 10 for x in range(0, 14)]
    show_frequency_for_all_years(names, years, f_name_data_dict)


main()



