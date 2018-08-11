#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from src.game import Game
from src.gui import PokerWindow


if __name__ == '__main__':
    app = QApplication([])
    poker = PokerWindow()
    sys.exit(app.exec_())
