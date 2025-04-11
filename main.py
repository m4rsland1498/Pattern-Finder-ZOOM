import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import time

def initialCanvas(screen, screenArray):
    pygame.draw.rect(screen, [0,0,0], (0,600,200,200))
    for i in range(8):
        for j in range(6):
            r=random.randint(0,80)
            g=random.randint(120,255)
            b=random.randint(0,120)
            screenArray.append(([r,g,b], (i*100, j*100, 100,100)))

    pygame.display.flip()

def drawShapes(screen, width, height):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
#    points = []
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

    #blitVals = [sqSubsurface, (100-0.5*length,700-0.5*length)]
    blitVals.append(sqSubsurface)
    blitVals.append((100-0.5*length,700-0.5*length))
    global xToFind, yToFind, lengthToFind
    xToFind = x
    yToFind = y
    lengthToFind = length

def drawSelect(screen, startPos, currentPos):
    # v1
    w = currentPos[0]-startPos[0]
    if w < 1:
        w = 1
    h = currentPos[1]-startPos[1]
    if h < 1:
        h = 1
    #pygame.draw.rect(screen, [0,0,255], (startPos[0], startPos[1], w, h))
    #pygame.display.flip()

    # v2
    selectBox = pygame.Surface((w, h), pygame.SRCALPHA)
    selectBox.set_alpha(128)
    selectBox.fill((50,200,255))
    screen.blit(selectBox, (startPos[0], startPos[1]))
    pygame.display.flip()

def redraw(screen, screenArray):
    screen.fill("white")
    pygame.draw.rect(screen, [0,0,0], (0,600,200,200))
    for i in screenArray:
        colour = i[0]
        pos_s = i[1]
        pygame.draw.rect(screen, colour, pos_s)
    screen.blit(blitVals[0], blitVals[1])
    pygame.display.flip()

def checkSelection():
    if (xToFind - 50) <= startPos[0] <= (xToFind + 50):
        if (yToFind - 50) <= startPos[1] <= (yToFind + 50):
            if (lengthToFind - 50) <= (currentPos[0] - startPos[0]) <= (lengthToFind + 50):
                if (lengthToFind - 50) <= (currentPos[1] - startPos[1]) <= (lengthToFind + 50):
                    print("Found!")

def main():
    pygame.init()
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    screen.fill("white")
    pygame.display.flip()

    # virtual height
    height = 600

    screenArray = []
    initialCanvas(screen, screenArray)
    for i in screenArray:
        colour = i[0]
        pos_s = i[1]
        pygame.draw.rect(screen, colour, pos_s)
    #numOfShapes = 10
    #for i in range(numOfShapes):
    #    drawShapes(screen, width, height)
    global blitVals
    blitVals = []
    toFind(screen, width, height)
    screen.blit(blitVals[0], blitVals[1])
    pygame.display.flip()

    running = True
    isJustClicked = False
    global startPos, currentPos
    startPos = pygame.mouse.get_pos()
    currentPos = pygame.mouse.get_pos()
    print(startPos)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pressed()[0] and isJustClicked == False:
                isJustClicked = True
                startPos = pygame.mouse.get_pos()
                drawSelect(screen, startPos, startPos)
            elif pygame.mouse.get_pressed()[0]:
                currentPos = pygame.mouse.get_pos()
                redraw(screen, screenArray)
                drawSelect(screen, startPos, currentPos)
            if not(pygame.mouse.get_pressed()[0]):
                checkSelection()
                startPos = pygame.mouse.get_pos()
                currentPos = pygame.mouse.get_pos()
                redraw(screen, screenArray)
                isJustClicked = False


    pygame.quit()

main()