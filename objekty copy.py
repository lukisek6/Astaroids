#IMPORTS
import pygame
import os
import math
import random
#GLOBAL VARIABLES AND INITS
pygame.font.init()
pygame.mixer.init()
pygame.init()

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astaroids!")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 125, 255)
YELLOW =(255,255,0)
GREEN = (0,255,0)

BULLET_HIT_SOUND = pygame.mixer.Sound('Assets2/rocket.wav')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets2/blaster.wav')
BACKGROUND_SOUND = pygame.mixer.Sound('Assets2/duel_of_the_fates.wav')
BACKGROUND_SOUND.set_volume(0.3)
JEDI_WIN_SOUND = pygame.mixer.Sound('Assets2/force.wav')
SEPARATIST_WIN_SOUND = pygame.mixer.Sound('Assets2/force.wav')
YELLOW_PICK_SOUND = pygame.mixer.Sound('Assets2/pick_sound.wav')
RED_PICK_SOUND = pygame.mixer.Sound('Assets2/pick_sound.wav')
BLUE_PICK_SOUND = pygame.mixer.Sound('Assets2/pick_sound.wav')
MAP_PICK_SOUND = pygame.mixer.Sound('Assets2/pick_sound.wav')

GREEN_PICK_SOUND = pygame.mixer.Sound('Assets2/pick_sound.wav')
CRUISER_PICK_SOUND = pygame.mixer.Sound('Assets2/pick_sound.wav')
JACHT_PICK_SOUND = pygame.mixer.Sound('Assets2/pick_sound.wav')
MAUL_PICK_SOUND = pygame.mixer.Sound('Assets2/pick_sound.wav')
NABOO_PICK_SOUND = pygame.mixer.Sound('Assets2/pick_sound.wav')
SMUGGLER_PICK_SOUND = pygame.mixer.Sound('Assets2/pick_sound.wav')
XWING_PICK_SOUND = pygame.mixer.Sound('Assets2/pick_sound.wav')
YWING_PICK_SOUND = pygame.mixer.Sound('Assets2/pick_sound.wav')

CRATE_POP_SOUND = pygame.mixer.Sound('Assets2/pop.wav')
CRATE_PICKUP_SOUND = pygame.mixer.Sound('Assets2/pick_up.wav')
BONUS_OFF_SOUND = pygame.mixer.Sound('Assets2/bonus_off.wav')
ROCKET_LOOP_SOUND = pygame.mixer.Sound('Assets2/rocket_loop.wav')
ROCKET_LOOP_SOUND.set_volume(0.1)

HEALTH_FONT = pygame.font.SysFont('candara', 40)
WINNER_FONT = pygame.font.SysFont('candara', 100)

FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 40,55

JEDI_HIT = pygame.USEREVENT + 1
SEPARATIST_HIT = pygame.USEREVENT + 2
ASTEROID_HIT = pygame.USEREVENT + 3

#SHIPS IMAGES
CRATE_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'bedna.png'))

CRATE = pygame.transform.rotate(pygame.transform.scale(
    CRATE_IMAGE, (30,30)), 0)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship1.png'))

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship2.png'))

BLUE_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship3.png'))

GREEN_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship4.png'))

CRUISER_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship12.png'))

JACHT_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship13.png'))

MAUL_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship14.png'))

NABOO_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship15.png'))

SMUGGLER_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship16.png'))

XWING_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship17.png'))

YWING_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship18.png'))

DROIDCRUISER_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship8.png'))

DROIDCRUISER_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    DROIDCRUISER_SPACESHIP_IMAGE, (170,270)), 90)

droidcruiser = pygame.Rect(WIDTH/2 -125, 500, 170, 270)

VENATOR_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'jedi_ship8.png'))

VENATOR_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    VENATOR_SPACESHIP_IMAGE, (170,270)), 270)

venator = pygame.Rect(WIDTH/2 -125, 80, 170, 270)

ASTEROID_IMAGE = pygame.image.load(
    os.path.join('Assets2', 'asteroid.png'))

ASTEROID = pygame.transform.rotate(pygame.transform.scale(
    ASTEROID_IMAGE, (240,240)), 0)

asteroid = pygame.Rect(WIDTH/2 -120, HEIGHT/2-120, 240, 240)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets2', 'space.png')), (WIDTH, HEIGHT))

