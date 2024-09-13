"""
Đánh giá:
Lê Tấn Trụ (nhóm trưởng) - triển khai chương trình - 10/10
Nguyễn Hồng Phúc - xác định thuật toán kiểm tra điều kiện thắng của người chơi - 10/10
Võ Thị Thu Tâm - xác định các bước và các hàm để triển khai bài toán - 10/10
"""


def create_board(n):
    board = [["_" for _ in range(n)] for _ in range(n)]
    return board


def show_board(board):
    n = len(board)

    print("    ", end="")
    for i in range(1, n + 1):
        print(f"{i}", end=" ")
    print(" ")

    for i, row in enumerate(board):
        print(f"{i + 1:2}|", end=" ")
        for x in row:
            print(x, end=" ")
        print()


def check_win(board, player):
    n = len(board)

    # Kiểm tra hàng và cột
    for i in range(n):
        for j in range(n - 4):  # Nếu còn ít hơn 5 ô, không thể thắng
            if all(board[i][j + k] == player for k in range(5)):
                return True  # Thắng theo hàng

            if all(board[j + k][i] == player for k in range(5)):
                return True  # Thắng theo cột

    # Kiểm tra đường chéo chính
    for i in range(n - 4):
        for j in range(n - 4):
            if all(board[i + k][j + k] == player for k in range(5)):
                return True  # Thắng theo đường chéo chính

    # Kiểm tra đường chéo phụ
    for i in range(n - 4):
        for j in range(4, n):
            if all(board[i + k][j - k] == player for k in range(5)):
                return True  # Thắng theo đường chéo phụ

    return False


def player_move(board, player, size):
    while True:
        try:
            row = int(input(f"Người chơi {player}, nhập dòng: ")) - 1
            col = int(input(f"Người chơi {player}, nhập cột: ")) - 1

            if 0 <= row < size and 0 <= col < size and board[row][col] == "_":
                return row, col
            else:
                print("Ô đã được đánh hoặc vượt quá giới hạn, vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng nhập một một số nguyên.")


def main():
    size = int(input("Nhập kích thước bàn cờ: "))

    board = create_board(size)
    players = ["X", "O"]
    current_player = players[0]

    while True:
        show_board(board)

        # Lượt của người chơi
        player_row, player_col = player_move(board, current_player, size)
        board[player_row][player_col] = current_player

        # Kiểm tra điều kiện thắng của người chơi
        if check_win(board, current_player):
            show_board(board)
            print(f"Chúc mừng! Người chơi {current_player} thắng!")
            break

        # Chuyển lượt sang người chơi tiếp theo
        current_player = players[1] if current_player == players[0] else players[0]


if __name__ == "__main__":
    main()
