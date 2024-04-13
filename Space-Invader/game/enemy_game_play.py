import random

from const.state import EnemyState, BulletState, RocketState, BossState
from const.value import *
from entities.enemy_entity import Enemy
from game.base_game_play import BaseGamePlay


class EnemyGamePlay(BaseGamePlay):

    def __init__(self, game_setting, player, score, boss):
        super().__init__(game_setting, player, score, boss)

    def generate_enemy(self, num_of_enemies):
        for i in range(num_of_enemies):
            self.enemies.append(Enemy(
                ENEMY_IMAGE,
                random.randint(MIN_X, MAX_X),
                random.randint(ENEMY_MIN_Y, MAX_Y),
                random.randint(MIN_HEALTH, MAX_HEALTH)
            ))

    def e_render(self):
        for enemy in self.enemies:
            enemy.draw(self.game_setting.screen)

    def e_next_state(self):
        self.boss.next_stage()
        for enemy in self.enemies:
            enemy.next_state()

    def e_is_clear(self):
        for enemy in self.enemies:
            if enemy.enemy_state != EnemyState.DEAD or self.boss.boss_state == BossState.ALIVE:
                return False
        return True

    def enemy_impact(self):
        for enemy in self.enemies:
            for bullet in self.bullets:
                if (enemy.enemy_state == EnemyState.ALIVE
                        and bullet.bullet_state == BulletState.FLYING
                        and (abs(bullet.X - enemy.X) < IMAGE_SIZE
                             and abs(bullet.Y - enemy.Y) < IMAGE_SIZE)):
                    bullet.hit()
                    if enemy.hit(COMMON_BULLET_DAMAGE):
                        self.score.plus_bullet()

    def boss_impact(self):
        for bullet in self.bullets:
            if (self.boss.boss_state == BossState.ALIVE and bullet.bullet_state == BulletState.FLYING) and (
                    abs(bullet.X - self.boss.X) < BOSS_IMAGE_SIZE and abs(bullet.Y - self.boss.Y) < BOSS_IMAGE_SIZE):
                bullet.hit()
                if self.boss.hit(COMMON_BULLET_DAMAGE):
                    self.score.plus_boss_bullet()

    def explode(self):
        for rocket in self.rockets:
            for enemy in self.enemies:
                if enemy.enemy_state == EnemyState.ALIVE and rocket.rocket_state == RocketState.JUST_EXPLODE:
                    if enemy.hit(ROCKET_DAMAGE):
                        self.score.plus_rocket()
            if self.boss.boss_state == BossState.ALIVE and rocket.rocket_state == RocketState.JUST_EXPLODE:
                if self.boss.hit(ROCKET_DAMAGE):
                    self.score.plus_boss_rocket()
