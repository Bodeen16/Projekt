import numpy as np
import scipy as sp
from Uppgift3 import rk4, odefun


def compute_area(a, N, b, t0, tf):
    J0 = 3 * sp.special.j0(2 * a)
    g = lambda t: a * np.sin(J0 * t)
    vL = lambda t: np.cos(g(t)) ** 2
    vR = lambda t: np.sin(g(t)) ** 2
    f = lambda t, U: odefun(t, U, b, vL, vR)

    U0 = np.array([0, 0, 0])
    t, U = rk4(f, t0, tf, U0, N)

    x = U[0, :]
    y = U[1, :]
    h = (tf - t0) / N

    A = 0
    for n in range(1, N):
        A += (x[n] * f(t[n], U[:, n])[1] - y[n] * f(t[n], U[:, n])[0]) * h

    A += (x[0] * f(t[0], U[:, 0])[1] - y[0] * f(t[0], U[:, 0])[0]) * h / 2
    A += (x[N] * f(t[N], U[:, N])[1] - y[N] * f(t[N], U[:, N])[0]) * h / 2

    return np.abs(0.5 * A)


def newtons_metod(a_start, N, Area, tol, delta):
    a = a_start
    diff = 1
    it = 0

    while diff > tol and it < 50:
        F = compute_area(a, N, b, t0, tf) - Area
        dF = (compute_area(a + delta, N, b, t0, tf) - compute_area(a - delta, N, b, t0, tf)) / (2 * delta) #framtagen med central differens

        newa = a - (F/dF)
        diff = np.abs(newa - a)
        a = newa
        it += 1
        print("it:", it, "a:", a, "diff:", diff)

    return a

b=1
t0=0
tf=29.91012112737822
N=1024
Area=20
tol=1e-9
delta=1e-6
a_start = 1.04 #1.04 & 1.08


a_lös = newtons_metod(a_start, N, Area, tol, delta)

#lösningarna blir 1.0823785863500923 & 1.0445636565833785
#Felkällorna vi har är båd enär vi räknar ut arean med trapezmetoden och att vi använder central differens för att beräkna derivatan eftersom både är approximationer.
