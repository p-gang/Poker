from src.gui.menu import *
from src.gui.music import MusicController
from src.gui.playerui import PlayerObject
from src.gui.scene import Scene


class CardObject(object):
    pass


class App(Scene):

    def __init__(self, frame_rate, size, screen):
        super().__init__(frame_rate, size, screen)

        self.size = size
        self.screen = screen

        self.seats = ((925, 850), (385, 755), (385, 300), (1450, 300), (1450, 755))
        self.music_control = MusicController()
        self.game_control = Game()
        self.game_status = self.game_control.table

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

    def states(self):
        if self.game_control.status == "game_start":
            self.draw_start()
        if self.game_control.status == "player_turn":
            self.draw_turn()

    def draw_start(self):
        for index, player in enumerate(self.game_status.players):
            self.draw_player(index, player)
            #self.draw_card(player)

    def draw_player(self, index, player):
        obj = PlayerObject(self.seats[index], player.name)
        self.objects.append(obj)

    def draw_card(self, index, player):
        obj = CardObject(self.seats[index], player.name)
        self.objects.append(obj)

    def create_menu(self, role):
        if role == "main":
            menu = MainMenu(self.frame_rate, self.size, self.screen, self.game_control, self.music_control)
            menu.create_menu()
        elif role == "game":
            menu = GameMenu(self.frame_rate, self.size, self.screen, self.game_control, self.music_control)
            menu.create_menu()
