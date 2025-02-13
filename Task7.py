# Task 7: Taylor Series Method
# Problem: Using the Taylor series method, solve dy/dx=y2+x2, y(0)=1, to compute y(0.1) and y(0.2).
# Use up to the third derivative for approximation.

import sympy as sp

def run(x1, x2):
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
  y_prime_0 = dy_dx.subs({x: x0, y: y0})
      
  # Second derivative
  y_double_prime = sp.diff(dy_dx, x) + sp.diff(dy_dx, y) * y_prime_0
  y_double_prime_0 = y_double_prime.subs({x: x0, y: y0})
      
  # Third derivative
  y_triple_prime = sp.diff(y_double_prime, x) + sp.diff(y_double_prime, y) * y_prime_0
  y_triple_prime_0 = y_triple_prime.subs({x: x0, y: y0})
      
  # Taylor series expansion around x = 0
  taylor_series = y0 + y_prime_0 * x + (y_double_prime_0 * x**2) / 2 + (y_triple_prime_0 * x**3) / 6

  y_01 = taylor_series.subs(x, x1).evalf()
  y_02 = taylor_series.subs(x, x2).evalf()

  # print("Taylor Series Approximation:", taylor_series)
  # print(f"y(0.1) ≈ {y_01}")
  # print(f"y(0.2) ≈ {y_02}")
  return taylor_series, y_01, y_02

