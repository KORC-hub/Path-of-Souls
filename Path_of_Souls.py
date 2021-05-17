import pygame as pg
from os import system
import sys, random
from data import player 
from data import medal as m
from data import enemy as e
import constants as c

# python Path_of_Souls.py
#C:\Lenguajes\Python\Pygame\Path of Souls

# main conditions for the execution of the window
pg.init() 
#pg.mixer.init()
screen = pg.display.set_mode((c.width,c.height))
pg.display.set_caption(c.name)
clock = pg.time.Clock()
player = player.jugador(c.position_personaje)

# adding the creation of each medal in a list
for i in range(4):
  c.medal_objects.append(m.medal_obj((random.randint(200,600),random.randint(50,400))))

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
	
    if c.state == 10:
      c.play = False
      c.end = True
    elif c.state % 2 != 0:
      c.play = False
      c.kinematics = True
    else:
      if c.x == 0:
        c.x += 1
        c.play = False
        c.introduction = True 

      screen.blit(c.state_image_room[c.state], c.position_base)

      if c.state == 0:
        pass
      else:
        if c.state_medal == (c.state - 1):
          m.medallas(screen,((player.rect.x+10),(player.rect.y+20),30,65))
        
      if c.state == 0:
        pass
      else:
        e.sprites.update(screen,((player.rect.x+10),(player.rect.y+20),30,65))

      player.handle_event(event)
      screen.blit(player.image,player.rect)

      if c.state_life == 0:
        c.play = False
        c.end = True
      elif c.state_life == 1 or 2 or 3:
        screen.blit(c.bar_life[c.state_life],c.position_vida)

      if c.state_medal == 0 or 1 or 2 or 3 or 4:
        screen.blit(c.bar_medal[c.state_medal],c.position_bar_medal)

      for event in pg.event.get():
        if event.type == pg.QUIT:
          pg.quit()
          sys.exit()
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_a: 
            c.state_life -= 1

    pg.display.flip()

 while c.art:

    mx,my = pg.mouse.get_pos()
    screen.blit(c.background, c.position_base)
    screen.blit(c.background_art, c.position_base_art)

    if c.button_x.collidepoint((mx,my)):
     if c.click:
      screen.blit(c.x_on, c.button_x)
      pg.display.update()
      pg.time.wait(50)
      c.art = False
      c.menu = True

    screen.blit(c.x_off, c.button_x)

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      if event.type == pg.MOUSEBUTTONDOWN:
        if event.dict['button'] == 4:
          if c.position_base_art[1] < c.position_base_art[0]:
            c.position_base_art[1] += 40
        elif event.dict['button'] == 5:
          if c.position_base_art[1] > c.limits_art:
            c.position_base_art[1] -= 40
        elif event.button == 1:
          c.click = True
      elif event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
          c.click = False
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
          c.click = False
          c.art = False
          c.menu = True


    pg.display.flip()

 while c.introduction:

    screen.blit(c.Guide, c.position_texto)
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
          c.introduction = False
          c.play = True

    pg.display.flip()

 while c.kinematics:

    print(c.state,c.state_life,c.kinematics_counter)

    if c.state == 1 or c.state == 9:
      screen.blit(c.kinematics_image[c.state], c.position_base)
    else:
      screen.blit(c.kinematics_image[c.state][c.kinematics_counter], c.position_base)

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_a:
          c.kinematics_counter = 1
        elif event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
          c.state += 1 
          c.kinematics_counter = 0
          c.kinematics = False
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