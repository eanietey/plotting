def grade(x):
    
    if grade >= 93:
        gpa = 4.0 #A
    elif grade >= 90:
        gpa = 3.7 #A-
    elif grade >= 87:
        gpa = 3.3 #B+
    elif grade >= 83:
        gpa = 3.0 #B
    elif grade >= 80:
        gpa = 2.7 #B-
    elif grade >= 77:
        gpa = 2.3 #C+
    elif grade >= 73:
        gpa = 2.0 #C
    elif grade >= 70:
        gpa = 1.7 #C-
    elif grade >= 60:
        gpa = 1.5 #D
    elif grade < 60:
        gpa = 0 #F
    return gpa
    
def convert_to_gpa(arr):
    return overall_gpa(arr[0], arr[1], arr[2])
    return [overall_gpa(arr[0]),

def overall_gpa(arr):
    ave = (arr[1]+arr[0]+arr[2])/3
    print(ave)


grades = [100, 100, 100]
x = overall_gpa(grades)
