import numpy as np

def iterative_inverse(A, B, tol, max_iter):
    """Iterative method for finding the inverse matrix."""
    n = A.shape[0]
    I = np.eye(n)  # Identity matrix
    for _ in range(max_iter):
        E = np.dot(A, B) - I  # Calculating the error
        B_new = B - np.dot(B, E)  # Proximity update
        # Checking if we have achieved accuracy
        if np.linalg.norm(E, ord='fro') < tol:
            return B_new
        B = B_new
    return B_new

def run(A):
    # Initial approximation
    trace_A = np.trace(A)
    B = (1 / trace_A) * np.eye(A.shape[0])

    # Iterative process
    A_inv_iterative = iterative_inverse(A, B, tol=1e-6, max_iter=100)

    # Using numpy's built-in function for comparison
    A_inv_numpy = np.linalg.inv(A)

    difference = np.abs(A_inv_iterative - A_inv_numpy)

    # Printing results
    # print("Inverse matrix (iterative method):")
    # print(A_inv_iterative)

    # print("\nInverse matrix (numpy.linalg.inv):")
    # print(A_inv_numpy)
    return A_inv_iterative, A_inv_numpy, difference

# def iterative_inverse(A, tol=1e-6, max_iter=500):
#     """Iterative method for finding the inverse matrix."""
#     n = A.shape[0]
#     I = np.eye(n)  

#     B = (1 / np.trace(A)) * A.T  

#     alpha = 0.1 

#     for i in range(max_iter):
#         E = np.dot(A, B) - I  
#         B_new = B - alpha * np.dot(B, E)  

#         if np.isnan(B_new).any() or np.isinf(B_new).any():
#             raise ValueError(f"Computation diverged at iteration {i}! Try reducing alpha.")

#         if np.linalg.norm(E, ord='fro') < tol:
#             return B_new  

#         B = B_new  

#     raise ValueError("Max iterations reached! Method did not converge.")

# def run(A):
#     try:
#         A_inv = iterative_inverse(A)
#         return A_inv

#     except ValueError as e:
#         return str(e)
