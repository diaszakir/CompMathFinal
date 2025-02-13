# Task 8: Simpson’s 3/8 Rule
# Problem: Using Simpson’s 3/8 Rule, compute ∫
# 5
# 2x
# 3 dx with 6 subintervals. Provide the absolute error
# compared to the exact value.

import numpy as np

# Function to integrate
def f(x):
    return x**3

def run(a, b, n):
    # # Simpson's 3/8 Rule
    # a, b = 2, 5
    # n = 6  # Must be a multiple of 3
    x = np.linspace(a, b, n+1)
    y = f(x)

    # Step
    h = (b - a) / n
    I = (3 * h / 8) * (y[0] + 3 * sum(y[1:-1:3]) + 3 * sum(y[2:-1:3]) + 2 * sum(y[3:-1:3]) + y[-1])

    # Exact value of the integral
    exact_value = (1/4) * (b**4 - a**4)

    # Absolute error
    absolute_error = abs(exact_value - I)

    # print(f"Approximate value of the integral using Simpson's 3/8 Rule: {I}")
    # print(f"Exact value of the integral: {exact_value}")
    # print(f"Absolute error: {absolute_error}")
    return I, exact_value, absolute_error
