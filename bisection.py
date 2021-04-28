import numpy as np

def find_pairs(f, step, a, b):
    x = a
    pairs = []
    while (x + step < b):
        if (f(x+step)/f(x) < 0):
             pairs.append([x, x+step])
        x += step
    return pairs

def bisection(f, pairs, tolerance):
    zeros = []
    for pair in pairs:
        mid = (pair[1]-pair[0])/2 + pair[0]
        while (abs(f(mid)) > tolerance):
            if (f(mid)/f(pair[0]) <0): pair[1] = mid
            else: pair[0] = mid
            mid = (pair[1]-pair[0])/2 + pair[0]
        zeros.append(mid)
    return zeros

def sinc(x):
    if (x ==0):
        return 1
    else:
        return np.sin(x)/x

pairs = find_pairs(sinc, 0.1, 0, 10)
print(pairs)
zeros = bisection(sinc, pairs, 1E-10)
print(zeros)
print(np.pi, 2.0*np.pi, 3.0*np.pi)
