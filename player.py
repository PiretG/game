import pygame
import base64

from io import BytesIO
from PIL import Image
from pic2str import ship


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()

        # Load byte data
        byte_data = base64.b64decode(ship)
        image = Image.open(BytesIO(byte_data))
        ship_image = pygame.image.frombuffer(image.tobytes(), image.size, image.mode)

        self.image = ship_image
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.max_y_constraint = constraint

    def controls(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_UP]:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.max_y_constraint:
            self.rect.bottom = self.max_y_constraint

    def update(self):
        self.controls()
        self.constraint()
