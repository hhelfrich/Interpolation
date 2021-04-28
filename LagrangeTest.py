import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


x_i = (0, 3, 5, 7, 13)
y_i = (-7, 6, -1, 11, 18)

def langrange_interpolation(x, x_i, y_i):
    N = len(x_i)
    result = 0
    for i in range(0, N):
        product =  1
        for j in range(0, N):
            if j != i:
                product = product*(x - x_i[j])/(x_i[i] - x_i[j])
        result += product*y_i[i]
    return result

result = langrange_interpolation(2, x_i, y_i)
print(result)
result = langrange_interpolation(9, x_i, y_i)
print(result)

def Gaussian(x, mu, sigma):
    return 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-(x - mu)**2/(2*sigma**2))

x = np.linspace(-4,4,10)

mu = 0
sigma = 1
y = Gaussian(x, mu, sigma)

x2 = np.linspace(-4,4,1000)
def langrange_interpolation1(x, x_f, y_f):
    N = len(x_f)
    result = 0
    for f in range(0, N):
        product =  1
        for j in range(0, N):
            if j != f:
                product = product*(x - x_f[j])/(x_f[f] - x_f[j])
        result += product*y_i[f]
    return result

y2 = Gaussian(x2, mu, sigma)

#y3 = langrange_interpolation1(Gaussian, x, y)

#print(y2, y3)

cs = CubicSpline(x_i, y_i)
print(cs(2), cs(9))
