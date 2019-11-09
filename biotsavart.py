#Stephen Greene
#Biot-Savart Law
#Numerical Integration 

import numpy as np
import matplotlib.pyplot as plt

def f(x,z): #the function in the integral of Biot Savart
    return x/((x**2+z**2)**1.5)
    
L = float(input('Enter wire length in meters: ')) #length of wire

#distance in meters from the wire you would like to measure over
X = float(input('Enter the distance from the wire you would like in meters: '))

#current
I = float(input('Enter the value of current in the wire in amps:'))

#for every meter we will take 1000 readings
n = X*100
#t is an integer value of how many readings we will take
t = int(n)
#how much to move x on by between readings
dx = X/t
start = -L/2
end = L/2
steps = 100
#step size for simpsons method
h = (end-start)/steps

#array to store B(x) values (we are excluding 0)
y = np.empty(t-1)
#smallest step size
x1 = dx
#creating an array of values for x we want to use
xa = np.linspace(x1,X,t-1)

#loop to calculate B(x) at all values for x
for k in range(t-1):
    #setting z to the value of -L/2
    z = start
    
    #Simpsons Method
    ans = f(xa[k],start)+f(xa[k],end)
    for i in range(steps-1):
        
        if(i%2==0):
          z = z+h
          ans = ans + 4*f(xa[k],z)
          
        else:
            z = z+h
            ans = ans +2*f(xa[k],z)
            
    ans = ans *(h/3)*((1.256*10**(-6))*I/4*np.pi)
    #saving the value of B(x) in the array
    y[k] = ans
    #moving k(x value) along by dx
    k = k+dx
          
plt.plot(xa,y, 'cadetblue')
plt.title('Magnitude of Magnetic Field over a Range of Distances')
plt.xlabel('Distance from wire(meters)')
plt.ylabel('Magnetic Field')
plt.show()                    
                   
