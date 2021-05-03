import pygame as pg
import random

# sizes windows
height = 563 # alto
width = 1001 # ancho

# Colors
white = (255, 255, 255) # color blanco
black = (0, 0, 0) # color negro

# window name
name = "Path of souls"

# coordinates [x,y]
position_base = [0,0]
position_base_art = [0,0]
position_texto = [width-935,height-500]
position_personaje = [width - 200,height/2]
position_Entrada = [width - 40,height/2]
position_vida = [820,0]
position_bar_medal = [10,3]
position_enemy = [200,200]
medal_objects = []
boss_objects = []


# medal coordinates
position_medalla = [random.randrange(130,330),random.randrange(50, 430)]

# boss coordinates
position_boss = [300,36]

# limits
limits = [0,0,901,465]
limits_art = -1001 + height

# size of objects
size_medal = [50,52]

# frames per second
fps = 15

# Accountants
move_boss = 0
x = 0
state = 1
state_life = 3
state_medal = 0

# state (Boolean)
running = True
menu = True
play = False
art = False
end = False
state_introduction = False
state_room1 = False
state_room2 = False
state_room3 = False
state_room4 = False

# Controls
click = False

# buttons
button_1 = pg.Rect(330, 450, 150, 50)
button_2 = pg.Rect(560, 450, 150, 50)

# picture background
background = pg.image.load("resources/graphics/states/menu.jpeg")
background_art = pg.image.load("resources/graphics/states/art.png")
background_end = pg.image.load("resources/graphics/states/end.png")

# picture maps
room0 = pg.image.load("resources/graphics/states/Sala_0.png")
room1 = pg.image.load("resources/graphics/states/Sala_1.png")
room2 = pg.image.load("resources/graphics/states/Sala_2.png")
room3 = pg.image.load("resources/graphics/states/Sala_3.png")
room4 = pg.image.load("resources/graphics/states/Sala_2.png")
state_image_room = [room0,room1,room2,room3,room4]

# picture player
player = pg.image.load("resources/graphics/Player/Ymir.png")

# picture enemy
obstaculo_1 = pg.image.load("resources/graphics/Boss/obstaculo_1.png")
obstaculo_2 = pg.image.load("resources/graphics/Boss/obstaculo_2.png")
obstaculo = [obstaculo_1,obstaculo_2]

# picture Boss

# picture Guide
Guide = pg.image.load("resources/graphics/Guide/Guide.png")

# picture life bar
life_n3 = pg.image.load("resources/graphics/vida/N_vida_3.png")
life_n2 = pg.image.load("resources/graphics/vida/N_vida_2.png")
life_n1 = pg.image.load("resources/graphics/vida/N_vida_1.png")
life_n0 = pg.image.load("resources/graphics/vida/N_vida_0.png")
bar_life = [life_n0,life_n1,life_n2,life_n3]

# picture medal
medal_n1 = pg.image.load("resources/graphics/medallas/medalla_1.png")
medal_n2 = pg.image.load("resources/graphics/medallas/medalla_2.png")
medal_n3 = pg.image.load("resources/graphics/medallas/medalla_3.png")
medal_n4 = pg.image.load("resources/graphics/medallas/medalla_4.png")
medals = [0,medal_n1,medal_n2,medal_n3,medal_n4]

# picture bar medal
Bar_medal_n0 = pg.image.load("resources/graphics/medallas/Barra_medalla_0.png")
Bar_medal_n1 = pg.image.load("resources/graphics/medallas/Barra_medalla_1.png")
Bar_medal_n2 = pg.image.load("resources/graphics/medallas/Barra_medalla_2.png")
Bar_medal_n3 = pg.image.load("resources/graphics/medallas/Barra_medalla_3.png")
Bar_medal_n4 = pg.image.load("resources/graphics/medallas/Barra_medalla_4.png")
bar_medal = [Bar_medal_n0,Bar_medal_n1,Bar_medal_n2,Bar_medal_n3,Bar_medal_n4]

# picture buttons
play_on  = pg.image.load("resources/graphics/botones/play_on.png")
play_off = pg.image.load("resources/graphics/botones/play_off.png")
art_on   = pg.image.load("resources/graphics/botones/art_on.png")
art_off  = pg.image.load("resources/graphics/botones/art_off.png")

# --- Sound ---

#S_introduccion = pg.mixer.Sound("resources/music/introduccion_juego.mp3")