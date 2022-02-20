import pygame
import random


class Asteroid(pygame.sprite.Sprite):

    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("asteroid.png")
        self.rect = self.image.get_rect(midtop=(x, y))
        self.speed = speed - 1

    def appear(self, x, y):
        self.rect = self.image.get_rect(midtop=(x, y))

    def update(self, height, width, asteroid_x, asteroid_y):
        if self.rect.y >= height or self.collision(asteroid_x, asteroid_y):
            self.appear(random.randint(10, width), 5)
        else:
            self.rect.y += self.speed

    def collision(self, asteroid_x, asteroid_y):
        return abs(self.rect.x - asteroid_x) <= 50 and abs(self.rect.y - asteroid_y) <= 20
