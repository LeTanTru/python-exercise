# import pygame
# import sys

# # Khai báo màu sắc
# WHITE = (211, 214, 219)
# BLACK = (239, 242, 250)
# CIRCLE = (5, 124, 250)
# CROSS = (239, 5, 140)
# BLUE = (0, 0, 255)  # Định nghĩa màu xanh dương
# # Kích thước của mỗi ô và kích thước bàn cờ
# CELL_SIZE = 50
# BOARD_SIZE = 10  # Kích thước bàn cờ nxn

# # Biến lưu trạng thái của bàn cờ
# board_state = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


# # Hàm vẽ bàn cờ
# def draw_board(screen):
#     for x in range(BOARD_SIZE):
#         for y in range(BOARD_SIZE):
#             rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
#             pygame.draw.rect(screen, WHITE, rect, 1)


# # Hàm vẽ các ký tự 'X' và 'O' lên bàn cờ
# def draw_symbols(screen):
#     font = pygame.font.SysFont(None, 40)
#     for x in range(BOARD_SIZE):
#         for y in range(BOARD_SIZE):
#             if board_state[x][y] == 'X':
#                 text_surface = font.render('X', True, CROSS)
#                 text_rect = text_surface.get_rect(center=(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2))
#                 screen.blit(text_surface, text_rect)
#             elif board_state[x][y] == 'O':
#                 text_surface = font.render('O', True, CIRCLE)
#                 text_rect = text_surface.get_rect(center=(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2))
#                 screen.blit(text_surface, text_rect)


# # Hàm kiểm tra chiến thắng
# def check_win(symbol):
#     for x in range(BOARD_SIZE):
#         for y in range(BOARD_SIZE):
#             if board_state[x][y] == symbol:
#                 # Kiểm tra hàng ngang
#                 if y <= BOARD_SIZE - 5:
#                     if all(board_state[x][y + i] == symbol for i in range(5)):
#                         return True, [(x, y + i) for i in range(5)]
#                 # Kiểm tra hàng dọc
#                 if x <= BOARD_SIZE - 5:
#                     if all(board_state[x + i][y] == symbol for i in range(5)):
#                         return True, [(x + i, y) for i in range(5)]
#                 # Kiểm tra đường chéo chính (\)
#                 if x <= BOARD_SIZE - 5 and y <= BOARD_SIZE - 5:
#                     if all(board_state[x + i][y + i] == symbol for i in range(5)):
#                         return True, [(x + i, y + i) for i in range(5)]
#                 # Kiểm tra đường chéo phụ (/)
#                 if x <= BOARD_SIZE - 5 and y >= 4:
#                     if all(board_state[x + i][y - i] == symbol for i in range(5)):
#                         return True, [(x + i, y - i) for i in range(5)]
#     return False, []


# # Hàm hiển thị cửa sổ thông báo
# def show_message(screen, message):
#     font = pygame.font.SysFont(None, 30)
#     text_surface = font.render(message, True, CROSS)
#     text_rect = text_surface.get_rect(center=(BOARD_SIZE * CELL_SIZE // 2, BOARD_SIZE * CELL_SIZE // 2))
#     screen.blit(text_surface, text_rect)


# # Hàm vẽ đường thắng
# def draw_win_line(screen, start_pos, end_pos):
#     pygame.draw.line(screen, CROSS, (start_pos[0] * CELL_SIZE + CELL_SIZE // 2, start_pos[1] * CELL_SIZE + CELL_SIZE // 2), (end_pos[0] * CELL_SIZE + CELL_SIZE // 2, end_pos[1] * CELL_SIZE + CELL_SIZE // 2), 5)


# # Hàm chính
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((BOARD_SIZE * CELL_SIZE, BOARD_SIZE * CELL_SIZE))
#     pygame.display.set_caption('Caro Game')

#     clock = pygame.time.Clock()

