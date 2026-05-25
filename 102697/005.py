def main() -> None:
    number = int(input())
    answer = ""

    if number % 3 == 0:
        answer += "Fizz"

    if number % 5 == 0:
        answer += "Buzz"

    print(answer)


if __name__ == "__main__":
    main()
