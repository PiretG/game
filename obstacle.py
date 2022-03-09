import base64
from io import BytesIO

import pygame
import random

from PIL import Image
from pic2str import asteroid
from pic2str import collision


class Asteroid(pygame.sprite.Sprite):

    def __init__(self, x, y, speed, game):
        super().__init__()

        # Load picture byte data
        byte_data = base64.b64decode(asteroid)
        image = Image.open(BytesIO(byte_data))
        asteroid_image = pygame.image.fromstring(image.tobytes(), image.size, image.mode)

        self.image = asteroid_image
        self.rect = self.image.get_rect(midtop=(x, y))

        # Load music byte data
        music_data = base64.b64decode(collision)
        self.sound = pygame.mixer.Sound(music_data)
        self.sound.set_volume(0.5)

        self.speed = speed - 1
        self.game = game

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
