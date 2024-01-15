import pygame, sys
import numpy as np

# initializes pygame
pygame.init()

# CONSTANTS
WID = 600
HEIGHT = 600
LIN_WID = 15
WN_LIN_WID = 15
BRD_ROW = 3
BRD_COL = 3
SQR_SIZ = 200
CIRCLE_RADIUS = 60
CIRCL_WID = 15
CROS_WID = 25
SPACE = 55
# rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# SCREEN
screen = pygame.display.set_mode((WID, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

# CONSOLE BOARD
board = np.zeros((BRD_ROW, BRD_COL))


# FUNCTIONS

def draw_lines():
    # horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQR_SIZ), (WID, SQR_SIZ), LIN_WID)
    # horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQR_SIZ), (WID, 2 * SQR_SIZ), LIN_WID)

    # vertical
    pygame.draw.line(screen, LINE_COLOR, (SQR_SIZ, 0), (SQR_SIZ, HEIGHT), LIN_WID)
    # vertical
    pygame.draw.line(screen, LINE_COLOR, (2 * SQR_SIZ, 0), (2 * SQR_SIZ, HEIGHT), LIN_WID)


def draw_figures():
    for row in range(BRD_ROW):
        for col in range(BRD_COL):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (int(col * SQR_SIZ + SQR_SIZ // 2), int(row * SQR_SIZ + SQR_SIZ // 2)),
                                   CIRCLE_RADIUS, CIRCL_WID)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQR_SIZ + SPACE, row * SQR_SIZ + SQR_SIZ - SPACE),
                                 (col * SQR_SIZ + SQR_SIZ - SPACE, row * SQR_SIZ + SPACE), CROS_WID)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQR_SIZ + SPACE, row * SQR_SIZ + SPACE),
                                 (col * SQR_SIZ + SQR_SIZ - SPACE, row * SQR_SIZ + SQR_SIZ - SPACE), CROS_WID)


def mark_square(row, col, plr):
    board[row][col] = plr


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BRD_ROW):
        for col in range(BRD_COL):
            if board[row][col] == 0:
                return False
    return True


def check_win(plr):
    # vertical win match check
    for col in range(BRD_COL):
        if board[0][col] == plr and board[1][col] == plr and board[2][col] == plr:
            draw_vertical_winning_line(col, plr)
            return True

    # horizontal win match check
    for row in range(BRD_ROW):
        if board[row][0] == plr and board[row][1] == plr and board[row][2] == plr:
            draw_horizontal_winning_line(row, plr)
            return True

    # ascending diagonal win check
    if board[2][0] == plr and board[1][1] == plr and board[0][2] == plr:
        draw_asc_diagonal(plr)
        return True

    # descending diagonal win check
    if board[0][0] == plr and board[1][1] == plr and board[2][2] == plr:
        draw_desc_diagonal(plr)
        return True

    return False


def draw_vertical_winning_line(col, plr):
    posX = col * SQR_SIZ + SQR_SIZ // 2

    if plr == 1:
        color = CIRCLE_COLOR
    elif plr == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), LIN_WID)


def draw_horizontal_winning_line(row, plr):
    posY = row * SQR_SIZ + SQR_SIZ // 2

    if plr == 1:
        color = CIRCLE_COLOR
    elif plr == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (WID - 15, posY), WN_LIN_WID)


def draw_asc_diagonal(plr):
    if plr == 1:
        color = CIRCLE_COLOR
    elif plr == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WID - 15, 15), WN_LIN_WID)


def draw_desc_diagonal(plr):
    if plr == 1:
        color = CIRCLE_COLOR
    elif plr == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15), (WID - 15, HEIGHT - 15), WN_LIN_WID)


def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BRD_ROW):
        for col in range(BRD_COL):
            board[row][col] = 0

    draw_lines()


# VARIABLES
plr = 1
game_over = False

# MAINLOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // SQR_SIZ)
            clicked_col = int(mouseX // SQR_SIZ)  # Fixed typo: SQR_SIZE to SQR_SIZ

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, plr)
                if check_win(plr):
                    game_over = True
                plr = plr % 2 + 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                plr = 1
                game_over = False

    pygame.display.update()
