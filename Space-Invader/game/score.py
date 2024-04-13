import pygame
from pygame.font import Font

from const.value import ENEMY_SCORE, BOSS_SCORE


class Score:
    score: int
    font: Font
    color: str
    X: float
    Y: float

    def __init__(self, font, size, color):
        self.score = 0
        self.font = pygame.font.SysFont(font, size)
        self.color = color
        self.X = 20
        self.Y = 650

    def draw(self, screen):
        score = self.font.render("Score: " + str(self.score), True, self.color)
        screen.blit(score, (self.X, self.Y))

    def plus_player(self):
        self.score += ENEMY_SCORE

    def plus_bullet(self):
        self.score += ENEMY_SCORE

    def plus_rocket(self):
        self.score += ENEMY_SCORE // 2

    def plus_boss_bullet(self):
        self.score += BOSS_SCORE

    def plus_boss_rocket(self):
        self.score += BOSS_SCORE // 2
