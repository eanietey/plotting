''' Work with a partner.
Don't run this file.
Save it and run the test file (test_index.py) after you finish each function.
'''
 
def get_first(data):
    return data[0]

def get_second(data):
     return data[1]

def start_at_0(): #Create a list that looks like this: 0,1,2,3,4
    return range(0, 5)  #wrong - fix this (use the range command)

def start_at_1():  #Create a list that looks like this: 1,2,3,4
    return range(1, 5)  #wrong - fix this (use the range command)

def start_at_2():  #Create a list that looks like this:  2,3,4,5
    return range(2, 6)  #wrong - fix this (use the range command)

def add_three(data):
    calc = data[0] + data[1] + data[2]
    return calc

def first_last(data):
    return data[0] + data[-1]

def two_list(data1, data2):  #input: two lists, data1 and data2
    #add the first element of data1 to the first element of data2
    return data1[0] + data2[0]

def max_list(data1, data2):
#if the maximum value of the first list is higher than the max value of the 2nd,
        #return the first list. Otherwise, return the second list.
        #if they have the same max value, return False.
    if max(data1) > max(data2):
        return data1
    else:
        return data2
        
    if max(data1) == max(data2):
        return False
    

def last_is_higher(data):
#if the last value in a list is higher than the first value, return True.
        # if it is equal to the first value, return the list.
        #if it is lower than the first value, return False.

    if data[-1] > data[0]:
        return True
    elif data[-1] == data[0]:
        return data
    elif data[-1] < data[0]
        return False
    


