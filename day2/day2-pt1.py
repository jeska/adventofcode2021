def main():
    hor, vert = 0, 0

    with open("day2-full.txt") as input_file:
        for line in input_file:
            cmd, units = line.split()[0], int(line.split()[1])
            if cmd == "forward":
                hor += units
            elif cmd == "down":
                vert += units
            elif cmd == "up":
                vert -= units

    print(hor, vert)
    print(hor * vert)


if __name__ == "__main__":
    main()
