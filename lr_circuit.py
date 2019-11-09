#Stephen Greene
#LR Circuit
#ODEs Runge-Kutta

import numpy as np
import matplotlib.pyplot as plt
#for square wave
from scipy import signal


#defining dI/dt
def f(T,I):
    return 1.0/0.9*(V(T)-8.0*I)
    
#defining square wave
def V(T):
    return signal.square(np.pi*2.0*T)
    
#ask user for input
#array for time and current, step size
n = int(input('Please enter value for n:  '))
T = np.linspace(0,4,n)
I = np.empty(n)
h = 4.0/n
I[0] = 1 #starting current

#Runge-Kutta 4 Method
for i in range(n-1):
    r1 = h*f(T[i],I[i])
    r2 = h*f(T[i]+(h/2.0),I[i]+(r1/2.0))
    r3 = h*f(T[i]+(h/2.0),I[i]+(r2/2.0))
    r4 = h*f(T[i]+h,I[i]+r3)
    
    I[i+1] = I[i]+(r1/6.0)+(r2/3.0)+(r3/3.0)+(r4/6.0)

#plotting
plt.plot(T,I, label ='I(t)')
plt.plot(T,V(T), label ='V(t)')
plt.plot(T,f(T,I), label = 'dI(T)/dT(T)')
plt.title('LR Circuit')
plt.xlabel('Time (s)')
plt.ylabel('I (T)')
plt.grid()
plt.legend()
plt.show()