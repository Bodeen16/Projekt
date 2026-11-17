import numpy as np 
import matplotlib.pyplot as plt
from Uppgift2 import robotcircle
import robot

"""
Lösningen för uppgift a finns på separat papper. 
"""

#Uppgift b;

def odefun(t, U, b, vL, vR):
    theta = U[2]

    dxdt = (vR(t) + vL(t))/2 * np.cos(theta)
    dydt = (vR(t) + vL(t))/2 * np.sin(theta)
    dthetadt = (vR(t) - vL(t))/b

    return np.array([dxdt, dydt, dthetadt])


#Uppgift c; 


def forward_euler(f, t0, tf, U0, N): 

    h = (tf - t0)/N 

    t = np.zeros(N + 1)
    U = np.zeros((3, N + 1))

    t[0] = t0
    U[:, 0] = U0

    for j in range(N):
        t[j + 1] = t[j] + h
        U[:, j + 1] = U[:, j] + h * f(t[j], U[:, j])
   
    return t, U


wL = 4
wR = 2
b = 1
x0 = 0
y0 = 0
theta0 = 0

U0 = np.array([x0, y0, theta0])

xbar, ybar, R, T_lap = robotcircle(b, wL, wR, x0, y0, theta0)

t0 = 0
tf = T_lap
N = 100

vL = lambda t: wL
vR = lambda t: wR

f = lambda t, U: odefun(t, U, b, vL, vR)

t, U = forward_euler(f, t0, tf, U0, N)

x = U[0, :]
y = U[1, :]
theta = U[2, :]

plt.figure()
robot.animate(x, y, theta)

plt.plot(x, y)
plt.axis("equal")
plt.grid(True)
plt.show()
