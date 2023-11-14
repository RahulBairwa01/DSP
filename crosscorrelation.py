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

c=[]
l=n-1
while l>=0:
    c.append(a[l])
    l= l-1;
print(c)

output_signal = convolve(b, c)
max =0;
for i in range(len(output_signal)):
    if(output_signal[i]>max):
     max = output_signal[i]
     
    
print(output_signal)
print(max)
plt.stem(output_signal)