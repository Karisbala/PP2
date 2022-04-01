import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
done = False
clock = pygame.time.Clock()
index = 0
paused = False

def button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pygame.font.SysFont("Arial", size)
    text_render = font.render(text, 1, fg)
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, bg, (x, y, w , h))
    print(screen.blit(text_render, (x, y)))
    return screen.blit(text_render, (x, y)) 

def play(paused):   
    if paused:
        pygame.mixer.music.unpause()
        paused = False
        return paused
    else:
        pygame.mixer.music.play()

def stop():
    pygame.mixer.music.pause()

def next(index):
    index += 1
    pygame.mixer.music.load(music_list[index])
    pygame.mixer.music.play()
    return index

def prev(index):
    index -= 1
    pygame.mixer.music.load(music_list[index])
    pygame.mixer.music.play()
    return index

music_list = ['audio/sample1.mp3','audio/sample2.mp3','audio/sample3.mp3','audio/sample4.mp3']
pygame.mixer.music.load(music_list[0])
b1 = button(screen, (220, 20), "Play", 50)
b2 = button(screen, (320, 20), "Stop", 50)
b3 = button(screen, (420, 20), "Next", 50)
b4 = button(screen, (20, 20), "Previous", 50)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    play(paused)
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    stop()
                    paused = True
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    next(index)
                    print(index)
                elif b4.collidepoint(pygame.mouse.get_pos()):
                    prev(index)        
        
        pygame.display.flip()
        clock.tick(60)