import pygame
import random
import sys

from player import Player
from question import QuestionSprite
from star import Star
from textinputbox import TextInputBox
from questions import level_1_questions
from obstacle import Asteroid


class Game:
    def __init__(self, x, y, speed):
        self.points = 0

        # Player setup
        player_sprite = Player((width / 2, height), width, speed)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Star setup
        star_sprite = Star(x, y, speed)
        self.star = pygame.sprite.GroupSingle(star_sprite)

        # Asteroids setup
        self.asteroids = []
        asteroid_y = 5
        for _ in range(10):
            asteroid = Asteroid(random.randint(10, width), asteroid_y, speed)
            # Set lag so that wouldn't appear all at once
            asteroid_y -= 30
            asteroid_sprite = pygame.sprite.GroupSingle(asteroid)
            asteroid_sprite.draw(screen)
            self.asteroids.append(asteroid_sprite)

        # Questions list setup
        questions = level_1_questions
        random.shuffle(level_1_questions)

        # Create group of all questions and group of answer boxes
        questions_list = []
        text_boxes = []
        for q in questions:
            q_sprite = QuestionSprite(250, 200, q.question)
            t_sprite = TextInputBox(100, 250, 250, q.answer, self)
            questions_list.append(pygame.sprite.GroupSingle(q_sprite))
            text_boxes.append(pygame.sprite.GroupSingle(t_sprite))
        self.questions_list = questions_list
        self.text_boxes = text_boxes

    def run(self):
        self.player.update()
        self.star.update(height, width, self.player.sprite.rect.x, self.player.sprite.rect.y)
        self.player.draw(screen)
        self.star.draw(screen)

        for asteroid in self.asteroids:
            asteroid.update(height, width, self.player.sprite.rect.x, self.player.sprite.rect.y)
            asteroid.draw(screen)

    def collision(self):
        return abs(self.player.sprite.rect.x - self.star.sprite.rect.x) <= 50 \
               and abs(self.player.sprite.rect.y - self.star.sprite.rect.y) <= 20

    def ask_question(self, event_list):
        # Take first question and textbox with correct answer from list
        question = self.questions_list[0]
        text_box = self.text_boxes[0]
        question.draw(screen)
        text_box.draw(screen)
        text_box.update(event_list)

        # Check if sprite has been killed
        if len(text_box.sprites()) == 0:
            # Remove question sprite
            question.sprite.kill()

            # Make star appear
            self.star.sprite.rect.x = random.randint(10, width)
            self.star.sprite.rect.y = 5
            self.star.draw(screen)

            # Remove used question and text box from questions list
            self.questions_list.pop(0)
            self.text_boxes.pop(0)


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
    speed = 3

    time = pygame.time.Clock()
    game = Game(star_x, star_y, speed)

    while len(game.questions_list) > 0:
        time.tick(40)
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, n))
        screen.blit(bg, (0, -height + n))

        if n == height:
            screen.blit(bg, (0, -height + n))
            n = 0
        n += 1

        font = pygame.font.SysFont('Arial', 20)
        text = font.render("Punktid: " + str(game.points), True, (255, 255, 255))
        screen.blit(text, (0, 0))

        event_list = pygame.event.get()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game.collision():
            game.ask_question(event_list)
        else:
            game.run()

        pygame.display.update()
