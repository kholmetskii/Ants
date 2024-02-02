import pygame
import math
import random


pygame.init()


class Ant:
    def __init__(self, x, y):  # initializing the ant
        self.x = x  # x coordinate
        self.y = y  # y coordinate
        self.angle = random.uniform(0, 2 * math.pi)  # angle
        self.food = True if random.uniform(0, 2) > 1 else False  # availability of food
        self.yellow_flag = False  # indication of the cry of the yellow point
        self.blue_flag = False  # indication of the cry of the blue point
        self.yellow_ang = random.uniform(0, 2 * math.pi)  # the angle to the yellow point
        self.blue_ang = random.uniform(0, 2 * math.pi)  # the angle to the blue point
        self.yellow_dis_counter = 100  # yellow counter
        self.blue_dis_counter = 100  # blue counter

    def step(self):

        self.yellow_dis_counter += 0.1  # increase the counters
        self.blue_dis_counter += 0.1

        self.angle += random.uniform(-0.01, 0.01)  # slightly change the angle for natural trajectory

        if self.x < 10:
            self.x = 10
            self.angle += math.pi
        elif self.x > width - 10:
            self.x = width - 10
            self.angle += math.pi  # reflection conditions from walls
        if self.y < 10:
            self.y = 10
            self.angle += math.pi
        elif self.y > height - 10:
            self.y = height - 10
            self.angle += math.pi

        self.x += math.sin(self.angle)
        self.y += math.cos(self.angle)  # move

        cl = screen.get_at((int(self.x), int(self.y)))  # the color on which the ant is located

        if cl == (255, 255, 0):  # if ant on yellow point
            self.food = True  # take the food
            self.yellow_dis_counter = 0  # update the yellow counter
            self.yellow_flag = True  # need to shout out
            self.angle = self.blue_ang  # heading to the blue point

        if cl == (0, 255, 255):  # if ant on blue point
            self.food = False  # leave the food
            self.blue_dis_counter = 0  # update the blue counter
            self.blue_flag = True  # need to shout out
            self.angle = self.yellow_ang  # heading to the yellow point

        if self.yellow_flag:  # if need to shout out about yellow point
            self.yellow_cry()  # shout out about yellow point
            self.yellow_flag = False
            if not self.food:  # if ant does not have the food
                self.angle = self.yellow_ang  # heading to the yellow point

        if self.blue_flag:  # if need to shout out about blue point
            self.blue_cry()  # shout out about blue point
            self.blue_flag = False
            if self.food:  # if ant has the food
                self.angle = self.blue_ang  # heading to the blue point

    def render(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 1)  # drawing an ant

    def set_yellow_ang(self, x, y, d):  # direction to the ant that is 'closer' to the yellow point
        an = math.acos((y - self.y) / d)
        self.yellow_ang = an if x > self.x else 2 * math.pi - an

    def set_blue_ang(self, x, y, d):  # direction to the ant that is 'closer' to the blue point
        an = math.acos((y - self.y) / d)
        self.blue_ang = an if x > self.x else 2 * math.pi - an

    def yellow_cry(self):  # cry about yellow point
        for i in range(count):  # check every ant that is in the radius of the scream
            x, y = ants[i].x, ants[i].y
            d = math.dist((self.x, self.y), (x, y))
            if d <= dst:  # if it is
                if ants[i].yellow_dis_counter > self.yellow_dis_counter:  # check if the listening ant has larger counter
                    ants[i].set_yellow_ang(self.x, self.y, d)  # go to ant which is 'closer' to yellow point
                    ants[i].yellow_flag = True  # need to shout out
                    ants[i].yellow_dis_counter = self.yellow_dis_counter  # update yellow counter
                    pygame.draw.line(screen, (255, 255, 153), (self.x, self.y), (x, y), 1)  # drawing a line between the ants

    def blue_cry(self):  # cry about blue point
        for i in range(count):  # check every ant that is in the radius of the scream
            x, y = ants[i].x, ants[i].y
            d = math.dist((self.x, self.y), (x, y))
            if d <= dst:  # if it is
                if ants[i].blue_dis_counter > self.blue_dis_counter:  # check if the listening ant has larger counter
                    ants[i].set_blue_ang(self.x, self.y, d)  # go to ant which is 'closer' to blue point
                    ants[i].blue_flag = True  # need to shout out
                    ants[i].blue_dis_counter = self.blue_dis_counter  # update blue counter
                    pygame.draw.line(screen, (153, 187, 255), (self.x, self.y), (x, y), 1)  # drawing a line between the ants


count = 600  # number of ants
dst = 40  # radius of scream
fps = 120
ants = [Ant(random.uniform(50, 1250), random.uniform(50, 750)) for _ in range(count)]  # make ants
width, height = 1300, 800  # size of screen
screen = pygame.display.set_mode((width, height))  # make the screen
pygame.display.set_caption('Ants')
showAnt = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            showAnt *= -1
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (300, 300), 25)  # draw yellow point
    pygame.draw.circle(screen, (0, 255, 255), (width - 300, height - 300), 25)  # draw blue point
    for ant in ants:
        ant.step()  # each ant nake the step
    if showAnt == 1:
        for ant in ants:
            ant.render()
    pygame.display.flip()
    clock.tick(fps)
