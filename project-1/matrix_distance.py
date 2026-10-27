
import numpy as np #to work with the matrics


def frobenius_distance(A, B):
    """
    Calculate the Frobenius distance between two matrices.

    Args:
        A: First matrix (NumPy array).
        B: Second matrix (NumPy array).

    Returns:
        float: Frobenius distance between A and B.
    """

    if A.shape != B.shape:
        raise ValueError("Matrices must have the same shape.")
         #use raise to show the error

    difference = A - B
    squared = difference ** 2
    total = np.sum(squared)#toget the sigma + 
    distance = np.sqrt(total)

    return float(distance)


# Example matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[2, 0],
              [3, 7]])

result = frobenius_distance(A, B)

print(f"Frobenius distance: {result:.3f}")

# Simple tests, we use assert to test , when sth is true it will continue
assert np.isclose(frobenius_distance(A, A), 0)#we know that the distance of a matrix from itself is 0
assert np.isclose(frobenius_distance(A, B), np.sqrt(14))

print("All tests passed!")
