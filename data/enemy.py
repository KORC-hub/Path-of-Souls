import pygame as pg
import random as r
from data import variables as v
from data import player 

class enemy(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = v.obstaculo_image[2]
		self.rect = self.image.get_rect()
		self.rect.x = r.randrange(200,700)
		self.rect.y = r.randrange(50,450)
		self.velocidad_x = r.randrange(-15,-5)
		self.velocidad_y = r.randrange(-15,-5)

	def update(self,screen,rect):
		self.rect.x += self.velocidad_x 
		self.rect.y += self.velocidad_y

		if self.rect.left < 110:
			self.velocidad_x += 10
		if self.rect.right > 900:
			self.velocidad_x -= 10
		if self.rect.bottom > 500:
			self.velocidad_y -= 10
		if self.rect.top < 50:
			self.velocidad_y += 5

		screen.blit(v.obstaculo_image[v.state],(self.rect.x,self.rect.y))

		if self.rect.colliderect(rect):
			v.state_personaje = 1 
			v.daño = True
			v.state_life -= 1
		else:
		 v.state_personaje = 0


sprites = pg.sprite.Group()

for x in range(5):
	enemy_object = enemy()
	sprites.add(enemy_object)