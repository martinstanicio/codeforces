from math import pow


def main() -> None:
    n, k = map(int, input().split())

    answer = int(pow(n, k))

    print(answer)


if __name__ == "__main__":
    main()
