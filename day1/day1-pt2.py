def main(inf: str):

    with open(inf) as input_file:
        depths = [int(line) for line in input_file.readlines()]

    return sum(
        [
            1
            for i in range(3, len(depths))
            if (depths[i - 3] + depths[i - 2] + depths[i - 1]) < (depths[i - 2] + depths[i - 1] + depths[i])
        ]
    )


if __name__ == "__main__":
    sample_result = main("day1-sample.txt")
    print(sample_result)
    assert sample_result == 5
    full_result = main("day1-full.txt")
    print(full_result)
    assert full_result == 1103
