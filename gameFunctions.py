import pygame
import sys
import roadDisplay as rd


def checkEvents(mycar):
    for event in pygame.event.get():
            # Observe events with the event function
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            keyDownEvents(mycar, event)
        
        elif event.type == pygame.KEYUP:
            keyUpEvents(mycar, event)

def keyDownEvents(mycar, event):
    if event.key == pygame.K_q:
        pygame.quit()
        sys.exit()

    if event.key == pygame.K_RIGHT:
        mycar.movingRight = True

    if event.key == pygame.K_LEFT:
        mycar.movingLeft = True

    if event.key == pygame.K_UP:
        mycar.movingUp = True

    if event.key == pygame.K_DOWN:
        mycar.movingDown = True

def keyUpEvents(mycar, event):
    if event.key == pygame.K_q:
        pygame.quit()
        sys.exit()

    if event.key == pygame.K_RIGHT:
        mycar.movingRight = False

    if event.key == pygame.K_LEFT:
        mycar.movingLeft = False

    if event.key == pygame.K_UP:
        mycar.movingUp = False

    if event.key == pygame.K_DOWN:
        mycar.movingDown = False

def updateScreen(roadSide, roadWhiteMarks, road, roadWhiteMarks2, roadSide2, \
    roadColor, roadsideColor, yellows, roadScreen, mycar):
    # Use the dimensions and color to give the road life!
    rd.roadLife(roadSide, roadWhiteMarks, road, roadWhiteMarks2, roadSide2,\
        roadColor, roadsideColor, yellows, roadScreen)
    mycar.drawMyCar()