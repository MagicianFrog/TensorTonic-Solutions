import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A) 
    rows, cols = A.shape
    X = np.zeros((cols, rows))
    for i in range(cols):
        for j in range(rows):
            X[i, j] = A[j, i]
    return X
    pass
