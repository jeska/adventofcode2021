##   abcdefg
# 0: abc efg
# 1:   c  f
# 2: a cde g
# 3: a cd fg
# 4:  bcd f
# 5: ab d fg
# 6: ab defg
# 7: a c  f
# 8: abcdefg
# 9: abcd fg

from collections import defaultdict


def main(inf: str):
    output_lengths = defaultdict(int)
    with open(inf) as input_file:
        for line in input_file:
            for digit in line.split()[-4:]:
                if len(digit) in [2, 3, 4, 7]:
                    output_lengths[len(digit)] += 1

    return sum([v for v in output_lengths.values()])


if __name__ == "__main__":
    sample_result = main("day8-sample.txt")
    print(sample_result)
    assert sample_result == 26
    full_result = main("day8-full.txt")
    print(full_result)
    assert full_result == 301
