import pygame

from bullet import Shot
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def shot(self):
        shot = Shot(
            self.position.x, self.position.y
        )
        shot.velocity += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

    def update(self, dt: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.shot()
        super().update(dt)

    def move(self, dt: float):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
