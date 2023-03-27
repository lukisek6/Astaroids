#IMPORTS
import pygame
import os
import math
import random
pygame.font.init()
pygame.mixer.init()
pygame.init()
#GLOBAL VARIABLES AND INITS
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astaroids!")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 125, 255)
YELLOW =(255,255,0)
GREEN = (0,255,0)

BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/rocket.wav')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/blaster.wav')
BACKGROUND_SOUND = pygame.mixer.Sound('Assets/duel_of_the_fates.wav')
BACKGROUND_SOUND.set_volume(0.5)
JEDI_WIN_SOUND = pygame.mixer.Sound('Assets/force.wav')
SEPARATIST_WIN_SOUND = pygame.mixer.Sound('Assets/sidius.wav')
YELLOW_PICK_SOUND = pygame.mixer.Sound('Assets/r2d2.wav')
RED_PICK_SOUND = pygame.mixer.Sound('Assets/roger-roger.wav')
BLUE_PICK_SOUND = pygame.mixer.Sound('Assets/r3s6.wav')
MAP_PICK_SOUND = pygame.mixer.Sound('Assets/set-for-stun.wav')

GREEN_PICK_SOUND = pygame.mixer.Sound('Assets/fisto.wav')
CRUISER_PICK_SOUND = pygame.mixer.Sound('Assets/clone.wav')
JACHT_PICK_SOUND = pygame.mixer.Sound('Assets/jacht.wav')
MAUL_PICK_SOUND = pygame.mixer.Sound('Assets/maul.wav')
NABOO_PICK_SOUND = pygame.mixer.Sound('Assets/naboo.wav')
SMUGGLER_PICK_SOUND = pygame.mixer.Sound('Assets/luke.wav')
XWING_PICK_SOUND = pygame.mixer.Sound('Assets/xwing.wav')
YWING_PICK_SOUND = pygame.mixer.Sound('Assets/ywing.wav')

HEALTH_FONT = pygame.font.SysFont('candara', 40)
WINNER_FONT = pygame.font.SysFont('candara', 100)

FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 40,55

JEDI_HIT = pygame.USEREVENT + 1
SEPARATIST_HIT = pygame.USEREVENT + 2
ASTEROID_HIT = pygame.USEREVENT + 3

#SHIPS IMAGES
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'jedi_ship.png'))

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'separatist_ship.png'))

BLUE_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'blue_ship.png'))

GREEN_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'green_ship.png'))

CRUISER_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'cruiser_ship.png'))

JACHT_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'jacht_ship.png'))

MAUL_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'maul_ship.png'))

NABOO_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'naboo_ship.png'))

SMUGGLER_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'smugler_ship.png'))

XWING_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'xwing_ship.png'))

YWING_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'ywing_ship.png'))

DROIDCRUISER_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'droidcruiser_ship.png'))

DROIDCRUISER_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    DROIDCRUISER_SPACESHIP_IMAGE, (120,500)), 90)

droidcruiser = pygame.Rect(WIDTH/2 -250, 500, 120, 500)

VENATOR_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'venator_ship.png'))

VENATOR_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    VENATOR_SPACESHIP_IMAGE, (170,270)), 270)

venator = pygame.Rect(WIDTH/2 -125, 80, 170, 270)

ASTEROID_IMAGE = pygame.image.load(
    os.path.join('Assets', 'asteroid.png'))

ASTEROID = pygame.transform.rotate(pygame.transform.scale(
    ASTEROID_IMAGE, (240,240)), 0)

asteroid = pygame.Rect(WIDTH/2 -120, HEIGHT/2-120, 240, 240)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.jpg')), (WIDTH, HEIGHT))

