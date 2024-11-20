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
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        pass

    def draw(self):
        pass

class Board:
    def __init__(self, width, height, screen, difficulty):

        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = generate_sudoku(self.width, self.difficulty)
        self.cells = [[Cell(self.board[i][j], i, j) for j in range(9)]for i in range(9)]


    def draw(self):
        # draw vertical lines
        for i in range(1,9):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(
                self.screen,
                "black",
                ((self.width/9)*i, 0),
                ((self.width/9)*i, self.width),
                line_width
            )

        # draw horizontal lines
        for i in range(1,10):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(
                self.screen,
                "black",
                (0,(self.width/9)*i ),
                (self.width, (self.width/9)*i),
                line_width
            )

    def select(self, row, col):
        self.selected =
    def click(self, row, col):
        pass
    def clear(self):
        pass
    def sketch(self, value):
        pass
    def place_number(self, value):
        pass
    def reset_to_original(self):
        pass
    def is_full(self):
        pass
    def update_board(self):
        pass
    def find_empty(self):
        pass
    def check_board(self):
        pass


