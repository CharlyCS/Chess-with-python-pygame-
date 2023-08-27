#JUEGO DE AJEDREZ
import pygame,sys
pygame.init()

#Definiendo colores 
BLACK = (0,0,0)
WHITE = (255,255,255)
CREAM =(252,204,116)
BROWN = (87,58,46)
size = (480,480)
#Se crea una ventana 
screen = pygame.display.set_mode(size)
clock=pygame.time.Clock()

torre_negro = pygame.image.load("ajedrezjuego/img/torre_negro.png").convert()
torre_negro.set_colorkey([255,255,255])
torre_negro_rect = torre_negro.get_rect()  # Obtener rectángulo de la imagen
offset1 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
torre_negro_rect.x = 0
torre_negro_rect.y = 0

caballo_negro = pygame.image.load("ajedrezjuego/img/caballo_negro.png").convert()
caballo_negro.set_colorkey([255,255,255])
caballo_negro_rect = caballo_negro.get_rect()  # Obtener rectángulo de la imagen
offset2 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
caballo_negro_rect.x =60
caballo_negro_rect.y =0

alfil_negro = pygame.image.load("ajedrezjuego/img/alfil_negro.png").convert()
alfil_negro.set_colorkey([255,255,255])
alfil_negro_rect = alfil_negro.get_rect()  # Obtener rectángulo de la imagen
offset3 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
alfil_negro_rect.x =120
alfil_negro_rect.y =0

torre_negro1 = pygame.image.load("ajedrezjuego/img/torre_negro.png").convert()
torre_negro1.set_colorkey([255,255,255])
torre_negro1_rect = torre_negro1.get_rect()  # Obtener rectángulo de la imagen
offset11 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
torre_negro1_rect.x = 420
torre_negro1_rect.y = 0

caballo_negro1 = pygame.image.load("ajedrezjuego/img/caballo_negro.png").convert()
caballo_negro1.set_colorkey([255,255,255])
caballo_negro1_rect = caballo_negro.get_rect()  # Obtener rectángulo de la imagen
offset21 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
caballo_negro1_rect.x =360
caballo_negro1_rect.y =0

alfil_negro1 = pygame.image.load("ajedrezjuego/img/alfil_negro.png").convert()
alfil_negro1.set_colorkey([255,255,255])
alfil_negro1_rect = alfil_negro1.get_rect()  # Obtener rectángulo de la imagen
offset31 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
alfil_negro1_rect.x =300
alfil_negro1_rect.y =0

rey_negro = pygame.image.load("ajedrezjuego/img/rey_negro.png").convert()
rey_negro.set_colorkey([255,255,255])
rey_negro_rect = rey_negro.get_rect()  # Obtener rectángulo de la imagen
offset4 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
rey_negro_rect.x =180
rey_negro_rect.y =0

reina_negro = pygame.image.load("ajedrezjuego/img/reina_negro.png").convert()
reina_negro.set_colorkey([255,255,255])
reina_negro_rect = reina_negro.get_rect()  # Obtener rectángulo de la imagen
offset5 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
reina_negro_rect.x =240
reina_negro_rect.y =0

peon_negro1 = pygame.image.load("ajedrezjuego/img/peon_negro.png").convert()
peon_negro1.set_colorkey([255,255,255])
peon_negro1_rect = peon_negro1.get_rect()  # Obtener rectángulo de la imagen
offset61 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_negro1_rect.x =0
peon_negro1_rect.y =60

peon_negro2 = pygame.image.load("ajedrezjuego/img/peon_negro.png").convert()
peon_negro2.set_colorkey([255,255,255])
peon_negro2_rect = peon_negro2.get_rect()  # Obtener rectángulo de la imagen
offset62 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_negro2_rect.x =60
peon_negro2_rect.y =60

peon_negro3 = pygame.image.load("ajedrezjuego/img/peon_negro.png").convert()
peon_negro3.set_colorkey([255,255,255])
peon_negro3_rect = peon_negro3.get_rect()  # Obtener rectángulo de la imagen
offset63 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_negro3_rect.x =120
peon_negro3_rect.y =60

peon_negro4 = pygame.image.load("ajedrezjuego/img/peon_negro.png").convert()
peon_negro4.set_colorkey([255,255,255])
peon_negro4_rect = peon_negro4.get_rect()  # Obtener rectángulo de la imagen
offset64 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_negro4_rect.x =180
peon_negro4_rect.y =60

