
import numpy as np
import matplotlib.pyplot as plt

# Input values
x = np.array([1, 2, 3, 4, 5])

# Function: y = 2x + 1
y = 2 * x + 1

# Display coordinates
print("X values:", x)
print("Y values:", y)

# Plot the graph
plt.plot(x, y, marker="o")
plt.xlabel("Input (x)")
plt.ylabel("Output (y)")
plt.title("Graph of y = 2x + 1")
plt.grid(True)
plt.show()
