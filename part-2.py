#Spencer Meren
#December 17, 2023
#CST-305

#Packages used: scipy, numpy, matplotlib, math
import scipy.integrate as spint
import numpy as np
import matplotlib.pyplot as plt

#import math as m

#Model
a = 0
b = 30
N = 30
stepSize = (b-a)/N

eq = "r(t)"

t = np.linspace(a,b,31)
#x = range(0,31,1) #all integers 0-30
rt = [0,0.934,0.842,0.929,1.045,1.230,1.058,0.802,1.041,1.085,1.061,0.973,0.952,1.092,1.156,1.131,1.121,1.351,1.185,0.940,0.918,0.881,0.976,1.070,1.194,1.123,1.222,0.858,0.942,1.040,1.027]
#r = lambda t : rt[t]
#y = r(x)

#Calculate total data downloaded
sum = 0
for i in range(0,31):
    sum += (rt[i] * 60) #Conversion: Mb/second * 1 minute * 60 seconds/1 minute

print("Total data downloaded (according to cumulative download rates): {} megabytes".format(sum))

#   Plot models

#Left sum
x_left = np.arange(a,b,(b-a)/N)

#Right sum
x_right = x_left + stepSize

plt.plot(t,rt)
plt.title("Right Riemann Sum of `{}` (N = {})".format(eq, N))
plt.xlabel('t - Minutes elapsed')
plt.ylabel('r(t) - Mb/s')
for i in range(0,31):
    plt.bar(i-1,rt[i],width=stepSize,alpha=0.2,align='edge',edgecolor='b',color='b')

plt.show()