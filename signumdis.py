import numpy as np
import matplotlib.pyplot as plt
n = range(-10, 10, 1)
y = []
for i in range(len(n)):
    if(n[i]>0):
        temp=1
    elif n[i]==0:
        temp=0
    else:
        temp=-1
    
    y.append(temp)
    
print(n)
print(y)
a=(int)(input("enter"))
plt.stem(n, y)
plt.title('Signum Function')
plt.axis([-5,5,-5,5])
plt.show()