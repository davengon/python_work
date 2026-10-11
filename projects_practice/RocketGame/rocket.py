import pygame

class Rockets:

    def __init__(self, Rocket_Game):
        self.screen = Rocket_Game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('projects_practice/RocketGame/rocket.bmp')
        self.fixed_image = pygame.transform.scale(self.image, (200, 150))
        self.image_rect = self.fixed_image.get_rect()

        self.image_rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.x = float(self.image_rect.x)
        self.y = float(self.image_rect.y)


    def update_movement(self):
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.x += 1
        if self.moving_left and self.image_rect.left > 0:
            self.x -= 1
        if self.moving_up and self.image_rect.top > self.screen_rect.top:
            self.y -= 1
        if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.y += 1

        self.image_rect.x = self.x
        self.image_rect.y = self.y


    def blitme(self):
        self.screen.blit(self.fixed_image, self.image_rect)
        