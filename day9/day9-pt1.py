def main(inf: str):
    height_map: list[list[int]] = []
    with open(inf) as input_file:
        for line in input_file:
            height_map.append([int(i) for i in line.strip()])

    local_mins = []
    for r_idx, row in enumerate(height_map):
        for c_idx, col in enumerate(row):
            top = height_map[r_idx - 1][c_idx] if r_idx > 0 else 99
            bottom = height_map[r_idx + 1][c_idx] if r_idx < len(height_map) - 1 else 99
            left = height_map[r_idx][c_idx - 1] if c_idx > 0 else 99
            right = height_map[r_idx][c_idx + 1] if c_idx < len(row) - 1 else 99
            if all([col < h for h in [top, bottom, left, right]]):
                local_mins.append(col)

    print(local_mins)

    return sum(local_mins) + len(local_mins)


if __name__ == "__main__":
    sample_result = main("day9-sample.txt")
    print(sample_result)
    assert sample_result == 15
    full_result = main("day9-full.txt")
    print(full_result)
    assert full_result == 478
