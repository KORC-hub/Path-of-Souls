import pygame as pg

height = 563 # alto
width = 1001 # ancho

white = (255, 255, 255)
black = (0, 0, 0)

pg.init()
screen = pg.display.set_mode((width,height))
pg.display.set_caption("Shooter")
clock = pg.time.Clock()

class Player(pg.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pg.image.load("C:/Lenguajes/Python/Pygame/Path of Souls/resources/graphics/Player/avatar_1.png").convert()
    self.image.set_colorkey(white)
    self.rect = self.image.get_rect()
    self.rect.centerx = width // 2
    self.rect.bottom = height // 2 
    self.speed = 3

  def update(self):
    self.speed_x = 0
    self.speed_y = 0
    keystate = pg.key.get_pressed()
    if keystate[pg.K_a]:
      self.speed_x -= self.speed
    if keystate[pg.K_d]:
      self.speed_x += self.speed
    self.rect.x += self.speed_x

    if keystate[pg.K_w]:
      self.speed_y -= self.speed
    if keystate[pg.K_s]:
      self.speed_y += self.speed
    self.rect.y += self.speed_y

    if self.rect.x > 928:
      self.rect.x = 928
    if self.rect.x < 0:
      self.rect.x = 0
    if self.rect.y > 480:
      self.rect.y = 480
    if self.rect.y < 0:
      self.rect.y = 0

  def shoot(self):
    bullet = Bullet(self.rect.centerx, self.rect.top)
    all_sprites.add(bullet)
    bullets.add(bullet)

class Bullet(pg.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    

all_sprites = pg.sprite.Group()

player = Player()
all_sprites.add(player)


# Game Loop
running = True
while running:
  # Keep loop running at the right speed
  clock.tick(60)
  # Process input (events)
  for event in pg.event.get():
    # check for closing window
    if event.type == pg.QUIT:
      running = False
    elif event.type == pg.MOUSEBUTTONUP:
        player.shoot() 
    
  pos = pg.mouse.get_pos()
  print(pos,"|",player.rect.x,player.rect.y)


  # Update
  all_sprites.update()

  #Draw / Render
  screen.fill(black)
  all_sprites.draw(screen)
  # *after* drawing everything, flip the display.
  pg.display.flip()

pg.quit()