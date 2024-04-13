import pygame

import ordinary_main
from Two_player_main import two_player_main
from endless_mode_main import endless_main

pygame.font.init()
pygame.init()

# Khởi tạo giá trị, biến toàn cục
GREY = (150, 150, 150)
WHITE = (255, 255, 255)
WHITE_1 = (230, 230, 230)
WHITE_B = (200, 200, 200)
GREEN_MONO = (0, 130, 0)
GREEN_DARK = (0, 90, 0)
GREEN_BRIGHT = (0, 230, 0)
BLACK = (0, 0, 0)
RoyalBlue4 = (39, 64, 139)
RoyalBlue3 = (58, 95, 205)
MidnightBlue = (25, 25, 112)
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
DarkOrchid4 = (104, 34, 139)
DarkOrchid1 = (191, 62, 255)
GRAY11 = (28, 28, 28)
GRAY22 = (22, 22, 22)
DarkSlateBlue = (72, 61, 139)
Dark_DarkSlateBlue = (31, 30, 70)
Cyan = (0, 200, 200)
Magenta1 = (255, 0, 255)
LightSeaGreen = (32, 178, 170)
Purple1 = (160, 32, 240)
Purple5 = (85, 26, 139)

screen = pygame.display.set_mode((600, 800))

bg_y = 0
image1 = True
image2 = False
image3 = False
last_click = -1000
bg = pygame.image.load('space-invaders-UI/bg.png')
game_name = pygame.image.load('space-invaders-UI/Name.png')

# Điều kiện chạy GUI
menu = True
tuto = False
panel = False
Ordin_mode_start = False
Endless_1 = False
Endless_2 = False



def background():
    global bg_y
    bg_y -= 1
    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y + 800))
    if bg_y == -800:
        bg_y = 0


def before_start_game():
    global panel
    global menu
    global tuto
    tuto = menu = panel = False


def Ordin_mode_starting():
    before_start_game()
    background()
    ordinary_main.main()


def EL_1P():
    endless_main()


def EL_2P():
    two_player_main()


def Name():
    GAMENAME = 'Space Campaign'
    pygame.display.set_caption(GAMENAME)


def Menu():
    background()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(game_name, (75, 50))
    font = pygame.font.SysFont('Comic Sans MS', 50)
    text_play = font.render('Play', True, BLACK)
    text_help = font.render('Tutorial', True, BLACK)
    text_quit = font.render('QUIT', True, BLACK)
    pygame.draw.rect(screen, GRAY11, (0, 0, 600, 800), 10)
    pygame.draw.rect(screen, WHITE, (160, 460, 280, 60), 0, 10)
    pygame.draw.rect(screen, GREEN_MONO, (160, 570, 280, 60), 0, 10)
    pygame.draw.rect(screen, RED, (160, 680, 280, 60), 0, 8)
    if mouse_x <= 160 + 280 and mouse_x >= 160 and mouse_y >= 680 and mouse_y <= 680 + 60:
        pygame.draw.rect(screen, DARK_RED, (160, 680, 280, 60), 0, 8)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                global running
                running = False
    if mouse_x <= 160 + 280 and mouse_x >= 160 and mouse_y >= 460 and mouse_y <= 460 + 60:
        pygame.draw.rect(screen, WHITE_B, (160, 460, 280, 60), 0, 10)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    global panel
                    panel = True
    if mouse_x <= 160 + 280 and mouse_x >= 160 and mouse_y >= 570 and mouse_y <= 570 + 60:
        pygame.draw.rect(screen, GREEN_DARK, (160, 570, 280, 60), 0, 10)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    global tuto
                    tuto = True
    screen.blit(text_play, (255, 450))
    screen.blit(text_help, (205, 560))
    screen.blit(text_quit, (230, 670))


