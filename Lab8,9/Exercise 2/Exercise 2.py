import pygame
from random import randrange
import random
from datetime import timedelta, datetime
import time
from pygame import mixer

# Sizes
resolution = 800
size = 40

# Start parametres
x, y = randrange(0, resolution, size), randrange(0, resolution, size)
apple = randrange(0, resolution, size), randrange(0, resolution, size)
blueberry = randrange(0, resolution, size), randrange(0, resolution, size)
goldenapple = randrange(0, resolution, size), randrange(0, resolution, size)
dirs = {'W': True, 'A': True, 'S': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
FPS = 5
score = 0
temp = 0
time_now = datetime.now()
clock = pygame.time.Clock()

# Initializing fonts, images
pygame.init()
mixer.init()
surface = pygame.display.set_mode([resolution, resolution])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Calibri', 26, bold=True)
font_end = pygame.font.SysFont('Calibri', 66, bold=True)
field = pygame.image.load('Lab8,9\Exercise 2\Images\\field.png').convert_alpha()

# Set a Caption
pygame.display.set_caption('Snake')
icon = pygame.image.load('Lab8,9\Exercise 2\Images\icon.png')
pygame.display.set_icon(icon)

# Load a background music
mixer.music.load("Lab8,9\Exercise 2\Audio\music.mp3")
mixer.music.set_volume(1)
mixer.music.play(-1)

# Main loop
RUN = True
while RUN:
    surface.blit(field, (0, 0))
    time_later = datetime.now()
    
    # Drawing snake apple
    [(pygame.draw.rect(surface, pygame.Color('brown'), (i, j, size - 2, size - 2))) for i, j in snake]
    if temp == 0:
        pygame.draw.rect(surface, pygame.Color('red'), (*apple, size, size))
    elif temp == 1:
        pygame.draw.rect(surface, pygame.Color('blue'), (*blueberry, size, size))
    elif temp == 2:
        pygame.draw.rect(surface, pygame.Color('orange'), (*goldenapple, size, size))
    
    # Show score
    render_score = font_score.render(f'Your score: {score}', 1, pygame.Color('white'))
    surface.blit(render_score, (5, 5))
    
    # Snake movements
    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-length:]
    
    # Eating apple
    if snake[-1] == apple:
        apple = randrange(0, resolution, size), randrange(0, resolution, size)
        pygame.mixer.Sound("Lab8,9\Exercise 2\Audio\eating.mp3").play()
        length += 1
        score += 1
        FPS += 1
        time_now = datetime.now()
        temp = random.randint(0, 2)
    elif snake[-1] == blueberry:
        blueberry = randrange(0, resolution, size), randrange(0, resolution, size)
        pygame.mixer.Sound("Lab8,9\Exercise 2\Audio\eating.mp3").play()
        length += 3
        score += 3
        FPS += 1
        time_now = datetime.now()
        temp = random.randint(0, 2)
    elif snake[-1] == goldenapple:
        goldenapple = randrange(0, resolution, size), randrange(0, resolution, size)
        pygame.mixer.Sound("Lab8,9\Exercise 2\Audio\eating.mp3").play()
        length += 5
        score += 5
        FPS += 1
        time_now = datetime.now()
        temp = random.randint(0, 2)
        
    # Game over 
    if x < 0 or x > resolution - size or y < 0 or y > resolution - size or len(snake) != len(set(snake)):
        pygame.mixer.Sound("Lab8,9\Exercise 2\Audio\death.mp3").play()
        pygame.mixer.music.stop()
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('red'))
            surface.blit(render_end, (resolution // 2 - 200, resolution // 3))
            pygame.display.flip()
            
            # For closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                    exit()
    
    # Update screen
    pygame.display.flip()
    clock.tick(FPS)
    
    # Close app checker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
            exit()
    
    # Controls
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'A': True, 'S': False, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'A': True, 'S': True, 'D': False}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'A': True, 'S': True, 'D': True}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'A': False, 'S': True, 'D': True}
        
    # Time for food
    if time_later - time_now > timedelta(seconds=5):
        apple = randrange(0, resolution, size), randrange(0, resolution, size)
        blueberry = randrange(0, resolution, size), randrange(0, resolution, size)
        goldenapple = randrange(0, resolution, size), randrange(0, resolution, size)
        pygame.mixer.Sound("Lab8,9\Exercise 2\Audio\\teleport.mp3").play()
        time_now = datetime.now()
    