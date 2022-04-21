#Imports
import pygame.gfxdraw
import pygame

#Initializing
pygame.init()

#Paint surface variables
screen_width = 700
screen_height =500
screen = pygame.display.set_mode((screen_width, screen_height))
baseLayer = pygame.Surface((screen_width, screen_height))

#Setting up FPS
clock = pygame.time.Clock()
FPS = 60

#Defining colors
white = (255, 255, 255)
blue = (67,238,250)
red = (255, 0, 0)
black = (0, 0, 0)
green = (38,245,45)
pink = (255,192,203)
orange = (255,165,0)
yellow = (255,255,0)
violet = (177, 3, 252)

#Defining rect value for colors in colorbox
col1= (22, 81, 30, 34)
col2= (56, 81, 34, 34)
col3= (22, 120, 30, 33)
col4= (56, 120, 34, 32)
col5= (22, 156, 30, 33)
col6= (56, 156, 34, 32)
col7= (22, 192, 30, 33)
col8= (56, 192, 34, 32)

#Rect that highlight which button is selected
buttonselect = (22, 81, 30, 34)

def drawrectangle():    
    pygame.gfxdraw.box(screen, col1, white)
    pygame.gfxdraw.box(screen, col2, blue)
    pygame.gfxdraw.box(screen, col3, red)
    pygame.gfxdraw.box(screen, col4, green)
    pygame.gfxdraw.box(screen, col5, pink)
    pygame.gfxdraw.box(screen, col6, orange)
    pygame.gfxdraw.box(screen, col7, yellow)
    pygame.gfxdraw.box(screen, col8, violet)

def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_pencil(screen, prevX, prevY, currentX, currentY, color):
    pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))

def draw_rect(screen, prevX, prevY, currentX, currentY, baseLayer, color):
    screen.blit(baseLayer, (0, 0))
    r = calculateRect(prevX, prevY, currentX, currentY)
    pygame.draw.rect(screen, color,pygame.Rect(r), 1)

def erase(screen, prevX, prevY, currentX, currentY):
    pygame.draw.line(screen, black, (prevX, prevY), (currentX, currentY), 20)

def main():
    global buttonselect, FPS

    #Mouse positions    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
    
    #Setting up canvas
    screen.fill((0, 0, 0))
    drawrectangle()
    isMouseDown = False
    mode = 'pencil'
    color = white

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            #Getting mouse positions
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))

            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]

            #Selecting modes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = 'pencil'
                elif event.key == pygame.K_g:
                    mode = 'rect'
                elif event.key == pygame.K_b:
                    mode = 'erase'

        #Check for button clicks
        t = pygame.mouse.get_pressed()
        if t[0] == 1:     
            mousepos = pygame.mouse.get_pos()
            if 22 < mousepos[0] < 52 and 81 < mousepos[1] < 115:
                color = white
                drawrectangle()         
                buttonselect = (22, 81, 30, 34)
                
            elif 56 < mousepos[0] < 90 and 81 < mousepos[1] < 115:
                color = blue
                drawrectangle()
                buttonselect = (56, 81, 34, 34)
                
            elif 22 < mousepos[0] < 52 and 120 < mousepos[1] < 153:
                color = red
                drawrectangle()
                buttonselect = (22, 120, 30, 33)
                
            elif 56 < mousepos[0] < 90 and 120 < mousepos[1] < 152:
                color = green
                drawrectangle()
                buttonselect = (56, 120, 34, 32)
                
            elif 22 < mousepos[0] < 52 and 156 < mousepos[1] < 189:
                color = pink
                drawrectangle()
                buttonselect = (22, 156, 30, 33)
                
            elif 56 < mousepos[0] < 90 and 156 < mousepos[1] < 188:
                color = orange
                drawrectangle()
                buttonselect = (56, 156, 34, 32)
                
            elif 22 < mousepos[0] < 52 and 192 < mousepos[1] < 225:
                color = yellow
                drawrectangle()
                buttonselect = (22, 192, 30, 33)
                
            elif 56 < mousepos[0] < 90 and 192 < mousepos[1] < 224:
                color = violet
                drawrectangle()
                buttonselect = (56, 192, 34, 32)

        #Drawing
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
            if mode == 'pencil':
                draw_pencil(screen, prevX, prevY, currentX, currentY, color)
                prevX = currentX
                prevY = currentY
            elif mode == 'rect':
                draw_rect(screen, prevX, prevY, currentX, currentY, baseLayer, color)
            elif mode == 'erase':
                erase(screen, prevX, prevY, currentX, currentY)
                prevX = currentX
                prevY = currentY
        pygame.gfxdraw.rectangle(screen, buttonselect, white)
        
        pygame.display.flip()
        clock.tick(FPS)
        
main()