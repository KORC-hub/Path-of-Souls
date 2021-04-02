import pygame as pg
import sys
from data import player

height = 563 # alto
width = 1001 # ancho
white = (255, 255, 255) # color blanco
black = (0, 0, 0) # color negro

pg.init() 
screen = pg.display.set_mode((width,height))
pg.display.set_caption("Path of souls")
clock = pg.time.Clock()
player= player.personaje((width/2, height/2))
posicion_base = [0,0]
fps = 15

all_sprites = pg.sprite.Group()

class Bullet(pg.sprite.Sprite):
  def __init__(self, mx, my):
    super().__init__()
    self.image = pg.Surface((50,10))
    self.image.fill((255,0,0))

  def update(self):
    self.rect.y -= 5

background = pg.image.load("C:/Lenguajes/Python/Pygame/Path of Souls/resources/graphics/menu.png")
sala1 = pg.image.load("C:/Lenguajes/Python/Pygame/Path of Souls/resources/graphics/Sala_1.png")
  
# Game Loop
running = True
while running:

  menu = True
  play = False

  while menu:
    screen.blit(background,[0,0])
    for event in pg.event.get():
    # check for closing window
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_RETURN:
          menu = False
          play = True
    pg.display.flip()
    
  while play:

    clock.tick(fps)
    # Process input (events)
    for event in pg.event.get():
      # check for closing window
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      #elif event.type == pg.MOUSEBUTTONUP:
          #player.shoot() 
      
    pos = pg.mouse.get_pos()
    print(pos)

    player.handle_event(event)
    screen.blit(sala1, posicion_base)
    screen.blit(player.image, player.rect)

    # *after* drawing everything, flip the display.
    pg.display.flip()

      #while sala1:
      #while sala2:
      #while sala3:
      #while sala4:
      #while sala5:
      #while final:
      
