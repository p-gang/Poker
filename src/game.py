from src.table import Table
from src.player import Player
from src.bot import bot

class Game:
    def __init__(self):
        player1 = Player(0, 'Winston')
        player1.small_blind = True
        player2 = bot(1, 'Adolf')
        player2.big_blind = True
        player3 = (2, 'Franklin')
        player4 = bot(3, 'Joseph')
        player5 = bot(4, 'Benito')

        self.is_starting = True
        self.table = Table([player1, player2, player3, player4, player5])
        self.is_dead = False


    def start_game(self):
        self.status = "player_turn"
        # ans = self.table.change_blind()
        # self.table.take_blind(ans[0], ans[1])
        # self.table.take_cards()
        # self.table.pre_flop()
        # if self.is_dead is True:
        #     self.start_game()
