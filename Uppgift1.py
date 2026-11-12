import numpy as np
import matplotlib.pyplot as plt 

"""
Ekvation 1: 
dxdt = v(t)*np.cos(th(t))

dydt = v(t)*np.sin(th(t))


Ekvation 2: 
v(t) = vR(t) + vL(t))/2


Ekvation 3: 
dthdt = (vR(t) - vL(t))/b


Ekvation 4: 
vL(t) = aLt + wL
vR(t) = aRt + wR


Konstanter: 

a = (aR + aL)/2

w = (wR + wL)/2

Da = (aR - aL)/(2*b)

Dw = (wR - wL)/b


Analytiska uttryck: 

(Matten är gjord på separat papper och vi får svaren)

1: dthdt = 2*Da*t + Dw
2: th(t) = Da*t**2 + Dw*t + th0
3: dxdt = (a*t + w) * np.cos(Da*t**2 + Dw*t + th0) (utan ekvation 2: v(t) * np.cos(Da*t**2 + Dw*t + th0))
4: dydt = (a*t + w) * np.sin(Da*t**2 + Dw*t + th0) (utan ekvation 2: v(t) * np.sin(Da*t**2 + Dw*t + th0))



"""