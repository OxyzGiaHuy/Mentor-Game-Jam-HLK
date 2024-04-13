import pygame.image

from const.state import RocketState, BulletState, EnemyState, EggState, PlayerState
from const.value import *
from entities.player_entity import Bullet, Rocket
from two_player.two_player_base import TwoPlayerBaseGamePlay


class Player1GamePlay(TwoPlayerBaseGamePlay):

    def __init__(self, game_setting, player1, player2, score, boss):
        super().__init__(game_setting, player1, player2, score, boss)

    def p1_fire(self):
        if len(self.bullets) < MAX_BULLET:
            bullet = Bullet(BULLET_IMAGE, self.player1.X, self.player1.Y)
            bullet.fire()
            self.bullets.append(bullet)

    def p1_fire_rocket(self):
        for rocket in self.rockets:
            if rocket.rocket_state == RocketState.READY:
                rocket.X = self.player1.X
                rocket.Y = self.player1.Y
                rocket.fire()
                break

    def p1_get_rocket(self):
        if self.score.score >= len(self.rockets) * BASE_SCORE_TO_ROCKET:
            rocket = Rocket(ROCKET_IMAGE, 0, 0)
            self.rockets.append(rocket)

    def p1_clear_bullet(self):
        for i in range(len(self.bullets) - 1, -1, -1):
            if self.bullets[i].bullet_state == BulletState.INVISIBLE:
                del self.bullets[i]

    def p1_i_frames(self):
        if self.player1.player_state == PlayerState.UNTARGETABLE:
            self.player1.untargetable_time -= 1
            self.game_setting.screen.blit(pygame.image.load(UNTARGETABLE_IMAGE),
                                          ((2 * self.player1.X + IMAGE_SIZE) / 2,
                                          (2 * (HEIGHT - self.player1.Y) + IMAGE_SIZE)/2))
        if self.player1.untargetable_time == 0:
            self.player1.player_state = PlayerState.PLAYING
            self.player1.untargetable_time = UNTARGETABLE_TIME

    def p1_impact(self):
        for enemy in self.enemies:
            if ((enemy.enemy_state != EnemyState.DEAD
                 and self.player1.player_state == PlayerState.PLAYING)
                    and (abs(self.player1.X - enemy.X) < IMAGE_SIZE
                         and abs(self.player1.Y - enemy.Y) < IMAGE_SIZE)):
                if enemy.hit(PLAYER_DAMAGE):
                    self.score.plus_player()
                if self.player1.hit():
                    self.player1.dead()
            for egg in enemy.eggs:
                if ((egg.egg_state != EggState.INVISIBLE and self.player1.player_state == PlayerState.PLAYING)
                        and (abs(self.player1.X - egg.X) < IMAGE_SIZE
                             and abs(self.player1.Y - egg.Y) < IMAGE_SIZE)):
                    egg.hit()
                    if self.player1.hit():
                        self.player1.dead()
        for egg in self.boss.eggs:
            if ((egg.egg_state != EggState.INVISIBLE and self.player1.player_state == PlayerState.PLAYING)
                    and (abs(self.player1.X - egg.X) < IMAGE_SIZE
                         and abs(self.player1.Y - egg.Y) < IMAGE_SIZE)):
                egg.hit()
                if self.player1.hit():
                    self.player1.dead()

    def p1_next_state(self):
        self.player1.explosion(self.game_setting.screen)
        self.p1_i_frames()
        for bullet in self.bullets:
            if bullet.bullet_state == BulletState.FLYING:
                bullet.moving()

        for rocket in self.rockets:
            if rocket.rocket_state == RocketState.EXPLODING:
                rocket.exploded()
            if rocket.rocket_state == RocketState.JUST_EXPLODE:
                rocket.get_explode()
            if rocket.rocket_state == RocketState.FLYING:
                rocket.moving()

    def p1_is_clear(self):
        for rocket in self.rockets:
            if (rocket.rocket_state == RocketState.FLYING
                    or rocket.rocket_state == RocketState.EXPLODING
                    or rocket.rocket_state == RocketState.JUST_EXPLODE):
                return False
        return True

    def p1_render(self):
        self.player1.draw(self.game_setting.screen)

        for bullet in self.bullets:
            if bullet.bullet_state == BulletState.FLYING:
                bullet.draw(self.game_setting.screen)
        for rocket in self.rockets:
            if rocket.rocket_state == RocketState.FLYING:
                rocket.draw(self.game_setting.screen)
            if rocket.rocket_state == RocketState.EXPLODING:
                rocket.exploding(EXPLOSION_IMAGE, self.game_setting.screen)
