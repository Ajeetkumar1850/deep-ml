import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	return float(np.mean(y_true == y_pred))