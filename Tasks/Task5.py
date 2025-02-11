#Task 5: Linear Curve Fitting
# Problem: Fit a line to data points:
# (1,5),(2,8),(3,12),(4,15),(5,20) using least squares.


import numpy as np
import matplotlib.pyplot as plt

# Data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 8, 12, 15, 20])

# Fit a straight line (linear regression)
coefficients = np.polyfit(x, y, 1)  # 1 indicates a linear fit
m, c = coefficients

# Line equation: y = mx + c
fit_line = m * x + c
# Plot
plt.scatter(x, y, color='red', label='Data Points')  # Scatter plot for data
plt.plot(x, fit_line, label=f'Best Fit: y = {m:.2f}x + {c:.2f}', color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Method of Least Squares: Linear Fit')
plt.grid()
plt.show()