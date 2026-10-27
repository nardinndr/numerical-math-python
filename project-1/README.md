# numerical-math-python
Python exercises and numerical math practice

## Exercise 1: Frobenius Distance Between Two Matrices

### Problem Statement

Given two matrices A and B of the same dimensions,
write a Python function called `frobenius_distance(A, B)`
that calculates the Frobenius distance between them.

The Frobenius distance is defined as:

$$
d_F(A,B) = \sqrt{\sum_{i=1}^{m}\sum_{j=1}^{n}(a_{ij}-b_{ij})^2}
$$

### Requirements

- Use Python and NumPy.
- Do not use `np.linalg.norm`.
- Return the distance as a floating-point number.
- Test the function using example matrices.

### Example

Given:

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
$$

$$
B = \begin{bmatrix} 2 & 0 \\ 3 & 7 \end{bmatrix}
$$

Expected output:

Frobenius distance: 3.742

### Solution

See [matrix_distance.py](matrix_distance.py)
for the Python implementation.
