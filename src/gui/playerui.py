import pygame

from src.gui.color import Color
from src.gui.object import GameObject
from src.gui.text import TextObject


class PlayerObject(GameObject):
    def __init__(self, seat, name, money):
        info_obj = pygame.display.Info()
        kx = 1920 / info_obj.current_w
        ky = 1080 / info_obj.current_h
        super().__init__(*seat, 50 / kx, 50 / ky)

        x, y = seat

        padding = 5
        self.name = TextObject(x + padding,
                               y + padding, name,
                               Color.GREEN.value,
                               "DejaVuSans",
                               int(16))

        self.money = TextObject(x + padding - 70,
                               y + padding + 2, money,
                               Color.GREEN.value,
                               "DejaVuSans",
                               int(16))

    def draw(self, screen):
        pygame.draw.rect(screen, Color.GREY.value, self.bounds)

        self.name.draw(screen)
        self.money.draw(screen)

    def update(self):
        pass