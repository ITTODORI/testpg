# pyGAME
import pygame #pip pygame

# init
pygame.init()
isRun = True

window = pygame.display.set_mode((500,500))

x = 250
y = 500

high = 20
large = 20
speed = 10

    # user input, database
while isRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500:
        x += speed

    # Asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,0,0),(x,y,high,large))
    # render
    pygame.display.update()

pygame.quit()
