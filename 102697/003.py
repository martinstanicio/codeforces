def main() -> None:
    number_of_triangles = int(input())
    sum_of_perimeters = 0

    for _ in range(number_of_triangles):
        side_length = int(input())
        perimeter = side_length * 3
        sum_of_perimeters += perimeter

    print(sum_of_perimeters)


if __name__ == "__main__":
    main()
