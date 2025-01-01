import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius


    def draw(self, screen: pygame.SurfaceType):
        return pygame.draw.polygon(
            screen, "black", 
            self.triangle(), 2
        )

    def update(self, dt: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
