import pygame


class GameSetting:
    def __init__(self, width, height, bg_image, icon_image, caption):
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.image.load(bg_image)
        self.background = pygame.transform.scale(self.background, (width, height))
        self.screen.blit(self.background, (0, 0))
        pygame.display.set_icon(icon_image)
        pygame.display.set_caption(caption)