class Player:
    def __init__(self, x, y, width, height,image,health,speed,bullet_speed,bullets,rotation):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.rect = pygame.Rect(x,y,width,height)
        self.health = health
        self.vel = speed
        self.bullet_speed = bullet_speed
        self.bullets = bullets
        self.rotation = rotation
        self.magazine = []
        self.damage = 1
        self.bullet_size = 7

        self.SPEED = speed
        self.BULLET_SPEED = bullet_speed
        self.BULLETS = bullets
    
    def chosen_ship(self):
        if self.image == 0:
            self.image = YELLOW_SPACESHIP_IMAGE
        elif self.image == 1:
            self.image = RED_SPACESHIP_IMAGE
        elif self.image == 2:
            self.image = BLUE_SPACESHIP_IMAGE
        elif self.image == 3:
            self.image = GREEN_SPACESHIP_IMAGE
        elif self.image == 4:
            self.image = CRUISER_SPACESHIP_IMAGE
        elif self.image == 5:
            self.image = JACHT_SPACESHIP_IMAGE
        elif self.image == 6:
            self.image = MAUL_SPACESHIP_IMAGE
        elif self.image == 7:
            self.image = NABOO_SPACESHIP_IMAGE
        elif self.image == 8:
            self.image = SMUGGLER_SPACESHIP_IMAGE
        elif self.image == 9:
            self.image = XWING_SPACESHIP_IMAGE
        elif self.image == 10:
            self.image = YWING_SPACESHIP_IMAGE

    def move(self,token,MAP,flame1,flame2):
        keys_pressed = pygame.key.get_pressed()

        if MAP !=0:
            #JEDI----PLAYER1
            if token == 1:
                if keys_pressed[pygame.K_a] and keys_pressed[pygame.K_w] and self.x - self.vel > 0 and self.y - self.vel > 0:
                    self.x -= self.vel
                    self.y -= self.vel
                    self.rotation = 45
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 225
                    flame1.x = (self.x+self.width+8)
                    flame1.y = (self.y+self.height*(2/3)+8)
                    flame1.update()
                elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_w] and self.x + self.vel + self.width < WIDTH and self.y - self.vel > 0:
                    self.x += self.vel
                    self.y -= self.vel
                    self.rotation = 315
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 90+45
                    flame1.x = (self.x-self.width/2+12)
                    flame1.y = (self.y+self.height*(2/3)+12)
                    flame1.update()
                elif keys_pressed[pygame.K_a] and keys_pressed[pygame.K_s] and self.x - self.vel > 0 and self.y + self.vel + self.height < HEIGHT - 15:
                    self.x -= self.vel
                    self.y += self.vel
                    self.rotation = 135
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 315
                    flame1.x = (self.x+self.width+7)
                    flame1.y = (self.y-9)
                    flame1.update()
                elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_s] and self.x + self.vel + self.width < WIDTH and self.y + self.vel + self.height < HEIGHT - 15:
                    self.x += self.vel
                    self.y += self.vel
                    self.rotation = 225
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 45
                    flame1.x = (self.x-7)
                    flame1.y = (self.y-7)
                    flame1.update()
                elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_a]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_w] and keys_pressed[pygame.K_s]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_a] and self.x - self.vel > 0:  # LEFT
                    self.x -= self.vel
                    self.rotation = 90
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 270
                    flame1.x = (self.x+self.height)
                    flame1.y = (self.y+self.width/2-8)
                    flame1.update()
                elif keys_pressed[pygame.K_d] and self.x + self.vel + self.width < WIDTH:  # RIGHT
                    self.x += self.vel
                    self.rotation = 270
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 90
                    flame1.x = (self.x-self.height/2)
                    flame1.y = (self.y+self.width/2-7)
                    flame1.update()
                elif keys_pressed[pygame.K_w] and self.y - self.vel > 0:  # UP
                    self.y -= self.vel
                    self.rotation = 0
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 180
                    flame1.x = (self.x+self.width/2-7)
                    flame1.y = (self.y+self.height-3)
                    flame1.update()
                elif keys_pressed[pygame.K_s] and self.y + self.vel + self.height < HEIGHT:  # DOWN
                    self.y += self.vel
                    self.rotation = 180
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 0
                    flame1.x = (self.x+self.width/2-8)
                    flame1.y = (self.y-self.height/2+3)
                    flame1.update()
            #SEPARATIST----PLAYER2
            elif token == 2:
                if keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_UP] and self.x - self.vel > 0 and self.y - self.vel > 0:
                    self.x -= self.vel
                    self.y -= self.vel
                    self.rotation = 45
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 225
                    flame2.x = (self.x+self.width+8)
                    flame2.y = (self.y+self.height*(2/3)+8)
                    flame2.update()
                elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_UP] and self.x + self.vel + self.width < WIDTH and self.y - self.vel > 0:
                    self.x += self.vel
                    self.y -= self.vel
                    self.rotation = 315
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 90+45
                    flame2.x = (self.x-self.width/2+12)
                    flame2.y = (self.y+self.height*(2/3)+12)
                    flame2.update()
                elif keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_DOWN] and self.x - self.vel > 0 and self.y + self.vel + self.height < HEIGHT:
                    self.x -= self.vel
                    self.y += self.vel
                    self.rotation = 135
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 315
                    flame2.x = (self.x+self.width+7)
                    flame2.y = (self.y-9)
                    flame2.update()
                elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_DOWN] and self.x + self.vel + self.width < WIDTH and self.y + self.vel + self.height < HEIGHT:
                    self.x += self.vel
                    self.y += self.vel
                    self.rotation = 225
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 45
                    flame2.x = (self.x-7)
                    flame2.y = (self.y-7)
                    flame2.update()
                elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_LEFT]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_DOWN]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_LEFT] and self.x - self.vel > 0:  # LEFT
                    self.x -= self.vel
                    self.rotation = 90
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 270
                    flame2.x = (self.x+self.height)
                    flame2.y = (self.y+self.width/2-8)
                    flame2.update()
                elif keys_pressed[pygame.K_RIGHT] and self.x + self.vel + self.width < WIDTH:  # RIGHT
                    self.x += self.vel
                    self.rotation = 270
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 90
                    flame2.x = (self.x-self.height/2)
                    flame2.y = (self.y+self.width/2-7)
                    flame2.update()
                elif keys_pressed[pygame.K_UP] and self.y - self.vel > 0:  # UP
                    self.y -= self.vel
                    self.rotation = 0
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 180
                    flame2.x = (self.x+self.width/2-7)
                    flame2.y = (self.y+self.height-3)
                    flame2.update()
                elif keys_pressed[pygame.K_DOWN] and self.y + self.vel + self.height < HEIGHT:  # DOWN
                    self.y += self.vel
                    self.rotation = 180
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 0
                    flame2.x = (self.x+self.width/2-8)
                    flame2.y = (self.y-self.height/2+3)
                    flame2.update()
        elif MAP == 0:#pygame.Rect(WIDTH/2 -120, HEIGHT/2-120, 240, 240)
            #JEDI
            if token == 1:
                if keys_pressed[pygame.K_a] and keys_pressed[pygame.K_w] and self.x - self.vel > 0 and self.y - self.vel > 0 and ( ( (self.x - self.vel > 760) or (self.x < 520) )or( (self.y<240) or (self.y - self.vel > 480) ) ):
                    self.x -= self.vel
                    self.y -= self.vel
                    self.rotation = 45
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 225
                    flame1.x = (self.x+self.width+8)
                    flame1.y = (self.y+self.height*(2/3)+8)
                    flame1.update()
                elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_w] and self.x + self.vel + self.width < WIDTH and self.y - self.vel > 0 and ( ( (self.x > 760) or (self.x + self.vel + self.width < 520) )or( (self.y<240) or (self.y - self.vel > 480) ) ):
                    self.x += self.vel
                    self.y -= self.vel
                    self.rotation = 315
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 90+45
                    flame1.x = (self.x-self.width/2+12)
                    flame1.y = (self.y+self.height*(2/3)+12)
                    flame1.update()
                elif keys_pressed[pygame.K_a] and keys_pressed[pygame.K_s] and self.x - self.vel > 0 and self.y + self.vel + self.height < HEIGHT - 15 and ( ( (self.x - self.vel > 760) or (self.x < 520) )or( (self.y + self.vel + self.height<240) or (self.y > 480) ) ):
                    self.x -= self.vel
                    self.y += self.vel
                    self.rotation = 135
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 315
                    flame1.x = (self.x+self.width+7)
                    flame1.y = (self.y-9)
                    flame1.update()
                elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_s] and self.x + self.vel + self.width < WIDTH and self.y + self.vel + self.height < HEIGHT - 15 and ( ( (self.x > 760) or (self.x + self.vel + self.width < 520) )or( (self.y + self.vel + self.height<240) or (self.y > 480) ) ):
                    self.x += self.vel
                    self.y += self.vel
                    self.rotation = 225
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 45
                    flame1.x = (self.x-7)
                    flame1.y = (self.y-7)
                    flame1.update()
                elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_a]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_w] and keys_pressed[pygame.K_s]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_a] and self.x - self.vel > 0 and ( ( (self.x - self.vel > 760) or (self.x < 520) )or( (self.y<240-SPACESHIP_WIDTH) or (self.y > 480) ) ):  # LEFT
                    self.x -= self.vel
                    self.rotation = 90
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 270
                    flame1.x = (self.x+self.height)
                    flame1.y = (self.y+self.width/2-8)
                    flame1.update()
                elif keys_pressed[pygame.K_d] and self.x + self.vel + self.width < WIDTH and ( ( (self.x > 760) or (self.x + self.vel + self.width < 520) )or( (self.y<240-SPACESHIP_WIDTH) or (self.y > 480) ) ):  # RIGHT
                    self.x += self.vel
                    self.rotation = 270
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 90
                    flame1.x = (self.x-self.height/2)
                    flame1.y = (self.y+self.width/2-7)
                    flame1.update()
                elif keys_pressed[pygame.K_w] and self.y - self.vel > 0 and ( ( (self.x > 760) or (self.x < 520-SPACESHIP_WIDTH) )or( (self.y<240) or (self.y - self.vel > 480) ) ):  # UP
                    self.y -= self.vel
                    self.rotation = 0
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 180
                    flame1.x = (self.x+self.width/2-7)
                    flame1.y = (self.y+self.height-3)
                    flame1.update()
                elif keys_pressed[pygame.K_s] and self.y + self.vel + self.height < HEIGHT and ( ( (self.x > 760) or (self.x < 520-SPACESHIP_WIDTH) )or( (self.y + self.vel + self.height<240) or (self.y > 480) ) ):  # DOWN
                    self.y += self.vel
                    self.rotation = 180
                    flame1.ON_OFF = "ON"
                    flame1.rotation = 0
                    flame1.x = (self.x+self.width/2-8)
                    flame1.y = (self.y-self.height/2+3)
                    flame1.update()
            #SEPARATIST
            elif token == 2:
                if keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_UP] and self.x - self.vel > 0 and self.y - self.vel > 0 and ( ( (self.x - self.vel > 760) or (self.x < 520) )or( (self.y<240) or (self.y - self.vel > 480) ) ):
                    self.x -= self.vel
                    self.y -= self.vel
                    self.rotation = 45
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 225
                    flame2.x = (self.x+self.width+8)
                    flame2.y = (self.y+self.height*(2/3)+8)
                    flame2.update()
                elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_UP] and self.x + self.vel + self.width < WIDTH and self.y - self.vel > 0 and ( ( (self.x > 760) or (self.x + self.vel + self.width < 520) )or( (self.y<240) or (self.y - self.vel > 480) ) ):
                    self.x += self.vel
                    self.y -= self.vel
                    self.rotation = 315
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 90+45
                    flame2.x = (self.x-self.width/2+12)
                    flame2.y = (self.y+self.height*(2/3)+12)
                    flame2.update()
                elif keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_DOWN] and self.x - self.vel > 0 and self.y + self.vel + self.height < HEIGHT and ( ( (self.x - self.vel > 760) or (self.x < 520) )or( (self.y + self.vel + self.height<240) or (self.y > 480) ) ):
                    self.x -= self.vel
                    self.y += self.vel
                    self.rotation = 135
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 315
                    flame2.x = (self.x+self.width+7)
                    flame2.y = (self.y-9)
                    flame2.update()
                elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_DOWN] and self.x + self.vel + self.width < WIDTH and self.y + self.vel + self.height < HEIGHT and ( ( (self.x > 760) or (self.x + self.vel + self.width < 520) )or( (self.y + self.vel + self.height<240) or (self.y > 480) ) ):
                    self.x += self.vel
                    self.y += self.vel
                    self.rotation = 225
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 45
                    flame2.x = (self.x-7)
                    flame2.y = (self.y-7)
                    flame2.update()
                elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_LEFT]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_DOWN]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_LEFT] and self.x - self.vel > 0 and ( ( (self.x - self.vel > 760) or (self.x < 520) )or( (self.y<240-SPACESHIP_WIDTH) or (self.y > 480) ) ):  # LEFT
                    self.x -= self.vel
                    self.rotation = 90
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 270
                    flame2.x = (self.x+self.height)
                    flame2.y = (self.y+self.width/2-8)
                    flame2.update()
                elif keys_pressed[pygame.K_RIGHT] and self.x + self.vel + self.width < WIDTH and ( ( (self.x > 760) or (self.x + self.vel + self.width < 520) )or( (self.y<240-SPACESHIP_WIDTH) or (self.y > 480) ) ):  # RIGHT
                    self.x += self.vel
                    self.rotation = 270
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 90
                    flame2.x = (self.x-self.height/2)
                    flame2.y = (self.y+self.width/2-7)
                    flame2.update()
                elif keys_pressed[pygame.K_UP] and self.y - self.vel > 0 and ( ( (self.x > 760) or (self.x < 520-SPACESHIP_WIDTH) )or( (self.y<240) or (self.y - self.vel > 480) ) ):  # UP
                    self.y -= self.vel
                    self.rotation = 0
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 180
                    flame2.x = (self.x+self.width/2-7)
                    flame2.y = (self.y+self.height-3)
                    flame2.update()
                elif keys_pressed[pygame.K_DOWN] and self.y + self.vel + self.height < HEIGHT and ( ( (self.x > 760) or (self.x < 520-SPACESHIP_WIDTH) )or( (self.y + self.vel + self.height<240) or (self.y > 480) ) ):  # DOWN
                    self.y += self.vel
                    self.rotation = 180
                    flame2.ON_OFF = "ON"
                    flame2.rotation = 0
                    flame2.x = (self.x+self.width/2-8)
                    flame2.y = (self.y-self.height/2+3)
                    flame2.update()

        self.update()

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_xy_ship(self):
        if self.rotation == 0:
            o,p = self.x+SPACESHIP_WIDTH/2,self.y-100
        elif self.rotation == 45:
            o,p = self.x-100,self.y-100
        elif self.rotation == 90:
            o,p = self.x-100,self.y+ SPACESHIP_HEIGHT/2 - 10
        elif self.rotation == 135:
            o,p = self.x + SPACESHIP_WIDTH/2-100,self.y+ SPACESHIP_HEIGHT/2 - 10 +100
        elif self.rotation == 180:
            o,p = self.x + SPACESHIP_WIDTH/2,self.y+100
        elif self.rotation == 225:
            o,p = self.x+ SPACESHIP_WIDTH/2+100,self.y + SPACESHIP_HEIGHT/2 - 10 +100
        elif self.rotation == 270:
            o,p = self.x+100,self.y + SPACESHIP_HEIGHT/2 - 10
        elif self.rotation == 315:
            o,p = self.x+ SPACESHIP_WIDTH/2+100,self.y + SPACESHIP_HEIGHT/2 - 10 -100
        return(o,p)

    def gun_fire_ship(self):
        o,p = self.get_xy_ship()
        bullet = Bullet(BLUE, self.x + SPACESHIP_WIDTH/2, self.y + SPACESHIP_HEIGHT/2 - 10, self.bullet_size,self.bullet_size, self.bullet_speed, o,p)
        self.magazine.append(bullet)
        BULLET_FIRE_SOUND.play()
    
    def reset(self):
        self.vel = self.SPEED
        self.bullet_speed = self.BULLET_SPEED
        self.bullets = self.BULLETS
        self.damage = 1
        self.bullet_size = 7
        BONUS_OFF_SOUND.play()

