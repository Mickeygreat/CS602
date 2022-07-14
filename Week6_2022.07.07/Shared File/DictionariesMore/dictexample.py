


import pprint as pp
# calculate the total enrollment of each class

def get_total_enrollment(data):

    total_enrollment = {}

    for semester in data:
        s_dict = data[semester]
        print("s_dict=", s_dict)
        for course in s_dict:
            print("course=", course)
            if course in total_enrollment.keys():
                total_enrollment[course] += s_dict[course]
            else:
                total_enrollment[course] = s_dict[course]
    
    return total_enrollment         
    
def get_enrollment(semester):
    if semester == "F19":
        enrollment = {'CS180': 10, 'CS150':15}
    elif semester == "S19":
        enrollment = {'CS180': 20, 'CS150':30}
    elif semester == "F20":
        enrollment = {'CS180': 25, 'CS150':20}
    elif semester == "S20":
        enrollment = {'CS180': 30, 'CS150':50}
    else:
        enrollment = {}
    return enrollment

def main():
    print("Calculate the sum of enrollments for semesters F19 S19 F20 S20")
    semesters = input("Enter semesters separated by a space: ").upper()
    semester_list = semesters.split()
    
    #create a dictionary of enrollments for courses by semester
    #data should look like this when we're done:
    #  {'S19': {'CS180': 20, 'CS150':30}, 
    #   'F20': {'CS180': 25, 'CS150':20}, 
    #   'S20': {'CS180': 30, 'CS150':50}}

    enrollment_dict = {}  
    for s in semester_list:
        # get the enrollment for one semester
        semester_enrollment_dict = get_enrollment(s)
        
        # add that dictionary to the master enrollment dictionary
        enrollment_dict[s] = semester_enrollment_dict
    pp.pprint(enrollment_dict)
    # calculate total enrollment of each class for all semesters chosen
    total_enrollment_by_course = get_total_enrollment(enrollment_dict)
    
    print("total_enrollment_by_course=", total_enrollment_by_course, "\n")
    print("Selected semesters:")
    for s in enrollment_dict:
        print(f"Semester: {s:3s}")
        semester_dict = enrollment_dict[s]
        for course in semester_dict:
            print(f"     {course:7s} {semester_dict[course]:3d}")
    
    print("Total Enrollment by Course:")
    for course in total_enrollment_by_course:
        print (f"{course:>10s} {total_enrollment_by_course[course]:3d}")

    
    
main()
