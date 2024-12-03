import math,random
import pygame

class SudokuGenerator:
    # initializes variables and board
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(row_length)] for j in range(row_length)]
        self.box_length = self.row_length ** .5

    # returns the board
    def get_board(self):
        return self.board

    # prints the board
    def print_board(self):
        print(self.board)

    # returns false if the number is present in the given row, prints true otherwise
    def valid_in_row(self, row, num):
        for number in self.board[row]:
            if num == number:
                return False
        return True

    # returns false if the number is present in the given column, prints true otherwise
    def valid_in_col(self, col, num):
        for row in self.board:
            if num == row[int(col)]:
                return False
        return True

    # returns false if the number is present in the given 3x3 box, drawn from top left, prints true otherwise
    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start+2):
            for j in range(int(col_start), int(col_start+2)):
                if num == self.board[i-1][j-1]:
                    return False
        return True

    # combo check of the above 3, if all true, returns true, otherwise false
    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num):
            return True
        return False

    # fills a 3x3 box from the given top left coordinates
    def fill_box(self, row_start, col_start):
        int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for row in range(0, 3):
            for col in range(0, 3):
                random_digit = random.choice(int_list)
                int_list.remove(random_digit)

                self.board[row_start][col_start] = random_digit
                col_start += 1

            col_start -= 3
            row_start += 1

    # given method, fills diagonal
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    # given method, fills remaining board
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][int(col)] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][int(col)] = 0
        return False

    # given method, fills the board
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    # removes a removed_cells number of cells from the board, setting them to 0
    def remove_cells(self):
        counter = 0

        while counter < self.removed_cells:
            row = random.randint(0, 8)
            col = random.randint(0, 8)

            if self.board[row][col] == 0:
                continue

            self.board[row][col] = 0
            counter += 1

# Generates a sudoku board, removes the appropriate number of cells and stores the solution
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

class Cell:
    def __init__(self, value, row, col, screen, screen_width):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = 0
        self.cell_size = screen_width / 9

    def set_cell_value(self, value):
        self.value = value


    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = self.col * self.cell_size
        y = self.row * self.cell_size

        # Cell outline already drawn in board class
        # pygame.draw.rect(self.screen, (0, 0, 0), (x, y, self.cell_size, self.cell_size), 1)
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, self.cell_size, self.cell_size), 3)

        font = pygame.font.Font(None, 36)
        if self.value != 0:
            text = font.render(str(self.value), True, "black")
            text_rect = text.get_rect(center=(x+self.cell_size/2,y+self.cell_size/2))
            self.screen.blit(text, text_rect)
        elif self.sketched_value != 0:
            sketched_font = pygame.font.Font(None, 24)
            sketched_text = sketched_font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(sketched_text, (x + 5, y + 5))

class Board:#Links logic to 2d list
    def __init__(self, width, height, screen, difficulty):
        if difficulty == 'easy':
            self.removed_cells = 30
        elif difficulty == 'medium':
            self.removed_cells = 40
        elif difficulty == 'hard':
            self.removed_cells = 50

        self.board = generate_sudoku(9, self.removed_cells)
        self.original_board = self.board
        self.width = width
        self.height = height
        self.screen = screen
        self.cells = [[Cell(self.board[i][j], i, j, self.screen, width) for j in range(9)]for i in range(9)]
        self.cell_size = width / 9

    def draw(self):
        # draw vertical lines
        for i in range(0, 10):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(
                self.screen,
                "black",
                (self.cell_size*i, 0),
                (self.cell_size*i, self.width),
                line_width
            )

        # draw horizontal lines
        for i in range(0, 10):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(
                self.screen,
                "black",
                (0, self.cell_size*i ),
                (self.width, self.cell_size*i),
                line_width
            )

        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()

    def select(self, row, col):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].selected = False

        self.selected_cell = self.cells[row][col]
        self.cells[row][col].selected = True

        # Red border done in cell class
        # cell_rect = pygame.Rect(row*self.cell_size, col*self.cell_size, self.cell_size, self.cell_size)
        # pygame.draw.rect(self.screen, "red", cell_rect, 2)

    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return int(y // self.cell_size), int(x // self.cell_size)
        return None

    def clear(self):
        if self.selected_cell and self.original_board[self.selected_cell.row][self.selected_cell.col] == 0:
            self.selected_cell.sketched_value = 0
            self.selected_cell.value = 0

    def sketch(self, value):
        if self.original_board[self.selected_cell.row][self.selected_cell.col] == 0:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(value)

            #Sketch value done in cell class
            # sketch_font = pygame.font.Font(None, 20)
            # sketch_surf = sketch_font.render(str(self.selected_cell.sketched_value), True, "lightgrey")
            # sketch_rect = sketch_surf.get_rect(
            #     topleft=(self.selected_cell.row*self.cell_size+3, self.selected_cell.col*self.cell_size))
            # self.screen.blit(sketch_surf, sketch_rect)

    def place_number(self):
        self.selected_cell.value = self.selected_cell.sketched_value
        self.board[self.selected_cell.row][self.selected_cell.col] = self.selected_cell.value

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                if self.original_board[i][j] == 0:
                    self.cells[i][j].set_cell_value(0)
                    self.cells[i][j].set_sketched_value(0)
        self.update_board()

    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True
    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.cells[i][j].value

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
    def check_board(self):
        sudoku_gen = SudokuGenerator(9, 0)
        sudoku_gen.board = self.board
        for i in range(9):
            for j in range(9):
                if not sudoku_gen.is_valid(i, j, self.board[i][j]):
                    return False


        return True

