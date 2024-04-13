from typing import List

from entities.enemy_entity import Enemy
from entities.player_entity import Player, Bullet, Rocket
from const.value import *
from game.game_setting import GameSetting
from game.score import Score


class TwoPlayerBaseGamePlay:
    enemies: List[Enemy] = []
    bullets: List[Bullet] = []
    game_setting: GameSetting
    player1: Player
    player2: Player
    score: Score
    rockets: List[Rocket] = []
    state: bool = False
    round: int

    def __init__(self, game_setting, player1, player2, score, boss):
        self.game_setting = game_setting
        self.player1 = player1
        self.player2 = player2
        self.score = score
        self.boss = boss
        self.rockets.append(Rocket(ROCKET_IMAGE, 0, 0))
