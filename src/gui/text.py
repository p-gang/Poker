import pygame


class TextObject:
    def __init__(self, x, y, text, color, font_name, font_size):
        self.pos = (x, y)
        self.text_func = text
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.bounds = self.get_screen(text)

    def draw(self, surface, centralized=False):
        text_surface, self.bounds = self.get_screen(self.text_func)

        if centralized:
            pos = (self.pos[0] - self.bounds.width // 2,
                   self.pos[1])
        else:
            pos = self.pos
        surface.blit(text_surface, pos)

    def get_screen(self, text):
        text_screen = self.font.render(text,
                                       False,
                                       self.color)
        return text_screen, text_screen.get_rect()

    def update(self):
        pass
