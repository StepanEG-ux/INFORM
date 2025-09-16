import pygame
from pygame.draw import rect,polygon,circle,line,arc
pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 400))

rect(screen, (0, 0, 255), (0, 300, 600, 100), 5)
rect(screen, (0, 255, 255), (0, 150, 600, 150), 5)
rect(screen, (255, 0, 255), (0, 0, 600, 150), 5)
circle(screen, (255, 0, 255), (500,55),50,50)

circle(screen, (255, 255, 255), (250,55),25,25)
circle(screen, (255, 255, 255), (225,57),25,25)
circle(screen, (255, 255, 255), (185,54),25,25)
circle(screen, (255, 255, 255), (270,75),25,25)
circle(screen, (255, 255, 255), (245,80),25,25)
circle(screen, (255, 255, 255), (230,75),25,25)
circle(screen, (255, 255, 255), (205,80),25,25)

rect(screen, (0, 0, 255), (300, 225, 200, 30), 5)
polygon(screen,(0,0,255),[(500,225),(545,225),(500,255)],5)
rect(screen, (255, 0, 0), (370, 95, 10, 130), 2)
polygon(screen,(0,255,0),[(380,95),(410,160),(380,225),(460,160),(380,95)],5)
rect(screen, (255, 66, 90), (100, 250, 5, 130), 2)
polygon(screen,(0,255,0),[(102.5,255),(25,280),(180,280)],5)
line(screen,(0,0,255),[(102.5,255),(50,180)],1)


































pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()