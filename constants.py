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
position_collision = [width - 100,height/2]
position_personaje = [width - 200,height/2]
position_Entrada = [990,height/2]
position_vida = [820,0]
position_bar_medal = [10,3]
position_enemy = [200,200]
medal_objects = []
boss_objects = []


# medal coordinates
position_medalla = [random.randrange(130,330),random.randrange(50, 430)]

# boss coordinates
position_boss_1 = [200,36]
position_boss_2 = [400,36]
position_boss_3 = [600,36]
position_boss = [position_boss_1,position_boss_2,position_boss_3]


#collider
collider = False

# limits
limits_art = -1001 + height
limits_map_1 = [36,900,2,420]
limits_map_2 = [100,850,2,420]
limit_entrada = [1,1,130,297]
limit_salida = [1,1,130,297]

# size of objects
size_medal = [50,52]

# frames per second
fps = 15

# Accountants
iterador = 0
move_boss = 0
x = 0
state = 0
kinematics_counter = 0
state_personaje = 0
state_life = 3
state_medal = 0

# state (Boolean)
running = True
menu = True
play = False
art = False
end = False
introduction = False
kinematics = False


# Controls
click = False

# buttons
button_1 = pg.Rect(330, 450, 150, 50)
button_2 = pg.Rect(560, 450, 150, 50)
button_x = pg.Rect(920, 10, 73, 50)

# picture background
background = pg.image.load("resources/graphics/states/menu.jpeg")
background_art = pg.image.load("resources/graphics/states/ART.png")
background_end = pg.image.load("resources/graphics/states/end.png")

# picture maps
room0 = pg.image.load("resources/graphics/states/Sala_0.png")
room1 = pg.image.load("resources/graphics/states/Sala_1.png")
room2 = pg.image.load("resources/graphics/states/Sala_2.png")
room3 = pg.image.load("resources/graphics/states/Sala_3.png")
room4 = pg.image.load("resources/graphics/states/Sala_4.png")
state_image_room = [room0,0,room1,0,room2,0,room3,0,room4]

# kinematics
cinematica_1 = pg.image.load("resources/graphics/cinematicas/cinematica 1.png")
cinematica_1_1 = pg.image.load("resources/graphics/cinematicas/cinematica 1.1.png")
cinematica_2 = pg.image.load("resources/graphics/cinematicas/cinematica 2.png")
cinematica_2_1 = pg.image.load("resources/graphics/cinematicas/cinematica 2.1.png")
cinematica_3 = pg.image.load("resources/graphics/cinematicas/cinematica 3.png")
cinematica_3_1 = pg.image.load("resources/graphics/cinematicas/cinematica 3.1.png")
cinematica_4 = pg.image.load("resources/graphics/cinematicas/cinematica 4.png")
cinematica_4_1 = pg.image.load("resources/graphics/cinematicas/cinematica 4.1.png")
kinematics_image = [0,cinematica_1,0,[cinematica_1_1,cinematica_2],0,[cinematica_2_1,cinematica_3],0,[cinematica_3_1,cinematica_4],0,cinematica_4_1]


# picture player
player = pg.image.load("resources/graphics/Player/Ymir.png")

# picture enemy
Pettra = pg.image.load("resources/graphics/Boss/ataquePettra.png")
Morrigan = pg.image.load("resources/graphics/Boss/ataqueMorrigan.png")
Mundus = pg.image.load("resources/graphics/Boss/ataqueMundus.png")
Akhlut = pg.image.load("resources/graphics/Boss/ataqueAkhlut.png")
obstaculo_image = [0,0,Pettra,Pettra,Morrigan,0,Mundus,0,Akhlut]

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
medals_obj = [medal_n1,medal_n2,medal_n3,medal_n4]

# picture buttons
play_on  = pg.image.load("resources/graphics/botones/play_on.png")
play_off = pg.image.load("resources/graphics/botones/play_off.png")
art_on   = pg.image.load("resources/graphics/botones/art_on.png")
art_off  = pg.image.load("resources/graphics/botones/art_off.png")
x_on   = pg.image.load("resources/graphics/botones/X_on.png")
x_off  = pg.image.load("resources/graphics/botones/X_off.png")

# --- Sound ---
