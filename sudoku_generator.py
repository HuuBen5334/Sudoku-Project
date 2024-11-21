import math,random
import pygame, sys

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        pass

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        pass

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        pass

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        pass

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        pass

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        pass
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        pass

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        pass
    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        pass

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
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
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        pass

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
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
        self.sketched_value = 0
        self.selected = False #To tell whether cell is selected or not

    def set_cell_value(self, value):
        self.value = value


    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        cell_size = 50 #Change it to whatever
        x = self.col * cell_size
        y = self.row * cell_size

        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, cell_size, cell_size), 1)
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_size, cell_size), 3)

        font = pygame.font.Font(None, 36)
        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + 15, y + 10))
        elif self.sketched_value != 0:
            sketched_font = pygame.font.Font(None, 24)
            sketched_text = sketched_font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(sketched_text, (x + 5, y + 5))

class Board:
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
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(9)]for i in range(9)]
        self.cell_size = width // 9

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
        self.selected_cell = self.cells[row][col]
        cell_rect = pygame.Rect(row*self.cell_size, col*self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, "red", cell_rect, 2)

    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return x // self.cell_size, y // self.cell_size
        return None

    def clear(self):
        if self.selected_cell and self.original_board[self.selected_cell.row][self.selected_cell.col] == 0:
            self.selected_cell.sketched_value = 0
            self.selected_cell.value = 0

    def sketch(self, value):
        if self.original_board[self.selected_cell.row][self.selected_cell.col] == 0:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)
            sketch_font = pygame.font.Font(None, 20)
            sketch_surf = sketch_font.render(str(self.selected_cell.sketched_value), True, "lightgrey")
            sketch_rect = sketch_surf.get_rect(
                topleft=(self.selected_cell.row*self.cell_size+3, self.selected_cell.col*self.cell_size))
            self.screen.blit(sketch_surf, sketch_rect)

    def place_number(self, value):
        self.selected_cell.value = value

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
                sudoku_gen.is_valid(i, j, self.board[i][j])


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