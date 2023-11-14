import numpy as np
import matplotlib.pyplot as plt

def overlap_add(x, h, N):
    M = len(h)
    L = N - M + 1
    num_blocks = int(np.ceil(len(x) / L))
    padded_x = np.pad(x, (0, num_blocks * L - len(x)), mode='constant')
    y = np.zeros(len(padded_x) + M - 1)
    for i in range(num_blocks):
        block = padded_x[i * L : i * L + N]
        conv_result = np.convolve(block, h)
        y[i * L : i * L + len(conv_result)] += conv_result
    return y[:len(x) + M - 1]

# Example input signals
n = int(input("Enter size of x(n): "))
x = [int(input(f"Enter x({i}): ")) for i in range(n)]

m = int(input("Enter size of h(n): "))
h = [int(input(f"Enter h({i}): ")) for i in range(m)]

# Length of FFT (Fast Fourier Transform)
N = 8

# Perform convolution using overlap-add method
convolved_signal = overlap_add(x, h, N)

# Plot the original and convolved signals
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.stem(x, use_line_collection=True)
plt.title('Original Signal')
plt.subplot(2, 1, 2)
plt.stem(convolved_signal, use_line_collection=True)
plt.title('Convolved Signal using Overlap-Add Method')
plt.tight_layout()
plt.show()