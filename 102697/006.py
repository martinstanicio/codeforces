from lib.euclidean_distance import euclidean_distance


def main() -> None:
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    N = euclidean_distance(x1, y1, x2, y2)

    print(N)


if __name__ == "__main__":
    main()
