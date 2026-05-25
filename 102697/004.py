def main() -> None:
    T = int(input())
    ans: list[int] = []

    for _ in range(T):
        n = int(input())

        ans.append(180 * (n - 2) if n >= 3 else 0)

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
