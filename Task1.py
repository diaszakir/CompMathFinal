import numpy as np
import matplotlib.pyplot as plt

def bisection_method(f, a, b, tol=1e-6):
    """Метод бисекции для поиска корня"""
    if f(a) * f(b) >= 0:
        return None, "Ошибка: f(a) и f(b) должны иметь разные знаки."

    midpoint = (a + b) / 2
    while abs(f(midpoint)) > tol:
        if f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        midpoint = (a + b) / 2

    return midpoint, None

def f(x):
    """Функция f(x) = cos(x) - x"""
    return np.cos(x) - x

def solve_task1(a, b):
    """Решение задачи методом бисекции и построение графика"""
    true_root, error_msg = bisection_method(f, a, b)
    if error_msg:
        return error_msg

    # Строим график
    x = np.linspace(a, b, 500)
    y = f(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="f(x) = cos(x) - x", color="blue")
    plt.axhline(0, color="red", linestyle="--", label="y = 0")
    plt.scatter(true_root, f(true_root), color='green', label="Root (Bisection)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Graphical Representation")
    plt.legend()
    plt.grid()
    plt.show()

    return f"True Root (Bisection Method): {true_root:.6f}"
