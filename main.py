#Main File

import pygame
from cell import *
from board import *
from sudoku_generator import *

def main():

    board_width = 675
    board_height = 675

    try:
        pygame.init()
        screen = pygame.display.set_mode((675, 750))

        board0 = Board(board_width, board_height, screen, 'easy')
        reset_button = pygame.Rect(125, 700, 100, 35)
        restart_button = pygame.Rect(290, 700, 100, 35)
        exit_button = pygame.Rect(450, 700, 100, 35)
        font0 = pygame.font.SysFont("Arial", 18)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    event_posX, event_posY = event.pos
                    if 0 <= event_posX < 675 and 0 <= event_posY < 675:
                        board0.currentRow, board0.currentColumn = board0.click(event_posX, event_posY)
                    if reset_button.collidepoint(event.pos):
                        #print("Reset Button Clicked!")
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
                    if restart_button.collidepoint(event.pos):
                        print("Restart Button Clicked!") #to-do with Luis
                    if exit_button.collidepoint(event.pos):
                        running = False
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
                        elif event.unicode in '123456789': #sketch
                            if board0.cells[board0.currentRow][board0.currentColumn].edited == False:
                                board0.sketch(event.unicode)
                        elif event.key == pygame.K_RETURN:
                            if board0.cells[board0.currentRow][board0.currentColumn].value == 0:
                                board0.place_number(board0.cells[board0.currentRow][board0.currentColumn].sketched_value)
                                board0.cells[board0.currentRow][board0.currentColumn].sketched_value = None
                        elif event.key == pygame.K_BACKSPACE:
                            if board0.cells[board0.currentRow][board0.currentColumn].edited == True:
                                board0.clear()         

            screen.fill((135, 206, 235))

            board0.draw()

            pygame.draw.rect(screen, (50, 100, 50), reset_button)
            text_surface0 = font0.render("Reset", True, (0, 0, 0))
            screen.blit(text_surface0, (150, 707))
            pygame.draw.rect(screen, (50, 100, 50), restart_button)
            text_surface1 = font0.render("Restart", True, (0, 0, 0))
            screen.blit(text_surface1, (310, 707))
            pygame.draw.rect(screen, (50, 100, 50), exit_button)
            text_surface2 = font0.render("Exit", True, (0, 0, 0))
            screen.blit(text_surface2, (485, 707))

            if board0.is_full() == True:
                print("Board Completed!")

                for row in board0.board:
                    print(row)

                if board0.check_board() == True:
                    print("Sucessful!")
                else:
                    print("Incorrect Board!")

            pygame.display.flip()

    finally:
        pygame.quit()

if __name__ == '__main__':
    main()

