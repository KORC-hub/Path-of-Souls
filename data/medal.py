import pygame as pg
import constants as c

class medal_obj():
	def __init__(self, loc):
		self.loc = loc

	def render(self, screen, x):
		screen.blit(c.medals[x],self.loc)

	# the medal hitbox is created
	def get_rect(self):
		return pg.Rect(self.loc[0], self.loc[1], 50, 52)

		# the rect of each object is compared to verify the collision
	def collision_test(self,rect):
		medal_rect = self.get_rect()
		return medal_rect.colliderect(rect)

# print and if the straight lines of the medal match and the player adds one to the status of the medal
def medallas(screen,player):
		c.medal_objects[c.state_medal].render(screen,c.state)
		if c.medal_objects[c.state_medal].collision_test(player):
		 c.state_medal += 1




