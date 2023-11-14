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

b=[]
l=n-1
while l>=0:
    b.append(a[l])
    l= l-1;
print("reverse",b)

x = np.array(a)
h = np.array(b)
output_signal = convolve(x, h)
max =0;

for i in range(len(output_signal)):
    if(output_signal[i]>max):
     max = output_signal[i]
     
    
print(output_signal)
print(max)
plt.stem(output_signal)
plt.show()