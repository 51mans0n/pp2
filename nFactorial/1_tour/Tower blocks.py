# Importing libraries
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
pygame.display.set_caption('Tower blocks the Game')
icon = pygame.image.load('nFactorial\\1_tour\Images\icon.png')
pygame.display.set_icon(icon)

# Set the display parametres
resolution = WIDTH, HEIGHT = 800, 800
surface = pygame.display.set_mode(resolution)
background = pygame.image.load("nFactorial\\1_tour\Images\\background.png").convert_alpha()


# Load png
block1 = pygame.image.load("nFactorial\\1_tour\Images\\block1.png").convert_alpha()
block1 = pygame.transform.scale(block1, (200, 200))
block2 = pygame.image.load("nFactorial\\1_tour\Images\\block2.png").convert_alpha()
block2 = pygame.transform.scale(block2, (200, 200))
block3 = pygame.image.load("nFactorial\\1_tour\Images\\block3.png").convert_alpha()
block3 = pygame.transform.scale(block3, (200, 200))
block4 = pygame.image.load("nFactorial\\1_tour\Images\\block4.png").convert_alpha()
block4 = pygame.transform.scale(block4, (200, 200))
block5 = pygame.image.load("nFactorial\\1_tour\Images\\block5.png").convert_alpha()
block5 = pygame.transform.scale(block5, (200, 200))
block6 = pygame.image.load("nFactorial\\1_tour\Images\\block6.png").convert_alpha()
block6 = pygame.transform.scale(block6, (200, 200))
block7 = pygame.image.load("nFactorial\\1_tour\Images\\block7.png").convert_alpha()
block7 = pygame.transform.scale(block7, (200, 200))
block8 = pygame.image.load("nFactorial\\1_tour\Images\\block8.png").convert_alpha()
block8 = pygame.transform.scale(block8, (200, 200))
block9 = pygame.image.load("nFactorial\\1_tour\Images\\block9.png").convert_alpha()
block9 = pygame.transform.scale(block9, (200, 200))
block10 = pygame.image.load("nFactorial\\1_tour\Images\\block10.png").convert_alpha()
block10 = pygame.transform.scale(block10, (200, 200))
block11 = pygame.image.load("nFactorial\\1_tour\Images\\block11.png").convert_alpha()
block11 = pygame.transform.scale(block11, (200, 200))
block12 = pygame.image.load("nFactorial\\1_tour\Images\\block12.png").convert_alpha()
block12 = pygame.transform.scale(block12, (200, 200))
block13 = pygame.image.load("nFactorial\\1_tour\Images\\block13.png").convert_alpha()
block13 = pygame.transform.scale(block13, (200, 200))
block14 = pygame.image.load("nFactorial\\1_tour\Images\\block14.png").convert_alpha()
block14 = pygame.transform.scale(block14, (200, 200))
block15 = pygame.image.load("nFactorial\\1_tour\Images\\block15.png").convert_alpha()
block15 = pygame.transform.scale(block15, (200, 200))
block16 = pygame.image.load("nFactorial\\1_tour\Images\\block16.png").convert_alpha()
block16 = pygame.transform.scale(block16, (200, 200))
start_window = pygame.image.load("nFactorial\\1_tour\Images\\start_window.png").convert_alpha()
start_window = pygame.transform.scale(start_window, (800, 800))
construction_crane = pygame.image.load("nFactorial\\1_tour\Images\construction_crane.png").convert_alpha()

# Load a background music
mixer.music.load("nFactorial\\1_tour\Audio\\background_music.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(-1)

# Some start parametres and variables
blocks = (block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12, block13, block14, block15, block16)
temp = random.randint(0, 15)
score = 0
best_score = 0
crane_pos_x = 200
crane_pos_y = 0
new_block_pos_x = crane_pos_x
new_block_pos_y = crane_pos_y
background_pos_x = 0
background_pos_y = -4200
flag = True
pose1x_for_block = 9999
pose2x_for_block = 9999
pose3x_for_block = 9999
pose1y_for_block = 600
pose2y_for_block = 500
pose3y_for_block = 400
counter = 0

# Font and text characteristics
show_score = pygame.font.Font('nFactorial\\1_tour\Fonts\Montserrat-Thin.ttf', 40)
show_last_score = pygame.font.Font('nFactorial\\1_tour\Fonts\Montserrat-Thin.ttf', 45)
show_game_over = pygame.font.Font('nFactorial\\1_tour\Fonts\Montserrat-Thin.ttf', 60)


# Main Loop
RUN1 = True
while RUN1:
    surface.blit(start_window, (0, 0))
    for event in pygame.event.get():
        
        # Close the program
        if event.type == pygame.QUIT:
            RUN1 = False
            exit()
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                RUN2 = True
                while RUN2:
                    surface.blit(background, (background_pos_x, background_pos_y))
                    surface.blit(construction_crane, (crane_pos_x, crane_pos_y))
                    surface.blit(blocks[temp], (new_block_pos_x, new_block_pos_y + 20))
                    surface.blit(blocks[temp], (pose1x_for_block, pose1y_for_block))
                    surface.blit(blocks[temp], (pose2x_for_block, pose2y_for_block))
                    surface.blit(blocks[temp], (pose3x_for_block, pose3y_for_block))
                    
                    # For closing the window
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            RUN2 = False
                            RUN1 = False
                            exit()
                    
                    # Construction crane movements
                    if flag == True:
                        crane_pos_x += 0.5
                        new_block_pos_x += 0.5
                    elif flag == False:
                        crane_pos_x -= 0.5
                        new_block_pos_x -= 0.5
                    if crane_pos_x <= 400:
                        crane_pos_y += 0.05
                        new_block_pos_y += 0.05
                    elif crane_pos_x > 400:
                        crane_pos_y -= 0.05
                        new_block_pos_y -= 0.05
                    if crane_pos_x >= 600:
                        flag = False
                    elif crane_pos_x <= 100:
                        flag = True
                        
                    
                    current_score = show_score.render(f'SCORE: {score}', True, 'orange') # True - smoothing
                    surface.blit(current_score, (580, 10))
                    
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_DOWN]:
                        
                        temp_blockpos_x = new_block_pos_x
                        temp_blockpos_y = new_block_pos_y
                        
                        RUN3 = True
                        while RUN3:
                            surface.blit(background, (background_pos_x, background_pos_y))
                            surface.blit(construction_crane, (crane_pos_x, crane_pos_y))
                            surface.blit(blocks[temp], (new_block_pos_x, temp_blockpos_y + 20))
                            surface.blit(blocks[temp], (pose1x_for_block, pose1y_for_block))
                            surface.blit(blocks[temp], (pose2x_for_block, pose2y_for_block))
                            surface.blit(blocks[temp], (pose3x_for_block, pose3y_for_block))
                    
                                
                            # For closing the window
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    RUN3 = False
                                    RUN2 = False
                                    RUN1 = False
                                    exit()
                            # Construction crane movements
                            if flag == True:
                                crane_pos_x += 0.5
                                new_block_pos_x += 0.5
                            elif flag == False:
                                crane_pos_x -= 0.5
                                new_block_pos_x -= 0.5
                            
                            
                            if crane_pos_x >= 600:
                                flag = False
                            elif crane_pos_x <= 100:
                                flag = True
                                
                            temp_blockpos_y += 0.5
                            
                            if counter == 0 and temp_blockpos_y >= 600 and (temp_blockpos_x >= 200 and temp_blockpos_x <= 500):
                                temp = random.randint(0, 15)
                                background_pos_y += 200
                                temp_blockpos_y -= 100
                                pose1y_for_block = temp_blockpos_y
                                pose1x_for_block = temp_blockpos_x
                                counter += 1
                                score += 1
                                RUN3 = False
                            elif counter == 1 and temp_blockpos_y >= 600 and (temp_blockpos_x >= 200 and temp_blockpos_x <= 500):
                                temp = random.randint(0, 15)
                                background_pos_y += 200
                                temp_blockpos_y -= 300
                                pose2y_for_block = temp_blockpos_y
                                pose2x_for_block = temp_blockpos_x
                                counter += 1
                                score += 1
                                RUN3 = False
                            elif counter == 2 and temp_blockpos_y >= 600 and (temp_blockpos_x >= 200 and temp_blockpos_x <= 500):
                                temp = random.randint(0, 15)
                                background_pos_y += 200
                                temp_blockpos_y -= 500
                                pose3y_for_block = temp_blockpos_y
                                pose3x_for_block = temp_blockpos_x
                                counter = 0
                                score += 1
                                RUN3 = False
                            elif temp_blockpos_y >= 600 and not (temp_blockpos_x >= 200 and temp_blockpos_x <= 500):
                                
                                # Dead window
                                while True:
                                    render_end = show_game_over.render('GAME OVER', 20, pygame.Color('red'))
                                    last_score = show_last_score.render(f'Your score was - {score}', 20, pygame.Color('orange'))
                                    surface.blit(render_end, (WIDTH // 2 - 200, WIDTH // 3))
                                    surface.blit(last_score, (WIDTH // 2 - 220, WIDTH // 2 - 50))
                                    pygame.display.flip()
                                    
                                    # For closing the window
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            RUN3 = False
                                            RUN2 = False
                                            RUN1 = False
                                            exit()
                                
                                
                            current_score = show_score.render(f'SCORE: {score}', True, 'orange') # True - smoothing
                            surface.blit(current_score, (580, 10))
                            pygame.display.flip()
                    
                    pygame.display.flip()
    
    
    pygame.display.flip()
    FPS.tick(60)
pygame.quit()

# Код не доделан как видите, мне не хватило 1 дня(тоесть 1 день делал его) чтобы доделать правильно его логику