from time import sleep

from src.player import Player
from src.table import Table


class Game:
    def __init__(self):
        player1 = Player(0, 'Winston')
        player1.small_blind = True
        player2 = Player(1, 'Adolf')
        player2.big_blind = True
        player3 = Player(2, 'Franklin')
        player4 = Player(3, 'Joseph')
        player5 = Player(4, 'Benito')

        self.table = Table([player1, player2, player3, player4, player5])
        self.is_starting = True

    def start_game(self):
        ans = self.table.change_blind()
        self.table.take_blind(ans[0], ans[1])
        self.table.take_cards()
