import random
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

platform_width = 200
platform_height = 30
platform_speed = 10
platform_move_left = False
platform_move_right = False

ball_radius = 10
ball_speed = 5
ball_move_x = 0
ball_move_y = ball_speed
first_collide = False

block_width = 60
block_height = 20
block_count = 10
blocks = []

for i in range(block_count):
    blocks.append(pygame.rect.Rect(i * (block_width + 10) + 50, 75, block_width, block_height))

platform = pygame.rect.Rect((WIDTH-platform_width)//2, HEIGHT-platform_height*2, platform_width, platform_height)
ball = pygame.rect.Rect(WIDTH/2-ball_radius, HEIGHT/2-ball_radius, ball_radius*2, ball_radius*2)

running = True
gameover = False

score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and platform.left > 0:
        platform.x -= platform_speed
    if keys[pygame.K_RIGHT] and platform.right < WIDTH:
        platform.x += platform_speed

    ball.x += ball_move_x
    ball.y += ball_move_y

    if ball.colliderect(platform):
        if not first_collide:
            ball_move_x = ball_speed * random.choice([-1, 1])
            first_collide = True
        ball_move_y *= -1

    if ball.right >= WIDTH or ball.left <= 0:
        ball_move_x *= -1

    if ball.top <= 0:
        ball_move_y *= -1

    if ball.bottom >= HEIGHT:
        gameover = True

    for block in blocks:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_move_y *= -1
            score += 1
            break

    screen.fill("black")
    pygame.draw.rect(screen, 'red', platform)
    pygame.draw.circle(screen, 'white', ball.center, ball_radius)
    if gameover:
        text = font.render("GG WP", True, "red")
        screen.blit(text, ((WIDTH - text.get_width())/2, (HEIGHT - text.get_height()) / 2))
    for block in blocks:
        pygame.draw.rect(screen, "green", block)

    text_score = font.render(str(score), True, "white")
    screen.blit(text_score, (50, 50))

    pygame.display.update()
    clock.tick(60)
