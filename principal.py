#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

# from configuracion import *
#from funcionesRESUELTO import *
from extras import *
from funciones import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        #Preparar la ventana
        pygame.display.set_caption("Tiene la Palabra")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #Inicializa el mezclador de musica
        pygame.mixer.init()

        # Obtener la ruta completa de los archivos de sonido
        acierto_sound_path = os.path.join(os.path.dirname(__file__), "acierto.wav")
        incorrecta_sound_path = os.path.join(os.path.dirname(__file__), "incorrecto.wav")

        # Cargar los archivos de sonido
        acierto_sound = pygame.mixer.Sound(acierto_sound_path)
        incorrecta_sound = pygame.mixer.Sound(incorrecta_sound_path)

        # Preparar la música de fondo
        if menu_state[1] == '1':
            pygame.mixer.music.load("musica_fondo.wav")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)

        else:
            pygame.mixer.music.stop()
            pygame.mixer.quit()


        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        candidata = ""
        diccionario = []
        palabrasAcertadas = []

        #lee el diccionario
        lectura(diccionario)

        #elige las 7 letras al azar y una de ellas como principal
        letrasEnPantalla = dame7Letras(letras,vocales,consonanteDif)
        letraPrincipal = dameLetra(letrasEnPantalla)

        #se queda con 7 letras que permitan armar muchas palabras, evita que el juego sea aburrido
        while(len(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))< MINIMO):
            letrasEnPantalla = dame7Letras(letras,vocales,consonanteDif)
            letraPrincipal = dameLetra(letrasEnPantalla)

        print(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))

        #dibuja la pantalla la primera vez
        dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)


        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

            #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra   #va concatenando las letras que escribe
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1] #borra la ultima

                    if e.key == K_RETURN:  #presionó enter
                        if esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario) and candidata not in palabrasSalidas:
                            puntos += procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario, palabrasSalidas)

                            if menu_state[1] == '1':
                                acierto_sound.play()
                                candidata=""

                        elif esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario) and candidata in palabrasSalidas:
                            puntos += procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario, palabrasSalidas)
                            if menu_state[1] == '1':
                                incorrecta_sound.play()
                                candidata=""

                        else:
                            if menu_state[1] == '1':
                                incorrecta_sound.play()
                                candidata=""





            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000


            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)

            pygame.display.flip()

        #Detener la música de fondo
        if menu_state[1] == '1':
            pygame.mixer.music.stop()
            pygame.mixer.quit()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
        print("palabras salidas: ", palabrasSalidas);

#Programa Principal ejecuta Main
menu_state = ["main","1"]
if __name__ == "__main__":
    menu_state = menu()
    while menu_state[0] == "play":
        main()
        menu_state = menu()