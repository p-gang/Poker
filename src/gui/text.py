import pygame


class TextObject:
    def __init__(self, x, y, text, color, font_name, font_size):
        info_obj = pygame.display.Info()
        kx = 1920 / info_obj.current_w
        ky = 1080 / info_obj.current_h
        self.pos = (x / kx, y / ky)
        self.text_func = text
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.bounds = self.get_screen(text)

    def draw(self, screen, centralized=False):
        text_screen, self.bounds = self.get_screen(self.text_func)

        if centralized:
            pos = (self.pos[0] - self.bounds.width // 2,
                   self.pos[1])
        else:
            pos = self.pos
        screen.blit(text_screen, pos)

    def get_screen(self, text):
        text_screen = self.font.render(text,
                                       False,
                                       self.color)
        return text_screen, text_screen.get_rect()

    def update(self):
        pass
