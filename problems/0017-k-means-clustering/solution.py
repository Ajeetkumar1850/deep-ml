def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here
	centroids = [tuple(c) for c in initial_centroids]

    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]

        for point in points:
            distances = [
                sum((a - b) ** 2 for a, b in zip(point, centroid))
                for centroid in centroids
            ]
            closest = distances.index(min(distances))
            clusters[closest].append(point)

        new_centroids = []
        for i in range(k):
            if clusters[i]:
                dimensions = len(centroids[i])
                new_centroid = tuple(
                    sum(point[d] for point in clusters[i]) / len(clusters[i])
                    for d in range(dimensions)
                )
                new_centroids.append(new_centroid)
            else:
                new_centroids.append(centroids[i])

        if new_centroids == centroids:
            break

        centroids = new_centroids

    return centroids
