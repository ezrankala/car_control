import pygame
# import settings

class Car():
    def __init__(self, carSettings, screen):
        self.carSettings =  carSettings
        self.screen = screen

        #load up the car
        self.myCar = pygame.image.load("images/resizedRedCar.png")

        # get the rectangle of the car
        self.rect = self.myCar.get_rect()

        #get the properties of the entire screen
        self.Road = screen.get_rect()

        # Place the car at the bottom center of the road
        self.rect.centerx = self.Road.centerx
        self.rect.bottom = self.Road.bottom

        # Store a decimal value for the car's center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Create flags for continious movements
        self.movingRight = False
        self.movingLeft = False
        self.movingUp = False
        self.movingDown = False

    
    def update(self):
        """Updates the car position once clicked"""
        if self.movingRight and (self.rect.right < self.Road.right):
            self.centerx += self.carSettings.carSpeed
        
        if self.movingLeft and (self.rect.left > 0):
            self.centerx -= self.carSettings.carSpeed
        
        if self.movingUp and (self.rect.top > 0):
            self.centery -= self.carSettings.carSpeed
        
        if self.movingDown and (self.rect.bottom < self.Road.bottom):
             self.centery += self.carSettings.carSpeed

        ## Update the rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def drawMyCar(self):
        # Draw the car (make it appear on screen)
        self.screen.blit(self.myCar, self.rect)

