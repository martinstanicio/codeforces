GRAVITY = {
    "EARTH": 9.807,
    "MARS": 3.711,
}


def main() -> None:
    planet = input()

    print(GRAVITY[planet])


if __name__ == "__main__":
    main()
