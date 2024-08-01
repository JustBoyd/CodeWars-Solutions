import numpy as np
def determinant(matrix):
    x = np.linalg.det(matrix)
    return round(x)