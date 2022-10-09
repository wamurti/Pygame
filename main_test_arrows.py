import pygame as pg
import os.path
import random
pg.init()
from pygame import mixer
from Classes import Boulder, Player

game_active = True
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
anim = 3
ALPHA =(0, 0, 0)
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))       #Screen size, should this be changed? 
pg.display.set_caption("Pygameforever")         #Game title
clock = pg.time.Clock()                         #How fast we want to run our game (fps/hz/pps)
bg = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
bg.fill((255,255,255))

# Font 

font = pg.font.Font('freesansbold.ttf', 75)
font_1= pg.font.Font('freesansbold.ttf', 50)
red = (200, 0, 0)
green = (0,200,0)
main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'Graphics', file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pg.get_error()))
    return surface

#Background Sound

mixer.init()
mixer.music.load(f"{main_dir}/Graphics/WoodlandFantasy.wav")
mixer.music.set_volume(0.2)
mixer.music.play(-1)
        

# Speed of Player Character
speed = 5


# A stationary enemy, that kills on contact. For holes and water etc.
class Hole(pg.sprite.Sprite):
    def __init__(self, width, height, posx, posy):
        super(Hole, self).__init__()
        
        self.image = pg.Surface((width,height))
        self.image = self.image.convert_alpha()
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect(center=(posx, posy))

# Arrows For Our Hero
class Arrow(pg.sprite.Sprite):
    def __init__(self):
        super(Arrow, self).__init__()
        
        self.image = load_image('arrow.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (10,30))
        
        self.rect = self.image.get_rect(midbottom = (playerCar.rect.midtop))
    
    def update(self):
        self.rect.move_ip(0, -10)
        if self.rect.y < -30:
            self.kill()

boulders = pg.sprite.Group()
ADDBOULDER = pg.USEREVENT +1
pg.time.set_timer(ADDBOULDER, 3000)

arrows = pg.sprite.Group()
holes = pg.sprite.Group()
waters = pg.sprite.Group()
boulders = pg.sprite.Group()
all_sprites_list = pg.sprite.Group()
playerCar = Player()
# Water-hole
water1 = Hole(300, 20, 420, 360)
water2 = Hole(20, 200, 270, 200)
water3 = Hole(20, 200, 560, 200)
water8 = Hole(400, 20, 450, 100)
# Dirt-hole
hole4 = Hole(70, 20, 460, 635)
hole5 = Hole(20, 70, 635, 550)
hole6 = Hole(70, 20, 600, 490)
hole7 = Hole(10, 70, 430, 600)
holes.add(hole4, hole5, hole6, hole7)
waters.add(water1, water2, water3, water8)
# Variables and list for shrink
liten = pg.transform.scale(playerCar.image, (60, 60))
mindre = pg.transform.scale(playerCar.image, (40, 40))
minst = pg.transform.scale(playerCar.image, (20, 20))
shrink = [liten, mindre, minst]


all_sprites_list.add(playerCar)
all_sprites_list.add(water1, water2, water3, water8, hole4, hole5, hole6, hole7)
#Load Images
map_surface = load_image('preview.png')
map_surface = pg.transform.scale(map_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
start_screen = load_image('blood_and_magic.png')
start_screen = pg.transform.scale(start_screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
end_screen = load_image('background.png')
end_screen = pg.transform.scale(end_screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
maps_cleared = 0
running = True

heart_1 = pg.transform.scale2x(load_image('Heart1.png'))
#pg.transform.scale2x(heart_1)
heart_2 = pg.transform.scale2x(load_image('Heart1.png'))
#pg.transform.scale2x(heart_2)
heart_3 = pg.transform.scale2x(load_image('Heart1.png'))
#pg.transform.scale2x(heart_3)
heart_rect_1 = heart_1.get_rect(center = (SCREEN_WIDTH - 16,15))
heart_rect_2 = heart_2.get_rect(center = (SCREEN_WIDTH - 50,15))
heart_rect_3 = heart_2.get_rect(center = (SCREEN_WIDTH - 84,15))

heart_1_empty = pg.transform.scale2x(load_image('Heart2.png'))
#pg.transform.scale2x(heart_1_empty)

heart_system = [heart_1,heart_rect_1, heart_2, heart_rect_2, heart_3, heart_rect_3, heart_1_empty]
number_of_hits = 0
maps_cleared = 0
def intro():
    intro =True
    while intro == True:
        keys = pg.key.get_pressed()
        for events in pg.event.get():              
            if events.type == pg.QUIT:
                pg.quit()
                exit()
            if keys[pg.K_SPACE]:
                intro = False
        screen.blit(start_screen, (0,0))
        hello = font_1.render("Welcome! Press Space to play!",True , green)
        helloRect = hello.get_rect()
        helloRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2) 
        screen.blit(hello, helloRect)
        pg.display.update()

def game_over():
    over = True
    
    while over == True:
        keys = pg.key.get_pressed()
            
        for events in pg.event.get():              
            if events.type == pg.QUIT:
                pg.quit()
                exit()
            if keys[pg.K_SPACE]:
                over = False
        screen.blit(end_screen, (0,0))
        goodbye = font.render("GAME OVER LOSER!",True , red)
        goodbyeRect = goodbye.get_rect()
        goodbyeRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2) 
        screen.blit(goodbye, goodbyeRect)
        pg.display.update()

def victory():
    winner = True
    
    while winner == True:
        keys = pg.key.get_pressed()
            
        for events in pg.event.get():              
            if events.type == pg.QUIT:
                pg.quit()
                exit()
            if keys[pg.K_SPACE]:
                winner = False
        screen.blit(end_screen, (0,0))
        hurray = font.render("You won! Hurray!",True , red)
        hurrayRect = hurray.get_rect()
        hurrayRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2) 
        screen.blit(hurray, hurrayRect)
        pg.display.update()
       

def game_loop():
    
    gaming = True
    
    while gaming:                            
        for events in pg.event.get():               
            if events.type == pg.QUIT:
                pg.quit()
                exit()
            if events.type == ADDBOULDER:
                new_boulder = Boulder()
                boulders.add(new_boulder)
                all_sprites_list.add(new_boulder)

            if events.type == pg.KEYDOWN:
                if events.key == pg.K_SPACE:
                    if len(arrows) < 1:
                        new_arrow = Arrow()
                        arrows.add(new_arrow)
                        all_sprites_list.add(new_arrow)
        
        if gaming:                         #What to do when game is active  

            keys = pg.key.get_pressed()
            playerCar.animate(False)
            if keys[pg.K_LEFT]:
                playerCar.animate(True)
                playerCar.moveLeft(speed)
                
            if keys[pg.K_RIGHT]:
                playerCar.animate(True)
                playerCar.moveRight(speed)
                
            if keys[pg.K_DOWN]:
                playerCar.animate(True)
                playerCar.moveBack(speed)
                
            if keys[pg.K_UP]:
                playerCar.animate(True)
                playerCar.moveForward(speed)
            
            if pg.sprite.groupcollide(arrows, boulders,True,True):
                print("TRÄFF")            

            if pg.sprite.spritecollideany(playerCar, boulders):
                global number_of_hits
            # Vad händer när spelaren blir träffad av en eldboll

                number_of_hits += 1
                if number_of_hits in range(0,15):
                    heart_system[0] = heart_system[6]
                    playerCar.moveBack(10)
                    playerCar.moveLeft(5)
                if number_of_hits in range(15,29):
                    heart_system[2] = heart_system[6]
                    playerCar.moveBack(10)
                    playerCar.moveLeft(5)
                if number_of_hits in range(30,44):
                    heart_system[4] = heart_system[6]
                    playerCar.moveBack(10)
                    playerCar.moveLeft(5)
                    playerCar.kill()
                    game_over()
                    gaming = False
                    

            if pg.sprite.spritecollideany(playerCar, holes):
                # If so, then remove the player and quit the game
                for i in shrink:
                    screen.blit(map_surface, (0,0))
                    screen.blit(i, (playerCar.rect))  
                    pg.display.update()
                    pg.time.wait(300)
                print("jord")

                playerCar.kill()
                game_over()
                gaming = False
            
            if pg.sprite.spritecollideany(playerCar, waters):
                # If so, then remove the player and quit the game
                for i in shrink:
                    screen.blit(map_surface, (0,0))
                    screen.blit(i, (playerCar.rect))  
                    pg.display.update()
                    pg.time.wait(300)
                print("vatten")

                playerCar.kill()
                game_over()
                gaming = False
                

            if playerCar.rect.bottom < 0:
                # If player clears the course
                global maps_cleared
                print("Du har nu klarat bana 1! ")
                maps_cleared += 1
                victory()
                gaming = False

        else:
            print("Game over")
            game_over()
        boulders.update()
        arrows.update()
        holes.update()
        playerCar.update()       # PLayer update /JL
        all_sprites_list.update()
        screen.blit(map_surface, (0,0))
        all_sprites_list.draw(screen)
        screen.blit(heart_system[0],heart_system[1])
        screen.blit(heart_system[2],heart_system[3])
        screen.blit(heart_system[4],heart_system[5])                   
        pg.display.update()                         
        clock.tick(60)   

while running:  
    intro()     
    game_loop()
    pg.quit()
    quit()
    