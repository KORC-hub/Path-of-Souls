import pygame as pg
import random as r
import constants as c
from data import player 

class medal_obj():
 def __init__(self, loc):
  self.loc = loc

 def render(self, screen, x):
  screen.blit(c.medals[x],self.loc)

  # the medal hitbox is created
 def get_rect(self):
  return pg.Rect(self.loc[0], self.loc[1], 50, 52)

  # the rect of each object is compared to verify the collision
 def collision_test(self,rect):
  medal_rect = self.get_rect()
  return medal_rect.colliderect(rect)


class enemy(pg.sprite.Sprite):
 def __init__(self):
  super().__init__()
  self.image = c.obstaculo[1]
  self.rect = self.image.get_rect()
  self.rect.x = r.randrange(200,700)
  self.rect.y = r.randrange(50,450)
  self.velocidad_x = r.randrange(-15,-5)
  self.velocidad_y = r.randrange(-15,-5)

 def update(self,screen,rect):
  self.rect.x += self.velocidad_x 
  self.rect.y += self.velocidad_y

  if self.rect.left < 110:
    self.velocidad_x += 5
  if self.rect.right > 900:
    self.velocidad_x -= 5
  if self.rect.bottom > 500:
    self.velocidad_y -= 5
  if self.rect.top < 50:
    self.velocidad_y += 5

  screen.blit(c.obstaculo[1],(self.rect.x,self.rect.y))

  if self.rect.colliderect(rect):
    c.state_life -= 1
    c.state_personaje = 1 
    self.velocidad_x = r.randrange(-15,-5)
    self.velocidad_y = r.randrange(-15,-5)


sprites = pg.sprite.Group()

for x in range(5):
  enemy_object = enemy()
  sprites.add(enemy_object)

# print and if the straight lines of the medal match and the player adds one to the status of the medal
def medallas(screen,player):
  c.medal_objects[c.state_medal].render(screen,c.state)
  if c.medal_objects[c.state_medal].collision_test(player):
   c.state_medal += 1





