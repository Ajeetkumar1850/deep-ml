
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        return [sum(row) / len(row) for row in matrix]

    elif mode == "column":
        cols = len(matrix[0])
        rows = len(matrix)
        return [
            sum(matrix[i][j] for i in range(rows)) / rows
            for j in range(cols)
        ]

    return []
