import pygame

from src.gui.color import Color
from src.gui.object import GameObject
from src.gui.text import TextObject


class PlayerObject(GameObject):
    def __init__(self, seat, name, money):
        super().__init__(*seat, 50, 50)

        x, y = seat

        padding = 5
        self.name = TextObject(self.bounds.x + padding,
                               self.bounds.y + padding, name,
                               Color.GREEN.value,
                               "DejaVuSans",
                               int(16))

        self.money = TextObject(self.bounds.x + padding - 70,
                                self.bounds.y + padding + 2, money,
                               Color.GREEN.value,
                               "DejaVuSans",
                               int(16))

    def draw(self, screen):
        pygame.draw.rect(screen, Color.GREY.value, self.bounds)

        self.name.draw(screen)
        self.money.draw(screen)

    def update(self):
        pass