import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

 
    black = (0, 0, 0)
    clock = pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    
    running = True
    while running:
        screen.fill(black)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

        
if __name__ == "__main__":
    main()
