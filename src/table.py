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
    return combination1, player1

class Table:
    _cards = []
    def __init__(self, players):
        self.players = players
        self.bank = 0
        self.blind = [10, 20]
        self.table_cards = []
        self.bet = 0
        self.playerturn = False

    def find_small_blind_player(self):
        p = self.players[0]
        for player in self.players:
            if player.small_blind:
                player.small_blind = False
                p = player
                break
        return p

    def set_up_que(self):
        que = []
        length = len(self.players)
        que.append(self.find_small_blind_player())
        ind = que[0].index
        if ind + 1 <= length:
            for i in range(ind + 1, length):
                que.append(self.players[i])
        if ind - 1 >= 0:
            for i in range(ind - 1, -1, -1):
                que.append(self.players[i])
        return que


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

    def take_blind(self, small_blind_player, big_blind_player):
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
        while card in self._cards:
            card = Card()
        self._cards.append(card)
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

    def player_turn(self):
        self.playerturn = True

    def check(self, player):
        pass

    def call(self, player):
        self.bank += self.bet
        player.money -= self.bet

    def bet(self, player):
        self.bank += self.bet
        player.money -= self.bet
        self.bet += self.bet

    def fold(self, player):
        self.players.remove(player)

    def ask_players(self):
        que = self.set_up_que()
        for player in que:
            if player.index == 0:
                for i in range(10000000000):
                    pass
            else:
                player.bot_decision(self)

    def pre_flop(self):
        self.ask_players()
        if self.check_on_one_player():
            return True

    def flop(self):
        for i in range(3):
            self.take_card_on_table()
            self.ask_players()
        if self.check_on_one_player():
            return True

    def turn(self):
        self.take_card_on_table()
        self.ask_players()
        if self.check_on_one_player():
            return True

    def river(self):
        self.take_card_on_table()
        self.ask_players()
        if self.check_on_one_player():
            return True

    def set_comb(self):
        check = Checker()
        for player in self.players:
            player.set_combination(check.find_combination(player.cards, self.table_cards))

    def winner(self):
        self.set_comb()
        winner_combination = [-1, -1]
        player_win = self.players[0]
        for player in self.players:
            print(player_win)
            print(player_win.get_combination())
            if player_win.get_combination()[0] < player.get_combination()[0]:
                player_win = player
                winner_combination = player.get_combination()

            if winner_combination[0] == player.get_combination()[0]:
                better_combination = check_better_combination(winner_combination, player.get_combination(), player_win, player)
                winner_combination = better_combination[0]
                player_win = better_combination[1]
        player_win.money += self.bank
        self.bank = 0
        return True
