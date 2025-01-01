import sys
import pygame

from asteroid import Asteroid
from bullet import Shot
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawables, updatables)
    Asteroid.containers = (asteroids, drawables, updatables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, drawables, updatables)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("red")

        dt = clock.tick(60) / 1000

        for drawable in drawables:
            drawable.draw(screen)

        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game Over!")
                sys.exit(1)

            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()


        pygame.display.flip()


if __name__ == '__main__':
    main()
