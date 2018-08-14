from src.app import App
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    info_obj = pygame.display.Info()
    size = (info_obj.current_w, info_obj.current_h)
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    app = App(60, size, screen)
    app.run()
