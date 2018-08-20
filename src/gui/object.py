import pygame

from pygame.rect import Rect


class GameObject:
    def __init__(self, x, y, w, h):
        info_obj = pygame.display.Info()
        kx = 1920 / info_obj.current_w
        ky = 1080 / info_obj.current_h
        self.bounds = Rect(x / kx, y / ky, w / kx, h / ky)

    def draw(self, screen):
        pass

    def update(self):
        pass
