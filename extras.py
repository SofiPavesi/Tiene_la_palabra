import pygame
import button
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), 80)
    background = pygame.image.load("images/Backgroum1.jpg").convert()
    screen.blit(background, [0, 0])
    #Linea del piso
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    ren1 = defaultFont.render(candidata, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    if(segundos<15):
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    #escribe grande la palabra (letra por letra) y la letra principal de otro color
    pos = 130
    for i in range(len(letrasEnPantalla)):
        if letrasEnPantalla[i] == letraPrincipal:
            screen.blit(defaultFontGrande.render(letrasEnPantalla[i], 1, COLOR_TIEMPO_FINAL), (pos, 100))
        else:
            screen.blit(defaultFontGrande.render(letrasEnPantalla[i], 1, COLOR_LETRAS), (pos, 100))
        pos = pos + TAMANNO_LETRA_GRANDE

    screen.blit(ren1, (190, 570))
    screen.blit(ren2, (680, 10))
    screen.blit(ren3, (10, 10))


def menu():
    pygame.init()

    #crea ventana de juego
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tiene la Palabra - Menú")
    background = pygame.image.load("images/backgroundMenu.jpg").convert()

    #variables de juego
    game_paused = False
    menu_state = ["main","1"]
    #define fuentes
    font = pygame.font.SysFont("arialblack", 40)

    #define colores
    TEXT_COL = (255, 255, 255)

    #Carga imagenes de botones
    play_img = pygame.image.load("images/button_play.png").convert_alpha()
    options_img = pygame.image.load("images/button_options.png").convert_alpha()
    levels_img = pygame.image.load("images/button_levels.png").convert_alpha()
    quit_img = pygame.image.load("images/button_quit.png").convert_alpha()


    audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
    back_img = pygame.image.load('images/button_back.png').convert_alpha()

    facil_img = pygame.image.load('images/button_facil.png').convert_alpha()
    media_img = pygame.image.load('images/button_Media.png').convert_alpha()
    desafiante_img = pygame.image.load('images/button_Desafiante.png').convert_alpha()

    mute_img = pygame.image.load('images/mute.png').convert_alpha()


    #instanciando botones
    play_button = button.Button(245, 100, play_img, 1)
    options_button = button.Button(245, 200, options_img, 1)
    levels_button = button.Button(245, 300, levels_img, 1)
    quit_button = button.Button(245, 400, quit_img, 1)

    audio_button = button.Button(245, 100, audio_img, 1)
    back_button = button.Button(450, 500, back_img, 1)

    facil_button = button.Button(245, 150, facil_img, 1)
    media_button = button.Button(245, 250, media_img, 1)
    desafiante_button = button.Button(245, 350, desafiante_img, 1)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        text_width, text_height = img.get_size()
        x = (SCREEN_WIDTH - text_width) // 2
        y = (SCREEN_HEIGHT - text_height) // 2
        screen.blit(img, (x, y))

    #loop Juego

    run = True
    menu_state = ["main", "1"]  #menu_state[0] es el estado del menú, menu_state[1] es el estado del audio

    while run:
        screen.fill((52, 78, 91))
        screen.blit(background, [0, 0])

        if menu_state[0] == "main":
            if play_button.draw(screen):
                menu_state[0] = "play"
                run = False
            if options_button.draw(screen):
                menu_state[0] = "options"
            if levels_button.draw(screen):
                menu_state[0] = "levels"
            if quit_button.draw(screen):
                run = False

        elif menu_state[0] == "options":
            screen.fill((52, 78, 91))
            screen.blit(background, [0, 0])

            if audio_button.draw(screen):
                menu_state[1] = '0' # Cambia a sin audio
                screen.blit(mute_img, (245, 250))  # Muestra la imagen mute

            if back_button.draw(screen):
                menu_state[0] = "main"

        elif menu_state[0] == "levels":
            screen.fill((52, 78, 91))
            screen.blit(background, [0, 0])

            if facil_button.draw(screen):
                print("Facil")
            if media_button.draw(screen):
                print("Media")
            if desafiante_button.draw(screen):
                print("Desafiante")
            if back_button.draw(screen):
                menu_state[0] = "main"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
    return menu_state