class Square:
    def __init__(self, color, x, y, width, height, speed):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.direction = 'E'
        self.speed = speed
class Bullet(Square):
    def __init__(self, color, x, y, width, height, speed, targetx,targety):
        super().__init__(color, x, y, width, height, speed)
        angle = math.atan2(targety-y, targetx-x) #get angle to target in radians
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.x = x
        self.y = y
    def move(self):
        #self.x and self.y are floats (decimals) so I get more accuracy
        #if I change self.x and y and then convert to an integer for
        #the rectangle.
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

class Cruiser:
    def __init__(self,x,y,width,height):
        self.magazine = []
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x,y,width,height)

    def get_xy_cruiser(self,ship):
        if ship.rotation == 0:
            o,p = ship.x+SPACESHIP_WIDTH/2,ship.y
        elif ship.rotation == 45:
            o,p = ship.x,ship.y
        elif ship.rotation == 90:
            o,p = ship.x,ship.y+ SPACESHIP_HEIGHT/2 - 10
        elif ship.rotation == 135:
            o,p = ship.x + SPACESHIP_WIDTH/2,ship.y+ SPACESHIP_HEIGHT/2 - 10 
        elif ship.rotation == 180:
            o,p = ship.x + SPACESHIP_WIDTH/2,ship.y
        elif ship.rotation == 225:
            o,p = ship.x+ SPACESHIP_WIDTH/2,ship.y + SPACESHIP_HEIGHT/2 - 10 
        elif ship.rotation == 270:
            o,p = ship.x,ship.y + SPACESHIP_HEIGHT/2 - 10
        elif ship.rotation == 315:
            o,p = ship.x+ SPACESHIP_WIDTH/2,ship.y + SPACESHIP_HEIGHT/2 - 10 
        return(o,p)

    def gun_fire_cruiser(self,jedi,separatist,token):
        if len(self.magazine) < (jedi.bullets+separatist.bullets):
            if token == 2:
                o,p = self.get_xy_cruiser(separatist)
            elif token == 1:
                o,p = self.get_xy_cruiser(jedi)
            bullet = Bullet(BLUE, WIDTH/2, self.y+self.width/2, 7,7, 5, o,p)
            self.magazine.append(bullet)
            BULLET_FIRE_SOUND.play()

