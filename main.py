import pygame
import sys
from constants import *
from player import Player
from asteroidfield import *
from asteroids import Asteroid
from shots import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt)
        for thing in asteroids:
            if thing.collision(player):
                print(f"Game over!")
                sys.exit() 
            for shot in shots:
                if thing.collision(shot):
                    shot.kill()
                    thing.kill()


        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/ 1000
   
 





if __name__ == "__main__":
    main()
