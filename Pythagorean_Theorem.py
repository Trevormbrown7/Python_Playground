# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.draw.circle(screen, ("green"), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), 200)
    pygame.draw.line(screen, ("white"), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), (mouse_pos[0], mouse_pos[1]), 2)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()