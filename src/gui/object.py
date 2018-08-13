from pygame.rect import Rect


class GameObject:
    def __init__(self, x, y, w, h):
        self.bounds = Rect(x, y, w, h)

    def draw(self, surface):
        pass

    def update(self):
        pass
