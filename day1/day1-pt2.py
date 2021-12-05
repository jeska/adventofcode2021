def main():

    increases = 0
    report = []
    with open("day1-full.txt", "r") as input_file:
        for line in input_file.readlines():
            report.append(int(line))
    prev_sum = report[0] + report[1] + report[2]
    for i in range(3, len(report)):
        print(i)
        current_sum = report[i - 2] + report[i - 1] + report[i]
        print(f"{prev_sum} | {current_sum} | {1 if current_sum > prev_sum else 0}")
        increases += 1 if current_sum > prev_sum else 0
        prev_sum = current_sum

    print(increases)


if __name__ == "__main__":
    main()
