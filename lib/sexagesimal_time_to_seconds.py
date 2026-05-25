SECONDS_IN_A_MINUTE = 60
SECONDS_IN_AN_HOUR = 60 * 60


def sexagesimal_time_to_seconds(hours: int, minutes: int, seconds: int) -> int:
    return hours * SECONDS_IN_AN_HOUR + minutes * SECONDS_IN_A_MINUTE + seconds
