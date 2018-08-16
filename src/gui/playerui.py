import pygame

from src.gui.color import Color
from src.gui.object import GameObject
from src.gui.text import TextObject


class PlayerObject(GameObject):
    def __init__(self, x, y, name):
        super().__init__(x, y, 50, 50)

        self.name = name

        padding = 5
        self.text = TextObject(x + padding,
                               y + padding, name,
                               Color.GREEN,
                               "DejaVuSans",
                               16)

    def draw(self, screen):
        pygame.draw.rect(screen, Color.GREY, self.bounds)

        self.text.draw()

    def update(self):
        pass