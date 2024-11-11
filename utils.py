import math
from robot_arm import compute_positions
import pygame

BLUE = (0, 0, 255)

def convert_points(points, fac_x, fac_y, offset_x, offset_y):
    pixel_points = []
    for x,y in points:
        new_point = (x*fac_x+offset_x, y*fac_y+offset_y)
        pixel_points.append(new_point)
    return pixel_points
    

def draw_robot(screen, q0, q1, a0, a1, fac_size):
    width, height = screen.get_size()
    points = compute_positions(q0, q1, a0, a1)
    pixel_points = convert_points(points, fac_size, fac_size, width//2, height//2)
    pygame.draw.lines(screen, BLUE, False, pixel_points, 5)

def draw_grid(screen, cell_size):
    width, height = screen.get_size()
    #draw axis
    pygame.draw.line(screen, (0,0,0), (0, height/2),(width, height/2), 2)
    pygame.draw.line(screen, (0,0,0), (width/2, 0),(width/2, height), 2)
    #dibujar lineas verticales
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, (20,20,20), (x,0), (x,height), 1)
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, (20,20,20), (0,y), (width,y), 1)


