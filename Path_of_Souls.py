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
player = player.jugador()

pg.mixer.music.load(v.music_1)
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.03)

def reiniciar():
  bf.reiniciar_life()
  bm.reiniciar_medal()
  e.reiniciar_enemy()
  v.x = 0
  v.state = 0
  v.score = 0
  v.Velocidad_enemigo = 0
  v.state_medal = 0
  v.medal_counter = -1
  v.daño = False
  v.medal_on = True
  v.state_life = 4
  v.pause = False
  v.end_game = False
  v.game_over = False
  v.menu = True

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

    screen.blit(v.background_menu,v.position_base)
    mx,my = pg.mouse.get_pos()

    if v.button_menu_play.collidepoint((mx,my)):
     if v.click:
      v.seleccion_opcion.play()
      screen.blit(v.play_on, v.button_menu_play)
      screen.blit(v.art_off, v.button_menu_art)
      pg.display.update()
      pg.time.wait(50)
      v.menu = False
      v.play = True
    elif v.button_menu_art.collidepoint((mx,my)):
     if v.click:
      v.seleccion_opcion.play()
      screen.blit(v.art_on, v.button_menu_art)
      screen.blit(v.play_off, v.button_menu_play)
      pg.display.update()
      pg.time.wait(50)
      v.menu = False
      v.art = True

    screen.blit(v.play_off, v.button_menu_play)
    screen.blit(v.art_off, v.button_menu_art)

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
      v.end_game = True
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
        e.enemy.update(screen, player.rect)

      player.handle_event(event)
      screen.blit(player.image,player.rect)

      screen.blit(v.barra, v.position_barra)
      score_text  = v.fuente.render(str(v.score), False, v.white_green)

      if v.score == 0:
        screen.blit(score_text, ((v.position_score[0] + 30),v.position_score[1]))
      else:
        screen.blit(score_text, v.position_score)

      if v.state_life <= 0:
        v.play = False
        v.game_over = True
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
          if event.key == pg.K_ESCAPE:
            v.play = False
            v.pause = True

    pg.display.flip()

 while v.pause:

    screen.blit(v.state_image_room[v.state], v.position_base)
    screen.blit(v.background_pause, v.position_base)
    mx,my = pg.mouse.get_pos()

    if v.button_pause_play.collidepoint((mx,my)):
     if v.click:
      v.seleccion_opcion.play()
      screen.blit(v.play_on, v.button_pause_play)
      screen.blit(v.exit_off, v.button_pause_exit)
      pg.display.update()
      pg.time.wait(50)
      v.pause = False
      v.play = True
    elif v.button_pause_exit.collidepoint((mx,my)):
     if v.click:
      v.seleccion_opcion.play()
      screen.blit(v.exit_on, v.button_pause_exit)
      screen.blit(v.play_off, v.button_pause_play)
      pg.display.update()
      pg.time.wait(50)
      reiniciar()

    screen.blit(v.play_off, v.button_pause_play)
    screen.blit(v.exit_off, v.button_pause_exit)

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
          v.click = True
      elif event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
          v.click = False
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
          v.click = False
          v.pause = False
          v.play = True

    pg.display.flip()
     

 while v.art:

    mx,my = pg.mouse.get_pos()
    screen.blit(v.background_menu, v.position_base)
    screen.blit(v.background_art, v.position_base_art)

    if v.button_x.collidepoint((mx,my)):
     if v.click:
      v.seleccion_opcion.play()
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


 while v.game_over:

    screen.blit(v.background_game_over, v.position_base)
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_ESCAPE: 
        reiniciar()

    pg.display.flip()

 while v.end_game:

    screen.blit(v.background_end_game, v.position_base)
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_ESCAPE:
        reiniciar()

    pg.display.flip()


