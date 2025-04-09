import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import time

def initialCanvas(screen):
    pygame.draw.rect(screen, [0,0,0], (0,600,200,200))
    for i in range(8):
        for j in range(6):
            r=random.randint(0,255)
            g=random.randint(0,255)
            b=random.randint(0,255)
            pygame.draw.rect(screen, [r,g,b], (i*100, j*100, 100,100))

    pygame.display.flip()

def drawShapes(screen, width, height):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    points = []
#    numOfPoints = random.randint(3,5)
#    for i in range(numOfPoints):
#        x = random.randint(0,width)
#        y = random.randint(0,height)
#        points.append((x,y))
#    pygame.draw.polygon(screen, [r,g,b], points)
    x = random.randint(0, width)
    y = random.randint(0, height)
    w = random.randint(1, width)
    h = random.randint(1, height-y)
    pygame.draw.rect(screen, [r,g,b], (x,y,w,h))
    pygame.display.flip()

def toFind(screen, width, height):
    displaySurface = pygame.display.get_surface()
    length = random.randint(50,200)
    x = random.randint(0,width-length)
    y = random.randint(0,height-length)
    sqRect = pygame.Rect(x,y,length,length)

    sqSubsurface = pygame.Surface((length,length))
    sqSubsurface.blit(displaySurface, (0,0), sqRect)


    screen.blit(sqSubsurface, (100-0.5*length,700-0.5*length))
    pygame.display.flip()

def main():
    pygame.init()
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    screen.fill("white")
    pygame.display.flip()

    # virtual height
    height = 600
    
    initialCanvas(screen)
    #numOfShapes = 10
    #for i in range(numOfShapes):
    #    drawShapes(screen, width, height)
    toFind(screen, width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    pygame.quit()

main()