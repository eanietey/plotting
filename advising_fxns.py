#Get first digit of course number.  Returns 1, 2, 3, or 4.
def first_digit(course_name):
    #example: MATH-140 should return 1.
    #         ENG-233 should return 2. 
    #use find() to get the index of the first digit.
    #I suggest locating the hyphen.
    diff = course_name.find("-")
    digit = course_name[diff+1]
    return int(digit) 

#Return True if upper level class. Otherwise return False.
def is_upper(course_name):
    first = first_digit(course_name)

    if first == 1 or first == 2:
        return False
    else:
        return True
    return 100  #if first digit is 1 or 2, return False. Otherwise, return True.

# return the next course in the list
def next_class(all_courses, current_course):
    #use .index to extract the location of the current_course in all_courses.
    i = all_courses.index(current_course)
    return all_courses[i+1]

#Given current class, return slice of all remaining classes.  
def remaining_courses(all_courses, current_course):
    #determine the index of the current_course in all_courses (use .index)
    x=all_courses.index(current_course)
    result = all_courses[x+1:]
    #Using the index you just determined, slice all_courses to just be the remaining ones
    return result

    
# Use a for-loop to count the remaining upper-level courses
def remaining_upper(remaining_courses):
    count = 0
    for course in remaining_courses:
        if is_upper(course) is True:
            count = count + 1 #this isn't right - you don't want to do this for all of them
    return count

# Use a for-loop to count the remaining lower level courses
def remaining_lower(remaining_courses):
    count = 0
    for course in remaining_courses:
         if is_upper(course) is False:
            count = count + 1
    return count
