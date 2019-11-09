#Stephen Greene
#Pendulum model with dampening
#Euler Cromer Method

import numpy as np
import matplotlib.pyplot as plt

n = 1000
dt = 0.01
z = np.empty(n)
z_ec = np.empty(n)
theta_ec = np.empty(n) #Euler Cromer method
t = np.linspace(0,100,n) # time 0-100 and n as defined
z[0] = 1
theta_ec[0] = 0
z_ec[0] = 1
l = 1
b_m = -0.01

#Euler Cromer
for j in range (n-1):
    z_ec[j+1] = z_ec[j]+((-9.8/1)*(np.sin(theta_ec[j])-(z_ec[j]*b_m))*dt)
    theta_ec[j+1] = theta_ec[j]+(z_ec[j+1]*dt)
    t[j+1] = t[j]+dt
    
#plotting
plt.subplot(221)
plt.title('Euler Cromer Method')
plt.plot(t,theta_ec, label = 'Theta')
plt.plot(t,z_ec, label = 'dTheta/dt')
plt.xlabel('Time(s)')
plt.axis()
plt.legend()
plt.grid()
plt.show()

plt.subplot(222)
plt.title('Euler Cromer Method')
plt.plot(theta_ec, z_ec, label = 'dTheta/dt')
plt.xlabel('Angle')
plt.ylabel('Angular Velocity')
plt.axis()
plt.legend()
plt.grid()
plt.show()
