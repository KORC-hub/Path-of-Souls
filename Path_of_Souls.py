import pygame as pg
import sys, random
from data import variables as v
from data import player 
from data import medal as m
from data import enemy as e
from data import bar_medal as bm
from data import bar_life as bf

# python Path_of_Souls.py
#C:\Lenguajes\Python\Pygame\Path of Souls

# main conditions for the execution of the window
pg.init() 
#pg.mixer.init()
screen = pg.display.set_mode((v.width,v.height))
pg.display.set_caption(v.name)
clock = pg.time.Clock()
player = player.jugador(v.position_personaje)

# adding the creation of each medal in a list
for i in range(4):
  v.medal_objects.append(m.medal_obj(v.medals[i],(random.randint(200,600),random.randint(50,400))))
  v.medal_objects.append(0)

for i in range(4):
  v.bar_medal_objects.append(bm.bar_medal_obj(v.bar_medal[i],(v.position_bar_medal[i],v.position_bar_medal[4])))
  v.bar_medal_objects.append(0)

for i in range(4):
  v.bar_life_objects.append(bf.bar_life_obj(v.life[0],(v.position_vida[i],v.position_vida[4])))

# Game Loop
while v.running:

 while v.menu:

    clock.tick(v.fps)

    screen.blit(v.background,v.position_base)
    mx,my = pg.mouse.get_pos()

    if v.button_1.collidepoint((mx,my)):
     if v.click:
      screen.blit(v.play_on, v.button_1)
      screen.blit(v.art_off, v.button_2)
      pg.display.update()
      pg.time.wait(50)
      v.menu = False
      v.play = True
    elif v.button_2.collidepoint((mx,my)):
     if v.click:
      screen.blit(v.art_on, v.button_2)
      screen.blit(v.play_off, v.button_1)
      pg.display.update()
      pg.time.wait(50)
      v.menu = False
      v.art = True

    screen.blit(v.play_off, v.button_1)
    screen.blit(v.art_off, v.button_2)

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
          v.click = True
      if event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
          v.click = False
     
    pg.display.flip()
   
 while v.play:
 
    clock.tick(v.fps)

    if v.state == 10:
      v.play = False
      v.end = True
    elif v.state % 2 != 0:
      v.play = False
      v.kinematics = True
    else:
      if v.x == 0:
        v.x += 1
        v.play = False
        v.introduction = True 

      screen.blit(v.state_image_room[v.state], v.position_base)

      if v.state == 0:
        pass
      else:
        if v.medal_on:
          m.medallas(screen,((player.rect.x+10),(player.rect.y+20),30,65))

      if v.state == 0:
        pass
      else:
        e.sprites.update(screen,((player.rect.x+10),(player.rect.y+20),30,65))

      player.handle_event(event)
      screen.blit(player.image,player.rect)

      if v.state_life <= 0:
        v.play = False
        v.end = True
      else:
        bf.render_bar_life(screen)

      bm.render_bar_medal(screen)

      for event in pg.event.get():
        if event.type == pg.QUIT:
          pg.quit()
          sys.exit()
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_a: 
            v.state_life -= 1

    pg.display.flip()

 while v.art:

    mx,my = pg.mouse.get_pos()
    screen.blit(v.background, v.position_base)
    screen.blit(v.background_art, v.position_base_art)

    if v.button_x.collidepoint((mx,my)):
     if v.click:
      screen.blit(v.x_on, v.button_x)
      pg.display.update()
      pg.time.wait(50)
      v.art = False
      v.menu = True

    screen.blit(v.x_off, v.button_x)

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      if event.type == pg.MOUSEBUTTONDOWN:
        if event.dict['button'] == 4:
          if v.position_base_art[1] < v.position_base_art[0]:
            v.position_base_art[1] += 40
        elif event.dict['button'] == 5:
          if v.position_base_art[1] > v.limits_art:
            v.position_base_art[1] -= 40
        elif event.button == 1:
          v.click = True
      elif event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
          v.click = False
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
          v.click = False
          v.art = False
          v.menu = True


    pg.display.flip()

 while v.introduction:

    screen.blit(v.Guide, v.position_texto)
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
          v.introduction = False
          v.play = True

    pg.display.flip()

 while v.kinematics:

    print(v.state,v.state_life,v.kinematics_counter, v.state_medal, v.medal_counter)

    if v.state == 1 or v.state == 9:
      screen.blit(v.kinematics_image[v.state], v.position_base)
    else:
      screen.blit(v.kinematics_image[v.state][v.kinematics_counter], v.position_base)

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_a:
          v.kinematics_counter = 1
        elif event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN: 
          v.state += 1 
          v.kinematics_counter = 0
          v.kinematics = False
          v.play = True

    pg.display.flip()

 while v.end:

    screen.blit(v.background_end, v.position_base)
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_ESCAPE: 
        v.x = 0
        v.state = 0
        v.state_medal = 0
        v.state_life = 3
        v.end = False
        v.menu = True

    pg.display.flip()