import pygame, sys
import random

class Cell:

    #Constructor for the Cell class

    def __init__(self, value, x, y, screen):
        self.value = value
        self.x = x
        self.y = y
        self.screen = screen
        self.sketched_value = None
        self.show = False
        self.rect1 = pygame.Rect(self.x, self.y, 75, 75)
        self.random_generated = False
        self.edited = False

    #Setter for this cell’s value

    def set_cell_value(self, value):
        self.value = value

    #Setter for this cell’s sketched value

    def set_sketched_value(self, value):
        self.sketched_value = value

    #Function to display cell object on PyGame screen

    def draw(self):

        #Variables
        color = (245, 245, 245)
        font0 = pygame.font.SysFont("Arial", 30)
        font1 = pygame.font.SysFont("Arial", 15)

        pygame.draw.rect(self.screen, color, self.rect1, width=0)

        #Showing Values
        if self.value != 0:
            text_surface0 = font0.render(f"{self.value}", True, (0, 0, 0))
            self.screen.blit(text_surface0, (self.x + 30, self.y + 20))

        if self.sketched_value != None:
            text_surface1 = font1.render(f"{self.sketched_value}", True, (50, 50, 50))
            self.screen.blit(text_surface1, (self.x + 10, self.y + 10))

        if self.show:
            pygame.draw.rect(self.screen, (255, 0, 0), self.rect1, width=3)

