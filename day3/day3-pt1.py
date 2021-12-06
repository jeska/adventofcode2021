from dataclasses import dataclass


def bin_to_dec(bin_num: str) -> int:
    match bin_num:
        case ["0"]:
            return 0
        case ["1"]:
            return 1
        case [x, *y] as b:
            return 2 ** (len(b) - 1) * int(x) + bin_to_dec(y)


@dataclass
class Bit:
    zeros: int = 0
    ones: int = 0

    def most_common(self):
        return 0 if self.zeros > self.ones else 1

    def least_common(self):
        return 0 if self.zeros < self.ones else 1


def main(inf: str):
    bits = []

    with open(inf) as input_file:
        for line in input_file:
            for i in range(0, len(line) - 1):
                try:
                    current_bit = bits[i]
                except IndexError:
                    current_bit = Bit()
                    bits.append(current_bit)
                finally:
                    if line[i] == "0":
                        current_bit.zeros += 1
                    else:
                        current_bit.ones += 1

    gamma = [str(bit.most_common()) for bit in bits]
    epsilon = [str(bit.least_common()) for bit in bits]

    return bin_to_dec(gamma) * bin_to_dec(epsilon)


if __name__ == "__main__":
    sample_result = main("day3-sample.txt")
    print(sample_result)
    assert sample_result == 198
    full_result = main("day3-full.txt")
    print(full_result)
    assert full_result == 3923414
