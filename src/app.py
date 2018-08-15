import sys

import pygame

from src.gui.menu import *
from src.gui.music import MusicController
from src.gui.scene import Scene


class App(Scene):

    def __init__(self, frame_rate, size, screen):
        super().__init__(frame_rate, size, screen)

        self.size = size
        self.screen = screen

        self.music_control = MusicController()

        self.create_menu("main")

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
                self.create_menu("game")
            elif event.type == self.music_control.MUSENDEVENT:
                self.music_control.start_next()

    def create_menu(self, role):
        if role == "main":
            menu = MainMenu(self.frame_rate, self.size, self.screen, self.music_control)
            menu.create_menu()
        elif role == "game":
            menu = GameMenu(self.frame_rate, self.size, self.screen, self.music_control)
            menu.create_menu()