class Crate(Player):
    def __init__(self,):
        pass

class animation:
    def __init__(self,x,y,rotation):
        self.x = x
        self.y = y
        self.number = 0
        self.ON_OFF = "OFF"
        self.image = FIRE_IMAGE = pygame.image.load(
            os.path.join('Assets2', 'flame'+str(self.number)+'.png'))
        self.rotation = rotation
        self.flame = pygame.transform.rotate(pygame.transform.scale(
            self.image, (15,25)), self.rotation)
        self.rect = pygame.Rect(self.x, self.y,15,25)

    def update(self):
        self.image = FIRE_IMAGE = pygame.image.load(
            os.path.join('Assets2', 'flame'+str(self.number)+'.png'))
        self.flame = pygame.transform.rotate(pygame.transform.scale(
            self.image, (15,25)), self.rotation)

class animation2:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.number = 0
        self.ON_OFF = "OFF"
        self.image = BOOM_IMAGE = pygame.image.load(
            os.path.join('Assets2', 'boom'+str(self.number)+'.png'))
        self.boom = pygame.transform.rotate(pygame.transform.scale(
            self.image, (25,25)), 0)

    def update(self):
        self.image = BOOM_IMAGE = pygame.image.load(
            os.path.join('Assets2', 'boom'+str(self.number)+'.png'))
        self.boom = pygame.transform.rotate(pygame.transform.scale(
            self.image, (25,25)), 0)
