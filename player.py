from circleshape import *
from constants import *
from shot import *
from constants import *
import sys 

class Player(CircleShape):
    FRICTION = SPEED_FRICTION
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  
        self.rotation = 0  
        self.shoot_timer = 0
        self.velocity = pygame.Vector2(0, 0)
        self.lives = 3 
        self.invulnerable_timer = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        if self.invulnerable_timer > 0:
            if int(self.invulnerable_timer * 10) % 2 == 0:  # Мерцание
                pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        else:
            pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
   

    def rotate(self, dt):
       self.rotation += PLAYER_TURN_SPEED * dt
        
    
    def update(self, dt):
        self.shoot_timer -=dt

        if self.invulnerable_timer > 0:
            self.invulnerable_timer -= dt
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
            
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.move(dt)

    def move(self, dt):
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        if keys[pygame.K_w]:
            self.velocity += forward * PLAYER_SPEED * dt
        elif keys[pygame.K_s]:
            self.velocity -= forward * PLAYER_SPEED * dt
        
        self.velocity *= self.FRICTION
        self.position += self.velocity * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def lose_life(self):
        if self.invulnerable_timer > 0:
            return 
        
        self.lives -= 1
        if self.lives <= 0:
            print("Game Over!")
            sys.exit()
        else:
            self.velocity = pygame.Vector2(0, 0)
            self.invulnerable_timer = 3
