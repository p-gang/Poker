from src.player import Player
from src.table import Table

class bot(Player):



    def __init__(self, index):
        self.money = 2000
        self.big_blind = False
        self.small_blind = False
        self.cards = []
        self.combination = []
        self.index = index

    def marking_situation(self, hand, bank):
        pass