#     current_symbol = 'X'

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = pygame.mouse.get_pos()
#                 x //= CELL_SIZE
#                 y //= CELL_SIZE
#                 if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board_state[x][y] == ' ':
#                     board_state[x][y] = current_symbol
#                     win, win_line = check_win(current_symbol)
#                     print(win_line)
#                     if win:
#                         show_message(screen, f'{current_symbol} wins! Press Y to play again, or N to exit.')
#                         start_pos, end_pos = win_line[0], win_line[-1]
#                         draw_win_line(screen, start_pos, end_pos)
#                         pygame.display.flip()
#                         while True:
#                             event = pygame.event.wait()
#                             if event.type == pygame.KEYDOWN:
#                                 if event.key == pygame.K_y:
#                                     board_state.clear()
#                                     board_state.extend([[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)])
#                                     break
#                                 elif event.key == pygame.K_n:
#                                     pygame.quit()
#                                     sys.exit()
#                     if current_symbol == 'X':
#                         current_symbol = 'O'
#                     else:
#                         current_symbol = 'X'

#         screen.fill(BLACK)
#         draw_board(screen)
#         draw_symbols(screen)
#         pygame.display.flip()
#         clock.tick(30)


# if __name__ == '__main__':
#     main()

import tkinter
import random
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
from functools import partial 

# true: player, false: computer

def isWin(b, mark):
    if ((b[0][0] == mark and b[0][1] == mark and b[0][2] == mark) or
        (b[1][0] == mark and b[1][1] == mark and b[1][2] == mark) or
        (b[2][0] == mark and b[2][1] == mark and b[2][2] == mark) or
        (b[0][0] == mark and b[1][0] == mark and b[2][0] == mark) or
        (b[0][1] == mark and b[1][1] == mark and b[2][1] == mark) or
        (b[0][2] == mark and b[1][2] == mark and b[2][2] == mark) or
        (b[0][0] == mark and b[1][1] == mark and b[2][2] == mark) or
        (b[0][2] == mark and b[1][1] == mark and b[2][0] == mark)):
        return True
    else: return False

def fullBoard():
    for i in board:
        if (i.count(" ") > 0):
            return False
    return True

def isPosAvailable(i, j):
    if board[i][j] == " ":
        return True
    return False

def minimax(board, depth, isMaximizing):
    if isWin(board, comp) == True and isMaximizing == False:
        return 10
    if isWin(board, player) == True and isMaximizing == True:
        return -10
    if fullBoard() == True:
        return 0

    if isMaximizing == True:
        bestScore = -100
        for i in range(3):
            for j in range(3):
                if isPosAvailable(i, j) == True:
                    board[i][j] = comp
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 100
        for i in range(3):
            for j in range(3):
                if isPosAvailable(i, j) == True:
                    board[i][j] = player
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    bestScore = min(score, bestScore)
        return bestScore

def bestMove():
    bestScore = -100

    hasMove = False
    for i in range(3):
        for j in range(3):
            if isPosAvailable(i, j) == True:
                board[i][j] = comp
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > bestScore:
                    bestScore = score
                    move = [i, j]
                    hasMove = True

    if hasMove == True: 
        board[move[0]][move[1]] = comp
        button[move[0]][move[1]].config(text = comp)
   
def inactivateButton():
    for i in range(3):
        for j in range(3):
            board[i][j] = '-'

def showNoti(gb):
    if isWin(board, player):
        box = messagebox.askquestion("Winner", "Player won the match. Do you want to play again?")
        inactivateButton()
        if (box == "yes"):
            gb.destroy()
            menuGame()
        else:
            gb.destroy()
    elif isWin(board, comp):
        box = messagebox.askquestion("Winner", "Computer won the match. Do you want to play again?")
        inactivateButton()
        if (box == "yes"):
            gb.destroy()
            menuGame()
        else:
            gb.destroy()
    elif(fullBoard()):
        box = messagebox.askquestion("Tie Game", "Tie Game. Do you want to play again?")
        inactivateButton()
        if (box == "yes"):
            gb.destroy()
            menuGame()
        else:
            gb.destroy()

def getMove(i, j, gb, turnPlayer):
    if board[i][j] == " ":
        if turnPlayer == True:
            board[i][j] = player
        button[i][j].config(text = board[i][j])
        showNoti(gb)
        if not fullBoard():
            turnPlayer = not turnPlayer

    if turnPlayer == False:
        bestMove()
        turnPlayer = not turnPlayer
        showNoti(gb)

def firstMoveComp():
    temp1 = random.randint(0, 2)
    temp2 = random.randint(0, 2)
    board[temp1][temp2] = comp
    return [temp1, temp2]

def gameBoard_playerFirst():
    global button
    button = [4]
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(getMove, i, j, boardGame, turnPlayer)
            
            button[i][j] = Button(boardGame, height = 5, width = 11, command = get_t)
            button[i][j].grid(row = m, column = n)
    boardGame.mainloop()

