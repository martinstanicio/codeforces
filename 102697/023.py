def main() -> None:
    initial_velocity = float(input())
    final_velocity = 0
    acceleration = -9.8
    max_height = (final_velocity**2 - initial_velocity**2) / (2 * acceleration)

    print(max_height)


if __name__ == "__main__":
    main()
