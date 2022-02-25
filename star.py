import pygame
import random


class Star(pygame.sprite.Sprite):

    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect(midtop=(x, y))
        self.speed = speed

    def appear(self, x, y):
        self.rect = self.image.get_rect(midtop=(x, y))

    def update(self, height, width, ship_x, ship_y):
        if self.rect.y >= height:
            self.appear(random.randint(10, width), 5)
        else:
            self.rect.y += self.speed
