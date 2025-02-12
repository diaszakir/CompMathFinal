# Task 6: First Derivative Using Newton’s Forward Difference Formula
# Problem: Given data points x=[0,1,2] and y=[1,3,7], estimate dy/dx at x=1.
import numpy as np

def run(x, y):
    # Step size
    h = x[1] - x[0]

    # Create forward difference table
    n = len(y)
    forward_diff = np.zeros((n, n))
    forward_diff[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            forward_diff[i, j] = forward_diff[i + 1, j - 1] - forward_diff[i, j - 1]

    # First derivative using Newton's forward formula
    dy_dx = (forward_diff[0, 1] / h) + (forward_diff[0, 2] / (2 * h)) * (2 * 1 - 1)
    return dy_dx