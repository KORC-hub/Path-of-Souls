import pygame as pg
from data import variables as v

class bar_life_obj():
	def __init__(self, image, loc):
		self.image = image
		self.loc = loc

	def render(self, screen):
		screen.blit(self.image,self.loc)

	def add(self):
		self.image = v.life[1]

	def reiniciar(self):
		self.image = v.life[0]

def render_bar_life(screen):
	for i in range(4):
		v.bar_life_objects[i].render(screen)
		if v.daño:
			v.bar_life_objects[v.state_life].add()
			v.score -= 200 
			v.perdida_vida.play()

def reiniciar_life():
	for i in range(4):
		v.bar_life_objects[i].reiniciar()