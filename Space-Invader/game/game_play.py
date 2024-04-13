import pygame

from const.state import PlayerState, BossState
from const.value import *
from game.enemy_game_play import EnemyGamePlay
from game.player_game_play import PlayerGamePlay


class GamePlay(PlayerGamePlay, EnemyGamePlay):

    def __init__(self, game_setting, player, score, boss):
        super().__init__(game_setting, player, score, boss)
        self.time = END_GAME_TIME

    def start(self):
        self.state = True
        self.round = 1
        for i in range(len(self.enemies) - 1, -1, -1):
            del self.enemies[i]
        self.generate_enemy(NUMBER_ENEMY_EACH_ROUND[self.round - 1])

    def next_round(self):
        if self.round >= MAX_ROUND:
            self.state = False
            Ordin_mode_start = False
            return
        self.round += 1
        self.generate_enemy(NUMBER_ENEMY_EACH_ROUND[self.round - 1])
        if self.round == BOSS_ROUND:
            self.boss.boss_state = BossState.ALIVE

    def round_draw(self):
        self.game_setting.screen.blit(pygame.font.SysFont('Comic Sans MS', 42).render
                                      ("ROUND: " + str(self.round), True, (255, 255, 255)),
                                      (350, 650))

    def render(self):
        self.game_setting.screen.blit(self.game_setting.background, (0, 0))
        self.score.draw(self.game_setting.screen)
        self.boss.draw(self.game_setting.screen)
        self.round_draw()
        self.e_render()
        self.p_render()

    def end_game(self):
        if self.player.player_state == PlayerState.DEAD:
            self.game_setting.screen.blit(pygame.font.SysFont('Comic Sans MS', 42).render
                                          ("Game Over", True, (255, 255, 255)),
                                          (CENTER_X, CENTER_Y))
            if self.time == 0:
                self.state = False
            self.time -= 1
        if self.round == MAX_ROUND and self.e_is_clear() and self.p_is_clear():
            self.game_setting.screen.blit(
                pygame.font.SysFont('Comic Sans MS', 42).render
                ('You Won', True, (255, 255, 255)),
                (CENTER_X, CENTER_Y))
            if self.time == 0:
                self.state = False
            self.time -= 1

    def handle_impact(self):
        self.player_impact()
        self.enemy_impact()
        self.boss_impact()
        self.explode()

    def next_state(self):
        if self.e_is_clear() and self.p_is_clear():
            self.next_round()

        self.handle_impact()
        self.clear_bullet()
        self.get_rocket()

        self.e_next_state()
        self.p_next_state()

        self.handle_key()
        self.end_game()

    def handle_key(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.moving_left()
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right()
                if event.key == pygame.K_UP:
                    self.player.moving_up()
                if event.key == pygame.K_DOWN:
                    self.player.moving_down()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_buttons = pygame.mouse.get_pressed()
                if mouse_buttons[0]:
                    if len(self.bullets) < 5:
                        self.fire()
                if mouse_buttons[2]:
                    self.fire_rocket()
