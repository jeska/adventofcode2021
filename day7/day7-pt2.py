def main(inf: str):
    with open(inf) as input_file:
        crab_positions = [int(i) for i in input_file.readline().split(",")]

    unique_positions = [p for p in range(0, max(crab_positions) + 1)]
    fuel_usage = {}

    for pos in unique_positions:
        # for i in crab_positions:
        # print(pos, i, abs(i - pos), sum(j for j in range(1, abs(i - pos) + 1)))
        fuel_usage[pos] = sum(
            [(abs(i - pos) / 2) * (abs(i - pos) + 1) for i in crab_positions]
        )

    return min(fuel_usage.values())


if __name__ == "__main__":
    sample_result = main("day7-sample.txt")
    print(sample_result)
    assert sample_result == 168
    full_result = main("day7-full.txt")
    print(full_result)
    # assert full_result == 356922