class Player():
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

    def move(self,token,MAP):
        keys_pressed = pygame.key.get_pressed()

        if MAP !=0:
            #JEDI----PLAYER1
            if token == 1:
                if keys_pressed[pygame.K_a] and keys_pressed[pygame.K_w] and self.x - self.vel > 0 and self.y - self.vel > 0:
                    self.x -= self.vel
                    self.y -= self.vel
                    self.rotation = 45
                elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_w] and self.x + self.vel + self.width < WIDTH and self.y - self.vel > 0:
                    self.x += self.vel
                    self.y -= self.vel
                    self.rotation = 315
                elif keys_pressed[pygame.K_a] and keys_pressed[pygame.K_s] and self.x - self.vel > 0 and self.y + self.vel + self.height < HEIGHT - 15:
                    self.x -= self.vel
                    self.y += self.vel
                    self.rotation = 135
                elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_s] and self.x + self.vel + self.width < WIDTH and self.y + self.vel + self.height < HEIGHT - 15:
                    self.x += self.vel
                    self.y += self.vel
                    self.rotation = 225
                elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_a]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_w] and keys_pressed[pygame.K_s]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_a] and self.x - self.vel > 0:  # LEFT
                    self.x -= self.vel
                    self.rotation = 90
                elif keys_pressed[pygame.K_d] and self.x + self.vel + self.width < WIDTH:  # RIGHT
                    self.x += self.vel
                    self.rotation = 270
                elif keys_pressed[pygame.K_w] and self.y - self.vel > 0:  # UP
                    self.y -= self.vel
                    self.rotation = 0
                elif keys_pressed[pygame.K_s] and self.y + self.vel + self.height < HEIGHT - 15:  # DOWN
                    self.y += self.vel
                    self.rotation = 180
            #SEPARATIST----PLAYER2
            elif token == 2:
                if keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_UP] and self.x - self.vel > 0 and self.y - self.vel > 0:
                    self.x -= self.vel
                    self.y -= self.vel
                    self.rotation = 45
                elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_UP] and self.x + self.vel + self.width < WIDTH and self.y - self.vel > 0:
                    self.x += self.vel
                    self.y -= self.vel
                    self.rotation = 315
                elif keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_DOWN] and self.x - self.vel > 0 and self.y + self.vel + self.height < HEIGHT:
                    self.x -= self.vel
                    self.y += self.vel
                    self.rotation = 135
                elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_DOWN] and self.x + self.vel + self.width < WIDTH and self.y + self.vel + self.height < HEIGHT:
                    self.x += self.vel
                    self.y += self.vel
                    self.rotation = 225
                elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_LEFT]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_DOWN]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_LEFT] and self.x - self.vel > 0:  # LEFT
                    self.x -= self.vel
                    self.rotation = 90
                elif keys_pressed[pygame.K_RIGHT] and self.x + self.vel + self.width < WIDTH:  # RIGHT
                    self.x += self.vel
                    self.rotation = 270
                elif keys_pressed[pygame.K_UP] and self.y - self.vel > 0:  # UP
                    self.y -= self.vel
                    self.rotation = 0
                elif keys_pressed[pygame.K_DOWN] and self.y + self.vel + self.height < HEIGHT:  # DOWN
                    self.y += self.vel
                    self.rotation = 180
        elif MAP == 0:#pygame.Rect(WIDTH/2 -120, HEIGHT/2-120, 240, 240)
            #JEDI
            if token == 1:
                if keys_pressed[pygame.K_a] and keys_pressed[pygame.K_w] and self.x - self.vel > 0 and self.y - self.vel > 0 and ( ( (self.x - self.vel > 760) or (self.x < 520) )or( (self.y<240) or (self.y - self.vel > 480) ) ):
                    self.x -= self.vel
                    self.y -= self.vel
                    self.rotation = 45
                elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_w] and self.x + self.vel + self.width < WIDTH and self.y - self.vel > 0 and ( ( (self.x > 760) or (self.x + self.vel + self.width < 520) )or( (self.y<240) or (self.y - self.vel > 480) ) ):
                    self.x += self.vel
                    self.y -= self.vel
                    self.rotation = 315
                elif keys_pressed[pygame.K_a] and keys_pressed[pygame.K_s] and self.x - self.vel > 0 and self.y + self.vel + self.height < HEIGHT - 15 and ( ( (self.x - self.vel > 760) or (self.x < 520) )or( (self.y + self.vel + self.height<240) or (self.y > 480) ) ):
                    self.x -= self.vel
                    self.y += self.vel
                    self.rotation = 135
                elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_s] and self.x + self.vel + self.width < WIDTH and self.y + self.vel + self.height < HEIGHT - 15 and ( ( (self.x > 760) or (self.x + self.vel + self.width < 520) )or( (self.y + self.vel + self.height<240) or (self.y > 480) ) ):
                    self.x += self.vel
                    self.y += self.vel
                    self.rotation = 225
                elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_a]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_w] and keys_pressed[pygame.K_s]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_a] and self.x - self.vel > 0 and ( ( (self.x - self.vel > 760) or (self.x < 520) )or( (self.y<240) or (self.y > 480) ) ):  # LEFT
                    self.x -= self.vel
                    self.rotation = 90
                elif keys_pressed[pygame.K_d] and self.x + self.vel + self.width < WIDTH and ( ( (self.x > 760) or (self.x + self.vel + self.width < 520) )or( (self.y<240) or (self.y > 480) ) ):  # RIGHT
                    self.x += self.vel
                    self.rotation = 270
                elif keys_pressed[pygame.K_w] and self.y - self.vel > 0 and ( ( (self.x > 760) or (self.x < 520) )or( (self.y<240) or (self.y - self.vel > 480) ) ):  # UP
                    self.y -= self.vel
                    self.rotation = 0
                elif keys_pressed[pygame.K_s] and self.y + self.vel + self.height < HEIGHT - 15 and ( ( (self.x > 760) or (self.x < 520) )or( (self.y + self.vel + self.height<240) or (self.y > 480) ) ):  # DOWN
                    self.y += self.vel
                    self.rotation = 180
            #SEPARATIST
            elif token == 2:
                if keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_UP] and self.x - self.vel > 0 and self.y - self.vel > 0 and ( ( (self.x - self.vel > 760) or (self.x < 520) )or( (self.y<240) or (self.y - self.vel > 480) ) ):
                    self.x -= self.vel
                    self.y -= self.vel
                    self.rotation = 45
                elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_UP] and self.x + self.vel + self.width < WIDTH and self.y - self.vel > 0 and ( ( (self.x > 760) or (self.x + self.vel + self.width < 520) )or( (self.y<240) or (self.y - self.vel > 480) ) ):
                    self.x += self.vel
                    self.y -= self.vel
                    self.rotation = 315
                elif keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_DOWN] and self.x - self.vel > 0 and self.y + self.vel + self.height < HEIGHT and ( ( (self.x - self.vel > 760) or (self.x < 520) )or( (self.y + self.vel + self.height<240) or (self.y > 480) ) ):
                    self.x -= self.vel
                    self.y += self.vel
                    self.rotation = 135
                elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_DOWN] and self.x + self.vel + self.width < WIDTH and self.y + self.vel + self.height < HEIGHT and ( ( (self.x > 760) or (self.x + self.vel + self.width < 520) )or( (self.y + self.vel + self.height<240) or (self.y > 480) ) ):
                    self.x += self.vel
                    self.y += self.vel
                    self.rotation = 225
                elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_LEFT]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_DOWN]:
                    self.x += 0
                    self.y += 0
                elif keys_pressed[pygame.K_LEFT] and self.x - self.vel > 0 and ( ( (self.x - self.vel > 760) or (self.x < 520) )or( (self.y<240) or (self.y > 480) ) ):  # LEFT
                    self.x -= self.vel
                    self.rotation = 90
                elif keys_pressed[pygame.K_RIGHT] and self.x + self.vel + self.width < WIDTH and ( ( (self.x > 760) or (self.x + self.vel + self.width < 520) )or( (self.y<240) or (self.y > 480) ) ):  # RIGHT
                    self.x += self.vel
                    self.rotation = 270
                elif keys_pressed[pygame.K_UP] and self.y - self.vel > 0 and ( ( (self.x > 760) or (self.x < 520) )or( (self.y<240) or (self.y - self.vel > 480) ) ):  # UP
                    self.y -= self.vel
                    self.rotation = 0
                elif keys_pressed[pygame.K_DOWN] and self.y + self.vel + self.height < HEIGHT and ( ( (self.x > 760) or (self.x < 520) )or( (self.y + self.vel + self.height<240) or (self.y > 480) ) ):  # DOWN
                    self.y += self.vel
                    self.rotation = 180

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

    def gun_fire_ship(self,token,event):
        if event.type == pygame.KEYDOWN:
            if token == 1:
                if event.key == pygame.K_LCTRL and len(self.magazine) < self.bullets:
                       o,p = self.get_xy_ship()
                       bullet = Bullet(BLUE, self.x + SPACESHIP_WIDTH/2, self.y + SPACESHIP_HEIGHT/2 - 10, 7,7, self.bullet_speed, o,p)
                       self.magazine.append(bullet)
                       BULLET_FIRE_SOUND.play()
            elif token == 2:
                if event.key == pygame.K_RCTRL and len(self.magazine) < self.bullets:
                       o,p = self.get_xy_ship()
                       bullet = Bullet(RED, self.x + SPACESHIP_WIDTH/2, self.y + SPACESHIP_HEIGHT/2 - 10, 7,7, self.bullet_speed, o,p)
                       self.magazine.append(bullet)
                       BULLET_FIRE_SOUND.play()
