from src.card import Card
from src.checker import Checker


def check_better_combination(combination1, combination2, player1, player2):
    if combination1 == 2:
        if combination1[1] > combination2[1] or combination1[2] > combination2[2]:
            return combination1, player1
        if combination1[1] < combination2[1] or combination1[2] < combination2[2]:
            return combination2, player2
    if combination1[1] > combination2[1]:
        return combination1, player1
    elif combination1[1] < combination2[1]:
        return combination2, player2
    return True


class Table:

    def __init__(self, players):
        self.players = players
        self.bank = 0
        self.blind = [10, 20]
        self.cards = []
        self.table_cards = []
        self.bet = 0

    def find_small_blind_player(self):
        for player in self.players:
            if player.small_blind:
                player.small_blind = False
                return player

    def change_blind(self):
        length = len(self.players)
        player = self.find_small_blind_player()
        player.small_blind = False
        index = player.index
        self.players[(index + 1) % length].big_blind = False
        self.players[(index + 1) % length].small_blind = True
        self.players[(index + 2) % length].big_blind = True
        small_blind_player = self.players[(index + 1) % length]
        big_blind_player = self.players[(index + 2) % length]
        return small_blind_player, big_blind_player

    def take_blind(self, big_blind_player, small_blind_player):
        big_blind_player.money -= self.blind[1]
        small_blind_player.money -= self.blind[0]
        self.bank = self.blind[1] + self.blind[0]

    def take_cards(self):
        for player in self.players:
            for _ in range(2):
                card = self.get_random_card()
                player.cards.append(card)

    def get_random_card(self):
        card = Card()
        while card in self.cards:
            card = Card()
        return card

    def check_on_one_player(self):
        if len(self.players) == 1:
            self.players[0].money += self.bank
            bank = 0
            return True
        return False

    def take_card_on_table(self):
        card = self.get_random_card()
        self.table_cards.append(card)

    def pre_flop(self):
        if self.check_on_one_player():
            return True

    def flop(self):
        for i in range(3):
            self.take_card_on_table()
        if self.check_on_one_player():
            return True

    def turn(self):
        self.take_card_on_table()
        if self.check_on_one_player():
            return True

    def river(self):
        self.take_card_on_table()
        if self.check_on_one_player():
            return True

    def set_comb(self):
        check = Checker()
        for player in self.players:
            player.set_combination(check.find_combination(player.cards, self.table_cards))

    def winner(self):
        self.set_comb()
        winner_combination = self.players[0].combination
        player_win = self.players[0]
        for player in self.players:
            if winner_combination[0] < player.get_combination()[0]:
                player_win = player
                winner_combination = player.get_combination()
            if winner_combination[0] == player.get_combination()[0]:
                better_combination = \
                check_better_combination(winner_combination, player.get_combination(), player_win, player)[0]
                winner_combination = better_combination[0]
                player_win = better_combination[1]
        player_win.money += self.bank
        self.bank = 0

        return True
