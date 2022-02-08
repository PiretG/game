import pygame, random


class Star(pygame.sprite.Sprite):

    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect(midtop=(x, y))
        self.speed = speed

    def appear(self, x, y):
        self.rect = self.image.get_rect(midtop=(x, y))

    def update(self, height, width, ship_x, ship_y):
        if self.rect.y >= height or self.collision(ship_x, ship_y):
            self.appear(random.randint(10, width), 5)
        else:
            self.rect.y += self.speed

    def collision(self, ship_x, ship_y):
        return abs(self.rect.x - ship_x) <= 20 and abs(self.rect.y - ship_y) <= 20

    def constraint(self, height):
        if self.y > height:
            self.kill()

    def kill(self):
        self.y = 0
        self.x = random.uniform(0, 640)
        #self.vy = random.uniform(1, 2)