#DO IT
def do_it():
    BACKGROUND_SOUND.play()
    First_SHIP, HEALTH1, SPEED1, BULLET_SPEED1, BULLETS1 = menu1()
    jedi = Player(100,360,SPACESHIP_WIDTH, SPACESHIP_HEIGHT,First_SHIP, HEALTH1, SPEED1, BULLET_SPEED1, BULLETS1,270)
    flame1 = animation(100,360,90)
    Second_SHIP, HEALTH2, SPEED2, BULLET_SPEED2, BULLETS2 = menu1()
    separatist = Player(1130, 360,SPACESHIP_WIDTH, SPACESHIP_HEIGHT,Second_SHIP, HEALTH2, SPEED2, BULLET_SPEED2, BULLETS2,90)
    flame2 = animation(1130,360,270)
    MAP = menu2()
    BACKGROUND_SOUND.stop()
    BACKGROUND_SOUND.play()
    main(jedi,separatist, MAP,flame1,flame2)
#MENU
def menu1():
    choice = 0
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    choice += 1
                if event.key == pygame.K_LEFT:
                    choice -= 1
                if event.key == pygame.K_SPACE:
                    if choice == 0:
                        HEALTH = 5
                        SPEED = 5
                        BULLET_SPEED = 12
                        BULLETS = 7
                        YELLOW_PICK_SOUND.play()
                    elif choice == 1:
                        HEALTH = 15
                        SPEED = 3
                        BULLET_SPEED = 10
                        BULLETS = 15
                        RED_PICK_SOUND.play()
                    elif choice == 2:
                        HEALTH = 1
                        SPEED = 10
                        BULLET_SPEED = 14
                        BULLETS = 2
                        BLUE_PICK_SOUND.play()
                    elif choice == 3:
                        HEALTH = 3
                        SPEED = 6
                        BULLET_SPEED = 15
                        BULLETS = 1
                        GREEN_PICK_SOUND.play()
                    elif choice == 4:
                        HEALTH = 20
                        SPEED = 2
                        BULLET_SPEED = 15
                        BULLETS = 10
                        CRUISER_PICK_SOUND.play()
                    elif choice == 5:
                        HEALTH = 10
                        SPEED = 4
                        BULLET_SPEED = 15
                        BULLETS = 1
                        JACHT_PICK_SOUND.play()
                    elif choice == 6:
                        HEALTH = 8
                        SPEED = 5
                        BULLET_SPEED = 10
                        BULLETS = 5
                        MAUL_PICK_SOUND.play()
                    elif choice == 7:
                        HEALTH = 4
                        SPEED = 7
                        BULLET_SPEED = 10
                        BULLETS = 2
                        NABOO_PICK_SOUND.play()
                    elif choice == 8:
                        HEALTH = 10
                        SPEED = 4
                        BULLET_SPEED = 8
                        BULLETS = 12
                        SMUGGLER_PICK_SOUND.play()
                    elif choice == 9:
                        HEALTH = 5
                        SPEED = 8
                        BULLET_SPEED = 10
                        BULLETS = 4
                        XWING_PICK_SOUND.play()
                    elif choice == 10:
                        HEALTH = 5
                        SPEED = 6
                        BULLET_SPEED = 10
                        BULLETS = 8
                        YWING_PICK_SOUND.play()
                    return(choice,HEALTH, SPEED, BULLET_SPEED, BULLETS)
                    run = False
        if choice == -1:
            choice = 10
        if choice == 11:
            choice = 0

        show_window(choice)
