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
posicion_texto = [0,height-192]

# fps
fps = 15

# --- imagenes ---

# fondos
background = pg.image.load("C:/Lenguajes/Python/Pygame/Path of Souls/resources/graphics/states/menu.png")
sala1 = pg.image.load("C:/Lenguajes/Python/Pygame/Path of Souls/resources/graphics/states/Sala_1.png")

# jugador
player = pg.image.load("C:/Lenguajes/Python/Pygame/Path of Souls/resources/graphics/Player/Ymir.png")

# Guide
Guide = pg.image.load("C:/Lenguajes/Python/Pygame/Path of Souls/resources/graphics/Guide/Guide.jpeg")


