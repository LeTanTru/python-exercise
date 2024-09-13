def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def check_winner(board, player):
    rows, cols = len(board), len(board[0])

    def check_line(line):
        for i in range(len(line) - 5 + 1):
            if all(line[i + j] == player for j in range(5)):
                return True
        return False

    for i in range(rows):
        if check_line(board[i]):
            return True

    for j in range(cols):
        if check_line([board[i][j] for i in range(rows)]):
            return True

    for i in range(rows - 5 + 1):
        for j in range(cols - 5 + 1):
            if check_line([board[i + k][j + k] for k in range(5)]):
                return True

    for i in range(rows - 5 + 1):
        for j in range(5 - 1, cols):
            if check_line([board[i + k][j - k] for k in range(5)]):
                return True

    return False


def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)


n = int(input("Nhập kích thước bàn cơ: "))
board = [[" " for _ in range(n)] for _ in range(n)]
current_player = "X"

while True:
    print_board(board)
    row = int(input(f"Người chơi {current_player}, Nhập hàng muốn đánh: "))
    col = int(input(f"Người chơi {current_player}, Nhập cột muốn đánh: "))

    if board[row][col] == " ":
        board[row][col] = current_player
    else:
        print("Ô này đã được đánh. Hãy đánh ô khác")
        continue

    if check_winner(board, current_player):
        print_board(board)
        print(f"Người chơi {current_player} chiến thắng")
        break

    if is_board_full(board):
        print_board(board)
        print("Đã hết ô cờ")
        break

    current_player = "O" if current_player == "X" else "X"
