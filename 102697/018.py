def main() -> None:
    test_cases = int(input())
    answers: list[float] = []

    for _ in range(test_cases):
        side_a, side_b = map(float, input().split())
        mechanical_advantage = side_a / side_b
        answers.append(mechanical_advantage)

    for a in answers:
        print(a)


if __name__ == "__main__":
    main()