peon_negro5 = pygame.image.load("ajedrezjuego/img/peon_negro.png").convert()
peon_negro5.set_colorkey([255,255,255])
peon_negro5_rect = peon_negro5.get_rect()  # Obtener rectángulo de la imagen
offset65 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_negro5_rect.x =240
peon_negro5_rect.y =60

peon_negro6 = pygame.image.load("ajedrezjuego/img/peon_negro.png").convert()
peon_negro6.set_colorkey([255,255,255])
peon_negro6_rect = peon_negro6.get_rect()  # Obtener rectángulo de la imagen
offset66 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_negro6_rect.x =300
peon_negro6_rect.y =60

peon_negro7 = pygame.image.load("ajedrezjuego/img/peon_negro.png").convert()
peon_negro7.set_colorkey([255,255,255])
peon_negro7_rect = peon_negro7.get_rect()  # Obtener rectángulo de la imagen
offset67 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_negro7_rect.x =360
peon_negro7_rect.y =60

peon_negro8 = pygame.image.load("ajedrezjuego/img/peon_negro.png").convert()
peon_negro8.set_colorkey([255,255,255])
peon_negro8_rect = peon_negro8.get_rect()  # Obtener rectángulo de la imagen
offset68 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_negro8_rect.x =420
peon_negro8_rect.y =60

torre_blanco = pygame.image.load("ajedrezjuego/img/torre_blanco.png").convert()
torre_blanco.set_colorkey([255,255,255])
torre_blanco_rect = torre_blanco.get_rect()  # Obtener rectángulo de la imagen
offset7 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
torre_blanco_rect.x =0
torre_blanco_rect.y =420

caballo_blanco = pygame.image.load("ajedrezjuego/img/caballo_blanco.png").convert()
caballo_blanco.set_colorkey([255,255,255])
caballo_blanco_rect = caballo_blanco.get_rect()  # Obtener rectángulo de la imagen
offset8 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
caballo_blanco_rect.x =60
caballo_blanco_rect.y =420

alfil_blanco = pygame.image.load("ajedrezjuego/img/alfil_blanco.png").convert()
alfil_blanco.set_colorkey([255,255,255])
alfil_blanco_rect = alfil_blanco.get_rect()  # Obtener rectángulo de la imagen
offset9 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
alfil_blanco_rect.x =120
alfil_blanco_rect.y =420

torre_blanco1 = pygame.image.load("ajedrezjuego/img/torre_blanco.png").convert()
torre_blanco1.set_colorkey([255,255,255])
torre_blanco1_rect = torre_blanco1.get_rect()  # Obtener rectángulo de la imagen
offset71 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
torre_blanco1_rect.x =420
torre_blanco1_rect.y =420

caballo_blanco1 = pygame.image.load("ajedrezjuego/img/caballo_blanco.png").convert()
caballo_blanco1.set_colorkey([255,255,255])
caballo_blanco1_rect = caballo_blanco1.get_rect()  # Obtener rectángulo de la imagen
offset81 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
caballo_blanco1_rect.x =360
caballo_blanco1_rect.y =420

alfil_blanco1 = pygame.image.load("ajedrezjuego/img/alfil_blanco.png").convert()
alfil_blanco1.set_colorkey([255,255,255])
alfil_blanco1_rect = alfil_blanco1.get_rect()  # Obtener rectángulo de la imagen
offset91 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
alfil_blanco1_rect.x =300
alfil_blanco1_rect.y =420

rey_blanco = pygame.image.load("ajedrezjuego/img/rey_blanco.png").convert()
rey_blanco.set_colorkey([255,255,255])
rey_blanco_rect = rey_blanco.get_rect()  # Obtener rectángulo de la imagen
offset10 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
rey_blanco_rect.x =180
rey_blanco_rect.y =420

reina_blanco = pygame.image.load("ajedrezjuego/img/reina_blanco.png").convert()
reina_blanco.set_colorkey([255,255,255])
reina_blanco_rect = reina_blanco.get_rect()  # Obtener rectángulo de la imagen
offset11 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
reina_blanco_rect.x =240
reina_blanco_rect.y =420

