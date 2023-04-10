import pygame
from random import randrange

# Sizes
resolution = 800
size = 50

# Start parametres
x, y = randrange(0, resolution, size), randrange(0, resolution, size)
apple = randrange(0, resolution, size), randrange(0, resolution, size)
dirs = {'W': True, 'A': True, 'S': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
FPS = 5
score = 0

# Initializing fonts, images
pygame.init()
surface = pygame.display.set_mode([resolution, resolution])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Calibri', 26, bold=True)
font_end = pygame.font.SysFont('Calibri', 66, bold=True)
field = pygame.image.load('Lab8\Exercise 2\Images\\field.png').convert_alpha()

# Set a Caption
pygame.display.set_caption('Snake')
icon = pygame.image.load('Lab8\Exercise 2\Images\icon.png')
pygame.display.set_icon(icon)

# Main loop
RUN = True
while RUN:
    surface.blit(field, (0, 0))
    
    # Drawing snake apple
    [(pygame.draw.rect(surface, pygame.Color('brown'), (i, j, size - 2, size - 2))) for i, j in snake]
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, size, size))
    
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
        length += 1
        score += 1
        FPS += 1
    
    # Game over 
    if x < 0 or x > resolution - size or y < 0 or y > resolution - size or len(snake) != len(set(snake)):
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
    