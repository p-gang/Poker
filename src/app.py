import sys

import pygame

from src.gui.menu import MainMenu


class App:

    def __init__(self, frame_rate, size):
        pygame.init()
        pygame.font.init()

        self.bg_img = pygame.transform.scale(pygame.image.load("images/bg.png"), size)

        self.frame_rate = frame_rate
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.size = size
        self.objects = []
        self.mouse_handlers = []
        self.menu_buttons = []

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

    def update(self):
        for object in self.objects:
            object.update()

    def draw(self):
        for object in self.objects:
            object.draw(self.screen)

    def create_menu(self):
        MainMenu(self.frame_rate, self.size)
