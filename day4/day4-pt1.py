def main():
    board_rows = []
    with open("day4-full.txt") as input_file:
        call_numbers = [int(i) for i in input_file.readline().split(",")]
        print("\t".join([str(i) for i in range(0, len(call_numbers))]))
        print("\t".join([str(i) for i in call_numbers]))

        for line in input_file:
            if len(line.strip()) > 0:
                board_rows.append([int(i) for i in line.strip().split()])

    num_boards = len(board_rows) // 5

    overall_win_cases = {}
    for i in range(num_boards):
        board = board_rows[i * 5 : i * 5 + 5]

        win_cases = []
        for row in board:
            win_cases.append(max([call_numbers.index(i) for i in row]))

        for col in range(0, 5):
            win_cases.append(max([call_numbers.index(row[col]) for row in board]))

        overall_win_cases[min(win_cases)] = [col for row in board for col in row]

    winner = min(overall_win_cases.keys())
    print(winner)
    winning_board = overall_win_cases[winner]
    unmarked_numbers = [i for i in call_numbers[winner + 1 :] if i in winning_board]
    print(unmarked_numbers)
    print(sum(unmarked_numbers))
    print(call_numbers[winner])
    print(sum(unmarked_numbers) * call_numbers[winner])


if __name__ == "__main__":
    main()
