import pygame
import sys

# Init
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Var
x, y = 250, 250
vel_x, vel_y = 0, 0 # Velocity
# Physics Constants
accel = 0.8    # How fast it speeds up
friction = 0.9 # How fast it slows down (0.9 = 10% loss per frame)
max_speed = 8

run = True
while run:
    clock.tick(60)
    window.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    # CONTROLER
    # 1. Acceleration (Input)
    if keys[pygame.K_LEFT]:  vel_x -= accel
    if keys[pygame.K_RIGHT]: vel_x += accel
    if keys[pygame.K_UP]:    vel_y -= accel
    if keys[pygame.K_DOWN]:  vel_y += accel

    # 2. Apply Friction (Always slowing down slightly)
    vel_x *= friction
    vel_y *= friction

    # 3. Cap the speed (Optional, prevents infinite acceleration)
    if vel_x > max_speed:  vel_x = max_speed
    if vel_x < -max_speed: vel_x = -max_speed
    if vel_y > max_speed:  vel_y = max_speed
    if vel_y < -max_speed: vel_y = -max_speed

    # 4. Update Position
    x += vel_x
    y += vel_y

    # Boundary check (simple version)
    x = max(0, min(x, 500 - 20))
    y = max(0, min(y, 500 - 20))

    pygame.draw.rect(window, (0, 255, 150), (x, y, 20, 20))
    pygame.display.update()

pygame.quit()