import numpy as np
import matplotlib.pyplot as plt 
import scipy as sp
from Uppgift3 import rk4, odefun
import robot 



def compute_area(N, x, y, f, h):
    n=1
    A=0
    while n < N:
        A = A + (x[n]*f(t[n], U[:, n])[1] - y[n]*f(t[n], U[:,n])[0])*h    
        n = n +1

    A = A + (x[0] * f(t[0], U[:, 0])[1] - y[0] * f(t[0], U[:, 0])[0]) * h / 2 \
        + (x[N] * f(t[N], U[:, N])[1] - y[N] * f(t[N], U[:, N])[0]) * h / 2
    return A

def Der_compute_area(N, x, y, f, h):
    n=1
    dA=0
    while n < N:
        dA = dA + (x[n]*acc(t[n], U[:, n])[1] - y[n]*acc(t[n], U[:,n])[0])*h    
        n = n +1

    dA = dA + (x[0] * acc(t[0], U[:, 0])[1] - y[0] * acc(t[0], U[:, 0])[0]) * h / 2 \
        + (x[N] * acc(t[N], U[:, N])[1] - y[N] * acc(t[N], U[:, N])[0]) * h / 2
    return dA
        
     

def acceleration(t, U, b, vL, vR, aL, aR, n):
    theta = U[2]

    ax = (aL(t) + aR(t))/2 * np.sin(theta) +(vR(t)+vL(t))/2 * np.cos(theta)*f(t, U)[2]
    ay = (aL(t) + aR(t))/2 * np.cos(theta) +(vR(t)+vL(t))/2 *-np.sin(theta)*f(t, U)[2]

    return np.array([ax, ay])


g = lambda t: a * np.sin(3*sp.special.j0(2*a)*t)
dg = lambda t: a* np.cos(3*sp.special.j0(2*a)*t)*3*sp.special.j0(2*a)

vL = lambda t: np.cos(g(t))**2
vR = lambda t: np.sin(g(t))**2
aL = lambda t: 2*np.cos(g(t))*-np.sin(g(t))*dg(t)
aR = lambda t: 2*np.sin(g(t))* np.cos(g(t))*dg(t)

f = lambda t, U: odefun(t, U, b, vL, vR)

acc = lambda t, U: acceleration(t, U, b, vL, vR, aL, aR, n)
 #kan behöva flytta in

b = 1
a = 1.04
x0 = 0
y0 = 0
theta0 = 0
U0 = np.array([x0, y0, theta0])
N=1024
t0=0
tf= 29.91012112737822
t, U = rk4(f, t0, tf, U0, N)

x = U[0, :]
y = U[1, :]

h = (tf - t0)/N


tol = 1e-7
it = 0
diff = 1 

while diff > tol:
    newa = a - (compute_area(N, x, y, f, h)/Der_compute_area(N, x, y, f, h))
    diff = np.abs(newa - a)
    a = newa
    it += 1
    print(it, a, diff)