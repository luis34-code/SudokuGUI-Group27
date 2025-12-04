import pygame

pygame.init()

screen = pygame.display.set_mode((450, 500))

screen.fill((255, 245, 225))


def start_screen():
    start_font = pygame.font.SysFont("Garamond", 50)
    start_title = start_font.render("Welcome to Sudoku", True, (200, 100, 100))
    screen.blit(start_title, (20, 100))

    other_font = pygame.font.SysFont("Trebuchet MS", 25)
    start_select_text = other_font.render("Select Game Mode:", True, (200, 100, 100))
    screen.blit(start_select_text, (110, 250))

    easy_select_text = other_font.render("Easy", True, (0, 200, 0))
    rect_easy = pygame.draw.rect(screen, (235, 235, 235), (12, 325, 75, 35), width=0)
    screen.blit(easy_select_text, (25, 325))

    medium_select_text = other_font.render("Medium", True, (255, 100, 0))
    rect_medium = pygame.draw.rect(screen, (235, 235, 235), (162, 325, 112, 35), width=0)
    screen.blit(medium_select_text, (175, 325))

    hard_select_text = other_font.render("Hard", True, (200, 0, 0))
    rect_hard = pygame.draw.rect(screen, (235, 235, 235), (365, 325, 75, 35), width=0)
    screen.blit(hard_select_text, (375, 325))
    pygame.display.update()

def win_game():
    win_font = pygame.font.SysFont("Garamond", 75)
    win_title = win_font.render("Game Won!", True, (200, 100, 100))
    screen.blit(win_title, (50, 100))
    exit_font = pygame.font.SysFont("Impact", 25)
    exit_select_text = exit_font.render("Exit", True, (200, 100, 100))
    rect_exit = pygame.draw.rect(screen, (235, 235, 235), (182, 325, 75, 35), width=0)
    screen.blit(exit_select_text, (200, 325))
    pygame.display.update()

def lose_game():
    win_font = pygame.font.SysFont("Garamond", 75)
    win_title = win_font.render("Game Over!", True, (200, 100, 100))
    screen.blit(win_title, (50, 100))
    exit_font = pygame.font.SysFont("Impact", 25)
    exit_select_text = exit_font.render("Restart", True, (200, 100, 100))
    rect_restart = pygame.draw.rect(screen, (235, 235, 235), (170, 325, 112, 35), width=0)
    screen.blit(exit_select_text, (190, 325))
    pygame.display.update()

