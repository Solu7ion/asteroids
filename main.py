import sys
import pygame
from constants import *
from player import *
from asteroid import * 
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (updatable, drawable, shots)
 
    clock = pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    font = pygame.font.Font(None, 36)
    score = 0 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                player.lose_life()
                asteroid.kill()
        
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    score += 10             
        
        lives_text = font.render(f"Lives: {player.lives}", True,"white") 
        score_text = font.render(f"Score: {score}", True, "white")
        
        screen.fill("black")
        screen.blit(lives_text, (10,10))
        screen.blit(score_text, (10, 50))
        
        for obj in drawable:
            obj.draw(screen)
            

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

        
if __name__ == "__main__":
    main()
