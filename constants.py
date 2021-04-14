import pygame as pg

# Medidas
height = 563 # alto
width = 1001 # ancho
screen = pg.display.set_mode((width,height))
# Colores
white = (255, 255, 255) # color blanco
black = (0, 0, 0) # color negro

# nombre de la ventana
name = "Path of souls"

# coordenadas 
posicion_base = [0,0]
posicion_texto = [width-935,height-500]
pisicion_personaje = [width - 200,height/2]
pisicion_Entrada = [width - 40,height/2]
posicion_enemy = [200,200]
limites = [0,0,901,465]
# fps
fps = 15

# Contador
x = 0

# state
state = 1
state_vida = 3
state_medalla = 0
running = True
menu = True
play = False
art = False
state_sala1 = False
state_sala2 = False
state_sala3 = False
state_sala4 = False
state_sala5 = False

# Controles
click = False

# --- imagenes ---

ruta_principal = "C:/Lenguajes/Python/Pygame/Path of Souls/resources/graphics/"

# fondos
background = pg.image.load(ruta_principal + "states/menu.jpeg")
sala1 = pg.image.load(ruta_principal + "states/Sala_1.png")
sala2 = pg.image.load(ruta_principal + "states/Sala_2.png")
sala3 = pg.image.load(ruta_principal + "states/Sala_2.png")
sala4 = pg.image.load(ruta_principal + "states/Sala_2.png")
#sala5 = pg.image.load()

# jugador
player = pg.image.load(ruta_principal + "Player/Ymir.png")

# Obtaculo
obstaculo = pg.image.load("C:/Lenguajes/Python/Pygame/Path of Souls/resources/graphics/Boss/obstaculo.png")

# Boss

# Guide
Guide = pg.image.load(ruta_principal + "Guide/Guide.png")

# Health
vida_n3 = pg.image.load(ruta_principal + "vida/N_vida_3.png")
vida_n2 = pg.image.load(ruta_principal + "vida/N_vida_2.png")
vida_n1 = pg.image.load(ruta_principal + "vida/N_vida_1.png")
vida_n0 = pg.image.load(ruta_principal + "vida/N_vida_0.png")

# Medallas
medalla_n0 = pg.image.load(ruta_principal + "medallas/N_medalla_0.png")
medalla_n1 = pg.image.load(ruta_principal + "medallas/N_medalla_1.png")
medalla_n2 = pg.image.load(ruta_principal + "medallas/N_medalla_2.png")
medalla_n3 = pg.image.load(ruta_principal + "medallas/N_medalla_3.png")
medalla_n4 = pg.image.load(ruta_principal + "medallas/N_medalla_4.png")

# Botones
play_on  = pg.image.load(ruta_principal + "botones/play_on.png")
play_off = pg.image.load(ruta_principal + "botones/play_off.png")
art_on   = pg.image.load(ruta_principal + "botones/art_on.png")
art_off  = pg.image.load(ruta_principal + "botones/art_off.png")