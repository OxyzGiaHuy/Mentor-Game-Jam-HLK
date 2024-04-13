import random

import pygame

IMAGE_SIZE = 32
BOSS_IMAGE_SIZE = 64
ROCKET_IMAGE_SIZE = 64
Enemy_images = ['image/Alien1.png', 'image/Alien2.png', 'image/Alien3.png', 'image/Alien4.png',
                'image/Alien5.png']
random_enemy_image = random.choice(Enemy_images)
raw_enemy_image = pygame.image.load(random_enemy_image)
ENEMY_IMAGE = pygame.transform.scale(raw_enemy_image, (IMAGE_SIZE, IMAGE_SIZE))
BULLET_IMAGE = pygame.image.load('image/bullet players.png')
RAW_PLAYER1_IMAGE = pygame.image.load('image/Spaceship1.png')
PLAYER1_IMAGE = pygame.transform.scale(RAW_PLAYER1_IMAGE, (IMAGE_SIZE, IMAGE_SIZE))
RAW_PLAYER2_IMAGE = pygame.image.load('image/Spaceship1.png')
PLAYER2_IMAGE = pygame.transform.scale(RAW_PLAYER2_IMAGE, (IMAGE_SIZE, IMAGE_SIZE))
RAW_ROCKET_IMAGE = pygame.image.load('image/Rocket.png')
ROCKET_IMAGE = pygame.transform.scale(RAW_ROCKET_IMAGE, (ROCKET_IMAGE_SIZE, ROCKET_IMAGE_SIZE))
EXPLOSION_IMAGE = pygame.image.load('image/exp 3.png')
BACKGROUND_IMAGE = 'image/background.png'
EGG_IMAGE = pygame.image.load('image/alien bullet.png')
RAW_BOSS_IMAGE = pygame.image.load('image/alien_boss.png')
BOSS_IMAGE = pygame.transform.scale(RAW_BOSS_IMAGE, (BOSS_IMAGE_SIZE, BOSS_IMAGE_SIZE))
UNTARGETABLE_IMAGE = 'image/untargetable.png'

WIDTH = 600
HEIGHT = 800
MIN_X = 20
MAX_X = 550
ENEMY_MIN_Y = 600
MAX_Y = 800
MIN_Y = 150
CENTER_X = 250
CENTER_Y = 400
BOSS_X = 250
BOSS_Y = 700
BOSS_HEALTH = 40

COMMON_BULLET_DAMAGE = 1
MAX_BULLET = 5
ROCKET_MOVING_TIME = 50
ROCKET_DAMAGE = 10
MIN_HEALTH = 2
MAX_HEALTH = 5
ENEMY_EXPLODING_TIME = 10
ENEMY_SCORE = 100
BOSS_SCORE = 1000
BASE_SCORE_TO_ROCKET = 1000
ROCKET_EXPLODING_TIME = 10
END_GAME_TIME = 100

INITIAL_PLAYER_X1 = 300
INITIAL_PLAYER_Y1 = 200
INITIAL_PLAYER_X2 = 500
INITIAL_PLAYER_Y2 = 200
PLAYER_LIVES = 5
PLAYER_DAMAGE = 5
PLAYER_EXPLODING_TIME = 10
CAPTION = 'Test'
RANDOM_TIME_SPAWN_EGG = 500
UNTARGETABLE_TIME = 150

MAX_ROUND = 5
BOSS_ROUND = 5
BEGIN_NUMBER_ENEMY = 5
ADD_ENEMY_ROUND = 3
PLAYER_REWARD_ROUND = 5
NUMBER_ENEMY_EACH_ROUND = [3, 5, 7, 9, 10]
FPS = 60
