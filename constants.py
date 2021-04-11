import pygame as pg


# Medidas
height = 563 # alto
width = 1001 # ancho

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

# fps
fps = 15

# Contador
x = 0

# state
state = 1
state_vida = 3
running = True
menu = True
play = False
state_sala1 = False
state_sala2 = False
state_sala3 = False
state_sala4 = False
state_sala5 = False

# Controles
click = False

# --- imagenes ---

ruta_principal = "C:/Lenguajes/Python/Pygame/"

# fondos
background = pg.image.load(ruta_principal + "Path of Souls/resources/graphics/states/menu.jpeg")
sala1 = pg.image.load(ruta_principal + "Path of Souls/resources/graphics/states/Sala_1.png")
sala2 = pg.image.load(ruta_principal + "Path of Souls/resources/graphics/states/Sala_2.png")
sala3 = pg.image.load(ruta_principal + "Path of Souls/resources/graphics/states/Sala_2.png")
sala4 = pg.image.load(ruta_principal + "Path of Souls/resources/graphics/states/Sala_2.png")
#sala5 = pg.image.load()

# jugador
player = pg.image.load(ruta_principal + "Path of Souls/resources/graphics/Player/Ymir.png")

# Guide
Guide = pg.image.load(ruta_principal + "Path of Souls/resources/graphics/Guide/Guide.png")

# vida
vida_n3 = pg.image.load(ruta_principal + "Path of Souls/resources/graphics/vida/N_vida_3.png")
vida_n2 = pg.image.load(ruta_principal + "Path of Souls/resources/graphics/vida/N_vida_2.png")
vida_n1 = pg.image.load(ruta_principal + "Path of Souls/resources/graphics/vida/N_vida_1.png")
vida_n0 = pg.image.load(ruta_principal + "Path of Souls/resources/graphics/vida/N_vida_0.png")