from lib.sexagesimal_time_to_seconds import sexagesimal_time_to_seconds


def main() -> None:
    _h = int(input())
    m = int(input())
    s = int(input())
    a = input()

    h = _h + (12 if a == "PM" else 0)

    t = sexagesimal_time_to_seconds(h, m, s)

    print(t)


if __name__ == "__main__":
    main()
