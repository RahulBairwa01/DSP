import numpy as np
import matplotlib.pyplot as plt

def circular_convolution(x, h):
    N = len(x)
    M = len(h)
    max_len = max(N, M)
    if N != M:
        x = np.pad(x, (0, max_len - N), 'constant')
        h = np.pad(h, (0, max_len - M), 'constant')
    
    y = np.zeros(max_len)
    for n in range(max_len):
        for m in range(max_len):
            y[n] += x[(n - m) % max_len] * h[m]
    n = range(0,max_len)
    plt.stem(n,y)
    return y

# Define input sequences x and h
x=[]
a=int(input("Size of my array:"))
for i in range(a):
    k=int(input("elements 1:"))
    x.append(k)
print(x)
h=[]
b=int(input("Size of my array:"))
for j in range(b):
    k=int(input("elements 2: "))
    h.append(k)
print(h)


# Perform circular convolution
result = circular_convolution(x, h)

print("Circular Convolution Result:",result)