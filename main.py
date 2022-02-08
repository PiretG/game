import pygame
import random
import sys

from player import Player
from question import Question
from star import Star
from textinputbox import TextInputBox


class Game:
    def __init__(self, x, y, speed):
        #player setup
        player_sprite = Player((width / 2, height), width, speed)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        #star setup
        star_sprite = Star(x, y, speed)
        self.star = pygame.sprite.GroupSingle(star_sprite)
        #question setup
        question_sprite = Question(250, 200, "This is Question nr 1")
        self.question = pygame.sprite.GroupSingle(question_sprite)
        #textbox setup
        box_sprite = TextInputBox(100, 250, 300)
        self.box = pygame.sprite.GroupSingle(box_sprite)

    def run(self, event_list):
        self.player.update()
        self.star.update(height, width, self.player.sprite.rect.x, self.player.sprite.rect.y)
        self.box.update(event_list)
        self.player.draw(screen)
        self.star.draw(screen)
        self.box.draw(screen)

        self.question.update()
        self.question.draw(screen)


if __name__ == '__main__':
    pygame.init()
    width = 500
    height = 500
    screen = pygame.display.set_mode([width, height])
    background = pygame.image.load("background.jpg")
    bg = pygame.transform.scale(background, (width, height))

    n = 0
    star_x = random.randint(10, width)
    star_y = 5
    speed = 5
    time = pygame.time.Clock()
    game = Game(star_x, star_y, speed)

    fly = True
    while fly:
        time.tick(40)
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, n))
        screen.blit(bg, (0, -height + n))

        if n == height:
            screen.blit(bg, (0, -height + n))
            n = 0
        n += 1

        event_list = pygame.event.get()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.run(event_list)
        pygame.display.update()
