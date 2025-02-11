#Task 4: Iterative Method for Matrix Inversion
# Problem: Compute the inverse of matrix
# using an iterative method with an initial guess based on its trace.

import numpy as np

import numpy as np

def iterative_inverse(A, B, tol, max_iter):
    """Iterative method for finding the inverse matrix."""
    n = A.shape[0]
    I = np.eye(n) 
    for _ in range(max_iter):
        E = np.dot(A, B) - I 
        B_new = B - np.dot(B, E)  
        if np.linalg.norm(E, ord='fro') < tol:
            return B_new
        B = B_new
    return B_new

A = np.array([[5, -3, 2], [-3, 9, -1], [2, -1, 7]], dtype=float)
B = np.linalg.inv(A) + 0.1 * np.random.randn(3, 3) 

A_inv = iterative_inverse(A, B, tol=1e-6, max_iter=100)
print("Inverse matrix (iteratively):")
print(A_inv)