peon_blanco1 = pygame.image.load("ajedrezjuego/img/peon_blanco.png").convert()
peon_blanco1.set_colorkey([255,255,255])
peon_blanco1_rect = peon_blanco1.get_rect()  # Obtener rectángulo de la imagen
offset121 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_blanco1_rect.x =0
peon_blanco1_rect.y =360

peon_blanco2 = pygame.image.load("ajedrezjuego/img/peon_blanco.png").convert()
peon_blanco2.set_colorkey([255,255,255])
peon_blanco2_rect = peon_blanco2.get_rect()  # Obtener rectángulo de la imagen
offset122 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_blanco2_rect.x =60
peon_blanco2_rect.y =360

peon_blanco3 = pygame.image.load("ajedrezjuego/img/peon_blanco.png").convert()
peon_blanco3.set_colorkey([255,255,255])
peon_blanco3_rect = peon_blanco3.get_rect()  # Obtener rectángulo de la imagen
offset123 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_blanco3_rect.x =120
peon_blanco3_rect.y =360

peon_blanco4 = pygame.image.load("ajedrezjuego/img/peon_blanco.png").convert()
peon_blanco4.set_colorkey([255,255,255])
peon_blanco4_rect = peon_blanco4.get_rect()  # Obtener rectángulo de la imagen
offset124 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_blanco4_rect.x =180
peon_blanco4_rect.y =360

peon_blanco5 = pygame.image.load("ajedrezjuego/img/peon_blanco.png").convert()
peon_blanco5.set_colorkey([255,255,255])
peon_blanco5_rect = peon_blanco5.get_rect()  # Obtener rectángulo de la imagen
offset125 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_blanco5_rect.x =240
peon_blanco5_rect.y =360

peon_blanco6 = pygame.image.load("ajedrezjuego/img/peon_blanco.png").convert()
peon_blanco6.set_colorkey([255,255,255])
peon_blanco6_rect = peon_blanco6.get_rect()  # Obtener rectángulo de la imagen
offset126 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_blanco6_rect.x =300
peon_blanco6_rect.y =360

peon_blanco7 = pygame.image.load("ajedrezjuego/img/peon_blanco.png").convert()
peon_blanco7.set_colorkey([255,255,255])
peon_blanco7_rect = peon_blanco7.get_rect()  # Obtener rectángulo de la imagen
offset127 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_blanco7_rect.x =360
peon_blanco7_rect.y =360

peon_blanco8 = pygame.image.load("ajedrezjuego/img/peon_blanco.png").convert()
peon_blanco8.set_colorkey([255,255,255])
peon_blanco8_rect = peon_blanco8.get_rect()  # Obtener rectángulo de la imagen
offset128 = (0, 0)  # Desplazamiento entre el puntero y la esquina superior izquierda de la imagen seleccionada
peon_blanco8_rect.x =420
peon_blanco8_rect.y =360


