import random
from typing import List

import pygame.image

from entities.entity import Entity, Position
from const.state import *
from const.value import *


class Egg(Entity):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, 0.1, 0.5, IMAGE_SIZE)
        self.egg_state = EggState.INVISIBLE
        self.time = 0

    def fall(self, destination):
        self.egg_state = EggState.FLYING
        self.time = (self.Y - destination.Y) / self.y_velocity

    def moving(self):
        if self.time <= 0:
            self.egg_state = EggState.INVISIBLE
            return
        self.Y -= self.y_velocity
        self.time -= 1

    def hit(self):
        self.time = 0


class Enemy(Entity):
    eggs: List[Egg] = []

    def __init__(self, image, x, y, enemy_health):
        super().__init__(image, x, y, 5, 5, 32)
        self.enemy_state = EnemyState.ALIVE
        self.health = enemy_health
        self.exploding_time = ENEMY_EXPLODING_TIME

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.exploding()
            return True
        return False

    def exploding(self):
        self.enemy_state = EnemyState.EXPLODING

    def dead(self):
        self.enemy_state = EnemyState.DEAD

    def spawn_egg(self):
        if len(self.eggs) < 2:
            if random.randint(0, RANDOM_TIME_SPAWN_EGG) < 4:
                egg = Egg(EGG_IMAGE, self.X, self.Y)
                egg.fall(Position(self.X, MIN_Y))
                self.eggs.append(egg)

    def clear_egg(self):
        for i in range(len(self.eggs) - 1, -1, -1):
            if self.eggs[i].egg_state == EggState.INVISIBLE:
                del self.eggs[i]

    def moving(self):
        self.X -= self.x_velocity
        if self.X <= MIN_X or self.X >= MAX_X:
            self.x_velocity *= -1

    def next_state(self):
        if self.enemy_state == EnemyState.ALIVE:
            self.moving()
            self.spawn_egg()
        if self.enemy_state == EnemyState.EXPLODING:
            if self.exploding_time == 0:
                self.dead()
            self.exploding_time -= 1
        self.clear_egg()
        for egg in self.eggs:
            if egg.egg_state == EggState.FLYING:
                egg.moving()

    def draw(self, screen):
        if self.enemy_state == EnemyState.ALIVE:
            super().draw(screen)
        if self.enemy_state == EnemyState.EXPLODING:
            screen.blit(EXPLOSION_IMAGE, ((2 * self.X + IMAGE_SIZE) / 2, (2 * (HEIGHT - self.Y) + IMAGE_SIZE) / 2))
        for egg in self.eggs:
            if egg.egg_state == EggState.FLYING:
                egg.draw(screen)


class Boss(Entity):
    eggs: List[Egg] = []

    def __init__(self, image, x, y, boss_health):
        super().__init__(image, x, y, 0, 0, 64)
        self.health = boss_health
        self.boss_state = BossState.SLEEP
        self.exploding_time = ENEMY_EXPLODING_TIME

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.exploding()
            return True
        return False

    def exploding(self):
        self.boss_state = BossState.EXPLODING

    def skill(self):
        if len(self.eggs) < 6:
            if random.randint(0, RANDOM_TIME_SPAWN_EGG) < 100:
                egg = Egg(EGG_IMAGE, random.randint(MIN_X, MAX_X), self.Y)
                egg.fall(Position(random.randint(MIN_X, MAX_X), HEIGHT - self.Y))
                self.eggs.append(egg)

    def dead(self):
        self.boss_state = BossState.DEAD
        self.health = BOSS_HEALTH

    def draw(self, screen):
        if self.boss_state == BossState.ALIVE:
            super().draw(screen)
        if self.boss_state == BossState.EXPLODING:
            screen.blit(EXPLOSION_IMAGE,
                        ((2 * self.X + IMAGE_SIZE) / 2,
                         (2 * (HEIGHT - self.Y) + IMAGE_SIZE) / 2))
        for egg in self.eggs:
            if egg.egg_state == EggState.FLYING:
                egg.draw(screen)

    def next_stage(self):
        if self.boss_state == BossState.ALIVE:
            self.skill()
        if self.boss_state == BossState.EXPLODING:
            if self.exploding_time == 0:
                self.dead()
            self.exploding_time -= 1
        self.clear_egg()
        for egg in self.eggs:
            if egg.egg_state == EggState.FLYING:
                egg.moving()

    def clear_egg(self):
        for i in range(len(self.eggs) - 1, -1, -1):
            if self.eggs[i].egg_state == EggState.INVISIBLE:
                del self.eggs[i]
