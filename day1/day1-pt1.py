def main(inf: str):

    with open(inf, "r") as input_file:
        depths = [int(line) for line in input_file.readlines()]

    return sum([1 for i in range(0, len(depths) - 1) if depths[i] < depths[i + 1]])


if __name__ == "__main__":
    sample_result = main("day1-sample.txt")
    print(sample_result)
    assert sample_result == 7
    full_result = main("day1-full.txt")
    print(full_result)
    assert full_result == 1139
