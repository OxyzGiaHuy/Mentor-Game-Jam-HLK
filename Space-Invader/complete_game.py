from GUI import *
from Two_player_main import *
from endless_mode_main import *
from ordinary_main import *
running = True
while running:
    GUI()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()