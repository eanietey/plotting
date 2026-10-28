def convert_gpa(grade):
    if grade >= 93: gpa = 4.0 #A
    elif grade >= 90: gpa = 3.7 #A-
    elif grade >= 87: gpa = 3.3 #B+
    elif grade >= 83: gpa = 3.0 #B
    elif grade >= 80: gpa = 2.7 #B-
    elif grade >= 77: gpa = 2.3 #C+
    elif grade >= 73: gpa = 2.0 #C
    elif grade >= 70: gpa = 1.7 #C-
    elif grade >= 67: gpa = 1.3 #D+
    elif grade >= 63: gpa = 1.0
    else: gpa = 0
    return gpa
        
