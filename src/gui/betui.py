import pygame

from src.gui.color import Color
from src.gui.object import GameObject
from src.gui.text import TextObject


class BetObject(GameObject):
    def __init__(self, x, y, w, h, bet):
        super().__init__(x, y, w, h)

        self.text = TextObject(self.bounds.x + self.bounds.width + 15,
                               self.bounds.y + 2, "Кто прочитал, тот сдохнет",
                               Color.GREEN.value,
                               "DejaVuSans",
                               int(16))

    def draw(self, screen):
        pygame.draw.rect(screen, Color.GREY.value, self.bounds)
        self.text.draw(screen)

    def update(self):
        pass
