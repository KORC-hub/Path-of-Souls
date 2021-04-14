import pygame as pg
import random as r
import constants as c

class boss(pg.sprite.Sprite):
 def __init__(self):
  self.image = pg.Surface(c.obstaculo).convert()
  self.rect = self.image.get_rect()
  self.rect.x = r.randrange(c.width - self.rect.width) 
  self.rect.y = r.randrange(-100, -40)
  self.speedy = r.randrange(1,10)



 def update(self):
  self.rect.y -= self.speedy




