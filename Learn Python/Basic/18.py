# pyGAME
import pygame #pip pygame

# init
pygame.init()
pygame.display.set_caption("myPYGAME")
window = pygame.display.set_mode((500,500))

# Var
x = 250
y = 250
width = 20
height = 20
speed = 10

isRun = True

    # user input, database
while isRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += speed

    # Asset
    window.fill((0,0,0))
    pygame.draw.rect(window,(255,0,0),(x,y,width,height))
    # render
    pygame.display.update()

pygame.quit()
