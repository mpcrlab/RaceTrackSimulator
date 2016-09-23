import constants #my constants file (constants.py)
import pygame

class Rover():
    def __init__(self):
        self.direction = "up"
        self.lead_x_change = 0
        self.lead_y_change = 0
        self.lead_x = 0
        self.lead_y = 0
        self.FOV = None

    def canMove(self, newX, newY, obstacles):
        newX = int(newX)
        newY = int(newY)
        i = 0
        for obstacle in obstacles:
            if obstacle.x == newX and obstacle.y == newY:
                print "hit a wall"
                return False
            i += 1
        return True

    def rotateImg(self, img):
        roverimg = img
        if self.direction == "right":
            roverimg = pygame.transform.rotate(img, 270)
        if self.direction == "left":
            roverimg = pygame.transform.rotate(img, 90)
        if self.direction == "up":
            roverimg = img
        if self.direction == "down":
            roverimg = pygame.transform.rotate(img, 180)
        return roverimg

    def drawFOV(self):
        fov_color = (23, 100, 255, 50)
        start_x = 0
        start_y = 0
        if self.direction == "up" or self.direction == "down":
            width_blocks = 5
            height_blocks = 2
            width = constants.BLOCK_SIZE * width_blocks
            height = constants.BLOCK_SIZE * height_blocks
            if self.direction == "up":
                start_x = self.lead_x - (2 * constants.BLOCK_SIZE)
                start_y = self.lead_y - (2 * constants.BLOCK_SIZE)
            elif self.direction == "down":
                start_x = self.lead_x - (2 * constants.BLOCK_SIZE)
                start_y = self.lead_y + constants.BLOCK_SIZE
        elif self.direction == "left" or self.direction == "right":
            width_blocks = 2
            height_blocks = 5
            width = constants.BLOCK_SIZE * width_blocks
            height = constants.BLOCK_SIZE * height_blocks
            if self.direction == "right":
                start_x = self.lead_x + (constants.BLOCK_SIZE)
                start_y = self.lead_y - (2 * constants.BLOCK_SIZE)
            if self.direction == "left":
                start_x = self.lead_x - (2 * constants.BLOCK_SIZE)
                start_y = self.lead_y - (2 *constants.BLOCK_SIZE)

        gameDisplay = pygame.display.get_surface()
        rect = pygame.Surface((width,height), pygame.SRCALPHA, 32)
        rect.fill(fov_color)
        gameDisplay.blit(rect, (start_x, start_y))