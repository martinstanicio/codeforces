SECONDS_IN_A_MINUTE = 60
SECONDS_IN_AN_HOUR = 60 * 60


def sexagesimal_time_to_seconds(h: int, m: int, s: int) -> int:
    return h * SECONDS_IN_AN_HOUR + m * SECONDS_IN_A_MINUTE + s
