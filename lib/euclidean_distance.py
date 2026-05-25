from math import pow, sqrt


def euclidean_distance(p: tuple[float, ...], q: tuple[float, ...]) -> float:
    distance_squared = sum(pow(qi - pi, 2) for (pi, qi) in zip(p, q))
    distance = sqrt(distance_squared)

    return distance
