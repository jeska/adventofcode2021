def main(inf: str):
    with open(inf) as input_file:
        crab_positions = [int(i) for i in input_file.readline().split(",")]

    unique_positions = set(crab_positions)
    fuel_usage = {}

    for pos in unique_positions:
        fuel_usage[pos] = sum([abs(i - pos) for i in crab_positions])

    return min(fuel_usage.values())


if __name__ == "__main__":
    sample_result = main("day7-sample.txt")
    print(sample_result)
    assert sample_result == 37
    full_result = main("day7-full.txt")
    print(full_result)
    assert full_result == 356922
