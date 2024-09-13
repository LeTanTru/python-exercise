import pygame
import sys

# Khai báo màu sắc
WHITE = (211, 214, 219)
BLACK = (239, 242, 250)
CIRCLE = (5, 124, 250)
CROSS = (239, 5, 140)
RESET = (0, 0, 0)
BLUE = (0, 0, 255)  # Định nghĩa màu xanh dương
# Kích thước của mỗi ô và kích thước bàn cờ
CELL_SIZE = 50
BOARD_SIZE = 10  # Kích thước bàn cờ nxn

EMPTY = None
# Biến lưu trạng thái của bàn cờ
board_state = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


# Hàm vẽ bàn cờ
def draw_board(screen):
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)


# Hàm vẽ các ký tự 'X' và 'O' lên bàn cờ
def draw_symbols(screen):
    font = pygame.font.SysFont(None, 40)
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board_state[x][y] == 'X':
                text_surface = font.render('X', True, CROSS)
                text_rect = text_surface.get_rect(center=(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text_surface, text_rect)
            elif board_state[x][y] == 'O':
                text_surface = font.render('O', True, CIRCLE)
                text_rect = text_surface.get_rect(center=(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text_surface, text_rect)


# Hàm kiểm tra chiến thắng
def check_win(symbol):
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board_state[x][y] == symbol:
                # Kiểm tra hàng ngang
                if y <= BOARD_SIZE - 5:
                    if all(board_state[x][y + i] == symbol for i in range(5)):
                        return True, [(x, y + i) for i in range(5)]
                # Kiểm tra hàng dọc
                if x <= BOARD_SIZE - 5:
                    if all(board_state[x + i][y] == symbol for i in range(5)):
                        return True, [(x + i, y) for i in range(5)]
                # Kiểm tra đường chéo chính (\)
                if x <= BOARD_SIZE - 5 and y <= BOARD_SIZE - 5:
                    if all(board_state[x + i][y + i] == symbol for i in range(5)):
                        return True, [(x + i, y + i) for i in range(5)]
                # Kiểm tra đường chéo phụ (/)
                if x <= BOARD_SIZE - 5 and y >= 4:
                    if all(board_state[x + i][y - i] == symbol for i in range(5)):
                        return True, [(x + i, y - i) for i in range(5)]
    return False, []


# Hàm hiển thị cửa sổ thông báo
def show_message(screen, message):
    font = pygame.font.SysFont(None, 30)
    text_surface = font.render(message, True, RESET)
    text_rect = text_surface.get_rect(center=(BOARD_SIZE * CELL_SIZE // 2, BOARD_SIZE * CELL_SIZE // 2))
    screen.blit(text_surface, text_rect)


# Hàm vẽ đường thắng
def draw_win_line(screen, start_pos, end_pos):
    pygame.draw.line(screen, CROSS, (start_pos[0] * CELL_SIZE + CELL_SIZE // 2, start_pos[1] * CELL_SIZE + CELL_SIZE // 2), (end_pos[0] * CELL_SIZE + CELL_SIZE // 2, end_pos[1] * CELL_SIZE + CELL_SIZE // 2), 3)


# Hàm chính
def main():
    pygame.init()
    screen = pygame.display.set_mode((BOARD_SIZE * CELL_SIZE, BOARD_SIZE * CELL_SIZE))
    pygame.display.set_caption('Caro Game')

    clock = pygame.time.Clock()

    current_symbol = 'X'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x //= CELL_SIZE
                y //= CELL_SIZE
                if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board_state[x][y] == EMPTY:
                    board_state[x][y] = current_symbol
                    win, win_line = check_win(current_symbol)
                    draw_symbols(screen)
                    if win:
                        show_message(screen, f'{current_symbol} wins! Press Y to play again, or N to exit.')
                        start_pos, end_pos = win_line[0], win_line[-1]
                        draw_win_line(screen, start_pos, end_pos)
                        pygame.display.flip()
                        while True:
                            event = pygame.event.wait()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    board_state.clear()
                                    board_state.extend([[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)])
                                    break
                                elif event.key == pygame.K_n:
                                    pygame.quit()
                                    sys.exit()
                    if current_symbol == 'X':
                        current_symbol = 'O'
                    else:
                        current_symbol = 'X'

        screen.fill(BLACK)
        draw_board(screen)
        draw_symbols(screen)
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
