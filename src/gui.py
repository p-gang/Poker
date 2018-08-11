from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter

class Game(QFrame):
    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Left:
           pass
        else:
            pass

    def update_status(self):
       pass


class PokerWindow(QMainWindow):

    def __init__(self, game):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setCentralWidget(self.Game)


        self.setWindowTitle('Poker')
        self.resize(600, 600)
        self.center()
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)
