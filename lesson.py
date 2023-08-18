import pygame
import random

pygame.init()


WIDTH = 600
HEIGHT = 400
FPS = 60
SPEED = 5

PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 20
BALL_RADIUS = 10
BALL_SPEED = 5
ball_x_speed = 0
ball_y_speed = SPEED
first_collision = True
score = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Курс PyGame")
pygame.display.set_icon(pygame.image.load("pig.bmp"))

font = pygame.font.Font(None, 36)  #====================================================

background_image = pygame.transform.scale(pygame.image.load("back.jpg"), (WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
game_over = False

platform_image = pygame.image.load("back.jpg")
platform_image = pygame.transform.scale(platform_image, (PLATFORM_WIDTH, PLATFORM_HEIGHT))
platform_rect = pygame.rect.Rect(WIDTH/2-PLATFORM_WIDTH/2, HEIGHT - PLATFORM_HEIGHT*2, PLATFORM_WIDTH, PLATFORM_HEIGHT)

ball_image = pygame.image.load("pig.bmp")
ball_image = pygame.transform.scale(ball_image, (BALL_RADIUS*2, BALL_RADIUS*2))
ball_rect = pygame.rect.Rect(WIDTH/2-BALL_RADIUS, HEIGHT/2-BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and platform_rect.left > 0:
        platform_rect.x -= SPEED
    if keys[pygame.K_d] and platform_rect.right < WIDTH:
        platform_rect.x += SPEED

    if platform_rect.colliderect(ball_rect):
        if first_collision:
            ball_x_speed = BALL_SPEED*random.choice([-1, 1])
            first_collision = False
        ball_y_speed = -BALL_SPEED
        score += 1 #====================================================

    ball_rect.x += ball_x_speed
    ball_rect.y += ball_y_speed

    if ball_rect.top <= 0:
        ball_y_speed *= -1
    if ball_rect.right >= WIDTH or ball_rect.left <= 0:
        ball_x_speed *= -1

    if ball_rect.bottom >= HEIGHT:
        game_over = True

    text = font.render(str(score), True, (255, 255, 255))#====================================================
    screen.blit(background_image, (0, 0))
    screen.blit(platform_image, platform_rect)
    screen.blit(ball_image, ball_rect)
    screen.blit(text, (10, 10))#====================================================
    if game_over:
        text = font.render("GG", True, (255, 255, 255))  # ====================================================
        screen.blit(text, (100, 100))  # ====================================================


    pygame.display.update()
    clock.tick(FPS)