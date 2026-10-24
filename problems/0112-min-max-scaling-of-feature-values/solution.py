def min_max(x: list[float]) -> list[float]:
    if not x:
        return []

    min_val = min(x)
    max_val = max(x)

    if min_val == max_val:
        return [0.0 for _ in x]

    return [(value - min_val) / (max_val - min_val) for value in x]