#DO IT
def do_it():
    BACKGROUND_SOUND.play()
    First_SHIP, HEALTH, SPEED, BULLET_SPEED, BULLETS = menu1()
    jedi = Player(100,360,SPACESHIP_WIDTH, SPACESHIP_HEIGHT,First_SHIP, HEALTH, SPEED, BULLET_SPEED, BULLETS,270)
    Second_SHIP, HEALTH, SPEED, BULLET_SPEED, BULLETS = menu1()
    separatist = Player(1130, 360,SPACESHIP_WIDTH, SPACESHIP_HEIGHT,Second_SHIP, HEALTH, SPEED, BULLET_SPEED, BULLETS,90)
    MAP = menu2()
    BACKGROUND_SOUND.stop()
    BACKGROUND_SOUND.play()
    main(jedi,separatist, MAP)

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

#MENU VIsUALIZATION
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
        "JEDI SHIP: HEALTH 5, SPEED 5, BULLET SPEED 12, BULLETS 7", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==1:
        RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(RED_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))

        yellow_ship_text = HEALTH_FONT.render(
        "DROID SHIP: HEALTH 15, SPEED 3, BULLET SPEED 10, BULLETS 15", 1, RED)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==2:
        BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        BLUE_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(BLUE_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "JEDI MASTER SHIP: HEALTH 1, SPEED 10, BULLET SPEED 14, BULLETS 2", 1, BLUE)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))
    
    elif choice ==3:
        GREEN_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        GREEN_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(GREEN_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "MASTER FISTO SHIP: HEALTH 3, SPEED 6, BULLET SPEED 15, BULLETS 1", 1, GREEN)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==4:
        CRUISER_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        CRUISER_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(CRUISER_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "CRUISER SHIP: HEALTH 20, SPEED 2, BULLET SPEED 15, BULLETS 10", 1, BLUE)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))
    
    elif choice ==5:
        JACHT_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        JACHT_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(JACHT_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "JACHT SHIP: HEALTH 10, SPEED 4, BULLET SPEED 15, BULLETS 1", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==6:
        MAUL_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        MAUL_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(MAUL_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "DARTH MAUL SHIP: HEALTH 8, SPEED 5, BULLET SPEED 10, BULLETS 5", 1, RED)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==7:
        NABOO_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        NABOO_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(NABOO_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "NABOO SHIP: HEALTH 4, SPEED 7, BULLET SPEED 10, BULLETS 2", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==8:
        SMUGGLER_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        SMUGGLER_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(SMUGGLER_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "SMUGGLER SHIP: HEALTH 10, SPEED 4, BULLET SPEED 8, BULLETS 12", 1, RED)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==9:
        XWING_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        XWING_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(XWING_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "XWING SHIP: HEALTH 5, SPEED 8, BULLET SPEED 10, BULLETS 4", 1, BLUE)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    elif choice ==10:
        YWING_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        YWING_SPACESHIP_IMAGE, (SPACESHIP_WIDTH*5, SPACESHIP_HEIGHT*5)), 0)
        WIN.blit(YWING_SPACESHIP, (WIDTH/2-SPACESHIP_WIDTH*2.5, HEIGHT/2-SPACESHIP_HEIGHT*2.5))
        
        yellow_ship_text = HEALTH_FONT.render(
        "YWING SHIP: HEALTH 5, SPEED 6, BULLET SPEED 10, BULLETS 8", 1, YELLOW)
        WIN.blit(yellow_ship_text, (WIDTH/2-yellow_ship_text.get_width() / 2, HEIGHT-50))

    pygame.display.update()

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

