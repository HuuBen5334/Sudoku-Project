import string

from pygame.examples.moveit import GameObject
from pygame.examples.playmus import Window

from sudoku_generator import *
import pygame, sys

def draw_button(screen, rect, text, is_hovered, button_font, button_color, button_hover_color, button_text_color):
    color = button_hover_color if is_hovered else button_color
    pygame.draw.rect(screen, color, rect)
    text_surf = button_font.render(text, True, button_text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)


def main():
    WIDTH = 630
    HEIGHT = 800

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill("white")

    # Beginning and End text
    welcome_text = 'Welcome to Sudoku!'
    welcome_font = pygame.font.Font(None, 80)

    win_text = 'Game Won!'
    win_font = pygame.font.Font(None, 80)

    lose_text = 'Game Over :('
    lose_text = pygame.font.Font(None, 80)

    # Define button properties
    button_font = pygame.font.Font(None, 36)
    button_color = (0, 0, 0)
    button_hover_color = (100, 100, 100)
    button_text_color = (255, 255, 255)
    button_width, button_height = 200, 50
    game_button_width, game_button_height = 100, 50

    # Button positions
    easy_button = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT // 2 - 100, button_width, button_height))
    medium_button = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height))
    hard_button = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT // 2 + 100, button_width, button_height))
    restart_button = pygame.Rect((WIDTH // 2 - game_button_width // 2, HEIGHT - 100, game_button_width, game_button_height))
    reset_button = pygame.Rect((WIDTH/4 - game_button_width, HEIGHT - 100, game_button_width, game_button_height))
    exit_button = pygame.Rect((WIDTH*(3/5) + game_button_width, HEIGHT - 100, game_button_width, game_button_height))

    board = None
    game_started = False

    while True:
        screen.fill("white")

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if not game_started:
            welcome_surf = welcome_font.render(welcome_text, True, "black")
            welcome_rect = welcome_surf.get_rect(center=(WIDTH//2, HEIGHT//2 - 200))
            screen.blit(welcome_surf, welcome_rect)

            # Draw buttons
            draw_button(screen, easy_button, "Easy", easy_button.collidepoint(mouse_pos), button_font, button_color, button_hover_color, button_text_color)
            draw_button(screen, medium_button, "Medium", medium_button.collidepoint(mouse_pos), button_font, button_color, button_hover_color, button_text_color)
            draw_button(screen, hard_button, "Hard", hard_button.collidepoint(mouse_pos), button_font, button_color, button_hover_color, button_text_color)

        if game_started:
            draw_button(screen, restart_button, "Restart", restart_button.collidepoint(mouse_pos), button_font, button_color, button_hover_color, button_text_color)
            draw_button(screen, reset_button, "Reset", reset_button.collidepoint(mouse_pos), button_font,
                        button_color, button_hover_color, button_text_color)
            draw_button(screen, exit_button, "Exit", exit_button.collidepoint(mouse_pos), button_font,
                        button_color, button_hover_color, button_text_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not game_started:
                    if easy_button.collidepoint(mouse_pos):
                        board = Board(WIDTH, HEIGHT, screen, 'easy')
                        game_started = True
                    elif medium_button.collidepoint(mouse_pos):
                        board = Board(WIDTH, HEIGHT, screen, 'medium')
                        game_started = True
                    elif hard_button.collidepoint(mouse_pos):
                        board = Board(WIDTH, HEIGHT, screen, 'hard')
                        game_started = True
                else:
                    if restart_button.collidepoint(mouse_pos):
                        main()
                    if reset_button.collidepoint(mouse_pos):
                        board.reset_to_original()
                    if exit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and game_started:
                fill_board_with_bs_numbers(board)
                x,y = event.pos
                if y < WIDTH:
                    row, col = board.click(x,y)
                    board.select(row,col)
            if event.type == pygame.KEYDOWN and game_started:
                if pygame.key.name(event.key).isdigit():
                    value = int(pygame.key.name(event.key))
                    board.sketch(value)
                if event.key == pygame.K_RETURN:
                    board.place_number()
                    if board.is_full():
                        print("board is full")
                        if board.check_board():
                            print("board checked")
                            screen.fill("white")
                            pygame.display.update()
                        else:
                            screen.fill("white")
                            lose_surf = lose_text.render(welcome_text, True, "black")
                            lose_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
                            screen.blit(lose_surf, lose_rect)

                if event.key == pygame.K_BACKSPACE:
                    board.clear()
                if event.key == pygame.K_LEFT:
                    col -= 1
                    if col < 0:
                        col = 8
                    board.select(row, col)
                if event.key == pygame.K_RIGHT:
                    col += 1
                    if col == 9:
                        col = 0
                    board.select(row, col)
                if event.key == pygame.K_UP:
                    row -= 1
                    if row < 0:
                        row = 8
                    board.select(row, col)
                if event.key == pygame.K_DOWN:
                    row += 1
                    if row == 9:
                        row = 0
                    board.select(row, col)

        if board:
            board.draw()

        pygame.display.update()

def fill_board_with_bs_numbers(board):
    for i in range(9):
        for j in range(9):
            board.select(i, j)
            board.sketch(1)
            board.place_number()

if __name__ == "__main__":
    main()