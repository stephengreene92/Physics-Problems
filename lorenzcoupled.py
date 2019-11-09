#Stephen Greene
#Lorentz (couples differential) equations
#ODEs Runge-Kutta

import numpy as np
import matplotlib.pyplot as plt

#defining f(x,y)
def f(x,y):
    return 10.0*(y-x)
    
#defining g(x,y,z)
def g(x,y,z):
    return(28*x)-y-(x*z)
    
#defining h(x,y,z)
def h(x,y,z):
    return (x*y)-((8.0/3.0)*z)
    
#ask user for input
#array for time and x,y,z step size
n = int(input('Please enter value for n: '))
t = np.linspace(0,50,n)
x = np.empty(n)
y = np.empty(n)
z = np.empty(n)
#inital conditions
x[0] = 0.0
y[0] = 1.0
z[0] = 0.0
dt = 50.0/n

#Runge-Kutta 4 Method (coupled)
for i in range(n-1):
    
    kf1 = dt*f(x[i],y[i])
    kg1 = dt*g(x[i],y[i],z[i])
    kh1 = dt*h(x[i],y[i],z[i])
    
    kf2 = dt*f(x[i]+(kf1/2.0),y[i]+(kg1/2.0))
    kg2 = dt*g(x[i]+(kf1/2.0),y[i]+(kg1/2.0),z[i]+(kh1/2.0))
    kh2 = dt*h(x[i]+(kf1/2.0),y[i]+(kg1/2.0),z[i]+(kh1/2.0))
    
    kf3 = dt*f(x[i]+(kf2/2.0),y[i]+(kg2/2.0))
    kg3 = dt*g(x[i]+(kf2/2.0),y[i]+(kg2/2.0),z[i]+(kh2/2.0))
    kh3 = dt*h(x[i]+(kf2/2.0),y[i]+(kg2/2.0),z[i]+(kh2/2.0))
    
    kf4 = dt*f(x[i]+kf3,y[i]+kg3)
    kg4 = dt*g(x[i]+kf3,y[i]+kg3,z[i]+kh3)
    kh4 = dt*h(x[i]+kf3,y[i]+kg3,z[i]+kh3)
    
    x[i+1] = x[i]+(kf1/6.0)+(kf2/3.0)+(kf3/3.0)+(kf4/6.0)
    y[i+1] = y[i]+(kg1/6.0)+(kg2/3.0)+(kg3/3.0)+(kg4/6.0)
    z[i+1] = z[i]+(kh1/6.0)+(kh2/3.0)+(kh3/3.0)+(kh4/6.0)
    
#plotting
plt.subplot(221)
plt.plot(t,y)
plt.title('Lorentz (coupled differential) equations')
plt.xlabel('Time (s)')
plt.ylabel('Y-Data')
plt.grid()
plt.legend()
plt.show()

plt.subplot(222)
plt.plot(x,z)
plt.title('Lorentz (coupled differential) equations')
plt.xlabel('Time (s)')
plt.ylabel('X-Data')
plt.grid()
plt.legend()
plt.show()


    
    