def Panel():
    lock = pygame.image.load(r'space-invaders-UI/lock.png')
    biglock = pygame.transform.scale(lock, (200, 272))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    smallfont = pygame.font.SysFont(None, 30)
    font = pygame.font.SysFont('Comic Sans MS', 35)
    global panel
    background()
    pygame.draw.rect(screen, Purple5, (100, 100, 400, 600), 0, 8)
    pygame.draw.rect(screen, DarkSlateBlue, (105, 105, 390, 590), 0, 8)
    pygame.draw.line(screen, BLACK, (105, 300), (494, 300), 5)
    pygame.draw.rect(screen, DarkOrchid1, (135, 175, 250, 55), 0, 8)
    pygame.draw.rect(screen, DarkOrchid1, (135, 400, 250, 55), 0, 8)
    pygame.draw.rect(screen, DarkOrchid1, (135, 550, 250, 55), 0, 8)
    pygame.draw.rect(screen, WHITE, (0, 0, 100, 100), 0, 8)
    if mouse_x <= 100 and mouse_x >= 0 and mouse_y >= 0 and mouse_y <= 100:
        pygame.draw.rect(screen, WHITE_B, (0, 0, 100, 100), 0, 8)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    panel = False
    pygame.draw.polygon(screen, BLACK, [[50, 15], [50, 85], [5, 50]])
    pygame.draw.rect(screen, BLACK, (50, 30, 40, 40))
    if mouse_x <= 125 + 160 and mouse_x >= 125 and mouse_y >= 175 and mouse_y <= 175 + 55:
        pygame.draw.rect(screen, DarkOrchid4, (135, 175, 250, 55), 0, 8)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    global Ordin_mode_passed
                    Ordin_mode_passed = True
                    global Ordin_mode_start
                    Ordin_mode_start = True
    if mouse_x <= 135 + 250 and mouse_x >= 135 and mouse_y >= 400 and mouse_y <= 400 + 55 :
        pygame.draw.rect(screen, DarkOrchid4, (135, 400, 250, 55), 0, 8)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    global Endless_1
                    Endless_1 = True
    if mouse_x <= 135 + 250 and mouse_x >= 135 and mouse_y >= 550 and mouse_y <= 550 + 55 :
        pygame.draw.rect(screen, DarkOrchid4, (135, 550, 250, 55), 0, 8)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    global Endless_2
                    Endless_2 = True
    Ordinary_Mode_text = font.render('Ordinary Mode', True, Magenta1)
    Endless_Mode_text = font.render('Endless Mode', True, Magenta1)
    Ordin_mode_text = font.render('Ordinary Mode', True, BLACK)
    One_player_mode_text = font.render('1-player mode', True, BLACK)
    Two_player_mode_text = font.render('2-player mode', True, BLACK)
    text_0_1 = smallfont.render('Complete Ordinary Mode', True, BLACK)
    text_0_2 = smallfont.render('to unlock Endless Mode', True, BLACK)
    text_1 = smallfont.render('Playing alone is still good', True, BLACK)
    text_2 = smallfont.render('Playing with friend is fun? Right?', True, BLACK)
    screen.blit(Ordinary_Mode_text, (180, 110))
    screen.blit(Ordin_mode_text, (130, 180))
    screen.blit(text_0_1, (120, 250))
    screen.blit(text_0_2, (120, 280))
    screen.blit(Endless_Mode_text, (190, 300))
    screen.blit(One_player_mode_text, (150, 400))
    screen.blit(Two_player_mode_text, (150, 550))
    screen.blit(text_1, (150, 470))
    screen.blit(text_2, (150, 620))


