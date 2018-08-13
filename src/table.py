from src.card import Card
from src.checker import Checker


def check_better_combination(self, combination1, combination2, player1, player2):
    if combination1 == 2:
        if combination1[1] > combination2[1]:
            return combination1, player1
        elif combination1[2] > combination2[2]:
            return combination1, player1
        if combination1[1] < combination2[1]:
            return combination2, player2
        elif combination1[2] < combination2[2]:
            return combination2, player2
    if combination1[1] > combination2[1]:
        return combination1, player1
    elif combination1[1] < combination2[1]:
        return combination2, player2


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


    def winner(self):
        check = Checker()
        winner_combination = []
        player_win = None
        for player in self.players():
            player.set_combination(check.find_combination(player.cards, self.table_cards))
            if player_win is None or winner_combination[0] < player.get_combination()[0]:
                player_win = player
                winner_combination = player.get_combination()
            elif winner_combination[0] == player.get_combination()[0]:
                ans = check_better_combination(winner_combination, player.get_combination(), player_win, player)[0]
                winner_combination = ans[0]
                player_win = ans[1]
        player_win.money += self.bank
        self.bank = 0
