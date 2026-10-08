import pygame

class Character:

    def __init__(self, new_screen):
        #Here I'm getting the general game screen and there I plan to place the image of my character
        self.screen = new_screen.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('projects_practice/creativecanvasdesign-pirate-captain-10313874_1920.bmp')
        self.fixed_image = pygame.transform.scale(self.image, (200, 150))
        self.image_rect = self.fixed_image.get_rect()

        self.image_rect.center = self.screen_rect.center


    def blitme(self):
        self.screen.blit(self.fixed_image, self.image_rect)

