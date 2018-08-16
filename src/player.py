from src import table
from src.entity import Entity


class Player(Entity):

    def __init__(self, index):
        self.cards = []
        self.money = 2000
        self.combination = []
        self.big_blind = False
        self.small_blind = False
        self.index = index

    def get_combination(self):
        return self.combination

    def set_combination(self, combination):
        self.combination = combination

    def check(self):
        pass

    def fold(self, table):
        table.players.remove(self)

    def call(self, table):
        table.bank += table.bet
        self.money -= table.bet

    def bet(self, table, bet):
        table.bank += bet
        self.money -= bet
        table.bet += bet

