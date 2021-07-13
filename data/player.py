import pygame as pg
from data import variables as v

class jugador(pg.sprite.Sprite):
  def __init__(self):
    pg.sprite.Sprite.__init__(self)
    self.sheet = v.player
    self.sheet.set_clip(pg.Rect(0,0,60,100))
    self.image = self.sheet.subsurface(self.sheet.get_clip())
    self.rect = self.image.get_rect()
    self.rect.topleft = v.position_personaje
    self.frame = 0
    self.speed = 20
    self.left_states  = { 0: (0,100,60,100), 1: (60,100,60,100), 2: (120,100,60,100), 3: (180,100,60,100)}
    self.right_states = { 0: (0,200,60,100), 1: (60,200,60,100), 2: (120,200,60,100), 3: (180,200,60,100)}
    self.up_states    = { 0: (0,300,60,100), 1: (60,300,60,100), 2: (120,300,60,100), 3: (180,300,60,100)}
    self.down_states  = { 0: (0,0,60,100), 1: (60,0,60,100), 2: (120,0,60,100), 3: (180,0,60,100)}

  def get_frame(self, frame_set):
    self.frame += 1
    if self.frame > (len(frame_set) - 1):
      self.frame = 0
    return frame_set[self.frame]

  def clip(self, clipped_rect):
    if type(clipped_rect) is dict:
      self.sheet.set_clip(pg.Rect(self.get_frame(clipped_rect)))
    else:
      self.sheet.set_clip(pg.Rect(clipped_rect))
    return clipped_rect

  def update(self, direction):
    if direction == 'left':
      self.clip(self.left_states)
      self.rect.x -= self.speed
    if direction == 'right':
      self.clip(self.right_states)
      self.rect.x += self.speed
    if direction == 'up':
      self.clip(self.up_states)
      self.rect.y -= self.speed
    if direction == 'down':
      self.clip(self.down_states)
      self.rect.y += self.speed

    if direction == 'stand_left':
        self.clip(self.left_states[0])
    if direction == 'stand_right':
        self.clip(self.right_states[0])
    if direction == 'stand_up':
        self.clip(self.up_states[0])
    if direction == 'stand_down':
        self.clip(self.down_states[0])

    if v.state == 2:
      limit = v.limits_map_2
    else:
      limit = v.limits_map_1

    print("|",v.state,v.state_life,v.kinematics_counter,v.state_medal, v.medal_counter,v.state_life,v.daño,"|",self.rect.x, self.rect.y,"|")

    if self.rect.y >= v.limit[2] and self.rect.y <= v.limit[3] and (self.rect.x < limit[0] or self.rect.x > limit[1]):
      if self.rect.y < v.limit[2]:
        self.rect.y = v.limit[2]
      elif self.rect.y > v.limit[3]:
        self.rect.y = v.limit[3]
      elif self.rect.x > v.limit[1]:
        self.rect.x = v.limit[1]
      elif self.rect.x < v.limit[0]:
        v.medal_on = True 
        v.medal_counter +=1 
        v.state += 1 
        if v.Velocidad_enemigo < 3:
          v.Velocidad_enemigo += 2
        self.rect.x = v.position_Entrada[0]
        self.rect.y = v.position_Entrada[1]
    else:
      if self.rect.x < limit[0]:
        self.rect.x = limit[0]
      elif self.rect.x > limit[1]:
        self.rect.x = limit[1]
      elif self.rect.y < limit[2]:
        self.rect.y = limit[2]
      elif self.rect.y > limit[3]:
        self.rect.y = limit[3]

    if v.daño:
      self.rect.x = v.position_collision[0]
      self.rect.y = v.position_collision[1]
      v.state_life -= 1
      v.score -= 20

    self.image = self.sheet.subsurface(self.sheet.get_clip())

  def handle_event(self, event):
    if event.type == pg.QUIT:
      game_over = True

    if event.type == pg.KEYDOWN:
      if event.key == pg.K_LEFT:
        self.update('left')
      if event.key == pg.K_RIGHT:
        self.update('right')
      if event.key == pg.K_UP:
        self.update('up')
      if event.key == pg.K_DOWN:
        self.update('down')

    if event.type == pg.KEYUP:
      if event.key == pg.K_LEFT:
        self.update('stand_left')
      if event.key == pg.K_RIGHT:
        self.update('stand_right')
      if event.key == pg.K_UP:
        self.update('stand_up')
      if event.key == pg.K_DOWN:
        self.update('stand_down')