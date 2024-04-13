import pygame.image

from const.state import RocketState, BulletState, EnemyState, EggState, PlayerState
from const.value import *
from entities.player_entity import Bullet, Rocket
from two_player.two_player_base import TwoPlayerBaseGamePlay


class Player2GamePlay(TwoPlayerBaseGamePlay):

    def __init__(self, game_setting, player1, player2, score, boss):
        super().__init__(game_setting, player1, player2, score, boss)

    def p2_fire(self):
        if len(self.bullets) < MAX_BULLET:
            bullet = Bullet(BULLET_IMAGE, self.player2.X, self.player2.Y)
            bullet.fire()
            self.bullets.append(bullet)

    def p2_fire_rocket(self):
        for rocket in self.rockets:
            if rocket.rocket_state == RocketState.READY:
                rocket.X = self.player2.X
                rocket.Y = self.player2.Y
                rocket.fire()
                break

    def p2_get_rocket(self):
        if self.score.score >= len(self.rockets) * BASE_SCORE_TO_ROCKET:
            rocket = Rocket(ROCKET_IMAGE, 0, 0)
            self.rockets.append(rocket)

    def p2_clear_bullet(self):
        for i in range(len(self.bullets) - 1, -1, -1):
            if self.bullets[i].bullet_state == BulletState.INVISIBLE:
                del self.bullets[i]

    def p2_i_frames(self):
        if self.player2.player_state == PlayerState.UNTARGETABLE:
            self.player2.untargetable_time -= 1
            self.game_setting.screen.blit(pygame.image.load(UNTARGETABLE_IMAGE),
                                          ((2 * self.player2.X + IMAGE_SIZE) / 2,
                                           (2 * (HEIGHT - self.player2.Y) + IMAGE_SIZE) / 2))
        if self.player2.untargetable_time == 0:
            self.player2.player_state = PlayerState.PLAYING
            self.player2.untargetable_time = UNTARGETABLE_TIME

    def p2_impact(self):
        for enemy in self.enemies:
            if ((enemy.enemy_state != EnemyState.DEAD
                 and self.player2.player_state == PlayerState.PLAYING)
                    and (abs(self.player2.X - enemy.X) < IMAGE_SIZE
                         and abs(self.player2.Y - enemy.Y) < IMAGE_SIZE)):
                if enemy.hit(PLAYER_DAMAGE):
                    self.score.plus_player()
                if self.player2.hit():
                    self.player2.dead()
            for egg in enemy.eggs:
                if ((egg.egg_state != EggState.INVISIBLE and self.player2.player_state == PlayerState.PLAYING)
                        and (abs(self.player2.X - egg.X) < IMAGE_SIZE
                             and abs(self.player2.Y - egg.Y) < IMAGE_SIZE)):
                    egg.hit()
                    if self.player2.hit():
                        self.player2.dead()
        for egg in self.boss.eggs:
            if ((egg.egg_state != EggState.INVISIBLE and self.player2.player_state == PlayerState.PLAYING)
                    and (abs(self.player2.X - egg.X) < IMAGE_SIZE
                         and abs(self.player2.Y - egg.Y) < IMAGE_SIZE)):
                egg.hit()
                if self.player2.hit():
                    self.player2.dead()

    def p2_next_state(self):
        self.player2.explosion(self.game_setting.screen)
        self.p2_i_frames()
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

    def p2_is_clear(self):
        for rocket in self.rockets:
            if (rocket.rocket_state == RocketState.FLYING
                    or rocket.rocket_state == RocketState.EXPLODING
                    or rocket.rocket_state == RocketState.JUST_EXPLODE):
                return False
        return True

    def p2_render(self):
        self.player2.draw(self.game_setting.screen)

        for bullet in self.bullets:
            if bullet.bullet_state == BulletState.FLYING:
                bullet.draw(self.game_setting.screen)
        for rocket in self.rockets:
            if rocket.rocket_state == RocketState.FLYING:
                rocket.draw(self.game_setting.screen)
            if rocket.rocket_state == RocketState.EXPLODING:
                rocket.exploding(EXPLOSION_IMAGE, self.game_setting.screen)
