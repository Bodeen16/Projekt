import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from Uppgift3 import rk4, odefun
import robot


def compute_area(a, N, b, t0,tf):
    J0 = 3 * sp.special.j0(2 * a)
    g = lambda t: a * np.sin(J0 * t)
    vL = lambda t: np.cos(g(t)) ** 2
    vR = lambda t: np.sin(g(t)) ** 2
    f = lambda t, U: odefun(t, U, b, vL, vR)

    U0 = np.array([0, 0, 0])
    t, U = rk4(f, t0, tf, U0, N)
    x = U[0, :]
    y = U[1, :]
    for i in range(1, len(x)):
        if x[i-1] < 0 and x[i] >= 0:
            tf = t[i - 1] + (0 - x[i - 1]) * (t[i]- t[i -1]) / (x[i] - x[i - 1])
            break

    t, U = rk4(f, t0, tf, U0, N)
    x = U[0, :]
    y = U[1, :]

    U0 = np.array([0, 0, 0])

    h = (tf - t0) / N

    A = 0
    for n in range(1, N):
        A += (x[n] * f(t[n], U[:, n])[1] - y[n] * f(t[n], U[:, n])[0]) * h

    A += (x[0] * f(t[0], U[:, 0])[1] - y[0] * f(t[0], U[:, 0])[0]) * h / 2
    A += (x[N] * f(t[N], U[:, N])[1] - y[N] * f(t[N], U[:, N])[0]) * h / 2

    return np.abs(A / 2), tf


def newtons_metod(a_start, N, Area, tol, delta,tf):
    a = a_start
    diff = 1
    it = 0

    while diff > tol and it < 50:
        F = compute_area(a, N, b, t0, tf)[0] - Area
        dF = (compute_area(a + delta, N, b, t0, tf)[0] - compute_area(a - delta, N, b, t0, tf)[0]) / (2 * delta)

        newa = a - (F / dF)
        diff = np.abs(newa - a)
        a = newa
        it += 1
        print("it:", it, "a:", a, "diff:", diff)
    tf = compute_area(a, N, b, t0, tf)[1]

    return a, tf


b = 1
t0 = 0
N = 1024
Area = 20
tol = 1e-9
delta = 1e-7
tf1 = 37  #37 för a=1.04, 75 för a=1.123
tf2 = 75
a_start1 = 1.04 #startgissning 1.04 & 1.12
a_start2 = 1.12


a_lös1, tf1 = newtons_metod(a_start1, N, Area, tol, delta, tf1)
a_lös2, tf2 = newtons_metod(a_start2, N, Area, tol, delta, tf2)



# Räkna fram banan för den hittade lösningen a_lös
for a, tf in [(a_lös1, tf1), (a_lös2, tf2)]:
    J0 = 3 * sp.special.j0(2 * a)
    g = lambda t: a * np.sin(J0 * t)
    vL = lambda t: np.cos(g(t)) ** 2
    vR = lambda t: np.sin(g(t)) ** 2
    f = lambda t, U: odefun(t, U, b, vL, vR)
    U0 = np.array([0, 0, 0])
    t, U = rk4(f, t0, tf, U0, N)

    x = U[0, :]
    y = U[1, :]
    theta = U[2, :]

    plt.figure()
    plt.plot(x, y)
    robot.animate(x, y, theta)
    plt.axis("equal")
    plt.grid(True)
    plt.show()

#Kontrollering av att a har 6 korrekta decimaler 
for N in [1024, 2048, 4096, 8192]:
    a1, _ = newtons_metod(a_start1, N, Area, tol, 1e-7, tf1)
    a2, _ = newtons_metod(a_start2, N, Area, tol, 1e-7, tf2)
    print("N =", N, " a1 =", a1, " a2 =", a2)