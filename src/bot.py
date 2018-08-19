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

    def check_on_same_rank(self, card1, card2):
        return card1.get_rank() == card2.get_rank()

    def check_on_same_suit(self, card1, card2):
        return card1.get_suit() == card2.get_suit()

    def check_cards(self):
        card1 = self.cards[0]
        card2 = self.cards[1]
        same_rank = self.check_on_same_rank(card1, card2)
        same_suit = self.check_on_same_suit(card1, card2)
        if same_rank:
            return 1
        if abs(card1.get_rank() - card2.get_rank()) == 1:
            if same_suit:
                return 2
            return 3
        if same_suit:
            return 4
        else:
            return 5
