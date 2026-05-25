from lib.euclidean_distance import euclidean_distance


def main() -> None:
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    p = (x1, y1)
    q = (x2, y2)

    N = euclidean_distance(p, q)

    print(N)


if __name__ == "__main__":
    main()
