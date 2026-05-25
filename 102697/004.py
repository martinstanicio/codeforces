from lib.sum_of_angles_in_polygon import sum_of_angles_in_polygon


def main() -> None:
    test_cases = int(input())
    answers: list[int] = []

    for _ in range(test_cases):
        sides = int(input())
        sum_of_angles = sum_of_angles_in_polygon(sides)

        answers.append(sum_of_angles)

    for a in answers:
        print(a)


if __name__ == "__main__":
    main()