def get_xy_droidcruiser(jedi):
    #droidcruiser bullets
    if jedi.rotation == 0:
        c,d = jedi.x+SPACESHIP_WIDTH/2,jedi.y
    elif jedi.rotation == 45:
        c,d = jedi.x,jedi.y
    elif jedi.rotation == 90:
        c,d = jedi.x,jedi.y+ SPACESHIP_HEIGHT/2 - 10
    elif jedi.rotation == 135:
        c,d = jedi.x + SPACESHIP_WIDTH/2,jedi.y+ SPACESHIP_HEIGHT/2 - 10 
    elif jedi.rotation == 180:
        c,d = jedi.x + SPACESHIP_WIDTH/2,jedi.y
    elif jedi.rotation == 225:
        c,d = jedi.x+ SPACESHIP_WIDTH/2,jedi.y + SPACESHIP_HEIGHT/2 - 10 
    elif jedi.rotation == 270:
        c,d = jedi.x,jedi.y + SPACESHIP_HEIGHT/2 - 10
    elif jedi.rotation == 315:
        c,d = jedi.x+ SPACESHIP_WIDTH/2,jedi.y + SPACESHIP_HEIGHT/2 - 10 
    return(c,d)
def get_xy_venator(separatist):
    #venator bullets
    if separatist.rotation == 0:
        a,b = separatist.x+SPACESHIP_WIDTH/2,separatist.y
    elif separatist.rotation == 45:
        a,b = separatist.x,separatist.y
    elif separatist.rotation == 90:
        a,b = separatist.x,separatist.y+ SPACESHIP_HEIGHT/2 - 10
    elif separatist.rotation == 135:
        a,b = separatist.x + SPACESHIP_WIDTH/2,separatist.y+ SPACESHIP_HEIGHT/2 - 10 
    elif separatist.rotation == 180:
        a,b = separatist.x + SPACESHIP_WIDTH/2,separatist.y
    elif separatist.rotation == 225:
        a,b = separatist.x+ SPACESHIP_WIDTH/2,separatist.y + SPACESHIP_HEIGHT/2 - 10 
    elif separatist.rotation == 270:
        a,b = separatist.x,separatist.y + SPACESHIP_HEIGHT/2 - 10
    elif separatist.rotation == 315:
        a,b = separatist.x+ SPACESHIP_WIDTH/2,separatist.y + SPACESHIP_HEIGHT/2 - 10 
    return(a,b)

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

