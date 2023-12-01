import pygame
import math
import random


pygame.init()


class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)
        self.food = True if random.uniform(0, 2) > 1 else False
        self.yellow_flag = False
        self.blue_flag = False
        self.yellow_ang = random.uniform(0, 2 * math.pi)
        self.blue_ang = random.uniform(0, 2 * math.pi)
        self.yellow_dis_counter = 100
        self.blue_dis_counter = 100

    def step(self):

        self.yellow_dis_counter += 0.1
        self.blue_dis_counter += 0.1

        self.angle += random.uniform(-0.01, 0.01)

        if self.x < 10:
            self.x = 10
            self.angle += math.pi
        elif self.x > width - 10:
            self.x = width - 10
            self.angle += math.pi
        if self.y < 10:
            self.y = 10
            self.angle += math.pi
        elif self.y > height - 10:
            self.y = height - 10
            self.angle += math.pi

        self.x += math.sin(self.angle)
        self.y += math.cos(self.angle)

        cl = screen.get_at((int(self.x), int(self.y)))

        if cl == (255, 255, 0):
            self.food = True
            self.yellow_dis_counter = 0
            self.yellow_flag = True
            self.angle = self.blue_ang

        if cl == (0, 255, 255):
            self.food = False
            self.blue_dis_counter = 0
            self.blue_flag = True
            self.angle = self.yellow_ang

        if self.yellow_flag:
            self.yellow_cry()
            self.yellow_flag = False
            if not self.food:
                self.angle = self.yellow_ang

        if self.blue_flag:
            self.blue_cry()
            self.blue_flag = False
            if self.food:
                self.angle = self.blue_ang

    def render(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 1)

    def set_yellow_ang(self, x, y, d):
        an = math.acos((y - self.y) / d)
        self.yellow_ang = an if x > self.x else 2 * math.pi - an

    def set_blue_ang(self, x, y, d):
        an = math.acos((y - self.y) / d)
        self.blue_ang = an if x > self.x else 2 * math.pi - an

    def yellow_cry(self):
        for i in range(count):
            x, y = ants[i].x, ants[i].y
            d = math.dist((self.x, self.y), (x, y))
            if d <= dst:
                if ants[i].yellow_dis_counter > self.yellow_dis_counter:
                    ants[i].set_yellow_ang(self.x, self.y, d)
                    ants[i].yellow_flag = True
                    ants[i].yellow_dis_counter = self.yellow_dis_counter
                    pygame.draw.line(screen, (255, 255, 153), (self.x, self.y), (x, y), 1)

    def blue_cry(self):
        for i in range(count):
            x, y = ants[i].x, ants[i].y
            d = math.dist((self.x, self.y), (x, y))
            if d <= dst:
                if ants[i].blue_dis_counter > self.blue_dis_counter:
                    ants[i].set_blue_ang(self.x, self.y, d)
                    ants[i].blue_flag = True
                    ants[i].blue_dis_counter = self.blue_dis_counter
                    pygame.draw.line(screen, (153, 187, 255), (self.x, self.y), (x, y), 1)


count = 550
dst = 40
fps = 120
ants = [Ant(random.uniform(50, 1250), random.uniform(50, 750)) for _ in range(count)]
width, height = 1300, 800
screen = pygame.display.set_mode((width, height))
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
    pygame.draw.circle(screen, (255, 255, 0), (300, 300), 25)
    pygame.draw.circle(screen, (0, 255, 255), (width - 300, height - 300), 25)
    for ant in ants:
        ant.step()
    if showAnt == 1:
        for ant in ants:
            ant.render()
    pygame.display.flip()
    clock.tick(fps)
