import numpy as np
import matplotlib.pyplot as plt
w = 2 * np.pi * 1 # frequency of the signal
n = np.arange(0, 20) # number of samples
y = np.sin(w * n)

plt.stem(n, y)
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.title('Discrete Sin(wt) Function')
plt.show()