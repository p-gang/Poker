import pygame

from src.gui.object import GameObject
from src.gui.text import TextObject


class Button(GameObject):
    def __init__(self, x, y, w, h, text, button_text_color, font_name, font_size, on_click=lambda x: None, padding=0):
        super().__init__(x, y, w, h)
        self.state = 'normal'
        self.on_click = on_click

        self.text = TextObject(self.bounds.x + padding,
                               self.bounds.y + padding, text,
                               button_text_color,
                               font_name,
                               font_size)

    def draw(self, screen):
        pygame.draw.rect(screen,
                         self.back_color,
                         self.bounds)
        self.text.draw(screen)

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)

    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'

    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.state = 'pressed'

    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'

    @property
    def back_color(self):
        return dict(normal=(0, 255, 0),
                    hover=(255, 255, 255),
                    pressed=(255, 255, 255))[self.state]


class ToggleButton(Button):

    def __init__(self, x, y, w, h, text, button_text_color, font_name, font_size, on_click=lambda x: None, padding=0,
                 state="normal"):
        super().__init__(x, y, w, h, text, button_text_color, font_name, font_size, on_click, padding)

        self.state = state

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)

    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state == 'normal':
                self.state = "toggled"
                self.on_click(self)
            else:
                self.state = "normal"
                self.on_click(self)

    @property
    def back_color(self):
        return dict(normal=(0, 255, 0),
                    toggled=(133, 133, 133))[self.state]

    def is_toggled(self):
        if self.state == "toggled":
            return True
        return False
