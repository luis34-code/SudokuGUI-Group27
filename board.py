import pygame, sys
from cell import *
from sudoku_stuff import *
from sudoku_generator import *

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None
        self.cells = []
        self.currentRow = 0
        self.currentColumn = 0
        if difficulty == "easy":
            self.board, self.winning_board = generate_sudoku(9, 30)
            self.original_board = [row[:] for row in self.board]
            #self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        if difficulty == "medium":
            self.board, self.winning_board = generate_sudoku(9, 40)
            self.original_board = [row[:] for row in self.board]
            #self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        if difficulty == "hard":
            self.board, self.winning_board = generate_sudoku(9, 50)
            self.original_board = [row[:] for row in self.board]
            #self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]

        cell_width = self.width//9
        cell_height = self.height//9

        for row in range(9):
            row_cells = []
            for col in range(9):
                x = col * cell_width
                y = row * cell_height
                cell0 = Cell(self.board[row][col], x, y, self.screen)
                if cell0.value != 0:
                    cell0.random_generated = True
                row_cells.append(cell0)
            self.cells.append(row_cells)

    #Constructor for the Board class.
	#screen is a window from PyGame.
	#difficulty is a variable to indicate if the user chose easy medium, or hard.

    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()

        color = (0, 0, 0)
        cell_bounds = self.width//9

        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, color, (i * cell_bounds, 0), (i * cell_bounds, self.height), width=3)
            else:
                pygame.draw.line(self.screen, color, (i * cell_bounds, 0), (i * cell_bounds, self.height), width=1)

        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, color, (0, i * cell_bounds), (self.width, i * cell_bounds), width=3)
            else:
                pygame.draw.line(self.screen, color, (0, i * cell_bounds), (self.width, i * cell_bounds), width=1)
    #Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
	#Draws every cell on this board.

    def select(self, row, col):
        for row0 in range(9):
            for col0 in range(9):
                self.cells[row0][col0].show = False

        self.selected_cell = (row, col)
        self.cells[row][col].show = True
    #Marks the cell at (row, col) in the board as the current selected cell.
	#Once a cell has been selected, the user can edit its value or sketched value.

    def click(self, x, y):   
        if 0 <= x < self.width and 0 <= y < self.height:
            row = y // (self.height//9)
            col = x // (self.width//9)

            self.select(row, col)
            return (row, col)
        return None
        

    #If a tuple of (x,y) coordinates is within the displayed board,
    #this function returns a tuple of the (row, col) of the cell which was clicked.
    #Otherwise, this function returns None.

    def clear(self):
        if (self.selected_cell == (self.currentRow, self.currentColumn)) & (self.cells[self.currentRow][self.currentColumn].random_generated == False):
            row, col = self.selected_cell
            if self.cells[row][col].sketched_value != None:
                self.cells[row][col].set_sketched_value(None)
            if self.original_board[row][col] == 0:
                self.board[row][col] = 0
                self.cells[row][col].set_cell_value(0)
                self.cells[row][col].edited = False
    #Clears the value cell.
    #Note that the user can only remove the cell values and
    #sketched values that are filled by themselves.

    def sketch(self, value):
        if (self.selected_cell == (self.currentRow, self.currentColumn)) & (self.cells[self.currentRow][self.currentColumn].random_generated == False):
            row, col = self.selected_cell
            self.cells[row][col].set_sketched_value(value)
            self.cells[row][col].edited = True

    #Sets the sketched value of the current selected cell equal to the user entered value.
    #It will be displayed in the top left corner of the cell using the draw() function.

    def place_number(self, value):
        if (self.selected_cell == (self.currentRow, self.currentColumn)) & (self.cells[self.currentRow][self.currentColumn].random_generated == False):
            row, col = self.selected_cell
            self.board[row][col] = int(value)
            self.cells[row][col].set_cell_value(value)
            self.cells[row][col].edited = True
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




