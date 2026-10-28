from advising_fxns import *

engr_math = ["MATH-110", "MATH-120", "MATH-210 and MATH-133",  "MATH-134","MATH-233", "MATH-331"]
current = input("Enter your current math course (eg, MATH-110): ")
current = current.upper() #converts to upper-case
print("Your next class is: ", next_class(engr_math, current))
remaining = remaining_courses(engr_math, current)
print("Your remaining math courses are:", remaining)
lower = remaining_lower(remaining)
print(f"You have {lower} remaining lower-level math courses")
upper = remaining_upper(remaining)
print(f"You have {upper} remaining upper-level math courses")

