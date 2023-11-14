import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 10)
y = x

plt.plot(x, y)
plt.xlabel('t')
plt.ylabel('r[t]')
plt.title('Ramp continuos Signal')
plt.show()
