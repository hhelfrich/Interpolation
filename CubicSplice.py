import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import fixed_quad
def f(x):
    return (x - 2)**3 - 3.5*x + 8

def fprime(x):
    return 3*(x-2)**2 - 3.5

def F(a, b):
    upper = (.25*(b-2)**4 - 1.75*b**2 + 8*b)
    lower = (.25*(a-2)**4 - 1.75*a**2 + 8*a)
    return upper - lower

def centralDiff(f, x, h):
    return (f(x + h/2) - f(x - h/2))/h

x = np.linspace(0, 4)
y = f(x)

cs = CubicSpline(x, y)

Integral = F(0, 4)
Integral1, err = fixed_quad(cs, 0, 4, n=2)
print(Integral, Integral1)
Integral, err = fixed_quad(f, 0, 4, n=2)
print(Integral)



