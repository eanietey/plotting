from advising_fxns import *

dsa = ["MATH-110", "MATH-120", "MATH-141",  "MATH-210", "MATH-133"]
current = input("Enter your current math course (eg, MATH-110): ")
current = current.upper() #converts to upper-case
print("Your next class is: ", next_class(dsa, current))
remaining = remaining_courses(dsa, current)
print("Your remaining math courses are:", remaining)
lower = remaining_lower(remaining)
print(f"You have {lower} remaining lower-level math courses")
upper = remaining_upper(remaining)
print(f"You have {upper} remaining upper-level math courses")


