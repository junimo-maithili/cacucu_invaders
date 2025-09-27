import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, screen_height, speed = 5):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill("white")
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
        self.constraint = screen_height

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.constraint + 50:
            self.kill()


    def update(self):
        self.rect.y -= self.speed