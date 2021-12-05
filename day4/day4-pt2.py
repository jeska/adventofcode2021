def main():
    board_rows = []
    with open("day4-full.txt") as input_file:
        call_numbers = [int(i) for i in input_file.readline().split(",")]
        for line in input_file:
            if len(line.strip()) > 0:
                board_rows.append([int(i) for i in line.strip().split()])

    num_boards = len(board_rows) // 5

    overall_win_cases = {}
    for i in range(num_boards):
        start, end = i * 5, i * 5 + 5
        board = board_rows[start:end]

        win_cases = []
        for row in board:
            win_cases.append(max([call_numbers.index(i) for i in row]))

        for col in range(0, 5):
            win_cases.append(max([call_numbers.index(row[col]) for row in board]))

        overall_win_cases[min(win_cases)] = [col for row in board for col in row]

    winner = max(overall_win_cases.keys())
    winning_board = overall_win_cases[winner]
    unmarked_numbers = [i for i in call_numbers[winner + 1 :] if i in winning_board]
    print(sum(unmarked_numbers) * call_numbers[winner])


if __name__ == "__main__":
    main()
