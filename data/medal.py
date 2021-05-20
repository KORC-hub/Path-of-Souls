import pygame as pg
from data import variables as v

class medal_obj():
	def __init__(self, image, loc):
		self.image = image
		self.loc = loc

	def render(self, screen):
		screen.blit(self.image,self.loc)

	def get_rect(self):
		return pg.Rect(self.loc[0], self.loc[1], 50, 52)

	def collision_test(self,rect):
		medal_rect = self.get_rect()
		return medal_rect.colliderect(rect)

def medallas(screen,player):
		v.medal_objects[v.state].render(screen)
		if v.medal_objects[v.state].collision_test(player):
		 v.bonus.play()
		 v.medal_on = False






