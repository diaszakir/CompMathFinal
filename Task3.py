#Task 3: Jacobi Method
# Problem: Solve the system of equations:
# 3x+y−z=1
# 2x−8y+z=−2
# −x+y+5z=3
# Start with an initial guess x0=[0,0,0]x0=[0,0,0].

import numpy as np

def jacobi_method(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0
    for _ in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            summation = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - summation) / A[i][i]
        # Checking if we have achieved the desired accuracy
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new
        print(x)
    return x

def run(A, b, x0, tol, max_iter):
    # A = np.array([[3, 1, -1], [2, -8, 1], [-1, 1, 5]], dtype=float)
    # b = np.array([1, -2, 3], dtype=float)
    # x0 = np.zeros(len(b))

    root = jacobi_method(A, b, x0, tol=1e-6, max_iter=100)
    return root
    # print(f"Root: {np.round(root,1)}")