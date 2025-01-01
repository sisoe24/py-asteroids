import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y, radius)
        self.rotation = 0
        self.radius = radius

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        random_angle = random.uniform(20, 50)

        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity = self.velocity.rotate(random_angle) * 1.2

        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2.velocity = self.velocity.rotate(-random_angle)


    def draw(self, screen: pygame.SurfaceType):
        return pygame.draw.circle(
            screen, "black", self.position, self.radius, 2
        )

    def update(self, dt: float):
        self.position += self.velocity * dt

