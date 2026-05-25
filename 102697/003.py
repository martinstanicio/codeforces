def main() -> None:
    n = int(input())
    ans = 0

    for _ in range(n):
        t = int(input())
        ans += t * 3

    print(ans)


if __name__ == "__main__":
    main()
