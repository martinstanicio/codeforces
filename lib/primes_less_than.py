from math import isqrt

SMALLEST_PRIME_NUMBER = 2


def primes_less_than(n: int) -> list[int]:
    if n <= 2:
        return []

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(SMALLEST_PRIME_NUMBER, isqrt(n) + 1):
        if not is_prime[i]:
            continue

        for j in range(i * i, n, i):
            is_prime[j] = False

    return [i for i in range(n) if is_prime[i]]
