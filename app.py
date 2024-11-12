import pygame
import pygame_widgets
import sys
import math
from robot_arm import compute_robot_angles
from utils import draw_robot, draw_grid
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

# Iniciar Pygame
pygame.init()

# Configurar display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Kinematics of a Robot Arm")
fac_size = 100

# Definir colores
WHITE = (255, 255, 255)

# Dibujar sliders
q0_slider = Slider(screen, 50, height-100, 200, 20, min=0, max=2*math.pi, step=0.01)
q1_slider = Slider(screen, 50, height-50, 200, 20, min=0, max=2*math.pi, step=0.01)

# Texto de los angulos
q0_text = TextBox(screen, 270, height-100, 50, 30)
q1_text = TextBox(screen, 270, height-50, 50, 30)

# Texto de la posicion del click
x_text = TextBox(screen, width-80, height-100, 50, 30)
y_text = TextBox(screen, width-80, height-50, 50, 30)

# Parametros del robot
a0, a1 = 1, 1
x, y = None, None
q0, q1 = 0, 0
is_computed = False
x_t, y_t = 0, 0

# Main loop
running = True
while running:
    # Event handling
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtener la posicion del click
            x, y = pygame.mouse.get_pos()
            x_t, y_t = x, y
            x = (x - width // 2) / fac_size
            y = (y - height // 2) / fac_size
            x_text.setText(str(x))
            y_text.setText(str(y))
            is_computed = False
       
    #Update values from sliders
    # q0 = q0_slider.getValue()
    # q1 = q1_slider.getValue()

    # get angles from inverse kinematics function
    if x is not None and y is not None and not is_computed:
        print(f"moving to point {x}, {y}...")
        try:
            q0, q1 = compute_robot_angles(x, y, a0, a1)
        except TypeError as e:
            print("posicion invalida amigo!!!!☠️☠️☠️☠️☠️")
            phi = math.atan2(y, x)
            print(phi)
            # hack para evitar numeros complejos
            l = a0 + a1 - (a0 + a1) * 0.01
            x_hat = l * math.cos(phi)
            y_hat = l * math.sin(phi)
            print(x_hat, y_hat)
            q0, q1 = compute_robot_angles(x_hat, y_hat, a0, a1)

        print(f"angles computed: {q0}, {q1}")
        is_computed = True
    # Update text boxes to show slider values
    q0_text.setText(str(q0))
    q1_text.setText(str(q1))

    # Fill the screen with white
    screen.fill(WHITE)
    draw_grid(screen, 50)
    pygame.draw.circle(screen, (255,0,0), (x_t,y_t), 9, 3)
    draw_robot(screen, q0, q1, a0, a1, fac_size)

    # Draw the sliders and text boxes
    pygame_widgets.update(events)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
