from lib.euclidean_distance import euclidean_distance


def main() -> None:
    D = int(input())
    _p: list[int] = []
    _q: list[int] = []

    for _ in range(D):
        pi = int(input())
        qi = int(input())

        _p.append(pi)
        _q.append(qi)

    p = tuple(_p)
    q = tuple(_q)

    d = euclidean_distance(p, q)

    print(d)


if __name__ == "__main__":
    main()
