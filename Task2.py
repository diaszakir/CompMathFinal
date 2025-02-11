import numpy as np

def newton_raphson(f, df, x0, tol):
    x = x0
    iterations = 0
    while abs(f(x)) > tol:
        x_new = x - f(x) / df(x)
        relative_error = abs((x_new - x) / x_new) if x_new != 0 else float('inf')
        x = x_new
        iterations += 1
    return x, iterations, relative_error

def false_position_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("Invalid initial values. f(a) and f(b) must be of different signs.")
        return None, 0, float('inf')

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

root_newton, iter_newton, err_newton = newton_raphson(f, df, 1.5, 1e-6)
root_false, iter_false, err_false = false_position_method(f, 0, 3, 1e-6)

if root_newton is not None:
    print(f"Newton-Raphson method: \nroot = {root_newton:.6f}, iterations = {iter_newton}, relative error = {err_newton:.6f}")
else:
    print("Newton-Raphson method's root is None")

if root_false is not None:
    print(f"False-Position method: \nroot = {root_false:.6f}, iterations = {iter_false}, relative error = {err_false:.6f}")
else:
    print("Метод фальш-позиции не сошелся.")
