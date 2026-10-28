#main section of code - test harness for index_fxns.py
#to run this code:  python3 test_index.py
from index_fxns  import *

good = "Correct"
incorrect = "Not correct; please revise"
data1 = [0,1,2,3]
data2 = [-1,5,-2,2]
data3 = [2.0,4.0]
data4 = [0,1,1,3,-1]
data5= [0,1,0]
#Test selection of first element in a list 
if get_first(data2)==100:
    print("get_first incomplete")
else:
    if get_first(data2)==-1:
        print("get_first: ",good)
    elif get_first(data2)==5:
        print("get_first: Not correct. Remember that the first element has index 0.")
    else:
        print("get_first: ",incorrect)
     
if get_second(data2)==100:
    print("get_second incomplete")
else:
    if get_second(data2)==5:
        print("get_second: ",good)
    elif get_second(data2)==-2:
        print("get_second: Not correct. Remember that the second element has index 1.")
    else:
        print("get_first: ",incorrect)

# return a range that is 0,1,2,3,4
x = start_at_0() 
if x[-1]==100: #bad: return range(101)
    print("start_at_0 incomplete")
else:       
    if x[0]==0 and x[1]==1 and x[-1]==4 and len(x)==5:
        print("start_at_0: ",good)
    else:
        print("start_at_0: ",incorrect)
        
# return a range that is 1,2,3,4
x = start_at_1() 
if x[-1]==100: #bad: return range(101)
    print("start_at_1 incomplete")
else:       
    if x[0]==1 and x[1]==2 and x[-1]==4 and len(x)==4:
        print("start_at_1: ",good)
    else:
        print("start_at_1: ",incorrect)
# return a range that is 2,3,4,5
x = start_at_2() 
if x[-1]==100: #bad: return range(101)
    print("start_at_2 incomplete")
else:       
    if x[0]==2 and x[1]==3 and x[-1]==5:
        print("start_at_2: ",good)
    else:
        print("start_at_2: ",incorrect)

#add first 3 elements
if add_three(data2)==100:
    print("add_three incomplete")
else:       
    if add_three(data2)==2:
        print("add_three: ",good)
    else:
        print("add_three: ",incorrect)

 #add first and last element
if first_last(data1)==100:
    print("first_last incomplete")
else:       
    if first_last(data2)==1 and first_last(data3)==6.0:
        print("first_last: ",good)
    else:
        print("first_last: ",incorrect)
 

#add first element of two lists
if two_list(data1, data2)==100:
    print("two_list incomplete")
else:       
    if two_list(data1, data2)== -1 and two_list(data3, data2)== 1.0 :
        print("two_list: ",good)
    else:
        print("two_list: ",incorrect)
 
#if the maximum value of the first list is higher than the max value of the 2nd,
#return the first list. Otherwise, return the second list.
#if they have the same max value, return False. 
if max_list(data1, data2)==100:
    print("two_list incomplete")
else:       
    if max_list(data1, data2)== data2 and max_list(data2, data3)== data2 and max_list(data1,data4)==False:
        print("max_list: ",good)
    else:
        print("max_list: ",incorrect)

#if the last value in a list is higher than the first value, return True.
# if it is equal to the first value, return the list.
#if it is lower than the first value, return False.
if last_is_higher(data1)==100:
    print("last_is_higher incomplete")
else:        
    if last_is_higher(data4) == False and last_is_higher(data1) == True and last_is_higher(data5) == data5:
        print("last_is_higher: ",good)
    else:
        print("last_is_higher: ",incorrect)



          

