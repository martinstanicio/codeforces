from lib.sum_of_angles_in_polygon import sum_of_angles_in_polygon


def main() -> None:
    T = int(input())
    ans: list[int] = []

    for _ in range(T):
        n = int(input())

        ans.append(sum_of_angles_in_polygon(n))

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
