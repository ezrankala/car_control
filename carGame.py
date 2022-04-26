import pygame
# import sys
from car import Car
import roadDisplay as rd
import gameFunctions as gf
import settings


def runGame():
    #Initialize the game 
    pygame.init()

    # Load your settings 
    carSettings = settings.Settings( 600, 700, 3, )

    # Give dimensions and color of the screen ( a road in this case) 
    displaySize = (carSettings.screenWidth, carSettings.screenHeight)

    # Give the road screen life dimensions and colors
    roadSide, roadWhiteMarks, road, roadWhiteMarks2, roadSide2, roadColor, \
        roadsideColor, yellows = rd.roadStructure()


    roadScreen = pygame.display.set_mode((displaySize))
    pygame.display.set_caption("Car control Game")

    # Place the car on the screen
    mycar = Car(carSettings, roadScreen)

    while True:
        gf.checkEvents(mycar)
        mycar.update()

        
        gf.updateScreen(roadSide, roadWhiteMarks, road, roadWhiteMarks2, \
            roadSide2, roadColor, roadsideColor, yellows, roadScreen, mycar)
        
        pygame.display.flip()

    # mycar.drawMyCar()

       
runGame()

