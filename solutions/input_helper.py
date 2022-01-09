def get_day_input_as_list(file_name: str, cast: type = int) -> list:
    """
    Reads a text file and returns a list of lines cast as the type of cast.
    """
    path = __file__.replace("solutions/input_helper.py", "inputs/")
    with open(f"{path}{file_name}", "r") as f:
        return [cast(_.replace("\n", "").strip()) for _ in f.readlines()]
