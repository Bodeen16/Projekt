import numpy as np
import matplotlib.pyplot as plt 
from Uppgift3 import rk4, odefun
from Uppgift2 import robotcircle
import robot 

#Uppgift a; 

wL = 4
wR = 2
b = 1
x0 = 0
y0 = 0
theta0 = 0

U0 = np.array([x0, y0, theta0])

xbar, ybar, R, T_lap = robotcircle(b, wL, wR, x0, y0, theta0)

t0 = 0
tf = 10
N = 100

vL = lambda t: 3*t + 5
vR = lambda t: 3*t + 1

f = lambda t, U: odefun(t, U, b, vL, vR)

t, U = rk4(f, t0, tf, U0, N)

x = U[0, :]
y = U[1, :]
theta = U[2, :]

plt.figure()
robot.animate(x, y, theta)

plt.plot(x, y)
plt.axis("equal")
plt.grid(True)
plt.show()

x_tf = U[0, -1]
y_tf = U[1, -1]
print("Slutposition fall a:", x_tf, y_tf)

#Åker med nosen framåt 



#Uppgift b; 

vL = lambda t: 3*t + 1
vR = lambda t: t + 6

f = lambda t, U: odefun(t, U, b, vL, vR)

t, U = rk4(f, t0, tf, U0, N)

x = U[0, :]
y = U[1, :]
theta = U[2, :]

plt.figure()
robot.animate(x, y, theta)

plt.plot(x, y)
plt.axis("equal")
plt.grid(True)
plt.show()

x_tf = U[0, -1]
y_tf = U[1, -1]
print("Slutposition fall b:", x_tf, y_tf)

#Åker med nosen framåt 


#Uppgift c; 

k = 2.7

vL = lambda t: k * (np.cos(k*t) - 0.75)
vR = lambda t: k * (np.cos(k*t) + 0.5)

f = lambda t, U: odefun(t, U, b, vL, vR)

t, U = rk4(f, t0, tf, U0, N)

x = U[0, :]
y = U[1, :]
theta = U[2, :]

plt.figure()
robot.animate(x, y, theta)

plt.plot(x, y)
plt.axis("equal")
plt.grid(True)
plt.show()

x_tf = U[0, -1]
y_tf = U[1, -1]
print("Slutposition fall c:", x_tf, y_tf)

#Roterar 


#Uppgift d; 

k = 0.75

vL = lambda t: k * (0.5 - 5*np.cos(5*k*t))
vR = lambda t: k * (1.5 + 5*np.cos(5*k*t))

f = lambda t, U: odefun(t, U, b, vL, vR)

t, U = rk4(f, t0, tf, U0, N)

x = U[0, :]
y = U[1, :]
theta = U[2, :]

plt.figure()
robot.animate(x, y, theta)

plt.plot(x, y)
plt.axis("equal")
plt.grid(True)
plt.show()

x_tf = U[0, -1]
y_tf = U[1, -1]
print("Slutposition fall d:", x_tf, y_tf)

#Åker med nosen framåt

#Vi kan utifrån animeringarna konstatera att roboten åker med nosen framåt i fall a, b och d, d.v.s. i 3 fall av 4.



