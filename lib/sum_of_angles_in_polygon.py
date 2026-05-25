def sum_of_angles_in_polygon(sides: int) -> int:
    if sides <= 2:
        return 0

    return 180 * (sides - 2)
