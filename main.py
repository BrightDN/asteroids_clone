import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots, updateable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color=(0,0,0), rect=None, special_flags=0)

        for object in updateable:
            object.update(dt)

        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_detection(shot):
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                print("Game over!")
                return
if __name__ == "__main__":
    main()

