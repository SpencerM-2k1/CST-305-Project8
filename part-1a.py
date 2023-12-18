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
N = 4
stepSize = (b-a)/N

eq = "f(x) = sin(x) + 1"

x = np.linspace(a, b, 100)
f = lambda t : np.sin(t) + 1
y = f(x)

#   Plot models

#Left sum
x_left = np.arange(a,b,(b-a)/N)

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.plot(x,y)
plt.title("Left Riemann Sum of `{}` (N = {})".format(eq, N))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.bar(x_left,f(x_left),width=stepSize,alpha=0.2,align='edge',edgecolor='b',color='b')
plt.plot(x_left,f(x_left),'b.',markersize=10)

#Middle sum
x_mid = x_left + stepSize/2

plt.subplot(1,3,2)
plt.plot(x,y)
plt.title("Middle Riemann Sum of `{}` (N = {})".format(eq, N))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.bar(x_left,f(x_mid),width=stepSize,alpha=0.2,align='edge',edgecolor='b',color='b')
plt.plot(x_mid,f(x_mid),'b.',markersize=10)

#Right sum
x_right = x_left + stepSize

plt.subplot(1,3,3)
plt.plot(x,y)
plt.title("Right Riemann Sum of `{}` (N = {})".format(eq, N))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.bar(x_left,f(x_right),width=stepSize,alpha=0.2,align='edge',edgecolor='b',color='b')
plt.plot(x_right,f(x_right),'b.',markersize=10)

plt.show()