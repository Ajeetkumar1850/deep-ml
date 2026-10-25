import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	if n_col is None:
        n_col = np.max(x) + 1

    return np.eye(n_col)[x]
