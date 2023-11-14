import numpy as np
import matplotlib.pyplot as plt
def unit_ramp(a,n):
	ramp =[]
	for sample in n:
		if sample<a:
			ramp.append(0)
		else:
			ramp.append(sample)
	return ramp

UL =(int)(input("enter up"))
LL =(int)(input("enter lw"))
a=(int)(input("enter"))
n = np.arange(LL, UL, 1)
r = unit_ramp(a,n)
plt.stem(n, r)
plt.xlabel('n')
plt.xticks(np.arange(LL, UL, 1))
plt.yticks([0, UL, 1])
plt.ylabel('r[n]')
plt.title('Unit discreate Ramp r[n]')
plt.savefig("UnitRamp.png")