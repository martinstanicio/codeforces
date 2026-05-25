def main() -> None:
    rows, _ = map(int, input().split())
    number_of_traps = 0

    for _ in range(rows):
        row = input()
        number_of_traps += row.count("x")

    print(number_of_traps)


if __name__ == "__main__":
    main()
