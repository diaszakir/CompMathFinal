import numpy as np

def newton_raphson(f, df, x0, tol, max_iterations=1000):
    x = x0
    iterations = 0
    while abs(f(x)) > tol:
        if df(x) == 0:
            return None, iterations, float('inf')

        x_new = x - f(x) / df(x)
        relative_error = abs((x_new - x) / x_new) if x_new != 0 else float('inf')
        
        x = x_new
        iterations += 1

        if iterations > max_iterations:
            return None, iterations, float('inf')

    return x, iterations, relative_error

def false_position_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        raise ValueError("Invalid initial values. f(a) and f(b) must be of different signs.")

    c = a
    iterations = 0
    while True:
        c_new = b - f(b) * (b - a) / (f(b) - f(a))
        relative_error = abs((c_new - c) / c_new) if c_new != 0 else float('inf')
        c = c_new
        iterations += 1
        if abs(f(c)) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, iterations, relative_error

def f(x):
    return x**2 - 4*np.sin(x)

def df(x):
    return 2*x - 4*np.cos(x)

def run(a, b, tol):
    root_newton, iter_newton, err_newton = newton_raphson(f, df, 1.5, tol)
    root_false, iter_false, err_false = false_position_method(f, a, b, tol)

    if root_newton is not None:
        print(f"Newton-Raphson method: \nroot = {root_newton:.6f}, iterations = {iter_newton}, relative error = {err_newton:.6f}")
    else:
        print("Newton-Raphson method's root is None")

    if root_false is not None:
        print(f"False-Position method: \nroot = {root_false:.6f}, iterations = {iter_false}, relative error = {err_false:.6f}")
    else:
        print("False-Position method's root is None")

    return root_newton, iter_newton, err_newton, root_false, iter_false, err_false