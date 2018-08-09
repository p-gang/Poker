from src.card import Card


class Table:

    def __init__(self, players):
        self.players = players
        self.bank = 0
        self.blind = [10, 20]
        self.cards = []
        self.table_cards = []
        self.bet = 0

    def take_blind(self, big_blind_player, small_blind_player):
        big_blind_player.money -= self.blind[1]
        small_blind_player.money -= self.blind[0]
        self.bank = self.blind[1] + self.blind[0]

    def take_cards(self):
        for p in self.players:
            for i in range(2):
                card = self.get_random_card()
                p.cards += card

    def get_random_card(self):
        card = Card()
        while card in self.cards:
            card = card.Card()
        self.cards += card
        return card.Card()

    def take_card_on_table(self):
        card = Card()
        self.table_cards += card

    def pre_flop(self):
        for p in self.players:
            p.ask_player()

    def flop(self):
        for i in range(3):
            self.take_card_on_table()
        for p in self.players:
            p.ask_player()

    def turn(self):
        self.take_card_on_table()
        for p in self.players:
            p.ask_player()

    def river(self):
        self.take_card_on_table()
        for p in self.players:
            p.ask_player()