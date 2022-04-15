from turtle import position
import pygame

def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_pencil(screen, prevX, prevY, currentX, currentY):
    pygame.draw.line(screen, (200, 200,200), (prevX, prevY), (currentX, currentY))

def draw_rect(screen, prevX, prevY, currentX, currentY, baseLayer):
    screen.blit(baseLayer, (0, 0))
    r = calculateRect(prevX, prevY, currentX, currentY)
    pygame.draw.rect(screen, (255,255, 255),pygame.Rect(r), 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    baseLayer = pygame.Surface((640, 480))

    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
        
    screen.fill((0, 0, 0))

    isMouseDown = False

    mode = 'pencil'

    while True:
        
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = 'pencil'
                elif event.key == pygame.K_g:
                    mode = 'rect'

        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
            if mode == 'pencil':
                draw_pencil(screen, prevX, prevY, currentX, currentY)
                prevX = currentX
                prevY = currentY
            elif mode == 'rect':
                draw_rect(screen, prevX, prevY, currentX, currentY, baseLayer)
        
        pygame.display.flip()
        clock.tick(60)
        


main()