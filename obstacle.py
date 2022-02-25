import pygame
import random


class Asteroid(pygame.sprite.Sprite):

    def __init__(self, x, y, speed, game):
        super().__init__()
        self.image = pygame.image.load("asteroid.png")
        self.rect = self.image.get_rect(midtop=(x, y))
        self.speed = speed - 1
        self.game = game
        self.sound = pygame.mixer.Sound('collision.wav')

    def appear(self, x, y):
        self.rect = self.image.get_rect(midtop=(x, y))

    def update(self, height, width, ship_x, ship_y):
        if self.collision(ship_x, ship_y):
            self.sound.play()
            self.game.points -= 1
        if self.rect.y >= height or self.collision(ship_x, ship_y):
            self.appear(random.randint(10, width), 5)
        else:
            self.rect.y += self.speed

    def collision(self, ship_x, ship_y):
        return -50 <= ship_x - self.rect.x <= 10 \
                and abs(ship_y - self.rect.y) <= 15
