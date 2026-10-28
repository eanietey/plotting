#main section of code - test harness for fxns.py
from functions  import *
from math import factorial
good = "Correct"
incorrect = "Not correct; please revise"
data1 = [0,1,2,3]
data2 = [-1,1,-2,2]
data3 = [2.0,4.0]
if get_length(data1)==100:
    print("get_length incomplete")
else:
    if get_length(data1)==4:
        print("get_length, 4 elements: ",good)
    else:
        print("get_length, 4 elements: ",incorrect)
    if get_length(data3)==2:
        print("get_length, 2 elements: ",good)
    else:
        print("get_length, 2 elements: ",incorrect)
if both_true(True,True)==100:
    print("both_true incomplete")
else:
    if both_true(True,True):
        print("both_true(True,True)",good)
    else:
        print("both_true(True,True)",incorrect)
    if both_true(True,False)==False:
        print("both_true(True,False)",good)
    else:
        print("both_true(False,False)",incorrect)
    if both_true(False,False)==False:
        print("both_true(False,False)",good)
    else:
        print("both_true(False,False)",incorrect)

if is_positive(4)  and  is_positive(-4)==False and is_positive(0)==False:
    print("is_positive: ",good)
else:
    print("is_positive: ",incorrect)

    
if mean(3,4,5)==100:
    print("mean(data_list) incomplete")
else:       
    if mean(1,2,3)==2:
        print("mean(1,2,3): ",good)
    else:
        print("mean(1,2,3): ",incorrect)
    if mean(0,1,14)== 5 :
        print("mean(0,1,14): ",good)
    else:
        print("mean(0,1,14): ",incorrect)
 
if interval(data1)==100:
    print("mean(data_list) incomplete")
else:       
    if interval(data1)==3 and interval(data3)==2.0:
        print("interval: ",good)
    else:
        print("interval: ",incorrect)
    print("This should print your error message:")
    interval(["hi","hi"])

if n_q_factorial(2,3)==100:
    print("mean(data_list) incomplete")
else:       
    if n_q_factorial(2,3)==12 and n_q_factorial(4,1)==factorial(4):
        print("n_q_factorial(n, q): ",good)
    else:
        print("n_q_factorial(n, q): ",incorrect)
    print("This should print your error message:")
    n_q_factorial("hi", "hi")
      
if is_higher(2,data1)==100:
    print("is_higher incomplete")
else:       
    if is_higher(2,data1)==False and is_higher(12,data1)==True: 
        print("is_higher: ",good)
    else:
        print("is_higher: ",incorrect)
    print("This should print your error message:")
    is_higher("hi", data1)


          

