from collections import defaultdict


def main(inf: str, num_days: int):
    fishies = {}
    with open(inf) as input_file:
        initial_state = [int(i) for i in input_file.readline().split(",")]
        fishies = {f: initial_state.count(f) for f in set(initial_state)}

    for i in range(0, num_days):
        new_fishies = defaultdict(int)
        for timer, num_fish in fishies.items():
            new_fishies[timer - 1] += num_fish
            if -1 in new_fishies.keys():
                spawns = new_fishies.pop(-1)
                new_fishies[6] += spawns
                new_fishies[8] += spawns
            fishies = new_fishies

    return sum([v for _, v in fishies.items()])


if __name__ == "__main__":
    sample_result_1 = main("day6-sample.txt", 18)
    print(sample_result_1)
    assert sample_result_1 == 26
    sample_result_2 = main("day6-sample.txt", 80)
    print(sample_result_2)
    assert sample_result_2 == 5934
    full_result = main("day6-full.txt", 80)
    print(full_result)
    assert full_result == 374994
    sample_result_2 = main("day6-sample.txt", 256)
    print(sample_result_2)
    assert sample_result_2 == 26984457539
    sample_result_2 = main("day6-full.txt", 256)
    print(sample_result_2)
    assert sample_result_2 == 1686252324092
