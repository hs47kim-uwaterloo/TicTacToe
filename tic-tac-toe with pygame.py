## Tic-Tac-Toe with pygame
import pygame
import time

pygame.init()


WIDTH = 660
HEIGHT = 660
OFFSET = 24
SQUARE_SIZE = 200
LINE_WIDTH = 6
# Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 153, 51)
LIGHT_ORANGE = (255, 204, 153)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
game_display.fill(ORANGE)
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

x_counter = 0
o_counter = 0
draw_counter = 0

def win(board, player):
    for a,b,c in zip(board[0], board[1], board[2]):
        if a == b == c == player: return True		    # vertical
    for i in range(3):
        if board[i].count(player) == 3: return True	    # horizontal

    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player: return True	# diagonals
    return False

def draw_environment(list_of_squares):
    pygame.draw.rect(game_display, ORANGE, (OFFSET, OFFSET, WIDTH-OFFSET*2, HEIGHT-OFFSET*2))
    for i in range(3):
        for j in range(3):
            box = pygame.draw.rect(game_display, LIGHT_ORANGE, (OFFSET+(SQUARE_SIZE+LINE_WIDTH)*i, OFFSET+(SQUARE_SIZE+LINE_WIDTH)*j, SQUARE_SIZE, SQUARE_SIZE))
            list_of_squares.append(box)
    pygame.display.update()

def end_screen(s, h, w, bground_col, fground_col):
    font = pygame.font.Font('freesansbold.ttf', 34)
    text = font.render(s, True, fground_col, bground_col)
    textRect = text.get_rect()
    textRect.center = (w // 2, h // 2)
    game_display.blit(text, textRect)
    pygame.display.update()


def main():
    global x_counter, o_counter, draw_counter

    list_of_squares = []
    b = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    draw_environment(list_of_squares)
    turn_count = 0
    p = ['X', 'O']

    while True:
        count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_screen(''.join(("X wins: ", str(x_counter), ", O wins: ", str(o_counter), ", Draws: ", str(draw_counter))), HEIGHT, WIDTH, WHITE, BLACK)
                time.sleep(1.8)
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for sq in list_of_squares:
                    if sq.collidepoint(pos):
                        if b[list_of_squares.index(sq)//3][list_of_squares.index(sq)%3] != 0: pass
                        elif turn_count%2 == 0:
                            pygame.draw.line(game_display, RED, (sq.center[0]-SQUARE_SIZE//3, sq.center[1]-SQUARE_SIZE//3), (sq.center[0]+SQUARE_SIZE//3, sq.center[1]+SQUARE_SIZE//3), LINE_WIDTH)
                            pygame.draw.line(game_display, RED, (sq.center[0]-SQUARE_SIZE//3, sq.center[1]+SQUARE_SIZE//3), (sq.center[0]+SQUARE_SIZE//3, sq.center[1]-SQUARE_SIZE//3), LINE_WIDTH)
                            b[list_of_squares.index(sq)//3][list_of_squares.index(sq)%3] = 'X'
                            turn_count += 1
                        else:
                            pygame.draw.circle(game_display, BLUE, sq.center, int(SQUARE_SIZE*0.45))
                            pygame.draw.circle(game_display, ORANGE, sq.center, int(SQUARE_SIZE*0.4))
                            b[list_of_squares.index(sq)//3][list_of_squares.index(sq)%3] = 'O'
                            turn_count += 1
                if win(b, p[turn_count%2-1]):
                    if p[turn_count%2-1] == "X":
                        end_screen('X won!', HEIGHT, WIDTH, WHITE, RED)
                        time.sleep(1)
                        x_counter += 1
                        main()
                    else:
                        end_screen('O won!', HEIGHT, WIDTH, WHITE, BLUE)
                        time.sleep(1)
                        o_counter += 1
                        main()
                else:
                    for i in range(3):
                        count += b[i].count('O')
                        count += b[i].count('X')
                    if count == 9:
                        end_screen('Draw!', HEIGHT, WIDTH, WHITE, BLACK)
                        time.sleep(1)
                        draw_counter += 1
                        main()

        pygame.display.update()




if __name__ == "__main__":
    main()