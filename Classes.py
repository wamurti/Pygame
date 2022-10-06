import random
import pygame as pg
import os.path
main_dir = os.path.split(os.path.abspath(__file__))[0]
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
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
        self.image = load_image('gif.gif1.gif').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, 0))

    def update(self):
        self.rect.move_ip(0, +7)
        if self.rect.top > 1000:
            self.kill()

# Object class Player


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.sprites.append(load_image('player1.png').convert_alpha())
        self.sprites.append(load_image('player2.png').convert_alpha())
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