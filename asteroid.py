import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y, radius)
        self.rotation = 0
        self.radius = radius

    def draw(self, screen: pygame.SurfaceType):
        return pygame.draw.circle(
            screen, "black", self.position, self.radius, 2
        )

    def update(self, dt: float):
        self.position += self.velocity * dt

