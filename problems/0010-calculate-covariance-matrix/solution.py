def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n = len(vectors[0])

    means = [sum(v) / n for v in vectors]

    covariance_matrix = []

    for i in range(n_features):
        row = []
        for j in range(n_features):
            cov = sum(
                (vectors[i][k] - means[i]) *
                (vectors[j][k] - means[j])
                for k in range(n)
            ) / (n - 1)

            row.append(cov)

        covariance_matrix.append(row)

    return covariance_matrix