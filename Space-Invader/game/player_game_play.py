import pygame.image

from const.state import RocketState, BulletState, EnemyState, EggState, PlayerState
from const.value import *
from entities.player_entity import Bullet, Rocket
from game.base_game_play import BaseGamePlay


class PlayerGamePlay(BaseGamePlay):

    def __init__(self, game_setting, player, score, boss):
        super().__init__(game_setting, player, score, boss)

    def fire(self):
        bullet = Bullet(BULLET_IMAGE, self.player.X, self.player.Y)
        bullet.fire()
        self.bullets.append(bullet)

    def fire_rocket(self):
        for rocket in self.rockets:
            if rocket.rocket_state == RocketState.READY:
                rocket.X = self.player.X
                rocket.Y = self.player.Y
                rocket.fire()
                break

    def get_rocket(self):
        if self.score.score >= len(self.rockets) * BASE_SCORE_TO_ROCKET:
            rocket = Rocket(ROCKET_IMAGE, 0, 0)
            self.rockets.append(rocket)

    def clear_bullet(self):
        for i in range(len(self.bullets) - 1, -1, -1):
            if self.bullets[i].bullet_state == BulletState.INVISIBLE:
                del self.bullets[i]

    def i_frames(self):
        if self.player.player_state == PlayerState.UNTARGETABLE:
            self.player.untargetable_time -= 1
            self.game_setting.screen.blit(pygame.image.load(UNTARGETABLE_IMAGE),
                                          ((2 * self.player.X + IMAGE_SIZE) / 2,
                                          (2 * (HEIGHT - self.player.Y) + IMAGE_SIZE)/2))
        if self.player.untargetable_time == 0:
            self.player.player_state = PlayerState.PLAYING
            self.player.untargetable_time = UNTARGETABLE_TIME

    def player_impact(self):
        for enemy in self.enemies:
            if ((enemy.enemy_state != EnemyState.DEAD
                 and self.player.player_state == PlayerState.PLAYING)
                    and (abs(self.player.X - enemy.X) < IMAGE_SIZE
                         and abs(self.player.Y - enemy.Y) < IMAGE_SIZE)):
                if enemy.hit(PLAYER_DAMAGE):
                    self.score.plus_player()
                if self.player.hit():
                    self.player.dead()
            for egg in enemy.eggs:
                if ((egg.egg_state != EggState.INVISIBLE and self.player.player_state == PlayerState.PLAYING)
                        and (abs(self.player.X - egg.X) < IMAGE_SIZE
                             and abs(self.player.Y - egg.Y) < IMAGE_SIZE)):
                    egg.hit()
                    if self.player.hit():
                        self.player.dead()
        for egg in self.boss.eggs:
            if ((egg.egg_state != EggState.INVISIBLE and self.player.player_state == PlayerState.PLAYING)
                    and (abs(self.player.X - egg.X) < IMAGE_SIZE
                         and abs(self.player.Y - egg.Y) < IMAGE_SIZE)):
                egg.hit()
                if self.player.hit():
                    self.player.dead()

    def p_next_state(self):
        self.player.explosion(self.game_setting.screen)
        self.i_frames()
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

    def p_is_clear(self):
        for rocket in self.rockets:
            if (rocket.rocket_state == RocketState.FLYING
                    or rocket.rocket_state == RocketState.EXPLODING
                    or rocket.rocket_state == RocketState.JUST_EXPLODE):
                return False
        return True

    def p_render(self):
        self.player.draw(self.game_setting.screen)

        for bullet in self.bullets:
            if bullet.bullet_state == BulletState.FLYING:
                bullet.draw(self.game_setting.screen)
        for rocket in self.rockets:
            if rocket.rocket_state == RocketState.FLYING:
                rocket.draw(self.game_setting.screen)
            if rocket.rocket_state == RocketState.EXPLODING:
                rocket.exploding(EXPLOSION_IMAGE, self.game_setting.screen)
