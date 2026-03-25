# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

x = 0
y = 250
h = 10
w = 10
speed = 5
Forward = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    rect = (x, y, h, w)

    if Forward:
        x += speed
        if x == SCREEN_WIDTH - w:
            Forward = False
    else:
        x -= speed
        if x == 0:
            Forward = True

    pygame.draw.rect(screen, (255, 255, 0), rect)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()