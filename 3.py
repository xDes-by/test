import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

platform_width = 200
platform_height = 30

platform = pygame.Rect((WIDTH-platform_width)//2, HEIGHT-platform_height*2, platform_width, platform_height)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    screen.fill("black")
    pygame.draw.rect(screen, 'red', platform)
    pygame.display.update()
    clock.tick(60)
