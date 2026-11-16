import numpy as np 
import matplotlib.pyplot as plt

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

#robotcircle från 2c
def robotcircle(b, wL, wR, x0, y0, theta0):
    w = (wR + wL)/2
    Dw = (wR - wL)/b

    x_m = x0 - (w/Dw) * np.sin(theta0)
    y_m = y0 + (w/Dw) * np.cos(theta0)

    R = np.abs(w/Dw)

    T_lap = 2*np.pi/np.abs(Dw)

    return x_m, y_m, R, T_lap


def forward_euler(f, t0, tf, U0, N): 

    return t, U

