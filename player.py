import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        image = pygame.image.load("./images/cacucu_img.png")
        image_width = 55
        image_length = 70
        image = pygame.transform.scale(image, (image_width, image_length))

        self.image = image.convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        
        self.speed = speed
        self.constraint = constraint
        self.image_width = image_width
        self.ready = True
        self.laser_elapsed = 0
        self.laser_cooldown = 600
        self.init_time = 0
        self.lasers = pygame.sprite.Group()


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.rect.x <= self.constraint - self.image_width*1.5:
                self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            if self.rect.x >= 0:
                self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.init_time = pygame.time.get_ticks()

    def recharge(self):
        # If laser isn't ready
        if not self.ready:
            current_time = pygame.time.get_ticks()
            # Check if difference in time matches cooldown
            if current_time - self.init_time >= self.laser_cooldown:
                self.ready = True
    
    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center, self.rect.bottom,  8))
        print("no way bro! (shoot laser)")

    def update(self):
        self.get_input()
        self.recharge()
        self.lasers.update()
