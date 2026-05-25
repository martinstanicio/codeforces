def main() -> None:
    N = int(input())
    ans = ""

    if N % 3 == 0:
        ans += "Fizz"

    if N % 5 == 0:
        ans += "Buzz"

    print(ans)


if __name__ == "__main__":
    main()