# Mục Tutorial
def Tutorial():
    cd = 100
    mouse_x, mouse_y = pygame.mouse.get_pos()
    font = pygame.font.SysFont('Comic Sans MS', 35)
    smallfont = pygame.font.SysFont('Comic Sans MS', 25)
    small2font = pygame.font.SysFont('Comic Sans MS', 24)
    small1font = pygame.font.SysFont('Comic Sans MS', 20)
    background()
    pygame.draw.rect(screen, RED, (525, 0, 75, 75))
    if mouse_x <= 525 + 75 and mouse_x >= 525 and mouse_y >= 0 and mouse_y <= 75:
        pygame.draw.rect(screen, DARK_RED, (525, 0, 75, 75))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    global tuto
                    tuto = False
    global image1, image2, image3
    pygame.draw.line(screen, BLACK, (533, 5), (590, 70), 8)
    pygame.draw.line(screen, BLACK, (533, 70), (590, 5), 8)
    pygame.draw.rect(screen, WHITE_B, (60, 150, 480, 450), 0, 8)
    pygame.draw.rect(screen, WHITE, (180, 600, 65, 65), 0, 8)
    pygame.draw.rect(screen, WHITE, (350, 600, 65, 65), 0, 8)
    pygame.draw.polygon(screen, BLACK, [[235, 603], [235, 660], [185, 635]])
    pygame.draw.polygon(screen, BLACK, [[360, 603], [360, 660], [410, 635]])
    time_now = pygame.time.get_ticks()
    global last_click
    if mouse_x <= 180 + 65 and mouse_x >= 180 and mouse_y >= 600 and mouse_y <= 600 + 65:
        pygame.draw.rect(screen, WHITE_B, (180, 600, 65, 65), 0, 8)
        pygame.draw.polygon(screen, GRAY11, [[235, 603], [235, 660], [185, 635]])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and time_now - last_click > cd:
                last_click = time_now
                if image3:
                    image2 = True
                    image3 = False
                if image2:
                    image1 = True
                    image2 = False
    if mouse_x <= 350 + 65 and mouse_x >= 350 and mouse_y >= 600 and mouse_y <= 600 + 65:
        pygame.draw.rect(screen, WHITE_B, (350, 600, 65, 65), 0, 8)
        pygame.draw.polygon(screen, GRAY11, [[360, 603], [360, 660], [410, 635]])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and time_now - last_click > cd:
                last_click = time_now
                if image3:
                    image3 = False
                    image4 = True
                elif image2:
                    image2 = False
                    image3 = True
                elif image1:
                    image1 = False
                    image2 = True
    if image1:
        list_1 = smallfont.render('1/3', True, WHITE)
        screen.blit(list_1, (278, 610))
        image_1 = smallfont.render('[Image of Gameplay]', True, WHITE)
        text_1_1 = smallfont.render('The aliens are coming! Your mission is to', True, WHITE)
        text_1_2 = smallfont.render('prevent their descent and invasion by', True, WHITE)
        text_1_3 = smallfont.render('shooting them down.', True, RED)
        screen.blit(image_1, (60, 150))
        screen.blit(text_1_1, (70, 450))
        screen.blit(text_1_2, (80, 480))
        screen.blit(text_1_3, (190, 510))
    elif image2:
        list_2 = smallfont.render('2/3', True, WHITE)
        screen.blit(list_2, (278, 610))
        image_2 = smallfont.render('[Image of Gameplay]', True, WHITE)
        text_2_1 = small1font.render('Eliminate the aliens to get much scores as you can!', True, GREEN_MONO)
        text_2_2 = smallfont.render('Careful! Aliens will shoot back at you.', True, WHITE)
        text_2_3 = smallfont.render('You only have 5 lives!', True, WHITE)
        screen.blit(image_2, (60, 150))
        screen.blit(text_2_1, (68, 465))
        screen.blit(text_2_2, (85, 485))
        screen.blit(text_2_3, (170, 510))
    elif image3:
        list_3 = smallfont.render('3/3', True, WHITE)
        screen.blit(list_3, (278, 610))
        text_3_1_0 = font.render('In one-player mode:', True, BLACK)
        text_3_1_1 = smallfont.render('- USE WASD to move spaceships', True, GREEN_MONO)
        text_3_1_2 = smallfont.render('- Click left mouse to shoot.', True, GREEN_MONO)
        text_3_1_3 = smallfont.render('- Click right mouse to launch rockets.', True, GREEN_MONO)
        text_3_2_0 = font.render('In two-player mode:', True, BLACK)
        text_3_1_1_0 = smallfont.render('- Player 1: ', True, GREEN_MONO)
        text_3_1_1_1 = smallfont.render('+ Move: WASD', True, GREEN_MONO)
        text_3_1_1_2 = smallfont.render('+ Shoot: "F"', True, GREEN_MONO)
        text_3_1_1_3 = smallfont.render('+ launch rockets: "G"', True, GREEN_MONO)
        text_3_1_2_0 = smallfont.render('- Player 2:', True, GREEN_MONO)
        text_3_1_2_1 = smallfont.render('+ Move: Arrow keys', True, GREEN_MONO)
        text_3_1_2_2 = smallfont.render('+ Shoot: "0"', True, GREEN_MONO)
        text_3_1_2_3 = smallfont.render('+ launch rockets: "1"', True, GREEN_MONO)
        text_3_1_2_4 = smallfont.render('+ each player have two lives', True, GREEN_MONO)
        screen.blit(text_3_1_0, (70, 160))
        screen.blit(text_3_1_1, (90, 210))
        screen.blit(text_3_1_2, (90, 235))
        screen.blit(text_3_1_3, (90, 260))
        screen.blit(text_3_2_0, (70, 290))
        screen.blit(text_3_1_1_0, (90, 335))
        screen.blit(text_3_1_1_1, (110, 365))
        screen.blit(text_3_1_1_2, (110, 390))
        screen.blit(text_3_1_1_3, (110, 415))
        screen.blit(text_3_1_2_0, (90, 440))
        screen.blit(text_3_1_2_1, (110, 465))
        screen.blit(text_3_1_2_2, (110, 490))
        screen.blit(text_3_1_2_3, (110, 515))
        screen.blit(text_3_1_2_4, (110, 535))


def GUI():
    Name()
    if menu:
        Menu()
    if tuto:
        Tutorial()
    if panel:
        Panel()
    if Ordin_mode_start:
        Ordin_mode_starting()
    if Endless_1:
        EL_1P()
    if Endless_2:
        EL_2P()

