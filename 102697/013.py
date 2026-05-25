def main() -> None:
    resistance_a = int(input())
    resistance_b = int(input())

    equivalent_parallel_resistance = (resistance_a * resistance_b) / (
        resistance_a + resistance_b
    )

    print(equivalent_parallel_resistance)


if __name__ == "__main__":
    main()
