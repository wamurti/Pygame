import pygame as pg
pg.init() 
game_active = True

screen = pg.display.set_mode((1000,1000))       #Screen size, should this be changed? 
pg.display.set_caption("Pygameforever")         #Game title
clock = pg.time.Clock()                         #How fast we want to run our game (fps/hz/pps)

while True:                                     #Infinite loop
    for events in pg.event.get():               #Our event-loop
        if events.type == pg.QUIT:
            pg.quit()
            exit()
    
    if game_active:                             #What to do when game is active
        print("Game is active")
    else:                                       #What to do when game is not active, aka gameover?
        print("Game is not active. Gameover?")


    pg.display.update()                         
    clock.tick(60)                              #Updates disp 60 times per sec
