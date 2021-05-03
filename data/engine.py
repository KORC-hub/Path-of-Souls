import pygame as pg
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


class boss_obj():
 def __init__(self, loc):
  self.loc = loc
  self.seed = 40
 def render(self, screen):
  move = [self.loc[1] - self.seed, self.loc[1] + self.seed]
  if self.loc[1] < 36:
    c.move_boss = 1
  elif self.loc[1] > 445:
    c.move_boss = 0

  self.loc[1] = move[c.move_boss]
  screen.blit(c.obstaculo[c.move_boss],self.loc)

 def get_rect(self):
  return pg.Rect(self.loc[0], self.loc[1], 50, 52)

 def collision_test(self,rect):
  medal_rect = self.get_rect()
  return medal_rect.colliderect(rect)

# print and if the straight lines of the medal match and the player adds one to the status of the medal
def medallas(screen,player):
  c.medal_objects[c.state_medal].render(screen,c.state)
  if c.medal_objects[c.state_medal].collision_test(player):
   c.state_medal += 1

def boss(screen,player):
  c.boss_objects[0].render(screen)
  if c.boss_objects[0].collision_test(player):
    c.state_life = 2
   




