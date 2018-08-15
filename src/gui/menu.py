import sys

import pygame

from src.gui.button import Button
from src.gui.scene import Scene
from src.game import Game

class MainMenu(Scene):
    done = False

    def __init__(self, frame_rate, size, screen):
        super().__init__(frame_rate, size, screen)

        self.size = size
        self.screen = screen
        self.bg_img = pygame.transform.scale(pygame.image.load("images/bg_blured.png"), self.size)
        self.create_menu()
        self.run()

    def run(self):
        while not self.done:
            self.handle_events()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type in (pygame.MOUSEBUTTONDOWN,
                              pygame.MOUSEBUTTONUP,
                              pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def create_menu(self):
        self.screen.blit(self.bg_img, (0, 0))
        for i, (text, handler) in enumerate((('PLAY', self.on_play),
                                             ('QUIT', self.on_quit))):
            btn = Button((self.size[0] - 130) // 2,
                         (self.size[1] - 50) // 2 + 65 * i,
                         130,
                         50,
                         text,
                         (0, 5, 255),
                         "DejaVuSans",
                         16,
                         handler,
                         padding=5)
            self.objects.append(btn)
            self.menu_buttons.append(btn)
            self.mouse_handlers.append(btn.handle_mouse_event)

    def on_play(self, button):
        self.done = True
        for btn in self.menu_buttons:
            self.objects.remove(btn)
        game = Game()
        game.start_game()
        # game = Game()
        # game.start_game()

    def on_quit(self, button):
        sys.exit()
