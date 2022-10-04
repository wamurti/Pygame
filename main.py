import pygame as pg
import os.path
pg.init() 
game_active = True
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))       #Screen size, should this be changed? 
pg.display.set_caption("Pygameforever")         #Game title
clock = pg.time.Clock()                         #How fast we want to run our game (fps/hz/pps)

main_dir = os.path.split(os.path.abspath(__file__))[0]

#Load Images
map_surface = pg.image.load(main_dir+'/Assets/Graphics/preview.png')
map_surface = pg.transform.scale(map_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))




while True:                                     #Infinite loop
    for events in pg.event.get():               #Our event-loop
        if events.type == pg.QUIT:
            pg.quit()
            exit()
    
    if game_active:                             #What to do when game is active
        print("Game is active")
    else:                                       #What to do when game is not active, aka gameover?
        print("Game is not active. Gameover?")

    screen.blit(map_surface, (0,0))
    pg.display.update()                         
    clock.tick(60)                              #Updates disp 60 times per sec
