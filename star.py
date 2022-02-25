import pygame
import random


class Star(pygame.sprite.Sprite):

    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect(midtop=(x, y))
        self.speed = speed
        self.sound = pygame.mixer.Sound('bonus.wav')
        self.sound.set_volume(0.2)

    def appear(self, x, y):
        self.rect = self.image.get_rect(midtop=(x, y))

    def update(self, height, width, ship_x, ship_y):
        if self.rect.y >= height:
            self.appear(random.randint(10, width), 5)
        else:
            self.rect.y += self.speed
        if self.collision(ship_x, ship_y):
            self.sound.play()

    def collision(self, ship_x, ship_y):
        return (-40 <= ship_x - self.rect.x <= 20) \
                and abs(ship_y - self.rect.y) <= 20
