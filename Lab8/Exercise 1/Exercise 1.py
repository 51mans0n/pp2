import pygame 
from pygame.locals import *
from datetime import datetime
import time
import random
from pygame import mixer

# Initializing
pygame.init()
FPS = pygame.time.Clock()
mixer.init()

# Set a Caption
pygame.display.set_caption('Racer the game')
icon = pygame.image.load('Lab8\Exercise 1\Images\icon.png')
pygame.display.set_icon(icon)

# Set the display parametres
resolution = WIDTH, HEIGHT = 800, 800
surface = pygame.display.set_mode(resolution)
road = pygame.image.load("Lab8/Exercise 1/Images/road.png").convert_alpha()
road = pygame.transform.scale(road, (800, 800))

# Load png
player = pygame.image.load("Lab8/Exercise 1/Images/player.png").convert_alpha()
player = pygame.transform.scale(player, (100, 200))
enemy = pygame.image.load("Lab8/Exercise 1/Images/enemy.png").convert_alpha()
enemy = pygame.transform.scale(enemy, (100, 200))
coin = pygame.image.load("Lab8/Exercise 1/Images/coin.png").convert_alpha()
coin = pygame.transform.scale(coin, (100, 75))

# Load a background music
mixer.music.load("Lab8\Exercise 1\Audio\music.mp3")
mixer.music.set_volume(0.4)
mixer.music.play(-1)

# Some parametres an start positions
player_speed = 5
player_x = 450
player_y = 550
bg_y = 0
coins = 0
enemy_x = random.randint(0, 700)
enemy_y = random.randint(-300, -100)
coin_x = random.randint(0, 700)
coin_y = random.randint(-200, -150)

# Font and text characteristics
myfont = pygame.font.Font('Lab8\Exercise 1\Fonts\Montserrat-Thin.ttf', 30)

# Main loop
run = True
while run:
    
    for event in pygame.event.get():
        
        # Close the programm
        if event.type == pygame.QUIT:
            run = False
            exit()
            
    # Overlay
    surface.blit(road, (0, bg_y))
    surface.blit(road, (0, bg_y - 800))
    surface.blit(player, (player_x, player_y))
    surface.blit(enemy, (enemy_x, enemy_y))
    surface.blit(coin, (coin_x, coin_y))
    balance = myfont.render(f'Balance: {coins}', True, 'Orange')
    surface.blit(balance, (600, 10))
    
    # Work with collisions
    player_rect = player.get_rect(topleft=(player_x, player_y))
    enemy_rect = enemy.get_rect(topleft=(enemy_x, enemy_y))
    coin_rect = coin.get_rect(topleft=(coin_x, coin_y))
    if player_rect.colliderect(enemy_rect):
        pygame.mixer.Sound("Lab8\Exercise 1\Audio\dead_end.mp3").play()
        print(f"You died, you collected {coins} coins")
        time.sleep(1)
        run = False
        exit()
    if player_rect.colliderect(coin_rect):
        coins += 1
        pygame.mixer.Sound("Lab8\Exercise 1\Audio\coin_sound.mp3").play()
        coin_y = 9999
        coin_x = 9999
    print(player_x, player_y, enemy_x, enemy_y)
    
    # Movements of player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x >= 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x <= 695:
        player_x += player_speed
    
    # Create new Enemy
    if enemy_y > 800:
        enemy_x = random.randint(0, 700)
        enemy_y = random.randint(-300, -100)
    if coin_y > 800:
        coin_x = random.randint(0, 700)
        coin_y = random.randint(-200, -150)
    
    # Road Driving Effect
    bg_y += 10
    if bg_y == 800:
        bg_y = 0
    enemy_y += 10
    coin_y += 10
            
    pygame.display.flip()
    FPS.tick(60)
pygame.quit()
        
                