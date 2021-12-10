# I am not happy & you need refactoring!!

from collections import defaultdict
from enum import Enum

class Digits(Enum):
    zero_digit = [0, 1, 2, 4, 5, 6]
    one_digit = [2, 5]
    two_digit = [0, 2, 3, 4, 6]
    three_digit = [0, 2, 3, 5, 6]
    four_digit = [1, 2, 3, 5]
    five_digit = [0, 1, 3, 5, 6]
    six_digit = [0, 1, 3, 4, 5, 6]
    seven_digit = [0, 2, 5]
    eight_digit = [0, 1, 2, 3, 4, 5, 6]
    nine_digit = [0, 1, 2, 3, 5, 6]

def pow_ten(i: int):
    return 10 ** (4 - i - 1)

def main(inf: str):
    segments = {num: letr for (num, letr) in enumerate("abcdefg")}
    sum = 0
    with open(inf) as input_file:
        for line in input_file:
            new_segments = defaultdict(str)
            
            all_digits = line.strip().split()
            signals = all_digits[:10]
            outputs = all_digits[-4:]

            wire_mapping = defaultdict(list)
            for signal in signals:
                wire_mapping[len(signal)].append(signal)

            # Segment 0 (top line "a") is the 7 signals minus the 1 signals
            new_segments[0] = [i for i in wire_mapping[3][0] if i not in wire_mapping[2][0]][0]
            # 2, 3, and 5 all have 5 signals
            # The top is the same, and there is overlap with the 4. Thus...
            bottom_left = []
            for signal in sorted(wire_mapping[5], key=len):
                x = [i for i in signal if i not in wire_mapping[4][0] and i != new_segments[0]]
                if len(x) == 1:  # if only 1 segment remains, it's the bottom
                    new_segments[6] = x[0]
                else:
                    bottom_left.append(x)
            
            new_segments[4] = [j for i in bottom_left for j in i if j != new_segments[6]][0]
            # we now know the top, bottom, and bottom left segments. We can now get top left.
            # Get the 0
            middle_candidates = []
            for signal in wire_mapping[6]:
                top_left = [
                    i
                    for i in signal
                    if i
                    not in [
                        new_segments[0][0],
                        new_segments[4][0],
                        new_segments[6][0],
                        wire_mapping[2][0][0],
                        wire_mapping[2][0][1],
                    ]
                ]
                # top right is the one with length 1
                if len(top_left) == 1:
                    new_segments[1] = top_left[0]
                else:
                    # otherwise the other one is the middle
                    middle_candidates = top_left
            new_segments[3] = [i for i in middle_candidates if i != new_segments[1]][0]

            # bottom right is the 6-length one with 1 leftover
            for signal in wire_mapping[6]:
                bottom_right = [i for i in signal if i not in new_segments.values()]
                # top right is the one with length 1
                if len(bottom_right) == 1:
                    new_segments[5] = bottom_right[0]
                    break

            # and only 1 remains
            new_segments[2] = [a for a in "abcdefg" if a not in new_segments.values()][0]

            local_sum = 0
            for i, output in enumerate(outputs):
                segments = [k for k, v in new_segments.items() if v in output]
                match sorted(segments):
                    case Digits.zero_digit.value:
                        local_sum += 0
                    case Digits.one_digit.value:
                        local_sum += pow_ten(i)
                    case Digits.two_digit.value:
                        local_sum += 2 * pow_ten(i)
                    case Digits.three_digit.value:
                        local_sum += 3 * pow_ten(i)
                    case Digits.four_digit.value:
                        local_sum += 4 * pow_ten(i)
                    case Digits.five_digit.value:
                        local_sum += 5 * pow_ten(i)
                    case Digits.six_digit.value:
                        local_sum += 6 * pow_ten(i)
                    case Digits.seven_digit.value:
                        local_sum += 7 * pow_ten(i)
                    case Digits.eight_digit.value:
                        local_sum += 8 * pow_ten(i)
                    case Digits.nine_digit.value:
                        local_sum += 9 * pow_ten(i)

            sum += local_sum
    return sum


if __name__ == "__main__":
    small_sample_result = main("day8-sample-small.txt")
    print(small_sample_result)
    assert small_sample_result == 5353
    sample_result = main("day8-sample.txt")
    print(sample_result)
    assert sample_result == 61229
    full_result = main("day8-full.txt")
    print(full_result)
    assert full_result == 908067
