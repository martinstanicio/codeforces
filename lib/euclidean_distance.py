from math import pow, sqrt


def euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