selected = None  # Bandera para indicar si la imagen está seleccionada

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botón izquierdo del ratón
                if torre_negro_rect.collidepoint(event.pos):
                    selected = torre_negro_rect   # Seleccionar la imagen 
                    offset1 = event.pos[0] - torre_negro_rect.x, event.pos[1] - torre_negro_rect.y
                elif caballo_negro_rect.collidepoint(event.pos):
                    selected = caballo_negro_rect   # Seleccionar la imagen 
                    offset2 = event.pos[0] - caballo_negro_rect.x, event.pos[1] - caballo_negro_rect.y
                elif alfil_negro_rect.collidepoint(event.pos):
                    selected = alfil_negro_rect   # Seleccionar la imagen 
                    offset3 = event.pos[0] - alfil_negro_rect.x, event.pos[1] - alfil_negro_rect.y
                elif torre_negro1_rect.collidepoint(event.pos):
                    selected = torre_negro1_rect   # Seleccionar la imagen 
                    offset11 = event.pos[0] - torre_negro1_rect.x, event.pos[1] - torre_negro1_rect.y
                elif caballo_negro1_rect.collidepoint(event.pos):
                    selected = caballo_negro1_rect   # Seleccionar la imagen 
                    offset21 = event.pos[0] - caballo_negro1_rect.x, event.pos[1] - caballo_negro1_rect.y
                elif alfil_negro1_rect.collidepoint(event.pos):
                    selected = alfil_negro1_rect   # Seleccionar la imagen 
                    offset31 = event.pos[0] - alfil_negro1_rect.x, event.pos[1] - alfil_negro1_rect.y
                elif rey_negro_rect.collidepoint(event.pos):
                    selected = rey_negro_rect   # Seleccionar la imagen 
                    offset4 = event.pos[0] - rey_negro_rect.x, event.pos[1] - rey_negro_rect.y
                elif reina_negro_rect.collidepoint(event.pos):
                    selected = reina_negro_rect   # Seleccionar la imagen 
                    offset5 = event.pos[0] - reina_negro_rect.x, event.pos[1] - reina_negro_rect.y
                elif peon_negro1_rect.collidepoint(event.pos):
                    selected = peon_negro1_rect   # Seleccionar la imagen 
                    offset61 = event.pos[0] - peon_negro1_rect.x, event.pos[1] - peon_negro1_rect.y
                elif peon_negro2_rect.collidepoint(event.pos):
                    selected = peon_negro2_rect   # Seleccionar la imagen 
                    offset62 = event.pos[0] - peon_negro2_rect.x, event.pos[1] - peon_negro2_rect.y
                elif peon_negro3_rect.collidepoint(event.pos):
                    selected = peon_negro3_rect   # Seleccionar la imagen 
                    offset63 = event.pos[0] - peon_negro3_rect.x, event.pos[1] - peon_negro3_rect.y
                elif peon_negro4_rect.collidepoint(event.pos):
                    selected = peon_negro4_rect   # Seleccionar la imagen 
                    offset64 = event.pos[0] - peon_negro4_rect.x, event.pos[1] - peon_negro4_rect.y
                elif peon_negro5_rect.collidepoint(event.pos):
                    selected = peon_negro5_rect   # Seleccionar la imagen 
                    offset65 = event.pos[0] - peon_negro5_rect.x, event.pos[1] - peon_negro5_rect.y
                elif peon_negro6_rect.collidepoint(event.pos):
                    selected = peon_negro6_rect   # Seleccionar la imagen 
                    offset66 = event.pos[0] - peon_negro6_rect.x, event.pos[1] - peon_negro6_rect.y
                elif peon_negro7_rect.collidepoint(event.pos):
                    selected = peon_negro7_rect   # Seleccionar la imagen 
                    offset67 = event.pos[0] - peon_negro7_rect.x, event.pos[1] - peon_negro7_rect.y
                elif peon_negro8_rect.collidepoint(event.pos):
                    selected = peon_negro8_rect   # Seleccionar la imagen 
                    offset68 = event.pos[0] - peon_negro8_rect.x, event.pos[1] - peon_negro8_rect.y
                elif torre_blanco_rect.collidepoint(event.pos):
                    selected = torre_blanco_rect   # Seleccionar la imagen 
                    offset7 = event.pos[0] - torre_blanco_rect.x, event.pos[1] - torre_blanco_rect.y
                elif caballo_blanco_rect.collidepoint(event.pos):
                    selected = caballo_blanco_rect   # Seleccionar la imagen 
                    offset8 = event.pos[0] - caballo_blanco_rect.x, event.pos[1] - caballo_blanco_rect.y
                elif alfil_blanco_rect.collidepoint(event.pos):
                    selected = alfil_blanco_rect   # Seleccionar la imagen 
                    offset9 = event.pos[0] - alfil_blanco_rect.x, event.pos[1] - alfil_blanco_rect.y
                elif torre_blanco1_rect.collidepoint(event.pos):
                    selected = torre_blanco1_rect   # Seleccionar la imagen 
                    offset71 = event.pos[0] - torre_blanco1_rect.x, event.pos[1] - torre_blanco1_rect.y
                elif caballo_blanco1_rect.collidepoint(event.pos):
                    selected = caballo_blanco1_rect   # Seleccionar la imagen 
                    offset81 = event.pos[0] - caballo_blanco1_rect.x, event.pos[1] - caballo_blanco1_rect.y
                elif alfil_blanco1_rect.collidepoint(event.pos):
                    selected = alfil_blanco1_rect   # Seleccionar la imagen 
                    offset91 = event.pos[0] - alfil_blanco1_rect.x, event.pos[1] - alfil_blanco1_rect.y
                elif rey_blanco_rect.collidepoint(event.pos):
                    selected = rey_blanco_rect    # Seleccionar la imagen 
                    offset10 = event.pos[0] - rey_blanco_rect.x, event.pos[1] - rey_blanco_rect.y
                elif reina_blanco_rect.collidepoint(event.pos):
                    selected = reina_blanco_rect    # Seleccionar la imagen 
                    offset11 = event.pos[0] - reina_blanco_rect.x, event.pos[1] - reina_blanco_rect.y
                elif peon_blanco1_rect.collidepoint(event.pos):
                    selected = peon_blanco1_rect    # Seleccionar la imagen 
                    offset121 = event.pos[0] - peon_blanco1_rect.x, event.pos[1] - peon_blanco1_rect.y
                elif peon_blanco2_rect.collidepoint(event.pos):
                    selected = peon_blanco2_rect    # Seleccionar la imagen 
                    offset122 = event.pos[0] - peon_blanco2_rect.x, event.pos[1] - peon_blanco2_rect.y
                elif peon_blanco3_rect.collidepoint(event.pos):
                    selected = peon_blanco3_rect    # Seleccionar la imagen 
                    offset123 = event.pos[0] - peon_blanco3_rect.x, event.pos[1] - peon_blanco3_rect.y
                elif peon_blanco4_rect.collidepoint(event.pos):
                    selected = peon_blanco4_rect    # Seleccionar la imagen 
                    offset124 = event.pos[0] - peon_blanco4_rect.x, event.pos[1] - peon_blanco4_rect.y
                elif peon_blanco5_rect.collidepoint(event.pos):
                    selected = peon_blanco5_rect    # Seleccionar la imagen 
                    offset125 = event.pos[0] - peon_blanco5_rect.x, event.pos[1] - peon_blanco5_rect.y
                elif peon_blanco6_rect.collidepoint(event.pos):
                    selected = peon_blanco6_rect    # Seleccionar la imagen 
                    offset126 = event.pos[0] - peon_blanco6_rect.x, event.pos[1] - peon_blanco6_rect.y
                elif peon_blanco7_rect.collidepoint(event.pos):
                    selected = peon_blanco7_rect    # Seleccionar la imagen 
                    offset127 = event.pos[0] - peon_blanco7_rect.x, event.pos[1] - peon_blanco7_rect.y
                elif peon_blanco8_rect.collidepoint(event.pos):
                    selected = peon_blanco8_rect    # Seleccionar la imagen 
                    offset128 = event.pos[0] - peon_blanco8_rect.x, event.pos[1] - peon_blanco8_rect.y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Botón izquierdo del ratón
                selected = None  # Desactivar la selección

    if selected == torre_negro_rect :
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        torre_negro_rect.x, torre_negro_rect.y = pygame.mouse.get_pos()[0] - offset1[0], pygame.mouse.get_pos()[1] - offset1[1]
    elif selected == torre_negro1_rect :
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        torre_negro1_rect.x, torre_negro1_rect.y = pygame.mouse.get_pos()[0] - offset11[0], pygame.mouse.get_pos()[1] - offset11[1]
    elif selected == caballo_negro_rect :
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        caballo_negro_rect.x, caballo_negro_rect.y = pygame.mouse.get_pos()[0] - offset2[0], pygame.mouse.get_pos()[1] - offset2[1]
    elif selected == alfil_negro_rect :
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        alfil_negro_rect.x, alfil_negro_rect.y = pygame.mouse.get_pos()[0] - offset3[0], pygame.mouse.get_pos()[1] - offset3[1]
    elif selected == caballo_negro1_rect :
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        caballo_negro1_rect.x, caballo_negro1_rect.y = pygame.mouse.get_pos()[0] - offset21[0], pygame.mouse.get_pos()[1] - offset21[1]
    elif selected == alfil_negro1_rect :
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        alfil_negro1_rect.x, alfil_negro1_rect.y = pygame.mouse.get_pos()[0] - offset31[0], pygame.mouse.get_pos()[1] - offset31[1]
    elif selected == rey_negro_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        rey_negro_rect.x, rey_negro_rect.y = pygame.mouse.get_pos()[0] - offset4[0], pygame.mouse.get_pos()[1] - offset4[1]
    elif selected == reina_negro_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        reina_negro_rect.x, reina_negro_rect.y = pygame.mouse.get_pos()[0] - offset5[0], pygame.mouse.get_pos()[1] - offset5[1]
    elif selected == peon_negro1_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_negro1_rect.x, peon_negro1_rect.y = pygame.mouse.get_pos()[0] - offset61[0], pygame.mouse.get_pos()[1] - offset61[1]
    elif selected == peon_negro2_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_negro2_rect.x, peon_negro2_rect.y = pygame.mouse.get_pos()[0] - offset62[0], pygame.mouse.get_pos()[1] - offset62[1]

    elif selected == peon_negro3_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_negro3_rect.x, peon_negro3_rect.y = pygame.mouse.get_pos()[0] - offset63[0], pygame.mouse.get_pos()[1] - offset63[1]

    elif selected == peon_negro4_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_negro4_rect.x, peon_negro4_rect.y = pygame.mouse.get_pos()[0] - offset64[0], pygame.mouse.get_pos()[1] - offset64[1]

    elif selected == peon_negro5_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_negro5_rect.x, peon_negro5_rect.y = pygame.mouse.get_pos()[0] - offset65[0], pygame.mouse.get_pos()[1] - offset65[1]

    elif selected == peon_negro6_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_negro6_rect.x, peon_negro6_rect.y = pygame.mouse.get_pos()[0] - offset66[0], pygame.mouse.get_pos()[1] - offset66[1]

    elif selected == peon_negro7_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_negro7_rect.x, peon_negro7_rect.y = pygame.mouse.get_pos()[0] - offset67[0], pygame.mouse.get_pos()[1] - offset67[1]

    elif selected == peon_negro8_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_negro8_rect.x, peon_negro8_rect.y = pygame.mouse.get_pos()[0] - offset68[0], pygame.mouse.get_pos()[1] - offset68[1]

    elif selected == torre_blanco_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        torre_blanco_rect.x, torre_blanco_rect.y = pygame.mouse.get_pos()[0] - offset7[0], pygame.mouse.get_pos()[1] - offset7[1]
    elif selected == caballo_blanco_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        caballo_blanco_rect.x, caballo_blanco_rect.y = pygame.mouse.get_pos()[0] - offset8[0], pygame.mouse.get_pos()[1] - offset8[1]
    elif selected == alfil_blanco_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        alfil_blanco_rect.x, alfil_blanco_rect.y = pygame.mouse.get_pos()[0] - offset9[0], pygame.mouse.get_pos()[1] - offset9[1]
    elif selected == torre_blanco1_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        torre_blanco1_rect.x, torre_blanco1_rect.y = pygame.mouse.get_pos()[0] - offset71[0], pygame.mouse.get_pos()[1] - offset7[1]
    elif selected == caballo_blanco1_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        caballo_blanco1_rect.x, caballo_blanco1_rect.y = pygame.mouse.get_pos()[0] - offset81[0], pygame.mouse.get_pos()[1] - offset81[1]
    elif selected == alfil_blanco1_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        alfil_blanco1_rect.x, alfil_blanco1_rect.y = pygame.mouse.get_pos()[0] - offset91[0], pygame.mouse.get_pos()[1] - offset91[1]

    elif selected == rey_blanco_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        rey_blanco_rect.x, rey_blanco_rect.y = pygame.mouse.get_pos()[0] - offset10[0], pygame.mouse.get_pos()[1] - offset10[1]
    elif selected == reina_blanco_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        reina_blanco_rect.x, reina_blanco_rect.y = pygame.mouse.get_pos()[0] - offset11[0], pygame.mouse.get_pos()[1] - offset11[1]
    elif selected == peon_blanco1_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_blanco1_rect.x, peon_blanco1_rect.y = pygame.mouse.get_pos()[0] - offset121[0], pygame.mouse.get_pos()[1] - offset121[1]
    elif selected == peon_blanco2_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_blanco2_rect.x, peon_blanco2_rect.y = pygame.mouse.get_pos()[0] - offset122[0], pygame.mouse.get_pos()[1] - offset122[1]
    elif selected == peon_blanco3_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_blanco3_rect.x, peon_blanco3_rect.y = pygame.mouse.get_pos()[0] - offset123[0], pygame.mouse.get_pos()[1] - offset123[1]
    elif selected == peon_blanco4_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_blanco4_rect.x, peon_blanco4_rect.y = pygame.mouse.get_pos()[0] - offset124[0], pygame.mouse.get_pos()[1] - offset124[1]
    elif selected == peon_blanco5_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_blanco5_rect.x, peon_blanco5_rect.y = pygame.mouse.get_pos()[0] - offset125[0], pygame.mouse.get_pos()[1] - offset125[1]
    elif selected == peon_blanco6_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_blanco6_rect.x, peon_blanco6_rect.y = pygame.mouse.get_pos()[0] - offset126[0], pygame.mouse.get_pos()[1] - offset126[1]
    elif selected == peon_blanco7_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_blanco7_rect.x, peon_blanco7_rect.y = pygame.mouse.get_pos()[0] - offset127[0], pygame.mouse.get_pos()[1] - offset127[1]
    elif selected == peon_blanco8_rect:
        # Obtener la posición actual del ratón y aplicar el desplazamiento
        peon_blanco8_rect.x, peon_blanco8_rect.y = pygame.mouse.get_pos()[0] - offset128[0], pygame.mouse.get_pos()[1] - offset128[1]

    screen.fill(CREAM) #color de fondo
    
    ##ZONA DE DIBUJO
    for x in range(0,480,120):
        pygame.draw.rect(screen, BROWN, (x+60,0,60,60))
    for x in range(0,480,120):
        pygame.draw.rect(screen, BROWN, (x,60,60,60))
    for x in range(0,480,120):
        pygame.draw.rect(screen, BROWN, (x+60,120,60,60))   
    for x in range(0,480,120):
        pygame.draw.rect(screen, BROWN, (x,180,60,60))
    for x in range(0,480,120):
        pygame.draw.rect(screen, BROWN, (x+60,240,60,60))
    for x in range(0,480,120):
        pygame.draw.rect(screen, BROWN, (x,300,60,60))
    for x in range(0,480,120):
        pygame.draw.rect(screen, BROWN, (x+60,360,60,60))   
    for x in range(0,480,120):
        pygame.draw.rect(screen, BROWN, (x,420,60,60))
    
    
    screen.blit(torre_negro, torre_negro_rect)
    screen.blit(caballo_negro, caballo_negro_rect)
    screen.blit(alfil_negro, alfil_negro_rect)
    screen.blit(rey_negro, rey_negro_rect)
    screen.blit(reina_negro, reina_negro_rect)
    screen.blit(alfil_negro1, alfil_negro1_rect)
    screen.blit(caballo_negro1, caballo_negro1_rect)
    screen.blit(torre_negro1, torre_negro1_rect)
    screen.blit(peon_negro1, peon_negro1_rect)
    screen.blit(peon_negro2, peon_negro2_rect)
    screen.blit(peon_negro3, peon_negro3_rect)
    screen.blit(peon_negro4, peon_negro4_rect)
    screen.blit(peon_negro5, peon_negro5_rect)
    screen.blit(peon_negro6, peon_negro6_rect)
    screen.blit(peon_negro7, peon_negro7_rect)
    screen.blit(peon_negro8, peon_negro8_rect)

    screen.blit(torre_blanco, torre_blanco_rect)
    screen.blit(caballo_blanco, caballo_blanco_rect)
    screen.blit(alfil_blanco, alfil_blanco_rect)
    screen.blit(rey_blanco, rey_blanco_rect)
    screen.blit(reina_blanco, reina_blanco_rect)
    screen.blit(alfil_blanco, alfil_blanco1_rect)
    screen.blit(caballo_blanco1, caballo_blanco1_rect)
    screen.blit(torre_blanco1, torre_blanco1_rect)
    screen.blit(peon_blanco1, peon_blanco1_rect)
    screen.blit(peon_blanco2, peon_blanco2_rect)
    screen.blit(peon_blanco3, peon_blanco3_rect)
    screen.blit(peon_blanco4, peon_blanco4_rect)
    screen.blit(peon_blanco5, peon_blanco5_rect)
    screen.blit(peon_blanco6, peon_blanco6_rect)
    screen.blit(peon_blanco7, peon_blanco7_rect)
    screen.blit(peon_blanco8, peon_blanco8_rect)
    ##
    pygame.display.flip() #actualizar pantalla
    clock.tick(60)

pygame.quit()



