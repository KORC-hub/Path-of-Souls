import pygame as pg
from os import system
import sys, random
from data import player 
from data import engine as e 
import constants as c

# main conditions for the execution of the window
pg.init() 
#pg.mixer.init()
screen = pg.display.set_mode((c.width,c.height))
pg.display.set_caption(c.name)
clock = pg.time.Clock()
player = player.jugador(c.position_personaje)

# adding the creation of each medal in a list
for i in range(4):
  c.medal_objects.append(e.medal_obj((random.randint(50,600),random.randint(50,400))))

for i in range(1):
  c.boss_objects.append(e.boss_obj(c.position_boss))

# Game Loop
while c.running:

 while c.menu:

    clock.tick(c.fps)

    screen.blit(c.background,c.position_base)
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
      if event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
          c.click = False
     
    pg.display.flip()
   
 while c.play:

    clock.tick(c.fps)

    if c.state == 0:
      screen.blit(c.state_image_room[c.state], c.position_base)
      mx,my = pg.mouse.get_pos()
      #print(mx,my)

      if c.x == 0:
        c.play = False
        c.state_introduction = True 

    elif c.state == 1:
      screen.blit(c.state_image_room[c.state], c.position_base)
      e.boss(screen,player.rect)

      if c.x == 1:
        c.play = False
        c.state_room1 = True
      elif c.state_medal == 0:
        e.medallas(screen,player.rect)

    elif c.state == 2:
      screen.blit(c.state_image_room[c.state], c.position_base)
      if c.x == 2:
        c.play = False
        c.state_room2 = True
      elif c.state_medal == 1:
        e.medallas(screen,player.rect)

    elif c.state == 3:
      screen.blit(c.state_image_room[c.state], c.position_base)
      if c.x == 3:
        c.play = False
        c.state_room3 = True
      if c.state_medal == 2:
        e.medallas(screen,player.rect)

    elif c.state == 4:
      screen.blit(c.state_image_room[c.state], c.position_base)
      if c.x == 4:
        c.play = False
        c.state_room4 = True
      if c.state_medal == 3:
        e.medallas(screen,player.rect)
        
    elif c.state == 5:
      c.play = False
      c.end = True 

    player.handle_event(event)
    screen.blit(player.image,player.rect)

    if c.state_life == 0 or 1 or 2 or 3:
      screen.blit(c.bar_life[c.state_life],c.position_vida)
    else:
      c.play = False
      c.end = True

    if c.state_medal == 0 or 1 or 2 or 3 or 4:
      screen.blit(c.bar_medal[c.state_medal],c.position_bar_medal)

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()

    pg.display.flip()

 while c.art:

    screen.blit(c.background, c.position_base)
    screen.blit(c.background_art, c.position_base_art)
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      if event.type == pg.MOUSEBUTTONDOWN:
        if event.dict['button'] == 4:
          if c.position_base_art[1] < c.position_base_art[0]:
            c.position_base_art[1] += 10
        elif event.dict['button'] == 5:
          if c.position_base_art[1] > c.limits_art:
            c.position_base_art[1] -= 10
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
          c.click = False
          c.art = False
          c.menu = True

    pg.display.flip()

 while c.state_introduction:

    if c.x == 0:
      pg.time.wait(500)
      c.x += 1

    screen.blit(c.Guide, c.position_texto)
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
          c.state_introduction = False
          c.play = True

    pg.display.flip()

 while c.state_room1:
    if c.x == 1:
      c.x += 1

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
          c.state_room1 = False
          c.play = True

    pg.display.flip()

 while c.state_room2:

    if c.x == 2:
      c.x += 1

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
          c.state_room2 = False
          c.play = True

    pg.display.flip()

 while c.state_room3:
    if c.x == 3:
      c.x += 1

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
          c.state_room3 = False
          c.play = True

    pg.display.flip()

 while c.state_room4:
    if c.x == 4:
      c.x += 1

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
        c.state_room4 = False
        c.play = True

    pg.display.flip()

 while c.end:

    screen.blit(c.background_end, c.position_base)
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_ESCAPE: 
        c.x = 0
        c.state = 0
        c.state_medal = 0
        c.state_life = 3
        c.end = False
        c.menu = True

    pg.display.flip()