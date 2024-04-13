from const.state import PlayerState, BossState
from const.value import *
from game.enemy_game_play import EnemyGamePlay
from two_player.p1_game_play import Player1GamePlay
from two_player.p2_game_play import Player2GamePlay


class TwoPlayerGamePlay(Player1GamePlay, Player2GamePlay, EnemyGamePlay):

    def __init__(self, game_setting, player1, player2, score, boss):
        super().__init__(game_setting, player1, player2, score, boss)
        self.time = END_GAME_TIME
        self.number_enemy = BEGIN_NUMBER_ENEMY

    def start(self):
        self.state = True
        self.round = 1
        for i in range(len(self.enemies) - 1, -1, -1):
            del self.enemies[i]
        self.generate_enemy(self.number_enemy)

    def next_round(self):
        self.round += 1
        self.generate_enemy(self.number_enemy)
        if self.round % BOSS_ROUND == 0:
            self.boss.boss_state = BossState.ALIVE
        if self.round % ADD_ENEMY_ROUND == 0:
            self.number_enemy += 1
        if self.round % PLAYER_REWARD_ROUND == 0:
            self.player.lives += 1


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
        self.p1_render()
        self.p2_render()

    def end_game(self):
        if self.player1.player_state == PlayerState.DEAD and self.player2.player_state == PlayerState.DEAD:
            self.game_setting.screen.blit(pygame.font.SysFont('Comic Sans MS', 42).render
                                          ("Game Over", True, (255, 255, 255)),
                                          (CENTER_X, CENTER_Y))
            if self.time == 0:
                self.state = False
            self.time -= 1
        if self.round == MAX_ROUND and self.e_is_clear() and self.p1_is_clear() and self.p2_is_clear():
            self.game_setting.screen.blit(
                pygame.font.SysFont('Comic Sans MS', 42).render
                ('You Won', True, (255, 255, 255)),
                (CENTER_X, CENTER_Y))
            if self.time == 0:
                self.state = False
            self.time -= 1

    def player_impact(self):
        if self.player1.player_state == PlayerState.PLAYING and self.player2.player_state == PlayerState.PLAYING:
            if abs(self.player1.X - self.player2.X) < IMAGE_SIZE and abs(self.player1.X - self.player2.X) < IMAGE_SIZE:
                self.player1.hit()
                self.player2.hit()

    def handle_impact(self):
        self.player_impact()
        self.p1_impact()
        self.p2_impact()
        self.enemy_impact()
        self.boss_impact()
        self.explode()

    def next_state(self):
        if self.e_is_clear() and self.p1_is_clear() and self.p2_is_clear():
            self.next_round()

        self.handle_impact()
        self.p1_clear_bullet()
        self.p1_get_rocket()
        self.p2_clear_bullet()
        self.p2_get_rocket()

        self.e_next_state()
        self.p1_next_state()
        self.p2_next_state()

        self.handle_key()
        self.end_game()

    def handle_key(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player1.moving_left()
                if event.key == pygame.K_d:
                    self.player1.moving_right()
                if event.key == pygame.K_w:
                    self.player1.moving_up()
                if event.key == pygame.K_s:
                    self.player1.moving_down()
                if event.key == pygame.K_f:
                    self.p1_fire()
                if event.key == pygame.K_g:
                    self.p1_fire_rocket()
                if event.key == pygame.K_LEFT:
                    self.player2.moving_left()
                if event.key == pygame.K_RIGHT:
                    self.player2.moving_right()
                if event.key == pygame.K_UP:
                    self.player2.moving_up()
                if event.key == pygame.K_DOWN:
                    self.player2.moving_down()
                if event.key == pygame.K_KP0:
                    self.p2_fire()
                if event.key == pygame.K_KP1:
                    self.p2_fire_rocket()
