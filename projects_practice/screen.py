import sys

import pygame

class Screen():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.background_color = (0, 0 , 150)

    def run_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.background_color)
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    new_screen = Screen()
    new_screen.run_screen()

