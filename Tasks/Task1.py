# Task 1: Graphical Method and Absolute Error
# Problem: Plot the graph of f(x)=cos(x)−x in the range x∈[0,1]. Use the graph to find an approximate
# root and calculate the absolute error compared to the root found using a numerical method.

import numpy as np
import matplotlib.pyplot as plt

def bisection_method(f, a, b, tol):
    # We check that the root really lies in the interval [a, b]
    if f(a) * f(b) >= 0:
        print("Invalid initial values. f(a) and f(b) must be of different signs.")
        return None

    # Finding midpoint
    midpoint = (a + b) / 2
    while abs(f(midpoint)) > tol:
        if f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        midpoint = (a + b) / 2

    return midpoint

# Definition of a function
def f(x):
  return np.cos(x) - x

# Plotting a graph
x = np.linspace(1, 4, 500)  # Range of x values
y = f(x)

# Creating graph
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = cos(x)-x")
plt.axhline(0, color='red', linestyle='--', label="y = 0")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graphical method")
plt.legend()
plt.grid()
plt.show()

# Finding approximate root from graph
approximate_root = 2.5
f_approx = f(approximate_root)

# Using bisection method
true_root = bisection_method(f, 0, 1, 1e-6)

# Find Absolute error with formula |X-X`|
absolute_error = abs(approximate_root - true_root)

# Output
print(f"Approximate Root (Graphical Method): {approximate_root}")
print(f"f(Approximate Root): {f_approx}")
print(f"True Root (Bisection Method): {true_root:.6f}")
print(f"Absolute Error: {absolute_error:e}")
