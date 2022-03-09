import pygame
import random
import base64

from io import BytesIO
from PIL import Image
from pic2str import star
from pic2str import bonus


class Star(pygame.sprite.Sprite):

    def __init__(self, x, y, speed):
        super().__init__()

        # Load picture byte data
        byte_data = base64.b64decode(star)
        image = Image.open(BytesIO(byte_data))
        star_image = pygame.image.fromstring(image.tobytes(), image.size, image.mode)

        self.image = star_image
        self.rect = self.image.get_rect(midtop=(x, y))
        self.speed = speed

        # Load music byte data
        music_data = base64.b64decode(bonus)
        self.sound = pygame.mixer.Sound(music_data)
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
