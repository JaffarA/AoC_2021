def get_day_input_as_list(file_name, cast=int) -> list:
    """
    Reads a text file and returns a list of lines cast as the type of cast.
    """
    with open(f"../inputs/{file_name}", "r") as f:
        return [cast(_.replace("\n", "").strip()) for _ in f.readlines()]
