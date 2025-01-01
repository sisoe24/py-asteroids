import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()

    Player.containers = (drawables, updatables)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

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

        pygame.display.flip()


if __name__ == '__main__':
    main()