def bullet_colliderects(jedi,separatist,venator_bullets,droidcruiser_bullets,asteroid,MAP):
    if MAP == 0:
        #JEDI BULLETS MOVEMENT
        for bullet in jedi.magazine:
            bullet.move()       
            #bullet_cleaning
            if separatist.rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(SEPARATIST_HIT))
                jedi.magazine.remove(bullet)
            elif asteroid.colliderect(bullet):
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
                pygame.event.post(pygame.event.Event(JEDI_HIT))
                separatist.magazine.remove(bullet)
            elif asteroid.colliderect(bullet):
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
    for bullet in venator_bullets:
        bullet.move()       
    #bullet_cleaning
        if separatist.rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SEPARATIST_HIT))
            venator_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            venator_bullets.remove(bullet)
        elif bullet.x < 0:
            venator_bullets.remove(bullet)
        elif bullet.y < 0:
            venator_bullets.remove(bullet)
        elif bullet.y > HEIGHT:
            venator_bullets.remove(bullet)

    #DROIDCRUISER BULLETS
    for bullet in droidcruiser_bullets:
        bullet.move()
    #bullet_cleaning
        if jedi.rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(JEDI_HIT))
            droidcruiser_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            droidcruiser_bullets.remove(bullet)
        elif bullet.x < 0:
            droidcruiser_bullets.remove(bullet)
        elif bullet.y < 0:
            droidcruiser_bullets.remove(bullet)
        elif bullet.y > HEIGHT:
            droidcruiser_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
