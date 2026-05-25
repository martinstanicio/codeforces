from lib.sexagesimal_time_to_seconds import sexagesimal_time_to_seconds


def main() -> None:
    hours = int(input())
    minutes = int(input())
    seconds = int(input())
    meridiem = input()  # AM | PM

    if meridiem == "PM":
        hours += 12

    total_seconds = sexagesimal_time_to_seconds(hours, minutes, seconds)

    print(total_seconds)


if __name__ == "__main__":
    main()
