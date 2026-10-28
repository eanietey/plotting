#Test harness for game_fxns.py.

from game_fxns import *

good = "Correct"
incorrect = "Not correct; please revise"
 
if get_number()==100:
    print("get_length incomplete")
else:
    my_list = []
    [my_list.append(get_number()) for i in range(1500)]
    if max(my_list) == 15 and min(my_list) == 1:
        print("get_number: ",good)
    else:
        print("get_number: ",incorrect)

if check(1,2) == 100:
    print("check incomplete")
else:
    if check(5,1)==False and check(1,5)==False and check(1,1)==True:
        print("check: ",good)
    else:
        print("check: ",incorrect)
