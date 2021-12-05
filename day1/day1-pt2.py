def main(inf: str):

    increases = 0
    report = []
    with open(inf) as input_file:
        report = [int(line) for line in input_file.readlines()]

    prev_sum = report[0] + report[1] + report[2]
    for i in range(3, len(report)):
        current_sum = report[i - 2] + report[i - 1] + report[i]
        increases += 1 if current_sum > prev_sum else 0
        prev_sum = current_sum

    return increases


if __name__ == "__main__":
    sample_result = main("day1-sample.txt")
    print(sample_result)
    assert sample_result == 5
    full_result = main("day1-full.txt")
    print(full_result)
    assert full_result == 1103
