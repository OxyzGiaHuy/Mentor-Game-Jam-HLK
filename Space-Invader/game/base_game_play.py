from typing import List

from entities.enemy_entity import Enemy
from entities.player_entity import Player, Bullet, Rocket
from const.value import *
from game.game_setting import GameSetting
from game.score import Score


class BaseGamePlay:
    enemies: List[Enemy] = []
    bullets: List[Bullet] = []
    game_setting: GameSetting
    player: Player
    score: Score
    rockets: List[Rocket] = []
    state: bool = False
    round: int

    def __init__(self, game_setting, player, score, boss):
        self.game_setting = game_setting
        self.player = player
        self.score = score
        self.boss = boss
        self.rockets.append(Rocket(ROCKET_IMAGE, 0, 0))
