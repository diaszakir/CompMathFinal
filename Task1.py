import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x) - x

def bisection_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        return None, "Invalid interval. f(a) and f(b) must have opposite signs."

    midpoint = (a + b) / 2
    while abs(f(midpoint)) > tol:
        if f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        midpoint = (a + b) / 2

    return midpoint, None

def solve_task1(a, b, tol):
    # Строим график
    x = np.linspace(a, b, 500)
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, label="f(x) = cos(x)-x")
    ax.axhline(0, color='red', linestyle='--', label="y = 0")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Graphical method")
    ax.legend()
    ax.grid()

    # Численный корень методом бисекции
    root, error_msg = bisection_method(f, a, b, tol)
    
    if error_msg:
        return error_msg, fig
    
    result_text = f"Root: {root:.6f}"
    return result_text, fig
