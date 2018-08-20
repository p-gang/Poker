
from src.entity import Entity


class Player(Entity):

    def __init__(self, index, name):
        self.cards = []
        self.money = 2000
        self.combination = []
        self.big_blind = False
        self.small_blind = False
        self.index = index
        self.name = name

    def get_combination(self):
        return self.combination

    def set_combination(self, combination):
        self.combination = combination

