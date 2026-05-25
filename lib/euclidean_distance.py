from math import pow, sqrt


def euclidean_distance(p: tuple[float, ...], q: tuple[float, ...]) -> float:
    d_squared = sum(pow(qi - pi, 2) for (pi, qi) in zip(p, q))
    d = sqrt(d_squared)

    return d
