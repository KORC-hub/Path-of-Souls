import pygame as pg
from os import system
import sys, random
from data import player
import constants as c

pg.init() 
pg.mixer.init()
screen = pg.display.set_mode((c.width,c.height))
pg.display.set_caption(c.name)
clock = pg.time.Clock()
player = player.jugador(c.pisicion_personaje)

class medal_obj():
 def __init__(self, loc):
  self.loc = loc

 def render(self, screen, x):
  screen.blit(c.medallas[x],self.loc)

 def get_rect(self):
  return pg.Rect(self.loc[0], self.loc[1], 8, 9)

 def collision_test(self,rect):
  medal_rect = self.get_rect()
  return medal_rect.colliderect(rect)

class enemy_obj():
 def __init__(self, loc):
  self.loc = loc

 def render(self, screen, x):
  screen.blit(c.medallas[x],self.loc)

 def collision_test(self, rect):
  medal_rect = pg.Rect(self.loc[0], self.loc[1], 50, 52)
  return medal_rect.colliderect(rect)

# Game Loop
while c.running:

 while c.menu:

  clock.tick(c.fps)

  screen.blit(c.background,c.posicion_base)
  mx,my = pg.mouse.get_pos()

  if c.button_1.collidepoint((mx,my)):
   if c.click:
    screen.blit(c.play_on, c.button_1)
    screen.blit(c.art_off, c.button_2)
    pg.display.update()
    pg.time.wait(50)
    c.menu = False
    c.play = True
  elif c.button_2.collidepoint((mx,my)):
   if c.click:
    screen.blit(c.art_on, c.button_2)
    screen.blit(c.play_off, c.button_1)
    pg.display.update()
    pg.time.wait(50)
    c.menu = False
    c.art = True

  screen.blit(c.play_off, c.button_1)
  screen.blit(c.art_off, c.button_2)

  for event in pg.event.get():
   if event.type == pg.QUIT:
    pg.quit()
    sys.exit()
   if event.type == pg.MOUSEBUTTONDOWN:
    if event.button == 1:
     c.click = True

  pg.display.flip()
   
 while c.play:

  clock.tick(c.fps)

  if c.state == 0:# --------------------------------------------------------------------------| sala introduccion   
   screen.blit(c.state_salas[c.state], c.posicion_base)
   mx,my = pg.mouse.get_pos()
   print(mx,my)
   if c.x == 0:                                                                 
    c.play = False
    c.state_introduccion = True                                                 
  elif c.state == 1:# ------------------------------------------------------------------------| sala 1
   if c.x == 1:
    c.play = False
    c.state_sala1 = True

   screen.blit(c.state_salas[c.state], c.posicion_base)
   medal_1 = medal_obj(c.posiciones_medallas[c.state])
   if c.state_medalla == 0:
    medal_1.render(screen,c.state)
    if medal_1.collision_test(player.rect):
     c.state_medalla = 1

  elif c.state == 2:# ------------------------------------------------------------------------| sala 2
   if c.x == 2:
    c.play = False
    c.state_sala2 = True

   screen.blit(c.state_salas[c.state], c.posicion_base)
   medal_2 = medal_obj(c.posiciones_medallas[c.state])

   if c.state_medalla == 1:
    medal_2.render(screen,c.state)
    if medal_2.collision_test(player.rect):
     c.state_medalla = 1
   
  elif c.state == 3:# ------------------------------------------------------------------------| sala 3
   if c.x == 3:
    c.play = False
    c.state_sala3 = True

   screen.blit(c.state_salas[c.state], c.posicion_base)
   medal_3 = medal_obj(c.posiciones_medallas[c.state])

   if c.state_medalla == 2:
    medal_3.render(screen,c.state)
    if medal_3.collision_test(player.rect):
     c.state_medalla = 1

  elif c.state == 4:# ------------------------------------------------------------------------| sala 4
   if c.x == 4:
    c.play = False
    c.state_sala4 = True

   screen.blit(c.state_salas[c.state], c.posicion_base)
   medal_4 = medal_obj(c.posiciones_medallas[c.state])

   if c.state_medalla == 3:
    medal_4.render(screen,c.state)
    if medal_4.collision_test(player.rect):
     c.state_medalla = 1

  player.handle_event(event)
  screen.blit(player.image, player.rect)

  if c.state_vida == 0 or 1 or 2 or 3:# ------------------------------------------------------| vida
   screen.blit(c.barra_vida[c.state_vida],c.posicion_vida)

  if c.state_medalla == 0 or 1 or 2 or 3 or 4:# ----------------------------------------------| medalla
   screen.blit(c.barra_madallas[c.state_medalla],c.posicion_barra_medalla)

  for event in pg.event.get():
   if event.type == pg.QUIT:
    pg.quit()
    sys.exit()
   elif event.type == pg.KEYDOWN:
    if event.key == pg.K_a:
     c.state_vida -= 1
    elif event.key == pg.K_s:
     c.state_medalla += 1

  pg.display.flip()

 while c.art:

  screen.blit(c.background, c.posicion_base)
  screen.blit(c.fondo_art, c.posicion_base_art)
  for event in pg.event.get():
   if event.type == pg.QUIT:
    pg.quit()
    sys.exit()
   if event.type == pg.MOUSEBUTTONDOWN:
    if event.dict['button'] == 4:
     if c.posicion_base_art[1] < c.posicion_base_art[0]:
      c.posicion_base_art[1] += 10
    elif event.dict['button'] == 5:
     if c.posicion_base_art[1] > c.limite_art:
      c.posicion_base_art[1] -= 10
   if event.type == pg.KEYDOWN:
    if event.key == pg.K_ESCAPE:
     c.click = False
     c.art = False
     c.menu = True

  pg.display.flip()

 while c.state_introduccion:

  if c.x == 0:
   pg.time.wait(500)
   c.x += 1

  screen.blit(c.Guide, c.posicion_texto)
  for event in pg.event.get():
   if event.type == pg.QUIT:
    pg.quit()
    sys.exit()
   if event.type == pg.KEYDOWN:
    if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
     c.state_introduccion = False
     c.play = True

  pg.display.flip()

 while c.state_sala1:
  if c.x == 1:
   c.x += 1

  for event in pg.event.get():
   if event.type == pg.QUIT:
    pg.quit()
    sys.exit()
   if event.type == pg.KEYDOWN:
    if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
     c.state_sala1 = False
     c.play = True

  pg.display.flip()

 while c.state_sala2:
  if c.x == 2:
   c.x += 1

  for event in pg.event.get():
   if event.type == pg.QUIT:
    pg.quit()
    sys.exit()
   if event.type == pg.KEYDOWN:
    if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
     c.state_sala2 = False
     c.play = True

  pg.display.flip()

 while c.state_sala3:
  if c.x == 3:
   c.x += 1

  for event in pg.event.get():
   if event.type == pg.QUIT:
    pg.quit()
    sys.exit()
   if event.type == pg.KEYDOWN:
    if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
     c.state_sala3 = False
     c.play = True

  pg.display.flip()

 while c.state_sala4:
  if c.x == 4:
   c.x += 1

  for event in pg.event.get():
   if event.type == pg.QUIT:
    pg.quit()
    sys.exit()
   if event.type == pg.KEYDOWN:
    if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
     c.state_sala4 = False
     c.play = True

  pg.display.flip()

