import numpy as np
import matplotlib.pyplot as plt 
import scipy as sp
from Uppgift3 import rk4, odefun
import robot 
a=1 # Vi gjorde en tidigare kontroll och kom fram till att a var över 1 för båda lösningar. a = 1 har vi satt för att få färre iterationer.
while a <= 1.131:
    b = 1
    x0 = 0
    y0 = 0
    theta0 = 0

    U0 = np.array([x0, y0, theta0])


    t0 = 0 
    tf = 100



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
    T = None
    for i in range(1, len(x)):
        if x[i-1] < 0 and x[i] >= 0:
            T = t[i - 1] + (0 - x[i - 1]) * (t[i]- t[i -1]) / (x[i] - x[i - 1])
            break
            #print("Omloppstid (s): ", T , "N =", N)
    
     
    tf= T
    t, U = rk4(f, t0, tf, U0, N)

    x = U[0, :]
    y = U[1, :]
    theta = U[2, :]

    n=1
    h = (tf - t0)/N
    A=0
    while n < N:
        A = A + (x[n]*f(t[n], U[:, n])[1] - y[n]*f(t[n], U[:,n])[0])*h
        n = n +1

    A = A + (x[0] * f(t[0], U[:, 0])[1] - y[0] * f(t[0], U[:, 0])[0]) * h / 2 \
        + (x[N] * f(t[N], U[:, N])[1] - y[N] * f(t[N], U[:, N])[0]) * h / 2

    print("Area:", abs(A) / 2, "a:", a, "tf:", tf, "N:", N)
    a+=0.001

#Denna beräknings syfte var att ta fram en "skiss" på hur integralen beter sig efter olika a. Vi kan konstatera att det finns två värden på a där arean blir 20 där både värdena på a är över 1.
#samt vet vi vad tf är för varje a, N i det här fallet är beroende på vad vi använder som startgissning tf, så man kan gå tillbaks till uppgift 5 och munellt testa de a vi har fått och få att 1024 är rimligt för både