#MENU VISUALIZATION
def show_window(choice):
    WIN.blit(SPACE, (0, 0))
    chose_text = HEALTH_FONT.render(
        "SHIP SELECTION", 1, YELLOW)
    WIN.blit(chose_text, (WIDTH/2-chose_text.get_width() / 2, 10))
    if choice ==0:
        YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(YELLOW_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "CLASSIC: HEALTH 5, SPEED 5, BULLET SPEED 12, BULLETS 7", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==1:
        RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(RED_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))

        yellow_ship_text = HEALTH_FONT.render(
        "BOMBER: HEALTH 15, SPEED 3, BULLET SPEED 10, BULLETS 15", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==2:
        BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        BLUE_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(BLUE_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "SPEEDO: HEALTH 1, SPEED 10, BULLET SPEED 14, BULLETS 2", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))
    
    elif choice ==3:
        GREEN_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        GREEN_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(GREEN_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "ONE SHOT: HEALTH 3, SPEED 6, BULLET SPEED 15, BULLETS 1", 1, GREEN)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==4:
        CRUISER_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        CRUISER_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(CRUISER_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "HEAVY: HEALTH 20, SPEED 2, BULLET SPEED 15, BULLETS 10", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))
    
    elif choice ==5:
        JACHT_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        JACHT_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(JACHT_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "JACHT: HEALTH 10, SPEED 4, BULLET SPEED 15, BULLETS 1", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==6:
        MAUL_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        MAUL_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(MAUL_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "WAR SHIP: HEALTH 8, SPEED 5, BULLET SPEED 10, BULLETS 5", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==7:
        NABOO_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        NABOO_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(NABOO_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "CORVETTE: HEALTH 4, SPEED 7, BULLET SPEED 10, BULLETS 2", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==8:
        SMUGGLER_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        SMUGGLER_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(SMUGGLER_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "SMUGGLER'S SHIP: HEALTH 10, SPEED 4, BULLET SPEED 8, BULLETS 12", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==9:
        XWING_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        XWING_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(XWING_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "FIGHTER: HEALTH 5, SPEED 8, BULLET SPEED 10, BULLETS 4", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==10:
        YWING_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        YWING_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(YWING_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "TACTICAL BOMBER: HEALTH 5, SPEED 6, BULLET SPEED 10, BULLETS 8", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    pygame.display.update()
#MENU2
def menu2():
    choice = 0
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    choice += 1
                if event.key == pygame.K_LEFT:
                    choice -= 1
                if event.key == pygame.K_SPACE:
                        MAP_PICK_SOUND.play()
                        return(choice)
        if choice == -1:
            choice = 4
        if choice == 5:
            choice = 0
        show_window2(choice)
#MENU2 VISUALIZATION        
def show_window2(choice):
    WIN.blit(SPACE, (0, 0))
    chose_text = HEALTH_FONT.render(
        "MAP SELECTION", 1, YELLOW)
    WIN.blit(chose_text, (WIDTH/2-140, 10))
    if choice ==0:
        WIN.blit(ASTEROID, (asteroid.x,asteroid.y))
    elif choice ==1:
        WIN.blit(VENATOR_SPACESHIP, (venator.x,venator.y))
    elif choice ==2:
        WIN.blit(DROIDCRUISER_SPACESHIP, (droidcruiser.x,droidcruiser.y))
    elif choice ==3:
        WIN.blit(DROIDCRUISER_SPACESHIP, (droidcruiser.x,droidcruiser.y))
        WIN.blit(VENATOR_SPACESHIP, (venator.x,venator.y))
    
    pygame.display.update()
#COLLIDERECTS
def bullet_colliderects(jedi,separatist,venator,droidcruiser,asteroid,MAP,booms):
    if MAP == 0:
        #JEDI BULLETS MOVEMENT
        for bullet in jedi.magazine:
            bullet.move()       
            #bullet_cleaning
            if separatist.rect.colliderect(bullet):
                boom = animation2(bullet.x,bullet.y)
                booms.append(boom)
                pygame.event.post(pygame.event.Event(SEPARATIST_HIT))
                jedi.magazine.remove(bullet)
            elif asteroid.colliderect(bullet):
                boom = animation2(bullet.x,bullet.y)
                booms.append(boom)
                pygame.event.post(pygame.event.Event(ASTEROID_HIT))
                jedi.magazine.remove(bullet)
            elif bullet.x > WIDTH:
                jedi.magazine.remove(bullet)
            elif bullet.x < 0:
                jedi.magazine.remove(bullet)
            elif bullet.y < 0:
                jedi.magazine.remove(bullet)
            elif bullet.y > HEIGHT:
                jedi.magazine.remove(bullet)

        #SEPARATIST BULLETS MOVEMENT
        for bullet in separatist.magazine:
            bullet.move()
            #bullet_cleaning
            if jedi.rect.colliderect(bullet):
                boom = animation2(bullet.x,bullet.y)
                booms.append(boom)
                pygame.event.post(pygame.event.Event(JEDI_HIT))
                separatist.magazine.remove(bullet)
            elif asteroid.colliderect(bullet):
                boom = animation2(bullet.x,bullet.y)
                booms.append(boom)
                pygame.event.post(pygame.event.Event(ASTEROID_HIT))
                separatist.magazine.remove(bullet)
            elif bullet.x > WIDTH:
                separatist.magazine.remove(bullet)
            elif bullet.x < 0:
                separatist.magazine.remove(bullet)
            elif bullet.y < 0:
                separatist.magazine.remove(bullet)
            elif bullet.y > HEIGHT:
                separatist.magazine.remove(bullet)
    else:
        #JEDI BULLETS MOVEMENT
        for bullet in jedi.magazine:
            bullet.move()       
            #bullet_cleaning
            if separatist.rect.colliderect(bullet):
                boom = animation2(bullet.x,bullet.y)
                booms.append(boom)
                pygame.event.post(pygame.event.Event(SEPARATIST_HIT))
                jedi.magazine.remove(bullet)
            elif bullet.x > WIDTH:
                jedi.magazine.remove(bullet)
            elif bullet.x < 0:
                jedi.magazine.remove(bullet)
            elif bullet.y < 0:
                jedi.magazine.remove(bullet)
            elif bullet.y > HEIGHT:
                jedi.magazine.remove(bullet)
        
        #SEPARATIST BULLETS MOVEMENT
        for bullet in separatist.magazine:
            bullet.move()
            #bullet_cleaning
            if jedi.rect.colliderect(bullet):
                boom = animation2(bullet.x,bullet.y)
                booms.append(boom)
                pygame.event.post(pygame.event.Event(JEDI_HIT))
                separatist.magazine.remove(bullet)
            elif bullet.x > WIDTH:
                separatist.magazine.remove(bullet)
            elif bullet.x < 0:
                separatist.magazine.remove(bullet)
            elif bullet.y < 0:
                separatist.magazine.remove(bullet)
            elif bullet.y > HEIGHT:
                separatist.magazine.remove(bullet)

    #VENATOR BULLETS
    for bullet in venator.magazine:
        bullet.move()       
        #bullet_cleaning
        if separatist.rect.colliderect(bullet):
            boom = animation2(bullet.x,bullet.y)
            booms.append(boom)
            pygame.event.post(pygame.event.Event(SEPARATIST_HIT))
            venator.magazine.remove(bullet)
        elif bullet.x > WIDTH:
            venator.magazine.remove(bullet)
        elif bullet.x < 0:
            venator.magazine.remove(bullet)
        elif bullet.y < 0:
            venator.magazine.remove(bullet)
        elif bullet.y > HEIGHT:
            venator.magazine.remove(bullet)

    #DROIDCRUISER BULLETS
    for bullet in droidcruiser.magazine:
        bullet.move()
        #bullet_cleaning
        if jedi.rect.colliderect(bullet):
            boom = animation2(bullet.x,bullet.y)
            booms.append(boom)
            pygame.event.post(pygame.event.Event(JEDI_HIT))
            droidcruiser.magazine.remove(bullet)
        elif bullet.x > WIDTH:
            droidcruiser.magazine.remove(bullet)
        elif bullet.x < 0:
            droidcruiser.magazine.remove(bullet)
        elif bullet.y < 0:
            droidcruiser.magazine.remove(bullet)
        elif bullet.y > HEIGHT:
            droidcruiser.magazine.remove(bullet)

    for boom in booms:
        boom.ON_OFF = "ON"
#WINNER
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    BULLET_HIT_SOUND.stop()
    BULLET_FIRE_SOUND.stop()
    SEPARATIST_WIN_SOUND.play()
    pygame.time.delay(3000)
#VISUALIZATION
def draw_window(separatist, jedi,MAP,venator,droidcruiser,crate,flame1,flame2,cas2,booms):
    #USED VARIABLES
    JEDI_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    jedi.image, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), jedi.rotation)
    
    SEPARATIST_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    separatist.image, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), separatist.rotation)

    #BACKGROUND
    WIN.blit(SPACE, (0, 0))

    #CRATES
    WIN.blit(CRATE,(crate.x,crate.y))

    #FLAME ANIMATIONS
    if flame1.ON_OFF == "ON":
        if cas2%7 == 0:
            flame1.number += 1
            if flame1.number == 8:
                flame1.number = 0
        flame1.update()
        WIN.blit(flame1.flame, (flame1.x, flame1.y))
        flame1.ON_OFF = "OFF"

    if flame2.ON_OFF == "ON":
        if cas2%7 == 0:
            flame2.number += 1
            if flame2.number == 8:
                flame2.number = 0
        flame2.update()
        WIN.blit(flame2.flame, (flame2.x, flame2.y))
        flame2.ON_OFF = "OFF"

    
    #TEXT
    separatist_health_text = HEALTH_FONT.render(
        "Health: " + str(separatist.health), 1, WHITE)
    jedi_health_text = HEALTH_FONT.render(
        "Health: " + str(jedi.health), 1, WHITE)
    WIN.blit(separatist_health_text, (WIDTH - separatist_health_text.get_width() - 10, 10))
    WIN.blit(jedi_health_text, (10, 10))

    #SHIPS
    WIN.blit(JEDI_SPACESHIP, (jedi.x, jedi.y))
    WIN.blit(SEPARATIST_SPACESHIP, (separatist.x, separatist.y))

    #BULLETS
    for bullet in separatist.magazine:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in jedi.magazine:
        pygame.draw.rect(WIN, BLUE, bullet)

    for bullet in venator.magazine:
        pygame.draw.rect(WIN, BLUE, bullet)

    for bullet in droidcruiser.magazine:
        pygame.draw.rect(WIN, RED, bullet)

    if MAP == 0:
        WIN.blit(ASTEROID, (asteroid.x,asteroid.y))
    elif MAP == 1:
        WIN.blit(VENATOR_SPACESHIP, (venator.x,venator.y))
    elif MAP == 2:
        WIN.blit(DROIDCRUISER_SPACESHIP, (droidcruiser.x,droidcruiser.y))
    elif MAP == 3:
        WIN.blit(VENATOR_SPACESHIP, (venator.x,venator.y))
        WIN.blit(DROIDCRUISER_SPACESHIP, (droidcruiser.x,droidcruiser.y))

    #BOOM ANIMATIONS
    for boom in booms:
        if boom.ON_OFF == "ON":
            if cas2%8 == 0:
                boom.number += 1
            if boom.number == 6:
                boom.ON_OFF = "OFF"
                booms.remove(boom)
            boom.update()
            WIN.blit(boom.boom, (boom.x,boom.y))

    pygame.display.update()
#CRATE HANDELING
def crate_spawn(jedi,separatist,cas,crate):
    if cas%60 == 0: #každou sekundu
        #print(cas/60)
        if cas/60 == 20: #kolik sekund
            cas = 0
            crate = pygame.Rect(random.randint(0,1250), random.randint(0,690), 30, 30)
            CRATE_POP_SOUND.play()
        if cas/60 == 15:
            jedi.reset()
            separatist.reset()
    return(cas,crate)
def crate_colliderects(jedi,separatist,crate):
    if crate.colliderect(jedi):
        bonus = random.randint(1,6)
        print(bonus)
        CRATE_PICKUP_SOUND.play()
        crate = crate = pygame.Rect(1500,1500,30,30)
        if bonus == 1:
            jedi.health += 3
        elif bonus == 2:
            jedi.vel = jedi.vel + 5
        elif bonus == 3:
            jedi.bullet_speed = 30
        elif bonus == 4:
            jedi.bullets = 30
        elif bonus == 5:
            jedi.bullet_size = 10
        elif bonus == 6:
            jedi.damage = 3
    elif crate.colliderect(separatist):
        bonus = random.randint(1,6)
        print(bonus)
        CRATE_PICKUP_SOUND.play()
        crate = pygame.Rect(1500,1500,30,30)
        if bonus == 1:
            separatist.health += 3
        elif bonus == 2:
            separatist.vel = separatist.vel * 2
        elif bonus == 3:
            separatist.bullet_speed = 30
        elif bonus == 4:
            separatist.bullets = 30
        elif bonus == 5:
            separatist.bullet_size = 10
        elif bonus == 6:
            separatist.damage = 3
    return(crate)
#MAIN CIRCLE
def main(jedi,separatist, MAP,flame1,flame2):
    
    #SHIPS
    jedi.chosen_ship()
    separatist.chosen_ship()
    
    venator = Cruiser(WIDTH/2 -125, 80, 170, 270)
    droidcruiser = Cruiser(WIDTH/2 -125, 500, 170, 270)

    cas = 0
    cas2 = 0
    crate = pygame.Rect(1500,1500,30,30)
    if MAP == 4:
        bonus = "ON"
        SPEED1 = jedi.vel
        BULLET_SPEED1 = jedi.bullet_speed
        BULLETS1 = jedi.bullets
        SPEED2 = separatist.vel
        BULLET_SPEED2 = separatist.bullet_speed
        BULLETS2 = separatist.bullets
    else:
        bonus = "OFF"

    booms = []

    clock = pygame.time.Clock()
    run = True
    while run:
        #QUIT
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            #GUN_FIRE_SPAWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(jedi.magazine) < jedi.bullets:
                    jedi.gun_fire_ship()
                if event.key == pygame.K_RCTRL and len(separatist.magazine) < separatist.bullets:
                    separatist.gun_fire_ship()
            if MAP == 1:
                venator.gun_fire_cruiser(jedi, separatist,2)
            elif MAP == 2:
                droidcruiser.gun_fire_cruiser(jedi, separatist,1)
            elif MAP == 3:
                venator.gun_fire_cruiser(jedi, separatist,2)
                droidcruiser.gun_fire_cruiser(jedi, separatist,1)
            #HIT
            if event.type == SEPARATIST_HIT:
                separatist.health -= jedi.damage
                BULLET_HIT_SOUND.play()

            if event.type == JEDI_HIT:
                jedi.health -= separatist.damage
                BULLET_HIT_SOUND.play()
    
            if event.type == ASTEROID_HIT:
                BULLET_HIT_SOUND.play()

        #WINNER
        winner_text = ""
        if separatist.health <= 0:
            winner_text = "Player 1 Wins!"
            separatist.health = 0

        if jedi.health <= 0:
            winner_text = "Player 2 Wins!"
            jedi.health = 0

        #CRATES
        if bonus == "ON":
            cas += 1
            cas,crate = crate_spawn(jedi,separatist,cas,crate)

        cas2 += 1
        #MOVEMENT AND POSITION
        jedi.move(1,MAP,flame1,flame2)
        separatist.move(2,MAP,flame1,flame2)
        #COLLIDERECTS
        bullet_colliderects(jedi,separatist,venator,droidcruiser,asteroid,MAP,booms)
        crate = crate_colliderects(jedi,separatist,crate)
        #VISUALIZACION
        draw_window(separatist, jedi,MAP,venator,droidcruiser,crate,flame1,flame2,cas2,booms)
        if winner_text == "Player 1 Wins!":
            BACKGROUND_SOUND.stop()
            #JEDI_WIN_SOUND.play()
            draw_winner(winner_text)
            break
        elif winner_text == "Player 2 Wins!":
            BACKGROUND_SOUND.stop()
            #SEPARATIST_WIN_SOUND.play()
            draw_winner(winner_text)
            break
    #SELFREPEATING
    do_it()

if __name__ == "__main__":
    do_it()