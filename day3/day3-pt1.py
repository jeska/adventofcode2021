from dataclasses import dataclass


def bin_to_dec(bin_num):
    return sum(
        [
            2 ** (len(bin_num) - i - 1) if bin_num[i] == "1" else 0
            for i in range(0, len(bin_num))
        ]
    )


@dataclass
class Bit:
    zeros: int = 0
    ones: int = 0

    def most_common(self):
        return 0 if self.zeros > self.ones else 1

    def least_common(self):
        return 0 if self.zeros < self.ones else 1


def main():
    bits = []

    with open("day3-full.txt") as input_file:
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

    print(gamma, bin_to_dec(gamma))
    print(epsilon, bin_to_dec(epsilon))

    print(bin_to_dec(gamma) * bin_to_dec(epsilon))


if __name__ == "__main__":
    main()
