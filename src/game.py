from src.table import Table
from src.player import Player


class Game:
    def __init__(self):
        player1 = Player(0, 'Kevin')
        player1.small_blind = True
        player2 = Player(1, 'Adolf')
        player2.big_blind = True
        self.table = Table([player1, player2])
        self.is_dead = False


    def start_game(self):
        self.status = "game_start"
        # ans = self.table.change_blind()
        # self.table.take_blind(ans[0], ans[1])
        # self.table.take_cards()
        # self.table.pre_flop()
        # if self.is_dead is True:
        #     self.start_game()
