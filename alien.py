import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, variation, x, y):
        super().__init__()

        image = pygame.image.load("./assets/ajaw_img_" + str(variation) + ".png")
        image_length = 60
        image_width = 43
        image = pygame.transform.scale(image, (image_length, image_width))
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, movement):
        self.rect.x += movement
