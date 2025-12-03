import pygame, sys
import math, random

pygame.init()

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))
    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        for row in self.board:
            print(row)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        for i in range(self.row_length):
            if self.board[i][col] == num:
                return False
        return True

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
        for i in range(self.box_length):
            for j in range(self.box_length):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num)

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        nums = list(range(1, self.row_length + 1))
        random.shuffle(nums)
        idx = 0
        for i in range(self.box_length):
            for j in range(self.box_length):
                self.board[row_start + i][col_start + j] = nums[idx]
                idx += 1
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)

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
        removed = 0
        total = self.removed_cells

        while removed < total:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)

            if self.board[row][col] != 0:
                self.board[row][col] = 0
                removed += 1


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
    winning_board = [row[:] for row in sudoku.get_board()]
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board, winning_board

import pygame, sys

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = value

    #Constructor for the Cell class

    def set_cell_value(self, value):
        self.value = value

    #Setter for this cell’s value

    def set_sketched_value(self, value):
        self.sketched_value = value

    #Setter for this cell’s sketched value

    def draw(self):
        rects = []

        color = (50, 100, 50)
        font = pygame.font.SysFont("Arial", 30)
        rect1 = pygame.draw.rect(self.screen, color, (0, 0, 50, 50), width=0)
        if self.value != 0:
            text_surface = font.render(f"{self.value}", True, (0, 0, 0))
        self.screen.blit(text_surface, (42, 35))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
        if rect1.collidepoint(mouseX, mouseY):
            if len(rects) != 0:
                rects = []
        else:
            rects.append(1)
        for r in rects:
            pygame.draw.rect(self.screen, (255, 0, 0), (24, 24, 51, 51), width=3)
        pygame.display.flip()

    #Draws this cell, along with the value inside it.
	#If this cell has a nonzero value, that value is displayed.
	#Otherwise, no value is displayed in the cell.
	#The cell is outlined red if it is currently selected.


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = False
        if difficulty == "easy":
            self.board, self.winning_board = generate_sudoku(9, 30)
            self.original_board = [row[:] for row in self.board]
            self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        if difficulty == "medium":
            self.board, self.winning_board = generate_sudoku(9, 40)
            self.original_board = [row[:] for row in self.board]
            self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        if difficulty == "hard":
            self.board, self.winning_board = generate_sudoku(9, 50)
            self.original_board = [row[:] for row in self.board]
            self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]

    #Constructor for the Board class.
	#screen is a window from PyGame.
	#difficulty is a variable to indicate if the user chose easy medium, or hard.

    def draw(self):

    #Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
	#Draws every cell on this board.

    def select(self, row, col):
        if 0 <= row < 9 and 0 <= col < 9:
            self.selected_cell = (row, col)
        else:
            self.selected_cell = None
    #Marks the cell at (row, col) in the board as the current selected cell.
	#Once a cell has been selected, the user can edit its value or sketched value.

    def click(self, x, y):
        if self.width > x > 0 != x % 50 and self.height > y > 0 != y % 50:
            row = x // 50
            col = y // 50
            coordinates = (row, col)
            return coordinates
        else:
            return None

    #If a tuple of (x,y) coordinates is within the displayed board,
    #this function returns a tuple of the (row, col) of the cell which was clicked.
    #Otherwise, this function returns None.

    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.original_board[row][col] == 0:
                self.board[row][col] = 0
                self.cells[row][col].set_cell_value(0)
            else:
                pass
    #Clears the value cell.
    #Note that the user can only remove the cell values and
    #sketched values that are filled by themselves.

    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].set_sketched_value(value)

    #Sets the sketched value of the current selected cell equal to the user entered value.
    #It will be displayed in the top left corner of the cell using the draw() function.

    def place_number(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            self.board[row][col] = value
            self.cells[row][col].set_cell_value(value)
    #Sets the value of the current selected cell equal to the user entered value.
    #Called when the user presses the Enter key.

    def reset_to_original(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.original_board[row][col] == 0:
                    self.board[row][col] = 0
                else:
                    self.board[row][col] = self.original_board[row][col]
    #Resets all cells in the board to their original values
    #(0 if cleared, otherwise the corresponding digit).

    def is_full(self):
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        else:
            return True
    #Returns a Boolean value indicating whether the board is full or not.

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.cells[row][col].value
    #Updates the underlying 2D board with the values in all cells.

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    cell_tuple = (row, col)
                    return cell_tuple
        else:
            return None
    #Finds an empty cell and returns its row and col as a tuple (x,y).

    def check_board(self):
        if self.board == self.winning_board:
            return True
        else:
            return False
    #Check whether the Sudoku board is solved correctly.

