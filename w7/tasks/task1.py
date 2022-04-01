import pygame
import os
import datetime
import math

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((800, 700))
done = False
clock = pygame.time.Clock()

mickeyclock = pygame.transform.scale(get_image('images\mickeyclock.jpeg'), (800, 700))
mickeyclock_minute = pygame.transform.scale(get_image('images\mickeyclockminute.png'), (150, 150))
mickeyclock_hour = pygame.transform.scale(get_image('images\mickeyclockhour.png'), (100, 100))
#angle = 0

w1, h1 = mickeyclock_minute.get_size()
box1 = [pygame.math.Vector2(p) for p in [(0, 0), (w1, 0), (w1, -h1), (0, -h1)]]

w2, h2 = mickeyclock_hour.get_size()
box2 = [pygame.math.Vector2(p) for p in [(0, 0), (w2, 0), (w2, -h2), (0, -h2)]]

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        current_time = datetime.datetime.now()
        
        second = current_time.second

        screen.fill((255, 255, 255))
        
        screen.blit(mickeyclock, (0, 0))
        pos = (screen.get_width()/2, screen.get_height()/2)

        #minute
        minute = current_time.minute
        angle = 135+(-minute - (second/60)) * (360/60)
        box_rotate1 = [p.rotate(angle) for p in box1]
        min_box1 = (min(box_rotate1, key=lambda p: p[0])[0], min(box_rotate1, key=lambda p: p[1])[1])
        max_box1 = (max(box_rotate1, key=lambda p: p[0])[0], max(box_rotate1, key=lambda p: p[1])[1])
        origin1 = (pos[0] + min_box1[0], pos[1] - max_box1[1])
        rotated_minute = pygame.transform.rotate(mickeyclock_minute, angle)
        screen.blit(rotated_minute, origin1)


        #hour
        hour = current_time.hour
        angle = 135+(-hour - minute/60 - second/3600) * (360/12)
        box_rotate2 = [p.rotate(angle) for p in box2]
        min_box2 = (min(box_rotate2, key=lambda p: p[0])[0], min(box_rotate2, key=lambda p: p[1])[1])
        max_box2 = (max(box_rotate2, key=lambda p: p[0])[0], max(box_rotate2, key=lambda p: p[1])[1])
        origin2 = (pos[0] + min_box2[0], pos[1] - max_box2[1])
        rotated_hour = pygame.transform.rotate(mickeyclock_hour,angle)        
        screen.blit(rotated_hour, origin2)

        #angle -= 1

        pygame.display.flip()
        clock.tick(60)