#VISUALIZATION
def draw_window(separatist, jedi,MAP,venator_bullets,droidcruiser_bullets):
    #USED VARIABLES
    JEDI_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    jedi.image, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), jedi.rotation)
    
    SEPARATIST_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    separatist.image, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), separatist.rotation)

    #BACKGROUND
    WIN.blit(SPACE, (0, 0))
    
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

    for bullet in venator_bullets:
        pygame.draw.rect(WIN, BLUE, bullet)

    for bullet in droidcruiser_bullets:
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

    pygame.display.update()
#GUN FIRE SPAWN
def gun_fire_venator(jedi,separatist,venator_bullets):
    if len(venator_bullets) < 5 and len(venator_bullets) < (jedi.bullets+separatist.bullets):
        a,b = get_xy_venator(separatist)
        bullet = Bullet(BLUE, WIDTH/2, 80+170/2, 7,7, 5, a,b)
        venator_bullets.append(bullet)
        BULLET_FIRE_SOUND.play()
def gun_fire_droidcruiser(jedi,separatist,droidcruiser_bullets):
    if len(droidcruiser_bullets) < 5 and len(droidcruiser_bullets) < (jedi.bullets+separatist.bullets):
        c,d= get_xy_droidcruiser(jedi)
        bullet = Bullet(RED,WIDTH/2, 500+60, 7,7, 5, c,d)
        droidcruiser_bullets.append(bullet)
        BULLET_FIRE_SOUND.play()
#MAIN CIRCLE
def main(jedi,separatist, MAP):
    
    #SHIPS
    jedi.chosen_ship()
    separatist.chosen_ship()
    
    venator_bullets = []
    droidcruiser_bullets = []

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
            jedi.gun_fire_ship(1,event)
            separatist.gun_fire_ship(2,event)      
            if MAP == 1:
                gun_fire_venator(jedi, separatist, venator_bullets)
            elif MAP == 2:
                gun_fire_droidcruiser(jedi, separatist, droidcruiser_bullets)
            elif MAP == 3:
                gun_fire_venator(jedi, separatist, venator_bullets)
                gun_fire_droidcruiser(jedi, separatist, droidcruiser_bullets)
            #HIT
            if event.type == SEPARATIST_HIT:
                separatist.health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == JEDI_HIT:
                jedi.health -= 1
                BULLET_HIT_SOUND.play()
    
            if event.type == ASTEROID_HIT:
                BULLET_HIT_SOUND.play()

        #WINNER
        winner_text = ""
        if separatist.health <= 0:
            winner_text = "Jedi Wins!"

        if jedi.health <= 0:
            winner_text = "Separatists Wins!"

        #MOVEMENT AND POSITION
        jedi.move(1,MAP)
        separatist.move(2,MAP)
        #GUN FIRE MOVEMENT
        bullet_colliderects(jedi,separatist,venator_bullets,droidcruiser_bullets,asteroid,MAP)
        #VISUALIZACION
        draw_window(separatist, jedi,MAP,venator_bullets,droidcruiser_bullets)
        if winner_text == "Jedi Wins!":
            BACKGROUND_SOUND.stop()
            JEDI_WIN_SOUND.play()
            draw_winner(winner_text)
            break
        elif winner_text == "Separatists Wins!":
            BACKGROUND_SOUND.stop()
            SEPARATIST_WIN_SOUND.play()
            draw_winner(winner_text)
            break
    #SELFREPEATING
    do_it()

if __name__ == "__main__":
    do_it()