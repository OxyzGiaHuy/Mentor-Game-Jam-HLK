import sys

import pygame.time

from Endless_mode.endless_game_play import EndlessGamePlay
from entities.enemy_entity import Boss
from entities.player_entity import Player
from const.value import *
from game.game_setting import GameSetting
from game.score import Score
from ordinary_main import game_setting

pygame.init()
player1 = Player(PLAYER1_IMAGE, INITIAL_PLAYER_X1, INITIAL_PLAYER_Y1, PLAYER_LIVES)
score = Score('Comic Sans MS', 40, (255, 255, 255))
boss = Boss(BOSS_IMAGE, BOSS_X, BOSS_Y, BOSS_HEALTH)
clock = pygame.time.Clock()

endless_game = EndlessGamePlay(game_setting, player1, score, boss)
def endless_main():
    endless_game.start()
    while endless_game.state:
        pygame.key.set_repeat(True)
        clock.tick(FPS)
        endless_game.render()
        endless_game.next_state()

        pygame.display.update()

    pygame.quit()
    sys.exit(0)



