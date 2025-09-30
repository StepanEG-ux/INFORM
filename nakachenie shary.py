import pygame
from pygame.draw import *
from pygame.font import SysFont
from random import randint
pygame.init()
points=0
FPS = 6
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''рисует новый шарик '''
    global x,y,r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
def collapse(b,pos):
    x,y,r,color,dx,dy =b
    return(x-pos[0])**2 + (y-pos[1]**2)<r**2
    
def click(event):
    print(x, y, r)
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False
b=new_ball()
points=0
frames=0
next_ball=60

while not finished:
    frames+=1
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen.get_at(event.pos) != (0,0,0,255):
                points +=1
                b=[new_ball(),new_ball()]
                next_ball -=5
                frames = 0

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
