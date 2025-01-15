#source venv/bin/activate
import pygame
from circleshape import *
from constants import *
from shot import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.x = x
        self.y = y
        self.delay_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += (dt * PLAYER_TURN_SPEED)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        inverted_dt = (dt - dt*2)
        self.delay_timer -= dt

        if keys[pygame.K_q] or keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(inverted_dt)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(inverted_dt)

        if keys[pygame.K_z] or keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE] and not self.delay_timer > 0:
            self.shoot()
            self.delay_timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation)
        direction *= PLAYER_SHOOT_SPEED
        shot.velocity = direction
        

