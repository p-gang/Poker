import pygame

from src.gui.color import Color
from src.gui.object import GameObject


class CardObject(GameObject):
    def __init__(self, coord, card, angle):
        super().__init__(*coord, 120, 200)
        
        path = "images/cards/" + card.get_suit().lower()[0] + str(card.get_rank()) + ".png"

        self.card_img = pygame.image.load(path)
        self.card_img = pygame.transform.scale(self.card_img, self.bounds.size)
        self.card_img = pygame.transform.rotate(self.card_img, angle)

    def draw(self, screen):
        screen.blit(self.card_img, (self.bounds.x, self.bounds.y))

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
