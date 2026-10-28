from advising_fxns import *
#Test harness for advising_fxns

engr_math = ["CS-101","ENG-101", "MATH-134","MATH-333", "MATH-431"]
good = " Correct"
incorrect = " Not correct; please revise"

if first_digit(engr_math[0])==100:
    print("first_digit incomplete")
else:
    c1 = first_digit(engr_math[0])
    c2 = first_digit(engr_math[1])
    c3 = first_digit(engr_math[-1])
    c4 = first_digit(engr_math[3])
    if c1==1 and c2==1 and c3==4 and c4==3:
        print("first_digit",good)
    else:
        print("incorrect result:")
        print("first_digit of CS-101: ", c1)
        print("first_digit of ENG-101: ", c2)
        print("first_digit of MATH-431: ", c3)
        print("first_digit of MATH-333: ", c4)

if is_upper(engr_math[0])==100:
    print("is_upper incomplete")
else:
    if is_upper(engr_math[0])==False and is_upper(engr_math[-1]):
        print("is_upper",good)
    else:
        print("is_upper",incorrect)

slice = ["ENG-101", "MATH-134","MATH-333", "MATH-431"]
if remaining_lower(slice)==100:
    print("remaining_lower incomplete")
else:
    if remaining_lower(slice)==2 and remaining_lower(["MATH-333", "MATH-431"])==0:
        print("remaining_lower",good)
    else:
        print("remaining_lower",incorrect)

if next_class(engr_math,engr_math[0])==100:
    print("next_class incomplete")
else:
    if next_class(engr_math,engr_math[0])=="ENG-101":
        print("next_class",good)
    else:
        print("next_class",incorrect)

remaining = remaining_courses(engr_math, "ENG-101")
if remaining==100:
    print("remaining_courses incomplete")
else:
    if remaining ==  ["MATH-134","MATH-333", "MATH-431"]:
        print("remaining",good)
    else:
        print("remaining",incorrect)

if remaining_upper(slice)==4:
    print("remaining_upper incomplete")
else:
    if remaining_upper(slice)==2 and remaining_upper(["MATH-431"])==1:
        print("remaining_upper",good)
    else:
        print("remaining_upper",incorrect)