def gameBoard_compFirst():
    global button
    button = [4]
    firstMove = firstMoveComp()
    turnPlayer = False

    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j) 
            button[i][j] = Button(boardGame, height = 5, width = 11)
            button[i][j].grid(row = m, column = n)
            if firstMove[0] == i and firstMove[1] == j:
                button[i][j].config(text = comp)
                turnPlayer = not turnPlayer
                break;
            
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = [4]
        for j in range(3):
            if firstMove[0] == i and firstMove[1] == j:
                continue
            else:
                n = j
                button[i].append(j)
                get_t = partial(getMove, i, j, boardGame, turnPlayer)  
               
                button[i][j] = Button(boardGame, height = 5, width = 11, command = get_t)
                button[i][j].grid(row = m, column = n)
            
    boardGame.mainloop()

def playerFirst():
    turn.destroy()
    global boardGame, turnPlayer, comp, player
    boardGame = Tk()
    boardGame.geometry("260x300")
    boardGame.resizable(width=False, height=False)
    boardGame.title("Tic Tac Toe Game")

    turnPlayer = True
    player = "X"
    player1 = Label(boardGame, text = "Player: X")
    player1.grid(row = 1, column = 1)
    comp = "O"
    player2 = Label(boardGame, text = "Computer: O")
    player2.grid(row = 2, column = 1)
    gameBoard_playerFirst()

def computerFirst():
    turn.destroy()
    global boardGame, turnPlayer, comp, player
    boardGame = Tk()
    boardGame.geometry("260x300")
    boardGame.resizable(width=False, height=False)
    boardGame.title("Tic Tac Toe Game")

    turnPlayer = False
    comp = "X"
    player1 = Label(boardGame, text = "Computer: X")
    player1.grid(row = 1, column = 1)
    player = "O"
    player2 = Label(boardGame, text = "Player: O")
    player2.grid(row = 2, column = 1)
    gameBoard_compFirst()

def chooseTurn():
    menu.destroy()
    global turn
    turn = Tk()
    turn.geometry("220x178")
    turn.resizable(width=False, height=False)
    turn.title("Choice")

    head = Label(turn, text = "Please choose turn: ",
                 bg = "deepskyblue1", fg = "black",
                 width = 500, height = 4, font = ('Century Gothic', 15, BOLD))

    button1 = Button(turn, text = "Player first", command = playerFirst,
                     activeforeground = 'red', activebackground = "cadetblue1", 
                     bg = "cadetblue1", fg = "black", width = 500, font = 'summer')

    button2 = Button(turn, text = "Computer first", command = computerFirst,
                     activeforeground = 'red', activebackground = "cadetblue1", 
                     bg = "cadetblue1", fg = "black", width = 500, font = 'summer')

    head.pack(side = 'top')
    button1.pack(side = 'top')
    button2.pack(side = 'top')

def exit():
    menu.destroy()

def menuGame():
    global menu, board
    menu = Tk()
    menu.geometry("300x210")
    menu.resizable(width=False, height=False)
    menu.title("Tic Tac Toe Game")
    board = [[" "," "," "], [" "," "," "], [" "," "," "]]
    
    head = Label(menu, text = "Welcome to tic-tac-toe game",
                 bg = "deepskyblue1", fg = "black",
                 width = 500, height = 4, font = ('Century Gothic', 15, BOLD))
    
    button1 = Button(menu, text = "Start Game", command = chooseTurn,
                     activeforeground = 'red', activebackground = "cadetblue1",
                     bg = "cadetblue1", fg = "black", width = 500, font = 'summer')

    button2 = Button(menu, text = "Exit", command = exit,
                     activeforeground = 'red', activebackground = "cadetblue1", 
                     bg = "cadetblue1", fg = "black", width = 500, font = 'summer')

    end = Label(menu, text = "Design by Pham Hien Doan Trang",
                fg = "mediumpurple2", 
                width = 50, height = 3, font = ('Century Gothic', 10, BOLD))
    
    head.pack(side = 'top')
    button1.pack(side = 'top')
    button2.pack(side = 'top')
    end.pack(side = "top")
    
    menu.mainloop()
  
# Call main function
if __name__ == '__main__':
    menuGame()
