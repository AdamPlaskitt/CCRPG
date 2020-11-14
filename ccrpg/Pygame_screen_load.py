import pygame
import time
import sys

FPS = 15
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELLSIZE = 20
assert WINDOW_WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOW_HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOW_WIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOW_HEIGHT / CELLSIZE)
screen = pygame.display.set_mode((0, 0))


#           R    G    B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BACKGROUND_COLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption('test')

screen.fill(WHITE)
time.sleep(2)
pygame.quit()
sys.exit()
