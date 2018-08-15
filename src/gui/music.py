import pygame


class MusicController:

    def __init__(self):
        self.paused = False

    def toggle(self):
        if self.paused:
            pygame.mixer.music.unpause()
        if not self.paused:
            pygame.mixer.music.pause()
        self.paused = not self.paused

    def is_paused(self):
        return self.paused
