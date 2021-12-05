def main(inf: str):
    horizontal, vertical = 0, 0

    with open(inf) as input_file:
        for line in input_file:
            cmd, units = line.split()[0], int(line.split()[1])
            match cmd:
                case "forward":
                    horizontal += units
                case "down":
                    vertical += units
                case "up":
                    vertical -= units

    return horizontal * vertical


if __name__ == "__main__":
    sample_result = main("day2-sample.txt")
    print(sample_result)
    assert sample_result == 150
    full_result = main("day2-full.txt")
    print(full_result)
    assert full_result == 1990000
