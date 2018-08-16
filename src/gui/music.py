import os
import random

import pygame


class MusicController:
    MUSENDEVENT = pygame.USEREVENT + 1

    directory = 'sounds'
    cur_song = None


    def __init__(self):
        self.paused = False

        self.songs = os.listdir(self.directory)
        random.shuffle(self.songs)

        pygame.mixer.music.set_endevent(self.MUSENDEVENT)

        self.start_next()

    def play_song(self, song):
        pygame.mixer.music.load(self.directory + "/" + song)
        pygame.mixer.music.play(1, 0.0)

    def toggle(self):
        if self.paused:
            pygame.mixer.music.unpause()
        if not self.paused:
            pygame.mixer.music.pause()
        self.paused = not self.paused

    def is_paused(self):
        return self.paused

    def get_cur_song(self):
        return self.cur_song

    def start_next(self):
        self.songs = self.songs[1:] + [self.songs[0]]
        self.cur_song = self.songs[0]
        pygame.mixer.music.load(self.directory + "/" + self.cur_song)
        pygame.mixer_music.play()
