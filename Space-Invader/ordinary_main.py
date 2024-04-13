import sys

import pygame.time

from entities.enemy_entity import Boss
from entities.player_entity import Player
from game.game_play import *
from const.value import *
from game.game_setting import GameSetting
from game.score import Score

pygame.init()
player1 = Player(PLAYER1_IMAGE, INITIAL_PLAYER_X1, INITIAL_PLAYER_Y1, PLAYER_LIVES)
score = Score('Comic Sans MS', 40, (255, 255, 255))
boss = Boss(BOSS_IMAGE, BOSS_X, BOSS_Y, BOSS_HEALTH)
clock = pygame.time.Clock()

game_setting = GameSetting(WIDTH, HEIGHT, BACKGROUND_IMAGE, PLAYER1_IMAGE, CAPTION)
ordin_game = GamePlay(game_setting, player1, score, boss)
def main():
    ordin_game.start()
    while ordin_game.state:
        pygame.key.set_repeat(True)
        clock.tick(FPS)
        ordin_game.render()
        ordin_game.next_state()

        pygame.display.update()

    pygame.quit()
    sys.exit(0)



