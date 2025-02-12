import numpy as np

def iterative_inverse(A, tol=1e-6, max_iter=500):
    """Iterative method for finding the inverse matrix."""
    n = A.shape[0]
    I = np.eye(n)  

    B = (1 / np.trace(A)) * A.T  

    alpha = 0.1 

    for i in range(max_iter):
        E = np.dot(A, B) - I  
        B_new = B - alpha * np.dot(B, E)  

        if np.isnan(B_new).any() or np.isinf(B_new).any():
            raise ValueError(f"Computation diverged at iteration {i}! Try reducing alpha.")

        if np.linalg.norm(E, ord='fro') < tol:
            return B_new  

        B = B_new  

    raise ValueError("Max iterations reached! Method did not converge.")

def run():
    A = np.array([[5, -3, 2], [-3, 9, -1], [2, -1, 7]], dtype=float)

    try:
        A_inv = iterative_inverse(A)
        return A_inv
    except ValueError as e:
        return e
