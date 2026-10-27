
import numpy as np

def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    rows, cols = new_shape

    # Check if reshaping is possible
    if len(a) * len(a[0]) != rows * cols:
        return []

    reshaped_matrix = np.array(a).reshape(new_shape).tolist()
    return reshaped_matrix
