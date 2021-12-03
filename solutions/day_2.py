from input_helper import get_day_input_as_list


def dive1(data: list) -> tuple:
    """returns (horizontal, depth)"""
    buckets = dict.fromkeys(["forward", "up", "down"], 0)
    for _ in data:
        cmd, var = _.split(" ")
        if cmd in buckets:
            buckets[cmd] += int(var)
    return (buckets["forward"], buckets["down"] - buckets["up"])


def dive2(data: list) -> tuple:
    """returns (horizontal, depth)"""
    buckets = dict.fromkeys(["horizontal", "depth", "aim"], 0)
    for _ in data:
        cmd, var = _.split(" ")
        var = int(var)
        if cmd == "forward":
            buckets["horizontal"] += var
            buckets["depth"] += buckets["aim"] * var
        elif cmd in ("up", "down"):
            buckets["aim"] += var if cmd == "down" else -var
    return (buckets["horizontal"], buckets["depth"])


if __name__ == "__main__":

    data = get_day_input_as_list("day_2.txt", str)

    result = dive1(data)
    print(result, result[0] * result[1])

    result = dive2(data)
    print(result, result[0] * result[1])
