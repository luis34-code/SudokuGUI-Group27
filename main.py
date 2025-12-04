#Imports
import pygame
from cell import *
from board import *
from sudoku_generator import *

def main():


    try:
        #PyGame Screen Initalization & Set-Up
        pygame.init()
        screen = pygame.display.set_mode((675, 750))
        pygame.display.set_caption("Sudoku")

        #Variables
        board_width = 675
        board_height = 675
        running = True
        beginning = True
        play_game = False
        show_gameOver = False
        show_gameWin = False

        #Start Screen
        start_font = pygame.font.SysFont("Garamond", 75)
        start_title = start_font.render("Welcome to Sudoku!", True, (0, 0, 0))
    
        other_font = pygame.font.SysFont("Trebuchet MS", 33)
        start_select_text = other_font.render("Select Game Mode:", True, (0, 0, 0))

        easy_select_text = other_font.render("Easy", True, (0, 0, 0))
        rect_easy = pygame.Rect((82, 473, 100, 45))

        medium_select_text = other_font.render("Medium", True, (0, 0, 0))
        rect_medium = pygame.Rect((265, 475, 130, 45))

        hard_select_text = other_font.render("Hard", True, (0, 0, 0))
        rect_hard = pygame.Rect((485, 473, 100, 45))

        #Game Win Screen
        win_font = pygame.font.SysFont("Garamond", 100)
        win_title = win_font.render("Game Won!", True, (0, 0, 0))

        exit_font = pygame.font.SysFont("Impact", 50)
        exit_select_text = exit_font.render("Exit", True, (0, 0, 0))
        rect_exit = pygame.Rect(278, 423, 100, 67)
        
        #Game Over Screen
        lose_font = pygame.font.SysFont("Garamond", 100)
        lose_title = lose_font.render("Game Over!", True, (0, 0, 0))

        restart_font = pygame.font.SysFont("Impact", 50)
        restart_select_text = restart_font.render("Restart", True, (0, 0, 0))
        rect_restart = pygame.Rect(240, 423, 170, 67)

        #Sudoku Screen Buttons
        reset_button = pygame.Rect(125, 700, 100, 35)
        restart_button = pygame.Rect(290, 700, 100, 35)
        exit_button = pygame.Rect(450, 700, 100, 35)
        font0 = pygame.font.SysFont("Arial", 18)

        #Game Loop
        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    event_posX, event_posY = event.pos
                    if reset_button.collidepoint(event.pos) & play_game == True:
                        board0.reset_to_original()
                        board0.cells = []
                        for row in range(9):
                            row_cells = []
                            for col in range(9):
                                x = col * (board0.width//9)
                                y = row * (board0.height//9)
                                cell0 = Cell(board0.board[row][col], x, y, board0.screen)
                                if cell0.value != 0:
                                    cell0.random_generated = True
                                row_cells.append(cell0)
                            board0.cells.append(row_cells)
                    if restart_button.collidepoint(event.pos) & play_game == True:
                        play_game = False
                        beginning = True
                    if exit_button.collidepoint(event.pos) & play_game == True:
                        running = False
                    if rect_easy.collidepoint(event.pos) & beginning == True:
                        board0 = Board(board_width, board_height, screen, "easy")
                        beginning = False
                        play_game = True
                    if rect_medium.collidepoint(event.pos) & beginning == True:
                        board0 = Board(board_width, board_height, screen, "medium")
                        beginning = False
                        play_game = True
                    if rect_hard.collidepoint(event.pos) & beginning == True:
                        board0 = Board(board_width, board_height, screen, "hard")
                        beginning = False
                        play_game = True
                    if rect_restart.collidepoint(event.pos) & show_gameOver == True:
                        show_gameOver = False
                        beginning = True
                    if rect_exit.collidepoint(event.pos) & show_gameWin == True:
                        running = False
                    if (0 <= event_posX < 675 and 0 <= event_posY < 675) & (play_game == True):
                        board0.currentRow, board0.currentColumn = board0.click(event_posX, event_posY)
                elif event.type == pygame.KEYDOWN:
                    if board0.selected_cell == None:
                        board0.select(board0.currentRow, board0.currentColumn)
                    else:
                        if event.key == pygame.K_UP:
                            if board0.currentRow != 0:
                                board0.currentRow -= 1
                            board0.select(board0.currentRow, board0.currentColumn)
                        elif event.key == pygame.K_DOWN:
                            if board0.currentRow != 8:
                                board0.currentRow += 1
                            board0.select(board0.currentRow, board0.currentColumn)
                        elif event.key == pygame.K_LEFT:
                            if board0.currentColumn != 0:
                                board0.currentColumn -= 1
                            board0.select(board0.currentRow, board0.currentColumn)
                        elif event.key == pygame.K_RIGHT:
                            if board0.currentColumn != 8:
                                board0.currentColumn += 1
                            board0.select(board0.currentRow, board0.currentColumn)
                        elif event.unicode in '123456789': 
                            if board0.cells[board0.currentRow][board0.currentColumn].edited == False:
                                board0.sketch(event.unicode)
                        elif event.key == pygame.K_RETURN:
                            if board0.cells[board0.currentRow][board0.currentColumn].value == 0:
                                board0.place_number(board0.cells[board0.currentRow][board0.currentColumn].sketched_value)
                                board0.cells[board0.currentRow][board0.currentColumn].sketched_value = None
                        elif event.key == pygame.K_BACKSPACE:
                            if board0.cells[board0.currentRow][board0.currentColumn].edited == True:
                                board0.clear()         

            #Start Screen Display
            if beginning:
                screen.fill((255, 245, 225))
                pygame.draw.rect(screen, (200, 200, 200), rect_hard)
                pygame.draw.rect(screen, (200, 200, 200), rect_medium)
                pygame.draw.rect(screen, (200, 200, 200), rect_easy)
                screen.blit(start_title, (100, 170))
                screen.blit(start_select_text, (190, 350))
                screen.blit(easy_select_text, (100, 475))
                screen.blit(medium_select_text, (275, 475))
                screen.blit(hard_select_text, (500, 475))
                
            #Active In-Progress Game Screen Display
            if play_game:
                screen.fill((255, 245, 225))

                board0.draw()

                pygame.draw.rect(screen, (200, 200, 200), reset_button)
                text_surface0 = font0.render("Reset", True, (0, 0, 0))
                screen.blit(text_surface0, (150, 707))
                pygame.draw.rect(screen, (200, 200, 200), restart_button)
                text_surface1 = font0.render("Restart", True, (0, 0, 0))
                screen.blit(text_surface1, (310, 707))
                pygame.draw.rect(screen, (200, 200, 200), exit_button)
                text_surface2 = font0.render("Exit", True, (0, 0, 0))
                screen.blit(text_surface2, (485, 707))

                if board0.is_full() == True:
                    if board0.check_board() == True:
                        play_game = False
                        show_gameWin = True
                    else:
                        play_game = False
                        show_gameOver = True

            #Win Screen Display
            if show_gameWin:
                screen.fill((255, 245, 225))
                pygame.draw.rect(screen, (200, 200, 200), rect_exit)
                screen.blit(win_title, (100, 200))
                screen.blit(exit_select_text, (290, 425))

            #Game Over Screen Display
            if show_gameOver:
                screen.fill((255, 245, 225))
                pygame.draw.rect(screen, (200, 200, 200), rect_restart)
                screen.blit(lose_title, (90, 200))
                screen.blit(restart_select_text, (250, 425))

            pygame.display.flip()

    finally:
        pygame.quit()

#Running Main Function
if __name__ == '__main__':
    main()

