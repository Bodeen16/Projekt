import numpy as np
import matplotlib.pyplot as plt 
import scipy as sp
from Uppgift3 import rk4, odefun
import robot 

b = 1
x0 = 0
y0 = 0
theta0 = 0

U0 = np.array([x0, y0, theta0])


t0 = 0 
tf = 30
a = 1


J0 = sp.special.j0(2*a)
g = lambda t: a * np.sin(3*J0*t)

vL = lambda t: np.cos(g(t))**2
vR = lambda t: np.sin(g(t))**2

f = lambda t, U: odefun(t, U, b, vL, vR)

N = 1
err = 1
while err >= 1e-07:
    t1, U1 = rk4(f, t0, tf, U0, N)
    N = N * 2
    t, U = rk4(f, t0, tf, U0, N)
    err = np.sqrt((U[0, -1] - U1[0,-1])**2 + (U[1, -1] - U1[1, -1])**2)

x = U[0, :]
y = U[1, :]
theta = U[2, :]

plt.figure()
robot.animate(x, y, theta)

plt.plot(x, y)
plt.axis("equal")
plt.grid(True)
plt.show()

#Uppgift a; 
for i in range(1, len(x)):
    if x[i-1] < 0 and x[i] >= 0:
        T = t[i - 1] + (0 - x[i - 1]) * (t[i]- t[i -1]) / (x[i] - x[i - 1])
        print("Omloppstid (s): ", T , "N =", N)
    
#Från kravet while err >= 1e-07 blir steglängden så liten för Rk4felet vilket följdaktligen säkrar minst 6 korrekta decimaler för omloppstiden T.
#När vi ökar antalet steg kan vi även konstatera att de första 6 decimalerna är oförändrade.


#Uppgift b;
     
   

