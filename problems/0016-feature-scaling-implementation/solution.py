
import numpy as np

def feature_scaling(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    std[std == 0] = 1
    standardized_data = (data - mean) / std

    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    diff = max_val - min_val
    diff[diff == 0] = 1
    normalized_data = (data - min_val) / diff

    return standardized_data, normalized_data
