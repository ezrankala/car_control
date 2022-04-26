import pygame

class RoadDisplay():
    def __init__(self, roadColor, sideMarkingColor, offroadColor):
        self.roadColor = roadColor
        self.sideMarkingColor = sideMarkingColor
        self.offroadColor = offroadColor

        
        

def roadStructure():
    #Road rectangles (sides and road)
    roadSide = (0, 0, 120, 700)
    roadWhiteMarks = (120, 0, 130, 700)
    road = (130, 0, 470, 700)
    roadWhiteMarks2 = (470, 0, 480, 700)
    roadSide2 = (480, 0, 600, 700)
    

    roadColor = pygame.Color(41,41,40)
    roadsideColor = pygame.Color(10, 150, 50)
    yellows = pygame.Color(250, 220, 70)
    return roadSide,roadWhiteMarks,road,roadWhiteMarks2,roadSide2,roadColor,\
        roadsideColor,yellows

def roadLife(roadSide, roadWhiteMarks, road, roadWhiteMarks2, roadSide2, \
    roadColor, roadsideColor, yellows, roadScreen):
    roadScreen.fill(roadsideColor, roadSide) 
    roadScreen.fill(yellows, roadWhiteMarks)
    roadScreen.fill(roadColor, road)
    roadScreen.fill(yellows, roadWhiteMarks2)
    roadScreen.fill(roadsideColor, roadSide2)
