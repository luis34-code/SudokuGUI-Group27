import pygame, sys
import random

class Cell:
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

    #Constructor for the Cell class

    def set_cell_value(self, value):
        self.value = value

    #Setter for this cell’s value

    def set_sketched_value(self, value):
        self.sketched_value = value
    
    #Setter for this cell’s sketched value

    def click_event(self, position):
        if self.rect1.collidepoint(position):
            self.show = not self.show

    def draw(self):

        #Variables
        color = (50, 100, 50)
        font0 = pygame.font.SysFont("Arial", 30)
        font1 = pygame.font.SysFont("Arial", 15)
        #rect1 = pygame.Rect(self.row, self.col, 75, 75)

        pygame.draw.rect(self.screen, color, self.rect1, width=0)

        #Showing Value
        if self.value != 0:
            text_surface0 = font0.render(f"{self.value}", True, (0, 0, 0))
            self.screen.blit(text_surface0, (self.x + 30, self.y + 20))

        if self.sketched_value != None:
            text_surface1 = font1.render(f"{self.sketched_value}", True, (200, 200, 200))
            self.screen.blit(text_surface1, (self.x + 10, self.y + 10))

        if self.show:
            pygame.draw.rect(self.screen, (255, 0, 0), self.rect1, width=3)

def main():

    try:
        pygame.init()
        screen = pygame.display.set_mode((500, 500))

        cell = Cell(0, 220, 230, screen)

        running = True
        while running:
            screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cell.click_event(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.unicode in '123456789':
                        cell.set_sketched_value(event.unicode)
                    if event.key == pygame.K_RETURN:
                        cell.set_cell_value(cell.sketched_value)
                        cell.sketched_value = None
        
            cell.draw()

            pygame.display.flip()
     
    finally:
        pygame.quit()

if __name__ == '__main__':
    main()