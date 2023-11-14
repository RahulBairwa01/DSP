import numpy as np
import matplotlib.pyplot as plt
a = 0.5 # constant value
t = np.linspace(0, 10, 1000) # time interval of the signal

y = np.exp(-a * t)

plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Continuous e^-at Function')
plt.show()