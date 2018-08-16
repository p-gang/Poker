import random


class Card:
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")

    def __init__(self, rank="", suit=""):
        if rank == "" or suit == "":
            self.suit = random.choice(self.RANKS)
            self.rank = random.choice(self.SUITS)
        else:
            self.suit = suit
            self.rank = rank

    def __repr__(self):
        return str(self.suit) + " : " + str(self.rank)

    def __eq__(self, other):
        return self.get_rank() == other.get_rank() and self.get_suit() == other.get_suit()

    def __lt__(self, other):
        if self.get_rank() < self.get_rank():
            return True

    def __gt__(self, other):
        if self.get_rank() > self.get_rank():
            return True

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit
