import sys

import pygame


class Scene:

    def __init__(self, frame_rate, size, screen):
        self.screen = screen

        self.frame_rate = frame_rate
        self.size = size
        self.clock = pygame.time.Clock()
        self.objects = []
        self.mouse_handlers = []
        self.menu_buttons = []

        self.bg_img = pygame.transform.scale(pygame.image.load("images/bg.png"), self.size)

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

    def update(self):
        for object in self.objects:
            object.update()

    def draw(self):
        for object in self.objects:
            object.draw(self.screen)

    def create_menu(self, role):
        pass
