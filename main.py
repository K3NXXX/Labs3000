import pygame as pg
import random
import time

max_x = 1920
max_y = 1080
center_x = 100
center_y = 100
snowflake_size = 200


class Snowflake: # опис сніжинки
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pg.image.load("snow.png")

    def screen_blit(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self): # по Y
        self.y += 10
        if self.y > max_y:
            self.y = 0 - snowflake_size
        if self.x > max_x:
            self.x = (0 - snowflake_size)
        if self.x < (0 - snowflake_size):
            self.x = max_x

        #-----------------------------------#
        # по X
        i = random.randint(4, 5)
        self.x += i
        if self.y > 200:
            i = random.randint(-10, -8)
            self.x += i
        if self.y > 600:
            i = random.randint(10, 13)
            self.x += i

snow = Snowflake(center_x,center_y)
pg.init()
background = (255, 255, 255)
screen = pg.display.set_mode((max_x, max_y), pg.FULLSCREEN)

clock = pg.time.Clock()

#-------------------------------------------------------------------------------------------------------#

run = True
while run:
    screen.fill(background)
    snow.screen_blit()
    snow.move()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False

    time.sleep(0.010)
    clock.tick(60)
    pg.display.flip()



