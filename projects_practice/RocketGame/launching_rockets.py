import pygame
import sys

from rocket import Rockets

class Rocket_Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Rockets!")
        self.screen = pygame.display.set_mode((1000, 1000))
        self.background_color = (150, 100, 120)
        self.rocket = Rockets(self)
        self.rocket_speed = 2.5

    def run_game(self):
        while True:
            self.update_screen()
            self._check_events()
            self.rocket.update_movement()

    def update_screen(self):
        self.screen.fill(self.background_color)
        self.rocket.blitme()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                print(event.key)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_d:
            self.rocket.moving_right = True
        elif event.key == pygame.K_a:
            self.rocket.moving_left = True
        elif event.key == pygame.K_w:
            self.rocket.moving_up = True
        elif event.key == pygame.K_s:
            self.rocket.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.rocket.moving_right = False
        elif event.key == pygame.K_a:
            self.rocket.moving_left = False
        elif event.key == pygame.K_w:
            self.rocket.moving_up = False
        elif event.key == pygame.K_s:
            self.rocket.moving_down = False


if __name__ == '__main__':
    new_game = Rocket_Game()
    new_game.run_game()
        
