import pygame as pg
import random as r
from data import variables as v
from data import player 

pg.mixer.init()

class enemy_obj(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = v.obstaculo_image[2]
		self.rect = self.image.get_rect()
		self.rect.x = r.randrange(200,700)
		self.rect.y = r.randrange(50,450)
		self.velocidad_x = -10
		self.velocidad_y = -10

	def update(self,screen,rect):
		self.rect.x += (self.velocidad_x * v.Velocidad_enemigo) 
		self.rect.y += (self.velocidad_y * v.Velocidad_enemigo)

		if self.rect.left < 110:
			self.velocidad_x += (10 * v.Velocidad_enemigo)
		if self.rect.right > 900:
			self.velocidad_x -= (10 * v.Velocidad_enemigo)
		if self.rect.bottom > 500:
			self.velocidad_y -= (10 * v.Velocidad_enemigo)
		if self.rect.top < 50:
			self.velocidad_y += (10 * v.Velocidad_enemigo)

		screen.blit(v.obstaculo_image[v.state],(self.rect.x,self.rect.y))

		if self.rect.colliderect(rect):
			v.daño = True
			v.score -= 200 
			v.perdida_vida.play()
		else:
			v.daño = False

	def reiniciar(self):
		self.velocidad_x = -10
		self.velocidad_y = -10



enemy = pg.sprite.Group()

for x in range(1):
	enemy_object = enemy_obj()
	enemy.add(enemy_object)

def reiniciar_enemy():
	enemy_object.reiniciar()