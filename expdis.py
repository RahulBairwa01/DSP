import numpy as np
import matplotlib.pyplot as plt
def exponential(a, n):
	expo =[]
	for sample in n:
		expo.append(np.exp(a * sample))
	return (expo)
		
UL = 1
LL = -1
n = np.arange(LL, UL, 0.1)
a=(int)(input("enter"))
x = exponential(a, n)
plt.stem(n, x)
plt.xlabel('n')
plt.xticks(np.arange(LL, UL, 0.1))
# plt.yticks([0, UL, 1])
plt.ylabel('x[n]')
plt.title('Exponential Signal e**(an)')
plt.savefig("Exponential.png")