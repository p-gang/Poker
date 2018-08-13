import pygame
import sys

from src.gui.button import Button


class MainMenu:
    done = False

    def __init__(self, frame_rate, size):
        self.frame_rate = frame_rate
        self.bg_blured_img = pygame.transform.scale(pygame.image.load("images/bg_blured.png"), size)

        self.size = size
        self.clock = pygame.time.Clock()
        self.objects = []
        self.mouse_handlers = []
        self.menu_buttons = []
        self.screen = pygame.display.set_mode(size)

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

    def draw(self):
        for object in self.objects:
            object.draw(self.screen)

    def create_menu(self):
        self.screen.blit(self.bg_blured_img, (0, 0))
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

    def on_quit(self, button):
        sys.exit()
