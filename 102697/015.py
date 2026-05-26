STARTING_STATION = "Airport"
TARGET_STATION = "Hotel"


def minimum_required_lines(
    graph: dict[str, set[str]],
    visited_stations: set[str],
    starting_station: str,
    target_station: str,
) -> int:
    if target_station in graph[starting_station]:
        return 1

    answer = len(graph) - 1
    new_visited_stations = visited_stations.copy()
    new_visited_stations.add(starting_station)

    for station in graph[starting_station]:
        if station in visited_stations:
            continue

        required_lines = minimum_required_lines(
            graph, new_visited_stations, station, target_station
        )

        answer = min(required_lines, answer)

    return answer + 1


def main() -> None:
    number_of_lines = int(input())
    graph: dict[str, set[str]] = {}

    for _ in range(number_of_lines):
        stations = input().split()

        for station_a in stations:
            if station_a not in graph:
                graph[station_a] = set()

            for station_b in stations:
                if station_a == station_b:
                    continue

                graph[station_a].add(station_b)

    answer = minimum_required_lines(graph, set(), STARTING_STATION, TARGET_STATION)

    print(answer)


if __name__ == "__main__":
    main()
