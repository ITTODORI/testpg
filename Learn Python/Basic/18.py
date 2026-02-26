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
accel = 0.8    # speeds up
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

    # 2. Apply Friction (slowing down slightly)
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
import random

# Initilaze

pygame.init()
WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKEPY")
clock = pygame.time.Clock()

# Physics & Game Constants
ACCEL = 0.8
FRICTION = 0.9
MAX_SPEED = 6
BLOCK_SIZE = 20

# VARIABLES
# varSnake
pos = pygame.math.Vector2(WIDTH // 2, HEIGHT // 2)
vel = pygame.math.Vector2(0, 0)
snake_body = [] 
snake_length = 5  # Initial length

# varFood
food_pos = pygame.math.Vector2(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))

def reset_game():
    global pos, vel, snake_body, snake_length
    pos = pygame.math.Vector2(WIDTH // 2, HEIGHT // 2)
    vel = pygame.math.Vector2(0, 0)
    snake_body = []
    snake_length = 5

run = True
while run:
    clock.tick(60)
    window.fill((20, 20, 25)) # drakBG

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 1. INPUT & PHYSICS
    keys = pygame.key.get_pressed()
    accel_vec = pygame.math.Vector2(0, 0)
    if keys[pygame.K_LEFT]:  accel_vec.x -= ACCEL
    if keys[pygame.K_RIGHT]: accel_vec.x += ACCEL
    if keys[pygame.K_UP]:    accel_vec.y -= ACCEL
    if keys[pygame.K_DOWN]:  accel_vec.y += ACCEL

    vel += accel_vec
    vel *= FRICTION 
    if vel.length() > MAX_SPEED:
        vel.scale_to_length(MAX_SPEED)

    pos += vel

    # 2. BOUNDARY WRAPPING (Snake)
    if pos.x > WIDTH: pos.x = 0
    if pos.x < 0: pos.x = WIDTH
    if pos.y > HEIGHT: pos.y = 0
    if pos.y < 0: pos.y = HEIGHT

    # 3. FOOD COLLISION
    dist_to_food = pos.distance_to(food_pos)
    if dist_to_food < 20:
        snake_length += 3 # Grow by 3 segments
        food_pos = pygame.math.Vector2(random.randint(20, WIDTH-20), random.randint(20, HEIGHT-20))

    # 4. SNAKE BODY LOGIC
    # Every 4 frames of movement, we "Solidify" a body segment.
    snake_body.append(list(pos))
    if len(snake_body) > snake_length * 4: # Multiply by 4 for a smoother trail
        snake_body.pop(0)

    # 5. GAME OVER (Self-Collision)
    # Only check segments that aren't right behind the head
    for segment in snake_body[:-20]:
        seg_vec = pygame.math.Vector2(segment[0], segment[1])
        if pos.distance_to(seg_vec) < 5:
            reset_game()

    # 6. DRAWING
    # Food
    pygame.draw.rect(window, (255, 50, 50), (food_pos.x, food_pos.y, 15, 15))

    # Draw Body
    for i, p in enumerate(snake_body):
        if i % 4 == 0: # Only draw every 4th recorded position for "Segment"
            alpha = min(255, (i + 1) * (255 // len(snake_body)))
            size = 10 + (i / len(snake_body)) * 10 #Tapered tail
            pygame.draw.circle(window, (0, alpha, 150), (int(p[0]), int(p[1])), int(size/2))

    # Draw Head (Squash and Stretch)
    draw_w = 22 + abs(vel.x) * 1.2
    draw_h = 22 + abs(vel.y) * 1.2
    head_rect = pygame.Rect(0, 0, draw_w, draw_h)
    head_rect.center = (pos.x, pos.y)
    pygame.draw.ellipse(window, (0, 255, 150), head_rect)

    pygame.display.update()

pygame.quit()
