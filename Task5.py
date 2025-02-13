import numpy as np
import matplotlib.pyplot as plt

def run(x, y):
    coefficients = np.polyfit(x, y, 1)  
    m, c = coefficients

    fit_line = m * x + c

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(x, y, color='red', label='Data Points')
    ax.plot(x, fit_line, label=f'Best Fit: y = {m:.2f}x + {c:.2f}', color='blue')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Method of Least Squares: Linear Fit')
    ax.legend()
    ax.grid()

    return fig