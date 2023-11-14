import numpy as np
import matplotlib.pyplot as plt

def convolve(x, h):
    N = len(x)
    M = len(h)
    y = np.zeros(N+M-1)
    for n in range(N+M-1):
        kmin = max(0, n-M+1)
        kmax = min(n, N-1)
        for k in range(kmin, kmax+1):
            y[n] += x[k] * h[n-k]
    return y
n=int(input("enter size1: "))
a=[];
for i in range(n):
    a.append(int(input()))

m=int(input("enter size2: "))
b=[];
for i in range(m):
    b.append(int(input()))

x = np.array(a)
h = np.array(b)
y = convolve(x, h)
print("convolution : ",y)
plt.stem(y)
plt.show()