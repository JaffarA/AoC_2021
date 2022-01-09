from input_helper import get_day_input_as_list


def list_of_ints_to_str(data: list) -> str:
    return "".join([str(_) for _ in data])


def binary_diagnostic1(data: list) -> tuple:
    """returns (gamma, epsilon)"""
    rates = {k: [] for k in ("gamma", "epsilon")}
    rows = {k: dict.fromkeys((0, 1), 0) for k in range(len(data[0]))}

    for row in data:
        for i, bit in enumerate(row):
            rows[i][bit] += 1

    for row in rows:
        mf_bit, lf_bit = 0, 1
        if rows[row][0] < rows[row][1]:
            mf_bit, lf_bit = lf_bit, mf_bit

        rates["gamma"].append(mf_bit)
        rates["epsilon"].append(lf_bit)

    return (list_of_ints_to_str(rates["gamma"]), list_of_ints_to_str(rates["epsilon"]))


def binary_diagnostic2(data: list) -> tuple:
    """returns (oxygen generator rating, co2 scrubber rating)"""
    rates = {_: [] for _ in ("o2_gen", "co2_sub")}
    n_len = len(data[0])

    for default_bit in (1, 0):
        rows = data.copy()
        for index in range(n_len):
            if len(rows) == 1:
                break
            freq = dict.fromkeys((0, 1), 0)
            for element in rows:
                freq[element[index]] += 1
            keep_bit = default_bit if freq[0] > freq[1] else default_bit ^ 1
            rows = list(filter(lambda row: row[index] == keep_bit, rows))
        rates[[*rates.keys()][default_bit]] = rows.pop()

    return (list_of_ints_to_str(rates["o2_gen"]), list_of_ints_to_str(rates["co2_sub"]))


if __name__ == "__main__":

    data = get_day_input_as_list("day_3.txt", lambda x: [int(_) for _ in x])

    result = binary_diagnostic1(data)
    print(result, int(result[0], base=2) * int(result[1], base=2))

    result = binary_diagnostic2(data)
    print(result, int(result[0], base=2) * int(result[1], base=2))
