import numpy as np
import matplotlib.pyplot as plt

def convolve(a,b):
    output =np.zeros(len(a)+len(b)-1)
    for i in range(len(output)):
        for j in range(len(b)):
            if j-i>=0 and j-i<len(a):
                output[i]+=a[j-i]*b[j]
    return output

n,m=map(int,input().split())
a=list(map(int,input("enter a").split()))
b=list(map(int,input("enter a").split()))

dif=abs(n-m)
a1=[0]*n;
b1=[0]*m;

j=0

for i in range (dif.n):
    a1[i]=a[j]
    j+=1

j=dif

for i in range(n):
    if j==max(n,m):
        break
    b[i]=a[j]
    j+=1
    
convolve(a1,b)
convolve(a,b)
convolve(b1,b)
