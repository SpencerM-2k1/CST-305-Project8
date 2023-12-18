#Spencer Meren
#December 17, 2023
#CST-305

#Packages used: scipy, numpy, matplotlib, math
import scipy.integrate as spint
import numpy as np
import matplotlib.pyplot as plt

#import math as m

#Model
a = -np.pi
b = np.pi
N = 300 #N = 300 used to illustrate a highly granular Riemann sum
stepSize = (b-a)/N

eq = "f(x) = 3x + 2x^2"

x = np.linspace(a, b, 100)
f = lambda t : 3*t + 2*(t**2)
y = f(x)

#   Plot models

#Left sum
x_left = np.arange(a,b,(b-a)/N)

#Right sum
x_right = x_left + stepSize

#plt.subplot(1,3,3)
plt.plot(x,y)
plt.title("Right Riemann Sum of `{}` (N = {})".format(eq, N))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.bar(x_left,f(x_right),width=stepSize,alpha=0.2,align='edge',edgecolor='b')
#plt.plot(x_right,f(x_right),'b.',markersize=10)

plt.show()