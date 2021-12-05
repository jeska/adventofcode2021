def main(inf: str):

    increases = 0
    with open(inf, "r") as input_file:
        first_depth, remaining_depths = (
            int(input_file.readline()),
            input_file.readlines(),
        )

    for line in remaining_depths:
        current_depth = int(line)
        increases += 1 if current_depth > first_depth else 0
        first_depth = current_depth

    return increases


if __name__ == "__main__":
    sample_result = main("day1-sample.txt")
    assert sample_result == 7
    full_result = main("day1-full.txt")
    assert full_result == 1139
