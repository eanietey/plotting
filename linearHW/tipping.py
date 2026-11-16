import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data = np.loadtxt("tips.csv", delimiter=",", dtype=str)
# data should be an np array. Write a temporary line of code that
# prints the first row of the array to check that this worked.

x = data[1:, 0].astype(np.float32) # I did this one for you
y = data[1:, 1].astype(np.float32)

print("y=",y)
print("x=",x)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]
fig = plt.figure()
plt.scatter(x,y)
plt.plot(x,linear(x,slope,intercept),label='linear fit')
plt.xlabel('Bills')
plt.ylabel('Tips')
plt.show()

print_equation(slope,intercept,'$','$')
#The equation of the line is: y = 0.18221473222560391 $/$ + -0.2922674195507699 $

def percent_tip(x, y):
    return y/x * 100

PctTip = data[1:,6].astype(np.float32)
p = percent_tip(x, PctTip)

params, params_cov = scipy.optimize.curve_fit(linear, x, p)
slope = params[0]
intercept = params[1]
fig = plt.figure()
plt.scatter(x,p)
plt.plot(x,linear(x,slope,intercept),label='linear fit')
plt.xlabel('Bills')
plt.ylabel('Tip percentage')
plt.show()

print_equation(slope,intercept,'$','%')
#The equation of the line is: y = -4.218462100353182 %/$ + 196.25632393318284 %
