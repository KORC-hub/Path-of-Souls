import pygame as pg
from data import variables as v

class bar_medal_obj():
	def __init__(self, image, loc):
		self.image = image
		self.loc = loc

	def render(self, screen):
		screen.blit(self.image,self.loc)

	def add(self):
		self.image = v.medals[v.medal_counter]

def render_bar_medal(screen):
	x = 2
	for i in range(4):
		v.bar_medal_objects[x].render(screen)
		x += 2
		if v.medal_on == False:
			v.bar_medal_objects[v.state].add()

