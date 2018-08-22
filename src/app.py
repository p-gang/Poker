from src.game import Game
from src.gui.betui import BetObject
from src.gui.cardui import CardObject, CardIconObject
from src.gui.menu import *
from src.gui.music import MusicController
from src.gui.playerui import PlayerObject
from src.gui.scene import Scene


class App(Scene):
    def __init__(self, frame_rate, size, screen):
        super().__init__(frame_rate, size, screen)

        self.size = size
        self.screen = screen
        self.seats = (
            (925, 850), (385, 755), (385, 300), (1450, 300), (1450, 755))
        self.music_control = MusicController()
        self.game = Game()
        self.table = self.game.table

        self.create_menu("main")

    def run(self):
        while True:
            self.screen.blit(self.bg_img, (0, 0))

            self.states()
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.create_menu("game")
            elif event.type == self.music_control.MUSENDEVENT:
                self.music_control.start_next()
            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def states(self):
        if self.game.is_starting:
            self.draw_start()
        if self.game.status == "player_turn":
            self.draw_turn()
        if self.game.status == "draw_bet":
            self.draw_bet()
        if self.game.status == "game_cards_taken":
            self.draw_table_cards()

    def draw_start(self):
        for index, player in enumerate(self.table.players):
            self.draw_player(index, player)
            self.draw_cards(index, player)

    def draw_turn(self):
        menu = TurnMenu(self.frame_rate, self.size, self.screen, self.game,
                        self.music_control, self.table, self.objects)
        menu.create_menu()
        self.objects = []
        self.game.status = ""

    def draw_bet(self):
        bet = 500

        obj = BetObject(925, 720, 25, 25, str(bet))
        self.objects.append(obj)

    def draw_player(self, index, player):
        obj = PlayerObject(self.seats[index], player.name, str(player.money))
        self.objects.append(obj)

    def draw_cards(self, index, player):
        if index == 0:
            for i, card in enumerate(player.cards):
                obj = CardObject((self.size[0] - 300 + 40 * i, self.size[1] - 300), card, -20 * i)
                self.objects.append(obj)
        else:
            obj = CardIconObject(self.seats[index], player.cards)
            self.objects.append(obj)

    def draw_table_cards(self):
        for i, card in enumerate(self.table.table_cards):
            obj = CardObject((650 + 130 * i, self.size[1] / 2 - 100), card, 0)
            self.objects.append(obj)

    def create_menu(self, role):
        if role == "main":
            menu = MainMenu(self.frame_rate, self.size, self.screen, self.game, self.music_control)
        else:
            menu = GameMenu(self.frame_rate, self.size, self.screen, self.game, self.music_control)
        menu.create_menu()
