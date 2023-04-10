import pygame 
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
icon = pygame.image.load('Lab8,9\Exercise 1\Images\icon.png')
pygame.display.set_icon(icon)

# Set the display parametres
resolution = WIDTH, HEIGHT = 800, 800
surface = pygame.display.set_mode(resolution)
road = pygame.image.load("Lab8,9/Exercise 1/Images/road.png").convert_alpha()
road = pygame.transform.scale(road, (800, 800))

# Load png
player = pygame.image.load("Lab8,9/Exercise 1/Images/player.png").convert_alpha()
player = pygame.transform.scale(player, (100, 200))
enemy = pygame.image.load("Lab8,9/Exercise 1/Images/enemy.png").convert_alpha()
enemy = pygame.transform.scale(enemy, (100, 200))
little_coin = pygame.image.load("Lab8,9/Exercise 1/Images/coin.png").convert_alpha()
little_coin = pygame.transform.scale(little_coin, (100, 75))
a_lot_of_coins = pygame.image.load("Lab8,9/Exercise 1/Images/a_lot_of_coins.png").convert_alpha()
a_lot_of_coins = pygame.transform.scale(a_lot_of_coins, (100, 85))
few_coins = pygame.image.load("Lab8,9/Exercise 1/Images/few_coins.png").convert_alpha()
few_coins = pygame.transform.scale(few_coins, (100, 90))

# Load a background music
mixer.music.load("Lab8,9\Exercise 1\Audio\music.mp3")
mixer.music.set_volume(0.4)
mixer.music.play(-1)

# Some parametres and start positions
player_speed = 10 # right or left
player_x = 450
player_y = 550
bg_y = 0
coins = 0
motion_effect = 10
temp = random.randint(0, 2)
enemy_x = random.randint(0, 700)
enemy_y = random.randint(-300, -200)
coin_x = random.randint(0, 700)
coin_y = random.randint(-200, -150)
coin = (little_coin, few_coins, a_lot_of_coins)
counter = 0

# Font and text characteristics
myfont = pygame.font.Font('Lab8,9\Exercise 1\Fonts\Montserrat-Thin.ttf', 30)
game_over = pygame.font.Font('Lab8,9\Exercise 1\Fonts\Montserrat-Thin.ttf', 60)
final_balance = pygame.font.Font('Lab8,9\Exercise 1\Fonts\Montserrat-Thin.ttf', 45)

# Main loop
run = True
while run:
    for event in pygame.event.get():
        
        # Close the program
        if event.type == pygame.QUIT:
            run = False
            exit()
            
    # Overlay
    surface.blit(road, (0, bg_y))
    surface.blit(road, (0, bg_y - 800))
    surface.blit(player, (player_x, player_y))
    surface.blit(enemy, (enemy_x, enemy_y))
    surface.blit(coin[temp], (coin_x, coin_y))
    balance = myfont.render(f'Balance: {coins}', True, 'Orange')
    surface.blit(balance, (600, 10))
    
    # Work with collisions
    player_rect = player.get_rect(topleft=(player_x, player_y))
    enemy_rect = enemy.get_rect(topleft=(enemy_x, enemy_y))
    coin_rect = coin[temp].get_rect(topleft=(coin_x, coin_y))
    if player_rect.colliderect(enemy_rect):
        pygame.mixer.Sound("Lab8,9\Exercise 1\Audio\dead_end.mp3").play()
        pygame.mixer.music.stop()
        
        # Dead window
        while True:
            render_end = game_over.render('GAME OVER', 20, pygame.Color('red'))
            last_balance = final_balance.render(f'Your balance was - {coins}', 20, pygame.Color('orange'))
            surface.blit(render_end, (WIDTH // 2 - 200, WIDTH // 3))
            surface.blit(last_balance, (WIDTH // 2 - 220, WIDTH // 2 - 50))
            pygame.display.flip()
            
            # For closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    exit()
    
    # Collect a coins
    if player_rect.colliderect(coin_rect):
        if temp == 0:
            coins += 1
        elif temp == 1:
            coins += 3
        elif temp == 2:
            coins += 5
        pygame.mixer.Sound("Lab8,9\Exercise 1\Audio\coin_sound.mp3").play()
        coin_y = 9999
        coin_x = 9999
        temp = random.randint(0, 2)
        if coins >= 2 and counter == 0:
            motion_effect += 1
            counter += 1
        if coins >= 5 and counter == 1:
            motion_effect += 2
            counter += 1
        if coins >= 10 and counter == 2:
            motion_effect += 3
            counter += 1
    
    # Movements of player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x >= 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x <= 695:
        player_x += player_speed
    
    # Create new Enemy
    if enemy_y > 800:
        enemy_x = random.randint(0, 700)
        enemy_y = random.randint(-400, -200)
    if coin_y > 800:
        coin_x = random.randint(0, 700)
        coin_y = random.randint(-200, -150)
    
    # Road Driving Effect
    bg_y += 5
    if bg_y == 800:
        bg_y = 0
    enemy_y += motion_effect
    coin_y += 5
            
    pygame.display.flip()
    FPS.tick(60)
pygame.quit()        