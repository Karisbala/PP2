#Imports
import time
import pygame
import random

#Initialzing 
pygame.init()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_COLOR = (50, 50, 50)

#Other Variables for use in the program
HEIGHT = 400
WIDTH = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
SCREEN.fill(BLACK)

BLOCK_SIZE = 20

#Setting up FPS
FPS = 5

#Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 15)

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Wall:
    def __init__(self, level):
        self.body = []
        f = open("levels/level{}.txt".format(level), "r")

        for y in range(0, HEIGHT//BLOCK_SIZE + 1):
            for x in range(0, WIDTH//BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226,135,67), rect)

class Food:
    def __init__(self):
        self.location = Point(random.randint(0, 400)//BLOCK_SIZE, random.randint(0, 400)//BLOCK_SIZE)

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)


class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0
        

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE
        
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE

    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect)


        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    def new_level(self):
        self.body.clear()

    def check_collision(self, food, wall):
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                food.location = Point(random.randint(0, 400)//BLOCK_SIZE, random.randint(0, 400)//BLOCK_SIZE)
                self.body.append(Point(food.location.x, food.location.y))
        
        for i in range(len(wall.body)):
            if self.body[0].x == wall.body[i].x:
                if self.body[0].y == wall.body[i].y:
                    time.sleep(1)
                    game_over()
            
            if food.location.x == wall.body[i].x:
                if food.location.y == wall.body[i].y:
                    food.location = Point(random.randint(0, 400)//BLOCK_SIZE, random.randint(0, 400)//BLOCK_SIZE)

        for i in range(len(self.body)):
            if food.location.x == self.body[i].x:
                if food.location.y == self.body[i].y:
                    food.location = Point(random.randint(0, 400)//BLOCK_SIZE, random.randint(0, 400)//BLOCK_SIZE)

def game_over():
    pygame.quit()

def main():
    global FPS
    
    #Level counter
    level_number = 1

    #Setting up objects
    snake = Snake()
    food = Food()
    wall = Wall(level_number)

    #Adding a new User event 
    SPEED_INC = pygame.USEREVENT + 1
    DISAP = pygame.USEREVENT + 2
    pygame.time.set_timer(DISAP, 10000)

    while True:
        #Cycles through all events occurring
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == SPEED_INC:
                FPS += 2
            if event.type == DISAP:
                food.location = Point(random.randint(0, 400)//BLOCK_SIZE, random.randint(0, 400)//BLOCK_SIZE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1

        #Moving snake
        snake.move()
        
        #Checking snake collisions
        snake.check_collision(food, wall)

        #New level logic
        if len(snake.body) > 10:
            level_number += 1
            wall = Wall(level_number)
            snake.new_level()
            snake = Snake()
            pygame.event.post(pygame.event.Event(SPEED_INC))
            
        #Score and level
        SCREEN.fill(BLACK)
        SCORE = len(snake.body) - 1
        scores = font_small.render('Score: %d' %SCORE, True, WHITE)
        SCREEN.blit(scores, (5, 5))
        level = font_small.render('Level: %d' %level_number, True, WHITE)
        SCREEN.blit(level, (5, 20))
        
        #Drawing objects
        snake.draw()
        food.draw()
        wall.draw()

        pygame.display.update()
        CLOCK.tick(FPS)

main()