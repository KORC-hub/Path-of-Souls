import pygame as pg
import random
pg.mixer.init()

# Medidas
height = 563 # alto
width = 1001 # ancho
screen = pg.display.set_mode((width,height))

# Colores
white = (255, 255, 255) # color blanco
black = (0, 0, 0) # color negro

# nombre de la ventana
name = "Path of souls"

# coordenadas [x,y]
posicion_base = [0,0]
posicion_base_art = [0,0]
posicion_texto = [width-935,height-500]
pisicion_personaje = [width - 200,height/2]
pisicion_Entrada = [width - 40,height/2]
posicion_vida = [820,0]
posicion_barra_medalla = [10,3]
posicion_enemy = [200,200]

# coordenadas medallas
posicion_medalla_n1 = [random.randrange(130,330),random.randrange(50, 430)]
posicion_medalla_n2 = [random.randrange(130,330),random.randrange(50, 430)]
posicion_medalla_n3 = [random.randrange(130,330),random.randrange(50, 430)]
posicion_medalla_n4 = [random.randrange(130,330),random.randrange(50, 430)]
posiciones_medallas = [0,posicion_medalla_n1,posicion_medalla_n2,posicion_medalla_n3,posicion_medalla_n4]

# limites
limites = [0,0,901,465]
limite_art = -1001 + height

# fps
fps = 15

# Contadores
x = 0
j = 1
state = 0
state_vida = 3
state_medalla = 0

# state (Boolean)
running = True
menu = True
play = False
art = False
state_introduccion = False
state_sala1 = False
state_sala2 = False
state_sala3 = False
state_sala4 = False

# Controles
click = False

#botones
button_1 = pg.Rect(330, 450, 150, 50)
button_2 = pg.Rect(560, 450, 150, 50)

# --- images --- ruta_principal: "C:/Lenguajes/Python/Pygame/Path of Souls/resources/graphics/"

# fondos
background = pg.image.load("resources/graphics/states/menu.jpeg")
fondo_art = pg.image.load("resources/graphics/states/art.png")
sala0 = pg.image.load("resources/graphics/states/Sala_0.png")
sala1 = pg.image.load("resources/graphics/states/Sala_1.png")
sala2 = pg.image.load("resources/graphics/states/Sala_2.png")
sala3 = pg.image.load("resources/graphics/states/Sala_2.png")
sala4 = pg.image.load("resources/graphics/states/Sala_2.png")
state_salas = [sala0,sala1,sala2,sala3,sala4]

# jugador
player = pg.image.load("resources/graphics/Player/Ymir.png")

# Obtaculo
obstaculo = pg.image.load("C:/Lenguajes/Python/Pygame/Path of Souls/resources/graphics/Boss/obstaculo.png")

# Boss

# Guide
Guide = pg.image.load("resources/graphics/Guide/Guide.png")

# Health
vida_n3 = pg.image.load("resources/graphics/vida/N_vida_3.png")
vida_n2 = pg.image.load("resources/graphics/vida/N_vida_2.png")
vida_n1 = pg.image.load("resources/graphics/vida/N_vida_1.png")
vida_n0 = pg.image.load("resources/graphics/vida/N_vida_0.png")
barra_vida = [vida_n0,vida_n1,vida_n2,vida_n3]

# Medallas
medalla_n1 = pg.image.load("resources/graphics/medallas/medalla_1.png")
medalla_n2 = pg.image.load("resources/graphics/medallas/medalla_2.png")
medalla_n3 = pg.image.load("resources/graphics/medallas/medalla_3.png")
medalla_n4 = pg.image.load("resources/graphics/medallas/medalla_4.png")
medallas = [0,medalla_n1,medalla_n2,medalla_n3,medalla_n4]

# Barra Medallas
Barra_medalla_n0 = pg.image.load("resources/graphics/medallas/Barra_medalla_0.png")
Barra_medalla_n1 = pg.image.load("resources/graphics/medallas/Barra_medalla_1.png")
Barra_medalla_n2 = pg.image.load("resources/graphics/medallas/Barra_medalla_2.png")
Barra_medalla_n3 = pg.image.load("resources/graphics/medallas/Barra_medalla_3.png")
Barra_medalla_n4 = pg.image.load("resources/graphics/medallas/Barra_medalla_4.png")
barra_madallas = [Barra_medalla_n0,Barra_medalla_n1,Barra_medalla_n2,Barra_medalla_n3,Barra_medalla_n4]

# Botones
play_on  = pg.image.load("resources/graphics/botones/play_on.png")
play_off = pg.image.load("resources/graphics/botones/play_off.png")
art_on   = pg.image.load("resources/graphics/botones/art_on.png")
art_off  = pg.image.load("resources/graphics/botones/art_off.png")

# --- Sound ---

S_introduccion = pg.mixer.Sound("resources/music/introduccion_juego.mp3")