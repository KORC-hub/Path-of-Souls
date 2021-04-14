import pygame as pg
from os import system
import sys, random
from data import player
#from data import engine as e
import constants as c

pg.init() 
screen = pg.display.set_mode((c.width,c.height))
pg.display.set_caption(c.name)
clock = pg.time.Clock()
player = player.jugador(c.pisicion_personaje)

enemies = []
"""
for i in range(5):
 enemies.append([0,e.entity(random.randint(0,600)-300,80,100,100,'enemy')])
"""
# Game Loop
while c.running:

 while c.menu:

  clock.tick(c.fps)

  screen.blit(c.background,c.posicion_base)

  mx, my = pg.mouse.get_pos()

  button_1 = pg.Rect(330, 450, 150, 50)
  button_2 = pg.Rect(560, 450, 150, 50)
  if button_1.collidepoint((mx, my)):
   if c.click:
    screen.blit(c.play_on, button_1)
    screen.blit(c.art_off, button_2)
    pg.display.update()
    pg.time.wait(50)
    c.menu = False
    c.play = True
  if button_2.collidepoint((mx, my)):
   if c.click:
    screen.blit(c.art_on, button_2)
    screen.blit(c.play_off, button_1)
    pg.display.update()
    pg.time.wait(50)
    c.menu = False
    c.art = True

  screen.blit(c.play_off, button_1)
  screen.blit(c.art_off, button_2)
 
  c.click = False

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

  for event in pg.event.get():
   if event.type == pg.QUIT:
    pg.quit()
    sys.exit()
   if event.type == pg.KEYDOWN:
    if event.key == pg.K_a:
     c.state_vida -= 1
    elif event.key == pg.K_s:
     c.state_medalla += 1


  if c.state == 1:
   screen.blit(c.sala1, c.posicion_base)
   if c.x == 0:
    c.play = False
    c.state_sala1 = True
  elif c.state == 2:
   if c.x == 1:
    c.play = False
    c.state_sala2 = True
   screen.blit(c.sala2, c.posicion_base)
   """
   for
   """
  elif c.state == 3:
   screen.blit(c.sala3, c.posicion_base)
  elif c.state == 4:
   screen.blit(c.sala4, c.posicion_base)
  elif c.state == 5:
   screen.blit(c.sala5, c.posicion_base)

  player.handle_event(event)
  screen.blit(player.image, player.rect)

  pos = pg.mouse.get_pos()
  print(pos, c.state)

  if c.state_vida == 3:
   screen.blit(c.vida_n3,(755, 20))
  elif c.state_vida == 2:
   screen.blit(c.vida_n2,(755, 20))
  elif c.state_vida == 1:
   screen.blit(c.vida_n1,(755, 20))
  elif c.state_vida == 0:
   screen.blit(c.vida_n0,(755, 20))

  if c.state_medalla == 0:
   screen.blit(c.medalla_n0,(60, 20))
  elif c.state_medalla == 1:
   screen.blit(c.medalla_n1,(60, 20))
  elif c.state_medalla == 2:
   screen.blit(c.medalla_n2,(60, 20))
  elif c.state_medalla == 3:
   screen.blit(c.medalla_n3,(60, 20))
  elif c.state_medalla == 4:
   screen.blit(c.medalla_n4,(60, 20))
  

  pg.display.flip()

 while c.state_sala1:

  if c.x == 0:
   pg.time.wait(500)
   c.x += 1

  screen.blit(c.Guide, c.posicion_texto)
  if event.type == pg.KEYDOWN:
   if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
    c.state_sala1 = False
    c.play = True
   

  for event in pg.event.get():
   if event.type == pg.QUIT:
    pg.quit()
    sys.exit()

  pg.display.flip()

 
 while c.state_sala2:

  if c.x == 1:
   c.x += 1

  if event.type == pg.KEYDOWN:
   if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
    c.state_sala2 = False
    c.play = True
   
  for event in pg.event.get():
   if event.type == pg.QUIT:
    pg.quit()
    sys.exit()

  pg.display.flip()
 #while sala3:
 #while final:

 #while c.art:
