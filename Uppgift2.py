import numpy as np

"""
Lösningen för uppgift a och b finns på separat papper. 
"""

#Uppgift c;

def robotcircle(b, wL, wR, x0, y0, theta0):
    w = (wR + wL)/2
    Dw = (wR - wL)/b

    x_m = x0 - (w/Dw) * np.sin(theta0)
    y_m = y0 + (w/Dw) * np.cos(theta0)

    R = np.abs(w/Dw)

    T_lap = 2*np.pi/np.abs(Dw)

    return x_m, y_m, R, T_lap



