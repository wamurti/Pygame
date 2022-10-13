import random
import pygame as pg
import os.path
main_dir = os.path.split(os.path.abspath(__file__))[0]
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
#screen size for menu button class /JL
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'Graphics', file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pg.get_error()))
    return surface


class Boulder(pg.sprite.Sprite):
    def __init__(self):
        super(Boulder, self).__init__()
        x = random.randint(100, 900)
        y = random.randint(-300, 0)
        self.image = load_image('gif.gif1.gif').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, y))

    def update(self):
        self.rect.move_ip(0, +7)
        if self.rect.top > 1000:
            self.kill()

# Object class Player


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.sprites.append(pg.transform.scale(load_image('player1.png').convert_alpha(),(60,60)))
        self.sprites.append(pg.transform.scale(load_image('player2.png').convert_alpha(),(60,60)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.start_x = SCREEN_WIDTH//2
        self.start_y = SCREEN_HEIGHT-110
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.frame = 0
        self.animation = False

    def animate(self, trueorfalse):
        self.animation = trueorfalse
    def update(self):
        if self.animation == True:
            self.current_sprite += 0.05

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]

    def moveRight(self, pixels):
        if self.rect.right > SCREEN_WIDTH+20:
            pixels = 0
        else:
            self.rect.x += pixels


    def moveLeft(self, pixels):
        if self.rect.left < 0:
            pixels = 0
        else:    
            self.rect.x -= pixels

    def moveForward(self, pixels):    
        self.rect.y -= pixels

    def moveBack(self, pixels):
        if self.rect.bottom > SCREEN_HEIGHT+20:
            pixels = 0
        else:
            self.rect.y += pixels
class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
         
    def get_image(self,frame,width,height,scale,colour):
        image = pg.Surface((width,height)).convert_alpha()
        image.blit(self.sheet, (0,0),((frame*width),0,width,height))
        image = pg.transform.scale(image, (width*scale,height*scale))
        image.set_colorkey(colour)
        return image

# Load button images, mouse and click

class Button():
    
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, scale *(width, height)).convert_alpha()
        #self.image = pg.Surface.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        action = False
        # get mouse position
        pos = pg.mouse.get_pos()
        #Check mouseover and clicked condition
        if  self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:  # Musen klickad [0]Vänster ([1]Mitten [2]höger) == 1 
                self.clicked = True
                action = True            # Ändra till start main.py eller vilken det är

        if pg.mouse.get_pressed()[0] == 0:      # Gör den falsk när klickad en gång. 
            self.clicked = False
        

        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action