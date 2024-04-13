from const.value import *


class Position:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


class Entity(Position):
    def __init__(self, image, x, y, x_velocity, y_velocity, size):
        super().__init__(x, y)
        self.image = image
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.size = size

    def draw(self, screen):
        screen.blit(self.image, ((2 * self.X + IMAGE_SIZE) / 2, (2 * (HEIGHT - self.Y) + IMAGE_SIZE) / 2))
