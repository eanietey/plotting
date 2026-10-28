'''  
These functions all take a list of numbers.
Flesh out the function definitions according to the instructions below.
To test if your definitions are correct, put this in your python scripts
folder along with the test harness provided on Canvas. Run:
python test_harness.py

Talk with a partner as you go along.
You can use your partner's code and also ask them for help.
'''
import math

#Hint: You can use the following functions to do this lab:
#math.factorial()
#len()
#min()
#max()



def get_length(data_list):
    return len(data_list)  #fix this so that it calculates how many elements are in the list

def both_true(n, m): #assume n and m are boolean variables (True or False)
    if n and m is True:
        return True
    else:
        return False
    #fix this so that it returns True if both inputs are True, False otherwise

def is_positive(n):
    if n>0:
        return True
    else:
        return False

    #fix this so that it returns True if the number is positive, False otherwise

#The following functions need to have try/except in them, in case the input is not numerical.
 
def mean(x,y,z):
    try:
        return (x+y+z)/3 #fix this to be the average of the 3 numbers (x,y and z)
    except:
        return "Input must be numerical" #fix this so that is prints "Input must be numerical"

def interval(data_list): #add a try/except block to this in case the input is not numerical.
    #fix this to be the max of the list minus the min of the list.
    try:
        x = max(data_list) - min(data_list)
        return x
    except:
        return "Input is not numerical"

def n_q_factorial(n, q): #add a try/except block to this in case the input is not numerical.
      #fix this to be n! times q!
    try:
      return math.factorial(n) * math.factorial(q)
    except:
        return "Input not numerical"
            


def is_higher(n, data_list):#add a try/except block to this in case the input is not numerical.
    #fix this so that it returns True if the n is higher than the maximum value of data_list
    try:
        maxi = max(data_list)

        if n > maxi:
            return True
        else:
            return False
    except:
        return  "Input is not numerical"
