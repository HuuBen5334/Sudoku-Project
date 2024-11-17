from sudoku_generator import *

def main():
    # Creates the board
    board = generate_sudoku(9, 9)

    # prints board to console
    for row in board:
        print(row)

if __name__ == '__main__':
    main()