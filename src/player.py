from src import table
from src.entity import Entity


class Player(Entity):

    def __init__(self):
        self.cards = ()
        self.money = 0

    def check(self):
        pass

    def fold(self, table):
        table.players.remove(self)

    def call(self, table):
        table.bank += table.bet
        self.money -= table.bet

    def bet(self, table):
        k = self.ask_bet()
        table.bank += k
        self.money -= k
        table.bet += k

    def ask_player(self):
        print("Bet is ", table.table.bet, "\n")
        print("What do you want to do?\n")
        print("input 1 if Check\n")
        print("input 2 if Fault\n")
        print("input 3 if Call\n")
        print("input 4 if Bet\n")
        s = int(input())
        if s == 1:
            self.check()

        if s == 2:
            self.fault(table)

        if s == 3:
            self.call(table)

        if s == 4:
            self.bet(table)

    def ask_bet(self):
        print("So,input how much bet you want to do?")
        s = int(input())
        print("Raise", s)
        return s