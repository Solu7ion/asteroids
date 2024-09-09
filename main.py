import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))

 
    black = (0, 0, 0)

    
    running = True
    while running:
        screen.fill(black)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        
if __name__ == "__main__":
    main()
