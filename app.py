import pygame
import pygame_widgets
import sys
import math
from robot_arm import compute_positions
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic Pygame Application")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

q0_slider = Slider(screen, 50, 500, 200, 20, min=0, max=2*math.pi, step=0.01)
q1_slider = Slider(screen, 50, 550, 200, 20, min=0, max=2*math.pi, step=0.01)

q0_text = TextBox(screen, 270, 500, 50, 20)
q1_text = TextBox(screen, 270, 550, 50, 20)

def convert_points(points, fac_x, fac_y):
    pixel_points = []
    for x,y in points:
        new_point = (x*fac_x, y*fac_y)
        pixel_points.append(new_point)
    return pixel_points
    
def draw_robot(screen, q0, q1):
    points = compute_positions(q0, q1)
    pixel_points = convert_points(points, 100, 100)
    pixel_points.insert(0, (0,0))
    pygame.draw.lines(screen, BLUE, False, pixel_points, 5)


# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Update values from sliders
    q0 = q0_slider.getValue()
    q1 = q1_slider.getValue()

    # Update text boxes to show slider values
    q0_text.setText(str(q0))
    q1_text.setText(str(q1))

    # Fill the screen with white
    screen.fill(WHITE)
    draw_robot(screen, q0, q1)

    # Draw the sliders and text boxes
    pygame_widgets.update(pygame.event.get())
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
