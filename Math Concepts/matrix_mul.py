
import numpy as np

# A vector
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vector addition:", a + b)
print("Scalar multiplication:", 2 * a)
print("Dot product:", np.dot(a, b))

# A matrix
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix shape:", A.shape)
print("Matrix addition:\n", A + B)
print("Matrix multiplication:\n", A @ B)
print("Transpose:\n", A.T)
