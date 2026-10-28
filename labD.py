from functions_file import convert_gpa

grades_list = [78, 91, 92, 89, 68, 97]

def average(grades):
    i = 0
    length = len(grades)
    add = 0
    add1 = 0
    
    while i < length:
        x = convert_gpa(grades[i])
        add += grades[i]
        add1 += x
        i+=1
        
    average = (add1/length)
    return average


print("Your average GPA (unweighted) is ", round(average(grades_list), 2) )
        
        
