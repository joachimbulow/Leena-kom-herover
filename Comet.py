import random

class Comet():
    def __init__(self, size, x, y):
        self.direction = random.randint(1, 6)
        self.size = size
        self.x = x
        self.y = y
        self.vel = 1

    def updateCoordinates(self, width, height):
        if(self.direction == 1):
            self.x += self.vel
            self.y += self.vel
        elif(self.direction == 2):
            self.x -= self.vel
            self.y -= self.vel
        elif (self.direction == 3):
            self.x += self.vel
            self.y -= self.vel
        elif (self.direction == 4):
            self.x -= self.vel
            self.y += self.vel
        elif (self.direction == 5):
            self.x += self.vel
        elif (self.direction == 6):
            self.y += self.vel
        # To make it wrap
        self.x = self.x % width
        self.y = self.y % height