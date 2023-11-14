import numpy as np
import matplotlib.pyplot as plt
def signum(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

x = np.linspace(-10, 10, 1000)
y = [signum(i) for i in x]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Signum Function')
plt.show()
