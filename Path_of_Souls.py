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
while running:

  menu = True
  sala1 = False

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

    pg.display.flip()

  #while introduccion:

  #while sala2:
  #while sala3:
  #while final: