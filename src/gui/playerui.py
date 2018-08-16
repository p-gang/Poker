import pygame

from src.gui.color import Color
from src.gui.object import GameObject
from src.gui.text import TextObject


class PlayerObject(GameObject):
    def __init__(self, seat, name):
        super().__init__(*seat, 50, 50)

        x, y = seat
        self.name = name

        padding = 5
        self.text = TextObject(x + padding,
                               y + padding, name,
                               Color.GREEN.value,
                               "DejaVuSans",
                               16)

    def draw(self, screen):
        pygame.draw.rect(screen, Color.GREY.value, self.bounds)

        self.text.draw(screen)

    def update(self):
        pass