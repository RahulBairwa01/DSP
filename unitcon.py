import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)
y = np.ones(1000)

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph of y=1')
plt.show()