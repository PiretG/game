import pygame
import pygame.gfxdraw


class QuestionSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, text):
        super().__init__()
        self.image = pygame.Surface((300, 300), pygame.SRCALPHA)
        self.color = (255, 255, 255)
        self.backcolor = None
        self.pos = (x, y)
        self.font = pygame.font.SysFont('Arial', 20)
        self.active = False
        self.text = text
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surface, text_rect)
        self.rect = self.image.get_rect(center=self.pos)


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
