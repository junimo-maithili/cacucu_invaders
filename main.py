import pygame, sys
from player import Player
from alien import Alien
from laser import Laser
import random

class Game:
    def __init__(self):
        player_sprite = Player((screen_width/2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.alien_setup(rows=6, columns=4)
        self.alien_movement = 1


    
    def alien_setup(self, rows, columns, x_offset=70, y_offset=100, x_distance=60, y_distance=50):
        for row_index, row in enumerate(range(rows)):
            for column_index, column in enumerate(range(columns)):
                x = row_index * x_distance + x_offset
                y = column_index * y_distance + y_offset

                if (row_index % 2 == 0 and column_index % 2 == 1) or (row_index % 2 == 1 and column_index % 2 == 0):
                    alien_sprite = Alien(2, x, y)
                else:
                    alien_sprite = Alien(1, x, y)
                
                self.aliens.add(alien_sprite)
    
    def check_alien_position(self):
        for alien in self.aliens.sprites():
            if alien.rect.right >= screen_width:
                self.alien_movement = -1
                self.move_alien_down(2)
            elif alien.rect.left <= 0:
                self.alien_movement = 1
                self.move_alien_down(2)

    def move_alien_down(self, distance):
        # Only move alien if it exists
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        # Don't shoot with dead aliens
        if self.aliens.sprites():
            random_alien = random.choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6, screen_height)
            self.alien_lasers.add(laser_sprite)

    def run(self):
        # Get new player and alien status
        self.player.update()
        self.aliens.update(self.alien_movement)
        self.check_alien_position()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.aliens.draw(screen)

        self.alien_shoot()
        self.alien_lasers.update()
        self.alien_lasers.draw(screen)
            


if __name__ == "__main__":
    pygame.init()
    screen_height = 600
    screen_width = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

     # Add custom event for alien shooting
    ALIEN_LASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIEN_LASER, 800)
    
    while True:
        for event in pygame.event.get():
            # End game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Deal with alien shooting
            if event.type == ALIEN_LASER:
                game.alien_shoot()
                game.alien_lasers.draw(screen)
        
        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)