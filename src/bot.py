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

    def get_combination(self):
        return self.combination

    def set_combination(self, combination):
        self.combination = combination

    def bot_decision(self, table):
        var = self.check_cards()
        if var < 3:
            if table.bet == 0:
                self.bet(table, var)
            else:
                self.cards(table)
        else:
            if table.bet == 0:
                self.call(table)
            else:
                self.fold(table)

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

