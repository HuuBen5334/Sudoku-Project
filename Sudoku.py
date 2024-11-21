from sudoku_generator import *


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((450, 450))
    pygame.display.set_caption("Sudoku")
    screen.fill((255, 255, 245))

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

