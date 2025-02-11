# Task 7: Taylor Series Method
# Problem: Using the Taylor series method, solve dy/dx=y2+x2, y(0)=1, to compute y(0.1) and y(0.2).
# Use up to the third derivative for approximation.

import sympy as sp

# Define variables and function
x = sp.Symbol('x')
y = sp.Function('y')(x)

# Differential equation
dy_dx = y**2 + x**2

# Taylor series expansion
x0 = 0
y0 = 1  # initial condition

# Calculate derivatives
# First derivative at x=0, y=y0
y_prime = dy_dx.subs([(x, x0), (y, y0)])
    
# Second derivative
y_double_prime = (sp.diff(dy_dx, x) + sp.diff(dy_dx, y) * dy_dx).subs([(x, x0), (y, y0)])
    
# Third derivative
temp = sp.diff(dy_dx, x) + sp.diff(dy_dx, y) * dy_dx
y_triple_prime = (sp.diff(temp, x) + sp.diff(temp, y) * dy_dx).subs([(x, x0), (y, y0)])
    
# Taylor series expansion around x = 0
taylor_series = y0 + y_prime * x + (y_double_prime * x**2) / 2 + (y_triple_prime * x**3) / 6
    
# Evaluate at specific points
x_eval = 0.1
y_01 = taylor_series.subs(x, x_eval)
    
x_eval = 0.2
y_02 = taylor_series.subs(x, x_eval)

# Execute and print results
print("Taylor Series Approximation:", taylor_series)
print(f"y(0.1) ≈ {y_01}")
print(f"y(0.2) ≈ {y_02}")

