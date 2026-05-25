def minimum_excluded_value(numbers: list[int]) -> int:
    i: int = 0

    while i in numbers:
        i += 1

    return i
