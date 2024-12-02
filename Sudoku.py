from sudoku_generator import *
import pygame, sys

def draw_button(screen, rect, text, is_hovered, button_font, button_color, button_hover_color, button_text_color):
    color = button_hover_color if is_hovered else button_color
    pygame.draw.rect(screen, color, rect)
    text_surf = button_font.render(text, True, button_text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)


def main():
    WIDTH = 900
    HEIGHT = 900
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill("white")

    # Define button properties
    button_font = pygame.font.Font(None, 36)
    button_color = (0, 0, 0)
    button_hover_color = (100, 100, 100)
    button_text_color = (255, 255, 255)
    button_width, button_height = 200, 50

    # Button positions
    easy_button = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT // 2 - 100, button_width, button_height))
    medium_button = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height))
    hard_button = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT // 2 + 100, button_width, button_height))

    board = None
    game_started = False

    while True:
        screen.fill("white")

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if not game_started:
            # Draw buttons
            draw_button(screen, easy_button, "Easy", easy_button.collidepoint(mouse_pos), button_font, button_color, button_hover_color, button_text_color)
            draw_button(screen, medium_button, "Medium", medium_button.collidepoint(mouse_pos), button_font, button_color, button_hover_color, button_text_color)
            draw_button(screen, hard_button, "Hard", hard_button.collidepoint(mouse_pos), button_font, button_color, button_hover_color, button_text_color)

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

        if board:
            board.draw()

        pygame.display.update()

if __name__ == "__main__":
    main()