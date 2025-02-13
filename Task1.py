import numpy as np
import matplotlib.pyplot as plt

def bisection_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("Invalid initial values. f(a) and f(b) must be of different signs.")
        return None

    midpoint = (a + b) / 2
    while abs(f(midpoint)) > tol:
        if f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        midpoint = (a + b) / 2

    return midpoint

def f(x):
    return np.cos(x) - x

def run(a, b, tol):
    x = np.linspace(0, 1, 500) 
    y = f(x)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y, label="f(x) = cos(x) - x", color="blue")
    ax.axhline(0, color="red", linestyle="--", label="y = 0")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Graphical Method")
    ax.legend()
    ax.grid()

    approximate_root = 0.5
    f_approx = f(approximate_root)

    true_root = bisection_method(f, a, b, tol)
    if true_root == None:
        absolute_error = 0
    else:
        absolute_error = abs(approximate_root - true_root)

    return fig, true_root, absolute_error  
