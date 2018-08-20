import pygame

from src.gui.color import Color
from src.gui.object import GameObject


class CardObject(GameObject):
    def __init__(self, coord, card, angle):
        x, y = coord
        self.coord = coord
        self.size = 120, 200

        super().__init__(x, y, *self.size)

        path = "images/cards/" + card.get_suit().lower()[0] + str(card.get_rank()) + ".png"

        self.card_img = pygame.image.load(path)
        self.card_img = pygame.transform.scale(self.card_img, self.size)
        self.card_img = pygame.transform.rotate(self.card_img, angle)

    def draw(self, screen):
        screen.blit(self.card_img, (self.bounds[0], self.bounds[1]))

    def update(self):
        pass


class CardIconObject(GameObject):
    def __init__(self, seat, cards):
        x, y = seat

        super().__init__(x + 45, y + 45, 50, 50)

        self.cards = cards

        padding = 5

    def draw(self, screen):
        pygame.draw.rect(screen, Color.GREY.value, self.bounds)

    def update(self):
        pass
