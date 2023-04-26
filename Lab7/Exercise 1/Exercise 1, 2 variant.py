import pygame
from pygame import mixer
import datetime

# Initializing libraries
pygame.init()
mixer.init()

# Background music
mixer.music.load('Lab7\Exercise 1\Sounds\clock_tick.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

screen = pygame.display.set_mode((800, 800))

# Set a caption
pygame.display.set_caption('My Clock, 2 variant')
icon = pygame.image.load('Lab7\Exercise 1\Images\icon.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

# Loading images
myClock = pygame.image.load('Lab7\Exercise 1\Images\clock.png')
myClock = pygame.transform.scale(myClock, (600, 600))
minute_arrow = pygame.image.load('Lab7\Exercise 1\Images\min.png')
second_arrow = pygame.image.load('Lab7\Exercise 1\Images\sec.png')

# Main Loop
RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
            exit()
            
    # Take a time in min and sec
    my_time = datetime.datetime.now()
    minuteINT = int(my_time.strftime("%M"))
    secondINT = int(my_time.strftime("%S"))

    # Take an angle to arrows
    angleMINUTE = minuteINT * 6 * -1
    angleSECOND = secondINT * 6 * -1

    # Rotation of arrows
    minute = pygame.transform.rotate(minute_arrow, angleMINUTE)
    second = pygame.transform.rotate(second_arrow, angleSECOND)

    # Add background
    screen.fill((255, 255, 255))
    screen.blit(myClock, (100, 100))
    
    # Image alignment
    screen.blit(second, (399 - int(second.get_width() / 2), 400 - int(second.get_height() / 2)))
    screen.blit(minute, ((399 - int(minute.get_width() / 2), 400 - int(minute.get_height() / 2))))
    
    pygame.draw.circle(screen, (0, 0, 0), (400, 400), 22)
    
    pygame.display.update()
    clock.tick(20)