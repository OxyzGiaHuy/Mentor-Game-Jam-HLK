import pygame.image

from entities.entity import Entity
from const.state import *
from const.value import *


class Player(Entity):
    def __init__(self, image, x, y, player_lives):
        super().__init__(image, x, y, 1, 1, 32)
        self.lives = player_lives
        self.player_state = PlayerState.PLAYING
        self.exploding_time = PLAYER_EXPLODING_TIME
        self.untargetable_time = UNTARGETABLE_TIME
        self.INITIAL_PLAYER_X = x
        self.INITIAL_PLAYER_Y = y

    def hit(self):
        self.lives -= 1
        self.X = self.INITIAL_PLAYER_X
        self.Y = self.INITIAL_PLAYER_Y
        self.exploding()
        if self.lives == 0:
            self.dead()
            return True
        return False

    def moving_up(self):
        self.Y += self.y_velocity
        if self.Y >= MAX_Y:
            self.Y = MAX_Y

    def moving_down(self):
        self.Y -= self.y_velocity
        if self.Y <= MIN_Y:
            self.Y = MIN_Y

    def moving_left(self):
        self.X -= self.x_velocity
        if self.X <= MIN_X:
            self.X = MIN_X

    def moving_right(self):
        self.X += self.x_velocity
        if self.X >= MAX_X:
            self.X = MAX_X

    def dead(self):
        self.player_state = PlayerState.DEAD

    def exploding(self):
        self.player_state = PlayerState.EXPLODING

    def explosion(self, screen):
        if self.player_state == PlayerState.EXPLODING:
            screen.blit(EXPLOSION_IMAGE, (self.X, HEIGHT - self.Y))
            self.exploding_time -= 1
        if self.exploding_time <= 0:
            self.exploding_time = PLAYER_EXPLODING_TIME
            self.untargetable()

    def untargetable(self):
        self.player_state = PlayerState.UNTARGETABLE

    def return_playing(self):
        self.player_state = PlayerState.PLAYING


class Bullet(Entity):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, 5, 5, 32)
        self.bullet_state = BulletState.INVISIBLE
        self.time = 0

    def fire(self):
        self.bullet_state = BulletState.FLYING
        self.time = (MAX_Y - self.Y) / self.y_velocity

    def moving(self):
        if self.time <= 0:
            self.bullet_state = BulletState.INVISIBLE
            return
        self.Y += self.y_velocity
        self.time -= 1

    def hit(self):
        self.time = 0


class Rocket(Entity):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, 5, 5, 32)
        self.time = ROCKET_MOVING_TIME
        self.rocket_state = RocketState.READY
        self.exploding_time = ROCKET_EXPLODING_TIME

    def fire(self):
        self.rocket_state = RocketState.FLYING
        self.time = ROCKET_MOVING_TIME
        self.y_velocity = (CENTER_Y - self.Y) / ROCKET_MOVING_TIME
        self.x_velocity = (CENTER_X - self.X) / ROCKET_MOVING_TIME

    def moving(self):
        if self.time == 0:
            self.rocket_state = RocketState.JUST_EXPLODE
            return True
        self.Y += self.y_velocity
        self.X += self.x_velocity
        self.time -= 1
        return False

    def get_explode(self):
        self.rocket_state = RocketState.EXPLODING

    def exploding(self, explode_image, screen):
        self.rocket_state = RocketState.EXPLODING
        screen.blit(explode_image, (self.X, self.Y))

    def exploded(self):
        if self.exploding_time == 0:
            self.rocket_state = RocketState.EXPLODED
            self.exploding_time = ROCKET_EXPLODING_TIME
        self.exploding_time -= 1
