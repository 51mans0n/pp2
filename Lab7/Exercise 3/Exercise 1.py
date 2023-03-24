import pygame

pygame.init()

surface = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

posX = 400
posY = 400

RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if posY > 20:
                posY -= 30
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if posY < 750:
                posY += 30   
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if posX > 20:
                posX -= 30
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if posX < 765:
                posX += 30

    surface.fill((255, 255, 255))
    pygame.draw.circle(surface, (255, 0, 0), (posX, posY), 25)
    pygame.display.flip()
    clock.tick(20)