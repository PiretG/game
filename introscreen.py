import pygame


class Button:
    def __init__(self, text, pos, font, game, screen, bg="black"):
        self.x, self.y = pos
        self.screen = screen
        self.game = game
        self.font = pygame.font.SysFont("Arial", font)
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def close(self):
        self.game.intro = False

    def pack(self):
        self.screen.blit(self.surface, (self.x, self.y))

    def clicked(self):
        """ Returns 1 if you click on the button """

    def mouse_click(self, event):
        """ checks if you click the mouse button and then if it's on the button """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                print(self)
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
