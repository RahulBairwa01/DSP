import numpy as np
import matplotlib.pyplot as plt

def circular_convolution(x, y):
    X = np.fft.fft(x)
    Y = np.fft.fft(y)
    Z = X * Y
    z = np.real(np.fft.ifft(Z))
    return z

n=int(input("enter size1: "))
x=[];
for i in range(n):
    x.append(int(input()))

m=int(input("enter size2: "))
y=[];
for i in range(m):
    y.append(int(input()))

if n < m:
    for i in range(n,m):
        x.append(0);
if n > m:
    for i in range(m,n):
        y.append(0);

z = circular_convolution(x, y)
print(z)
plt.stem(x)
plt.show()
plt.stem(y)
plt.show()
plt.stem(z)
plt.show()