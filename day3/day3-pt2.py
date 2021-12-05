def bin_to_dec(bin_num):
    return sum(
        [
            2 ** (len(bin_num) - i - 1) if bin_num[i] == "1" else 0
            for i in range(0, len(bin_num))
        ]
    )


def main():
    nums = []

    with open("day3-full.txt") as input_file:
        for line in input_file:
            nums.append(line.strip())

    num_bits = len(nums[0])

    o2_rating_candidates, co2_rating_candidates = nums, nums.copy()
    stop = False
    i = 0

    while i < num_bits and not stop:
        total_nums = len(o2_rating_candidates)
        bit_pos_sum = sum(int(bit[i]) for bit in o2_rating_candidates)
        if bit_pos_sum >= total_nums / 2:
            print(f"We have more 1s, all should have 1 in the {i} position")
            o2_rating_candidates = [c for c in o2_rating_candidates if c[i] == "1"]
        else:
            print(f"We have more 0s, all should have 0 in the {i} position")
            o2_rating_candidates = [c for c in o2_rating_candidates if c[i] == "0"]

        if len(o2_rating_candidates) == 1:
            stop = True
        i += 1

    print(o2_rating_candidates)
    print(bin_to_dec(o2_rating_candidates[0]))

    stop = False
    i = 0

    while i < num_bits and not stop:
        total_nums = len(co2_rating_candidates)
        bit_pos_sum = sum(int(bit[i]) for bit in co2_rating_candidates)
        if bit_pos_sum >= total_nums / 2:
            print(f"We have more 1s, all should have 0 in the {i} position")
            co2_rating_candidates = [c for c in co2_rating_candidates if c[i] == "0"]
        else:
            print(f"We have more 0s, all should have 1 in the {i} position")
            co2_rating_candidates = [c for c in co2_rating_candidates if c[i] == "1"]

        if len(co2_rating_candidates) == 1:
            stop = True
        i += 1

    print(co2_rating_candidates)
    print(bin_to_dec(co2_rating_candidates[0]))


if __name__ == "__main__":
    main()
