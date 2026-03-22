# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

def draw_circle():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    r = 200
    pygame.draw.circle(screen, ("green"), (x, y), r)
    return x, y, r

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    x, y, r = draw_circle()
    pygame.draw.line(screen, ("white"), (x, y), (mouse_pos[0], mouse_pos[1]), 2)
    pygame.draw.line(screen, ("white"), (x, y), (x-r, y), 2)
    pygame.draw.line(screen, ("white"), (x, y), (x, y-r), 2)
    #x2 + y2 = z2
    z = (x**2 + y**2)**0.5
    pygame.draw.line(screen, ("white"), (x, y), (z, z), 2)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()