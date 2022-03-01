import pygame
import sys


class Button:
    def __init__(self, text, pos, font, game, screen, bg="black"):
        self.x, self.y = pos
        self.screen = screen
        self.game = game
        self.font = pygame.font.SysFont("Arial", font)
        self.text = self.font.render(text, True, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def close(self, level):
        if level == 0:
            self.game.intro = False
        else:
            self.game.level = level

    def pack(self):
        self.screen.blit(self.surface, (self.x, self.y))

    def mouse_click(self, event):
        """ checks if you click the mouse button and then if it's on the button """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.clicked():
                    return 1
                    pass
        return 0

    def clicked(self):
        """ checks if the mouse is on the button """
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            return 1
            pass
        return 0


class Button2:
    def __init__(self, text, pos, font, game, screen, bg="black"):
        self.x, self.y = pos
        self.screen = screen
        self.game = game
        self.font = pygame.font.SysFont("Arial", font)
        self.text = self.font.render(text, True, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def close(self):
        self.game.intro = False
        self.game.end = True

    def pack(self):
        self.screen.blit(self.surface, (self.x, self.y))

    def mouse_click(self, event):
        """ checks if you click the mouse button and then if it's on the button """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.clicked():
                    pygame.quit()
                    sys.exit()

    def clicked(self):
        """ checks if the mouse is on the button """
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            pygame.quit()
            sys.exit()


class Button3:
    def __init__(self, text, pos, font, game, screen, bg="black"):
        self.x, self.y = pos
        self.screen = screen
        self.game = game
        self.font = pygame.font.SysFont("Arial", font)
        self.text = self.font.render(text, True, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def close(self):
        self.game.end = False
        self.game.intro = True
        self.game.level = 0

    def pack(self):
        self.screen.blit(self.surface, (self.x, self.y))

    def mouse_click(self, event):
        """ checks if you click the mouse button and then if it's on the button """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.clicked():
                    return 1
                    pass
        return 0

    def clicked(self):
        """ checks if the mouse is on the button """
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            return 1
            pass
        return 0
