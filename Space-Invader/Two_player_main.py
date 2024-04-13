import sys

import pygame.time

from entities.enemy_entity import Boss
from entities.player_entity import Player
from const.value import *
from game.score import Score
from ordinary_main import game_setting
from two_player.two_player_game_play import TwoPlayerGamePlay

pygame.init()
player1 = Player(PLAYER1_IMAGE, INITIAL_PLAYER_X1, INITIAL_PLAYER_Y1, PLAYER_LIVES)
player2 = Player(PLAYER2_IMAGE, INITIAL_PLAYER_X2, INITIAL_PLAYER_Y2, PLAYER_LIVES)
score = Score('Comic Sans MS', 40, (255, 255, 255))
boss = Boss(BOSS_IMAGE, BOSS_X, BOSS_Y, BOSS_HEALTH)
clock = pygame.time.Clock()

two_player_game = TwoPlayerGamePlay(game_setting, player1, player2, score, boss)
def two_player_main():

    two_player_game.start()
    while two_player_game.state:
        pygame.key.set_repeat(True)
        clock.tick(FPS)
        two_player_game.render()
        two_player_game.next_state()

        pygame.display.update()

    pygame.quit()
    sys.exit(0)


