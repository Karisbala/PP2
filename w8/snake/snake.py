import time
import pygame
import random

BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
FPS = 5
BLOCK_SIZE = 20


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

# class Free_space:
#     def __init__(self):
#         self.space = []
#         self.free = []
#         for y in range(0, HEIGHT//BLOCK_SIZE + 1):
#             for x in range(0, WIDTH//BLOCK_SIZE + 1):
#                 self.space.append(Point(x, y))

#     def free_space(self, snake, wall):
#         for i in range(len(self.space)):
#             for j in range(len(snake.body)):
#                 if snake.body[j].x == self.space[i].x:
#                     if snake.body[j].y == self.space[i].y:
#                         self.free.append(self.space[i])
#         for i in range(len(self.space)):
#             for j in range(len(wall.body)):
#                 if wall.body[j].x == self.space[i].x:
#                     if wall.body[j].y == self.space[i].y:
#                         self.free.append(self.space[i])
#         print(len(self.free), len(self.space))

        

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
        #self.level = 1

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


def game_over():
    pygame.quit()


def main():
    global SCREEN, CLOCK, FPS
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    level = [1, 2]
    iter_level = iter(level)
    snake = Snake()
    food = Food()
    wall = Wall(next(iter_level))
    # ground = Free_space()
    SPEED_INC = pygame.USEREVENT + 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == SPEED_INC:
                FPS += 2
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

        
        snake.move()
        

        snake.check_collision(food, wall)

        if len(snake.body) > 4 and len(snake.body) % 2 == 1:
            level = next(iter_level)
            wall = Wall(level)
            snake.new_level()
            snake = Snake()
            pygame.event.post(pygame.event.Event(SPEED_INC))
            

        SCREEN.fill(BLACK)

        
        snake.draw()
        food.draw()
        wall.draw()
        # ground.free_space(snake, wall)
        drawGrid()

        pygame.display.update()
        CLOCK.tick(FPS)


def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)


main()