from lib.euclidean_distance import euclidean_distance


def main() -> None:
    px = int(input())
    py = int(input())
    qx = int(input())
    qy = int(input())

    p = (px, py)
    q = (qx, qy)

    distance = euclidean_distance(p, q)

    print(distance)


if __name__ == "__main__":
    main()
