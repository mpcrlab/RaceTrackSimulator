import constants #my constants file (constants.py)
import pygame
from Rover import *
from Obstacle import *
class Simulation():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.gameDisplay = pygame.display.set_mode((constants.DISPLAY_WIDTH,constants.DISPLAY_HEIGTH))
        pygame.display.set_caption('RaceTrackSimulator')
        self.img = pygame.image.load('car.png')
        self.done = False
        self.rover = Rover()
        self.obstacles = []
        self.run()

    def run(self):
        self.get_initial_rover_position()
        while not self.done or self.outOfBounds():
            self.keyboardEventHandeling()
            self.rover.lead_x, self.rover.lead_y = self.getNextPosition()
            self.updateScreen()
        self.endSession()

    def loadWorld(self):
        lines = open('worlds/world.txt', 'r')
        world = []
        for line in lines:
            world.append(line)
        return world

    def pixelizeWorld(self):
        world = self.loadWorld()
        self.obstacles = []
        y = 0
        x = 0
        for lines in world:
            for pixel in lines:
                if pixel == 'o':
                    obstacle = Obstacle()
                    obstacle.x = round(x * constants.BLOCK_SIZE / constants.BLOCK_SIZE) * constants.BLOCK_SIZE
                    obstacle.y = round(y * constants.BLOCK_SIZE / constants.BLOCK_SIZE) * constants.BLOCK_SIZE
                    gameDisplay = pygame.display.get_surface()
                    rect = (obstacle.x, obstacle.y, constants.BLOCK_SIZE, constants.BLOCK_SIZE)
                    pygame.draw.rect(gameDisplay, constants.BLACK, rect)
                    self.obstacles.append(obstacle)
                x += 1
            y += 1
            x = 0

    def get_initial_rover_position(self):
        world = self.loadWorld()
        y = 0
        x = 0
        for lines in world:
            for pixel in lines:
                if pixel == 'x':
                    self.rover.lead_x = round(x * constants.BLOCK_SIZE / constants.BLOCK_SIZE) * constants.BLOCK_SIZE
                    self.rover.lead_y = round(y * constants.BLOCK_SIZE / constants.BLOCK_SIZE) * constants.BLOCK_SIZE
                x += 1
            y += 1
            x = 0
    def getNextPosition(self):
        new_x = self.rover.lead_x + self.rover.lead_x_change
        new_y = self.rover.lead_y + self.rover.lead_y_change
        if self.rover.canMove(new_x, new_y, self.obstacles):
            return new_x, new_y
        else:
            return self.rover.lead_x, self.rover.lead_y
    def endSession(self):
        self.done = True
        pygame.quit()
        quit()

    def outOfBounds(self):
        if self.rover.lead_x >= constants.DISPLAY_WIDTH or self.rover.lead_x < 0 or self.rover.lead_y >= constants.DISPLAY_HEIGTH or self.rover.lead_y < 0:
            self.done = True
            return True
        else:
            return False

    def updateScreen(self):
        self.gameDisplay.fill(constants.WHITE)
        self.pixelizeWorld()
        roverimg = self.rover.rotateImg(self.img)
        self.gameDisplay.blit(roverimg, [self.rover.lead_x, self.rover.lead_y, constants.BLOCK_SIZE, constants.BLOCK_SIZE])
        self.rover.drawFOV()
        pygame.display.update()
        self.clock.tick(constants.FPS)

    def keyboardEventHandeling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.rover.lead_x_change = -constants.BLOCK_SIZE
                    self.rover.lead_y_change = 0
                    self.rover.direction = "left"
                elif event.key == pygame.K_RIGHT:
                    self.rover.lead_x_change = constants.BLOCK_SIZE
                    self.rover.lead_y_change = 0
                    self.rover.direction = "right"
                elif event.key == pygame.K_UP:
                    self.rover.lead_y_change = -constants.BLOCK_SIZE
                    self.rover.lead_x_change = 0
                    self.rover.direction = "up"
                elif event.key == pygame.K_DOWN:
                    self.rover.lead_y_change = constants.BLOCK_SIZE
                    self.rover.lead_x_change = 0
                    self.rover.direction = "down"