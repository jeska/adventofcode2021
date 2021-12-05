def main():
    hor, depth, aim = 0, 0, 0

    with open("day2-full.txt") as input_file:
        for line in input_file:
            cmd, units = line.split()[0], int(line.split()[1])
            if cmd == "forward":
                hor += units
                depth += aim * units
            elif cmd == "down":
                aim += units
            elif cmd == "up":
                aim -= units

    print(hor, depth, aim)
    print(hor * depth)


if __name__ == "__main__":
    main()
