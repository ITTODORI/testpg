import pygame
import sys

# Init
pygame.init()
pygame.display.set_caption("pyGame")
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Var
x, y = 250, 250
vel_x, vel_y = 0, 0 # Velocity
# Physics Constants
accel = 0.8    # How fast it speeds up
friction = 0.9 # How fast it slows down (10% loss per frame)
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

    # 3. Cap the speed
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

# VERSE.II
# Init
pygame.init()
WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAMEPY")
clock = pygame.time.Clock()

# Physics Constants
ACCEL = 0.8
FRICTION = 0.9
MAX_SPEED = 8

# Player Variables
pos = pygame.math.Vector2(250, 250)
vel = pygame.math.Vector2(0, 0)
trail_positions = [] # Past positions for the animation

run = True
while run:
    clock.tick(60)
    window.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 1. INPUT & ACCELERATION
    keys = pygame.key.get_pressed()
    accel_vec = pygame.math.Vector2(0, 0)
    
    if keys[pygame.K_LEFT]:  accel_vec.x -= ACCEL
    if keys[pygame.K_RIGHT]: accel_vec.x += ACCEL
    if keys[pygame.K_UP]:    accel_vec.y -= ACCEL
    if keys[pygame.K_DOWN]:  accel_vec.y += ACCEL

    # Apply acceleration to velocity
    vel += accel_vec

    # 2. FRICTION & CAPPING
    vel *= FRICTION # Natural slowdown
    if vel.length() > MAX_SPEED:
        vel.scale_to_length(MAX_SPEED)

    # 3. UPDATE POSITION
    pos += vel

    # Boundary check
    pos.x = max(0, min(pos.x, WIDTH - 20))
    pos.y = max(0, min(pos.y, HEIGHT - 20))

    # 4. ANIMATION LOGIC (Trail)
    # Store current pos; keep only the last 6 frames
    trail_positions.append(list(pos))
    if len(trail_positions) > 6:
        trail_positions.pop(0)

    # DRAW TRAIL (Oldest to Newest)
    for i, p in enumerate(trail_positions):
        # Calculate fade: older squares are darker/smaller
        alpha = (i + 1) * 30 
        color = (0, alpha, alpha // 2)
        size_shrink = (6 - i) * 2
        pygame.draw.rect(window, color, (p[0] + size_shrink/2, p[1] + size_shrink/2, 20 - size_shrink, 20 - size_shrink))

    # 5. ANIMATION LOGIC (Squash & Stretch)
    # The faster we go, the "longer" we get in that direction
    stretch_x = 20 + abs(vel.x) * 1.5
    stretch_y = 20 + abs(vel.y) * 1.5
    
    # Counter-squash: If we stretch one way, we should thin out the other way
    # to keep the "volume" looking consistent
    draw_w = stretch_x - (abs(vel.y) * 0.5)
    draw_h = stretch_y - (abs(vel.x) * 0.5)

    # DRAW PLAYER
    # We offset by half the stretch to keep it centered on the 'pos'
    rect_x = pos.x - (draw_w - 20) / 2
    rect_y = pos.y - (draw_h - 20) / 2
    pygame.draw.rect(window, (0, 255, 150), (rect_x, rect_y, draw_w, draw_h))

    pygame.display.update()

pygame.quit()