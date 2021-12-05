def main():

    increases = 0
    with open("day1-sample.txt", "r") as input_file:
        prev_m = int(input_file.readline())
        for line in input_file.readlines():
            current_m = int(line)
            increases += 1 if current_m > prev_m else 0
            prev_m = current_m

    print(increases)


if __name__ == "__main__":
    main()
