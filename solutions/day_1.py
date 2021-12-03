from input_helper import get_day_input_as_list


def sonar_sweep1(data: list) -> int:
    ref = {-1: None, 0: data[0], "count": 0}
    for _ in data[1:]:
        ref[-1], ref[0] = ref[0], _
        if ref[0] > ref[-1]:
            ref["count"] += 1
    return ref["count"]


def sonar_sweep2(data: list) -> int:
    sliding_windows = []
    for _ in range(len(data)):
        window_slice = data[_ : _ + 3]
        if len(window_slice) == 3:
            sliding_windows.append(sum(window_slice))
    return sonar_sweep1(sliding_windows)


if __name__ == "__main__":

    data = get_day_input_as_list("day_1.txt")

    result = sonar_sweep1(data)
    print(result)

    result = sonar_sweep2(data)
    print(result)
