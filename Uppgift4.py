import numpy as np
import matplotlib.pyplot as plt 
from Uppgift3 import rk4, odefun
import robot 

b = 1
x0 = 0
y0 = 0
theta0 = 0

U0 = np.array([x0, y0, theta0])

t0 = 0
tf = 10



#Uppgift a; 

vL = lambda t: 3*t + 5
vR = lambda t: 3*t + 1

f = lambda t, U: odefun(t, U, b, vL, vR)

N = 100
err = 1
while err >= 1e-05:
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

x_tf = U[0, -1]
y_tf = U[1, -1]
print("Slutposition fall a:", x_tf, y_tf, "N =", N, "fel =", err)

#Åker med nosen framåt 
#N = 400



#Uppgift b; 

vL = lambda t: 3*t + 1
vR = lambda t: t + 6

f = lambda t, U: odefun(t, U, b, vL, vR)

N = 100
err = 1
while err >= 1e-05:
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

x_tf = U[0, -1]
y_tf = U[1, -1]
print("Slutposition fall b:", x_tf, y_tf, "N =", N, "fel =", err)

#Åker med nosen framåt 
#N = 1600


#Uppgift c; 

k = 2.7

vL = lambda t: k * (np.cos(k*t) - 0.75)
vR = lambda t: k * (np.cos(k*t) + 0.5)

f = lambda t, U: odefun(t, U, b, vL, vR)

N = 100
err = 1
while err >= 1e-05:
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

x_tf = U[0, -1]
y_tf = U[1, -1]
print("Slutposition fall c:", x_tf, y_tf, "N =", N, "fel =", err)

#Roterar / backar bitvis 
#N = 400


#Uppgift d; 

k = 0.75

vL = lambda t: k * (0.5 - 5*np.cos(5*k*t))
vR = lambda t: k * (1.5 + 5*np.cos(5*k*t))

f = lambda t, U: odefun(t, U, b, vL, vR)

N = 100
err = 1
while err >= 1e-05:
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

x_tf = U[0, -1]
y_tf = U[1, -1]
print("Slutposition fall d:", x_tf, y_tf, "N =", N, "fel =", err)

#Åker med nosen framåt
#N = 400


#Vi kan utifrån animeringarna konstatera att roboten åker med nosen framåt i fall a, b och d, d.v.s. i 3 fall av 4.
#Själva felet i slutpositionen fås genom att dubbla N och beräkna det euklidiska avståndet mellan lösningarna för N och 2N, tills skillnaden är under 1e-05.



