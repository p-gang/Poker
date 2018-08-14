import sys

import pygame

from src.gui.menu import MainMenu
from src.gui.scene import Scene


class App(Scene):

    def __init__(self, frame_rate, size, screen):
        super().__init__(frame_rate, size, screen)

        self.size = size
        self.screen = screen
        pygame.mixer.music.load('sounds/stressed_out.ogg')
        pygame.mixer.music.play(-1, 0.0)

        self.create_menu()

    def run(self):
        while True:
            self.screen.blit(self.bg_img, (0, 0))

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
                self.create_menu()

    def create_menu(self):
        MainMenu(self.frame_rate, self.size, self.screen)
