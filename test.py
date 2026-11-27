import numpy as np
import scipy as sp
from Uppgift3 import rk4, odefun


def compute_area(a, N, b=1.0, t0=0.0, tf=29.91012112737822):
    w = 3.0 * sp.special.j0(2.0 * a)
    g = lambda t: a * np.sin(w * t)
    vL = lambda t: np.cos(g(t)) ** 2
    vR = lambda t: np.sin(g(t)) ** 2
    f = lambda t, U: odefun(t, U, b, vL, vR)

    U0 = np.array([0.0, 0.0, 0.0])
    t, U = rk4(f, t0, tf, U0, N)

    x = U[0, :]
    y = U[1, :]
    h = (tf - t0) / N

    # Trapetsregeln för 0.5 * int_0^tf (x * dy/dt - y * dx/dt) dt
    A = 0.0
    for n in range(1, N):
        fn = f(t[n], U[:, n])
        A += (x[n] * fn[1] - y[n] * fn[0]) * h

    f0 = f(t[0], U[:, 0])
    fN = f(t[N], U[:, N])
    A += (x[0] * f0[1] - y[0] * f0[0]) * h / 2.0
    A += (x[N] * fN[1] - y[N] * fN[0]) * h / 2.0

    return np.abs(0.5 * A)


def solve_newton(a_start, N=1024, target=20.0, tol=1e-9, delta=1e-6):
    a = a_start
    diff = 1.0
    it = 0

    while diff > tol and it < 50:
        F = compute_area(a, N) - target
        dF = (compute_area(a + delta, N) - compute_area(a - delta, N)) / (2.0 * delta)

        newa = a - F / dF
        diff = np.abs(newa - a)
        a = newa
        it += 1
        print(f"Start {a_start} | it {it}: a = {a:.10f}, diff = {diff:.2e}")

    return a


a1 = solve_newton(1.04, N=1024)
print("-" * 50)
a2 = solve_newton(1.08, N=1024)

print(f"\nLösning 1: a = {a1:.8f}")
print(f"Lösning 2: a = {a2:.8f}")