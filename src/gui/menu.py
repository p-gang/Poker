import sys

from src.gui.button import *
from src.gui.scene import Scene


class MainMenu(Scene):
    done = False

    def __init__(self, frame_rate, size, screen, game, music_control):
        super().__init__(frame_rate, size, screen)

        self.game = game
        self.music_control = music_control
        self.BUTTONS = (('PLAY', self.on_play),
                        ('QUIT', self.on_quit))

        self.size = size
        self.screen = screen
        self.bg_img = pygame.transform.scale(pygame.image.load("images/bg_blured.png"), self.size)

    def run(self):
        while not self.done:
            self.screen.blit(self.bg_img, (0, 0))

            self.handle_events()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
        self.bg_img = pygame.transform.scale(pygame.image.load("images/bg.png"), self.size)
        self.screen.blit(self.bg_img, (0, 0))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == self.music_control.MUSENDEVENT:
                self.music_control.start_next()
            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def append_btn(self, btn):
        self.objects.append(btn)
        self.menu_buttons.append(btn)
        self.mouse_handlers.append(btn.handle_mouse_event)

    def create_menu(self, role=""):
        self.screen.blit(self.bg_img, (0, 0))
        for i, (text, handler) in enumerate(self.BUTTONS):
            btn = Button((self.size[0] - 130) // 2,
                         (self.size[1] - 50) // 2 + 65 * i - 65,
                         130,
                         50,
                         text,
                         (0, 5, 255),
                         "DejaVuSans",
                         16,
                         handler,
                         padding=5)
            self.append_btn(btn)
        state = "toggled" if self.music_control.is_paused() else "normal"
        sound_btn = ToggleButton(self.size[0] - 100, self.size[1] - 100, 50, 50, 'S', (0, 5, 255),
                                 "DejaVuSans",
                                 16,
                                 self.on_sound,
                                 padding=5,
                                 state=state)
        self.append_btn(sound_btn)
        self.run()

    def on_play(self, button):
        self.done = True

        self.game.start_game()

    def on_sound(self, button):
        self.music_control.toggle()

    def on_quit(self, button):
        sys.exit()


class GameMenu(MainMenu):
    done = False

    def __init__(self, frame_rate, size, screen, game, music_control):
        super().__init__(frame_rate, size, screen, game, music_control)

        self.BUTTONS = (('Resume', self.on_resume),
                        ('New game', self.on_play),
                        ('Back', self.on_back),
                        ('QUIT', self.on_quit))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.on_resume()
            elif event.type == self.music_control.MUSENDEVENT:
                self.music_control.start_next()
            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def on_resume(self, button=None):
        self.done = True

    def on_back(self, button):
        self.on_resume()
        menu = MainMenu(self.frame_rate, self.size, self.screen, self.game, self.music_control)
        menu.create_menu()


class TurnMenu(GameMenu):
    done = False

    def __init__(self, frame_rate, size, screen, game, music_control, game_status, objects):
        super().__init__(frame_rate, size, screen, game, music_control)

        self.objects = objects
        self.game_status = game_status
        self.BUTTONS = (('Call', self.on_call),
                        ('Check', self.on_check),
                        ('Fold', self.on_fold))

    def run(self):
        while not self.done:
            self.handle_events()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                menu = GameMenu(self.frame_rate, self.size, self.screen, self.game, self.music_control)
                menu.create_menu()
            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def create_menu(self, role=""):
        for i, (text, handler) in enumerate(self.BUTTONS):
            btn = Button(1000 + 110 * i,
                         700,
                         90,
                         50,
                         text,
                         (0, 5, 255),
                         "DejaVuSans",
                         16,
                         handler,
                         padding=5)
            self.append_btn(btn)
        self.run()

    def on_call(self, button):
        self.done = True
        self.game_status.call(self.game_status.players[0])

    def on_check(self, button):
        self.done = True
        self.game_status.call(self.game_status.players[0])

    def on_fold(self, button):
        self.done = True
        self.game_status.call(self.game_status.players[0])
