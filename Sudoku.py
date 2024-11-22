from sudoku_generator import *
import pygame, sys

if __name__ == "__main__":
    WIDTH = 900
    HEIGHT = 900
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill("white")
    board = Board(WIDTH, HEIGHT, screen, 'easy')
    board.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
