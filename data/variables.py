import pygame as pg
import random

pg.mixer.init()

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
position_collision = [width - 50,height/2]
position_personaje = [width - 50,height/2]
position_Entrada = [990,height/2]
position_vida = [823,772,721,670,512]
position_bar_medal = [331,274,217,160,505]
position_enemy = [200,200]

# listas de objetos
medal_objects = [0,0,]
bar_medal_objects = [0,0,]
bar_life_objects = []
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
limit = [1,950,120,297]

# size of objects
size_medal = [50,52]

# frames per second
fps = 15

# Accountants
score = 0
iterador = 0
move_boss = 0
x = 0
state = 0
kinematics_counter = 0
medal_counter = -1
state_life = 4
state_medal = 0

# state (Boolean)
running = True
menu = True
play = False
art = False
end = False
introduction = False
kinematics = False
daño = False
medal_on = True

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
Akhlut = pg.image.load("resources/graphics/Boss/ataqueAkhlut.png")
Mundus = pg.image.load("resources/graphics/Boss/ataqueMundus.png")
obstaculo_image = [0,0,Pettra,Pettra,Morrigan,0,Akhlut,0,Mundus]

# picture Boss

# picture Guide
Guide = pg.image.load("resources/graphics/Guide/Guide.png")

# picture life bar
life_off = pg.image.load("resources/graphics/vida/vida_off.png")
life_on = pg.image.load("resources/graphics/vida/vida_on.png")
life = [life_on,life_off]

# picture medal
medal_n1 = pg.image.load("resources/graphics/medallas/medalla_1.png")
medal_n2 = pg.image.load("resources/graphics/medallas/medalla_2.png")
medal_n3 = pg.image.load("resources/graphics/medallas/medalla_3.png")
medal_n4 = pg.image.load("resources/graphics/medallas/medalla_4.png")
medals = [medal_n1,medal_n2,medal_n3,medal_n4]

medal_n1_off = pg.image.load("resources/graphics/medallas/medalla_1_off.png")
medal_n2_off = pg.image.load("resources/graphics/medallas/medalla_2_off.png")
medal_n3_off = pg.image.load("resources/graphics/medallas/medalla_3_off.png")
medal_n4_off = pg.image.load("resources/graphics/medallas/medalla_4_off.png")
bar_medal = [medal_n1_off,medal_n2_off,medal_n3_off,medal_n4_off]

# picture buttons
play_on  = pg.image.load("resources/graphics/botones/play_on.png")
play_off = pg.image.load("resources/graphics/botones/play_off.png")
art_on   = pg.image.load("resources/graphics/botones/art_on.png")
art_off  = pg.image.load("resources/graphics/botones/art_off.png")
x_on   = pg.image.load("resources/graphics/botones/X_on.png")
x_off  = pg.image.load("resources/graphics/botones/X_off.png")

# --- music ---

music_1 = "resources/music/juego.mp3"


# --- Sound ---

bonus = pg.mixer.Sound("resources/sound/Bonificación.mp3")
perdida_vida = pg.mixer.Sound("resources/sound/perdida_vida.mp3")
seleccion_opcion = pg.mixer.Sound("resources/sound/seleccion_opcion_menu.mp3")
