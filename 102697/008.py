from math import pow, sqrt


def main() -> None:
    dimension = int(input())
    distance_squared = 0

    for _ in range(dimension):
        pi = int(input())
        qi = int(input())

        distance_squared += pow(qi - pi, 2)

    distance = sqrt(distance_squared)

    print(distance)


if __name__ == "__main__":
    main()
