import pygame as pg
import sys
from data import player
import constants as c

pg.init() 
screen = pg.display.set_mode((c.width,c.height))
pg.display.set_caption(c.name)
clock = pg.time.Clock()
player= player.personaje((c.width/2, c.height/2))

# Game Loop
running = True
menu = True
sala1 = False
x = 0
while running:

  while menu:

    screen.blit(c.background,c.posicion_base)
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()

      if event.type == pg.KEYDOWN:
        if event.key == pg.K_RETURN:
          menu = False
          sala1 = True

    pg.display.flip()
    
  while sala1:

    clock.tick(c.fps)

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()

    pos = pg.mouse.get_pos()
    print(pos)

    player.handle_event(event)
    screen.blit(c.sala1, c.posicion_base)
    screen.blit(player.image, player.rect)

    if x == 0:
      sala1 = False
      introduccion = True

    pg.display.flip()

  while introduccion:
    pg.time.wait(500)
    screen.blit(c.Guide, c.posicion_texto)
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()

    if event.type == pg.KEYDOWN:
      if event.key == pg.K_RETURN:
        x += 1
        introduccion = False
        sala1 = True

    pg.display.flip()

  #while sala2:
  #while sala3:
  #while final: