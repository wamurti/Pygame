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

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'Graphics', file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pg.get_error()))
    return surface.convert()

# Object class Player
class Sprite(pg.sprite.Sprite):
	def __init__(self, color, height, width):
		super().__init__()

		self.image = pg.Surface([width, height])
		self.image.fill((255,0,0))
		self.image.set_colorkey((0,255,0))

		pg.draw.rect(self.image,color,pg.Rect(0, 0, width, height))

		self.rect = self.image.get_rect()

	def moveRight(self, pixels):
		self.rect.x += pixels

	def moveLeft(self, pixels):
		self.rect.x -= pixels

	def moveForward(self, speed):
		self.rect.y += speed * speed/10

	def moveBack(self, speed):
		self.rect.y -= speed * speed/10

all_sprites_list = pg.sprite.Group()
playerCar = Sprite((255,0,0), 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300


all_sprites_list.add(playerCar)

#Load Images
map_surface = load_image('preview.png')
map_surface = pg.transform.scale(map_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))




while True:                                     #Infinite loop
    for events in pg.event.get():               #Our event-loop
        if events.type == pg.QUIT:
            pg.quit()
            exit()
    
    if game_active:                             #What to do when game is active

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            playerCar.moveLeft(10)
        if keys[pg.K_RIGHT]:
            playerCar.moveRight(10)
        if keys[pg.K_DOWN]:
            playerCar.moveForward(10)
        if keys[pg.K_UP]:
            playerCar.moveBack(10)



    else:                                       #What to do when game is not active, aka gameover?
        print("Game is not active. Gameover?")

    screen.blit(map_surface, (0,0))
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pg.display.update()                         
    clock.tick(60)                              #Updates disp 60 times per sec
