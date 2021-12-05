def main(inf: str):
    hor, depth, aim = 0, 0, 0

    with open(inf) as input_file:
        for line in input_file:
            cmd, units = line.split()[0], int(line.split()[1])
            match cmd:
                case "forward":
                    hor += units
                    depth += aim * units
                case "down":
                    aim += units
                case "up":
                    aim -= units

    return hor * depth


if __name__ == "__main__":
    sample_result = main("day2-sample.txt")
    print(sample_result)
    assert sample_result == 900
    full_result = main("day2-full.txt")
    print(full_result)
    assert full_result == 1975421260
