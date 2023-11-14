import numpy as np
import matplotlib.pyplot as plt
w = 2 * np.pi * 1 # frequency of the signal
t = np.linspace(0, 1, 1000) # time interval of the signal

y = np.sin(w * t)

plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sin(wt) Function')
plt.show()