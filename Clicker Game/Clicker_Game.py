import pygame
import sys
import os

from pygame.constants import MOUSEBUTTONDOWN

# Constants
# ––Colors––
RED = (255, 0, 0)
RED_HOVER = (200, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Classes
class Button:
    def __init__(self, color, rect, text="", text_size=0, hover=False):
        self.color = color
        self.rect = pygame.Rect(rect)
        self.text = text
        self.text_size = text_size
        self.hover = hover
        self.font = pygame.font.Font(os.path.join("Roboto", "Robo.ttf"), self.text_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        t = self.font.render(self.text, True, (255, 255, 255))
        text_rect = t.get_rect(center=self.rect.center)
        screen.blit(t, text_rect)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.hover = True
            self.color = RED_HOVER
        else:
            self.hover = False
            self.color = RED

    def handle_event(self, score, click_power):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            autoclick.can_afford()
            score += click_power
        return score

    def upgrade(self, score, auto_clicker, cost):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if score >= cost:
                score -= cost
                if auto_clicker == 0:
                    auto_clicker += 0.01
                else: auto_clicker *= 2
                cost += 5
        return score, auto_clicker, cost

class Upgrade:
    def __init__(self, name, cost, cost_multiplier, level, effect):
        self.name = name
        self.cost = cost
        self.cost_multiplier = cost_multiplier
        self.level = level
        self.effect = effect

    def can_afford(self, score):
        if score >= self.cost:
            print("can afford")

    def purchase(self):
        pass

# Functions
def draw_score(screen, text, font, color, center):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=center)
    screen.blit(surface, rect)

def main():
    # Pygame Init
    pygame.init()
    WINDOW_WIDTH = 1080
    WINDOW_HEIGHT = 720
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Clicker Game")
    running = True
    clock = pygame.time.Clock()
    click_power = 0.5
    auto_clicker = 0
    cost = 5

    # Instances
    clicker_button = Button(RED, (0, 0, 200, 200), "", 22)
    clicker_button.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    upgrade_button = Button(BLUE, (2, 100, 150, 70), "Auto Clicker", 17)
    upgrade_button_02 = Button(BLUE, (2, 175, 150, 70), "Upgrade #2", 17)
    autoclick = Upgrade("Auto Click", 10, 2)

    # Variables
    buttons = [clicker_button, upgrade_button, upgrade_button_02]
    score = 0
    score_font = pygame.font.Font(os.path.join("Roboto", "Roboto-Bold.ttf"), 25)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                score = clicker_button.handle_event(score, click_power)
                score, auto_clicker, cost = upgrade_button.upgrade(score, auto_clicker, cost)

        screen.fill((255,255,255))

        draw_score(screen, f"${score:,.2f}", score_font, (0, 0, 0),
                  (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 300))
        draw_score(screen, f"Cost: {cost} – Auto Rate: {auto_clicker}", score_font, (0, 0, 0),
                  (200, 50))

        score += auto_clicker

        # Loop through all the buttons... Update, then draw them
        for button in buttons:
            button.update()
            button.draw(screen)

        # If any button = hover state true, then change the global mouse pointer
        if any(button.hover for button in buttons):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Entry Guard
if __name__ == '__main__':
    main()

