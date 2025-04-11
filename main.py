import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import time

def initialCanvas(screen):
    pygame.draw.rect(screen, [0,0,0], (0,600,200,200))
    global screenArray
    screenArray = []
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
    length = random.randint(100,195)
    x = random.randint(0,width-length)
    y = random.randint(0,height-length)
    sqRect = pygame.Rect(x,y,length,length)

    sqSubsurface = pygame.Surface((length,length))
    sqSubsurface.blit(displaySurface, (0,0), sqRect)

    global blitVals
    blitVals = []
    blitVals.append(sqSubsurface)
    blitVals.append((100-0.5*length,700-0.5*length))
    global xToFind, yToFind, lengthToFind
    xToFind = x
    yToFind = y
    lengthToFind = length

def drawSelect(screen, startPos, currentPos):
    w = currentPos[0]-startPos[0]
    h = currentPos[1]-startPos[1]
    global startX, startY
    startX = startPos[0]
    startY = startPos[1]
    if w == 0:
        w = 1
    elif w < 0:
        startX = currentPos[0]
    if h == 0:
        h = 1
    elif h < 0:
        startY = currentPos[1]

    selectBox = pygame.Surface((abs(w), abs(h)), pygame.SRCALPHA)
    selectBox.set_alpha(128)
    selectBox.fill((50,200,255))
    screen.blit(selectBox, (startX, startY))
    pygame.display.flip()

def redraw(screen):
    screen.fill("black")
    global screenArray
    pygame.draw.rect(screen, [0,0,0], (0,600,200,200))
    for i in screenArray:
        colour = i[0]
        pos_s = i[1]
        pygame.draw.rect(screen, colour, pos_s)
    screen.blit(blitVals[0], blitVals[1])
    pygame.font.init()
    myFont = pygame.font.SysFont("Courier", 100)
    textSurface = myFont.render("ZoomIn_g", False, (0,255,0))
    screen.blit(textSurface, (250, 640))
    pygame.display.flip()

def checkSelection(screen):
    global startX, startY
    if (xToFind - 50) <= startX <= (xToFind + 50):
        if (yToFind - 50) <= startY <= (yToFind + 50):
            if (lengthToFind - 50) <= abs(currentPos[0] - startPos[0]) <= (lengthToFind + 50):
                if (lengthToFind - 50) <= abs(currentPos[1] - startPos[1]) <= (lengthToFind + 50):
                    initialCanvas(screen)
                    global isFound
                    isFound = True

def main():
    pygame.init()
    global width, height
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    screen.fill("black")
    pygame.display.flip()

    global isFound
    isFound = False

    # virtual height
    height = 600

    global screenArray
    screenArray = []
    initialCanvas(screen)
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
    global startX, startY
    startX = startPos[0]
    startY = startPos[1]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if isFound:
                isFound = False
                toFind(screen, width, height)
            if pygame.mouse.get_pressed()[0] and isJustClicked == False:
                isJustClicked = True
                startPos = pygame.mouse.get_pos()
                drawSelect(screen, startPos, startPos)
            elif pygame.mouse.get_pressed()[0]:
                currentPos = pygame.mouse.get_pos()
                redraw(screen)
                drawSelect(screen, startPos, currentPos)
            if not(pygame.mouse.get_pressed()[0]):
                checkSelection(screen)
                startPos = pygame.mouse.get_pos()
                currentPos = pygame.mouse.get_pos()
                redraw(screen)
                isJustClicked = False

    pygame.quit()

main()