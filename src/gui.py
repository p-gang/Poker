from PyQt5.QtWidgets import *


class Game(QGraphicsScene):

    def __init__(self):
        super().__init__()

        self.set_scene()

    def set_scene(self):
        pass


class PokerWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'Poker'
        self.width = 640
        self.height = 480

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.showFullScreen()