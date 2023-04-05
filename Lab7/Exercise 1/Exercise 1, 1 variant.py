import pygame
from datetime import datetime
from pygame import mixer
import math

# Set Parameters for Programm
resolution = WIDTH, HEIGHT = 1200, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
radius = H_HEIGHT - 50
radius_list = {'sec': radius - 10, 'min': radius - 55, 'hour': radius - 100, 'digit': radius - 30}

pygame.init()
mixer.init()

# Load a Background Sound
mixer.music.load('Lab7\Exercise 1\Sounds\clock_tick.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

surface = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

# Set a Caption
pygame.display.set_caption('My Clock, 1 variant')
icon = pygame.image.load('Lab7\Exercise 1\Images\icon.png')
pygame.display.set_icon(icon)

# Create Convenient Dictionary 
clock12 = dict(zip(range(12), range(0, 360, 30)))
clock60 = dict(zip(range(60), range(0, 360, 6)))

# Create Function for finding Position of Arrows
def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
            exit()
    # Set the Visual Component     
    surface.fill(pygame.Color('black'))
    time = datetime.now()
    hour, minute, second = time.hour % 12, time.minute, time.second
    pygame.draw.circle(surface, pygame.Color('darkslategray'), (H_WIDTH, H_HEIGHT), radius)
    
    # Set The Size of The Clock Marks
    for digit, pos in clock60.items():
        RADIUS = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
        pygame.draw.circle(surface, pygame.Color('gainsboro'), get_clock_pos(clock60, digit, 'digit'), RADIUS, 7)
    
    # Draw an Arrows
    pygame.draw.line(surface, pygame.Color('yellow'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 5)
    pygame.draw.line(surface, pygame.Color('orange'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 8)
    pygame.draw.line(surface, pygame.Color('red'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock12, hour, 'hour'), 15)
    pygame.draw.circle(surface, pygame.Color('white'), (H_WIDTH, H_HEIGHT), 8)
    
    pygame.display.update()
    clock.tick(20)