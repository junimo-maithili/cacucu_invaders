import pygame, sys
from player import Player
from alien import Alien
from laser import Laser
import random

class Game:
    # Constructor class for game
    def __init__(self):
        # Player setup
        player_sprite = Player((screen_width/2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.alien_setup(rows=8, columns=4)
        self.alien_movement = 1

        # Health and score setup
        self.lives = 3
        self.lives_surface = pygame.image.load("./images/cacucu_img.png").convert_alpha()
        self.lives_x_start_pos = screen_width - self.lives_surface.get_size()[0] * 2 + 20


    # Creates alien sprites positioned in an array
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
    
    # Handles alien movement in the x-direction
    def check_alien_position(self):
        for alien in self.aliens.sprites():
            if alien.rect.right >= screen_width:
                self.alien_movement = -1
                self.move_alien_down(2)
            elif alien.rect.left <= 0:
                self.alien_movement = 1
                self.move_alien_down(2)

    # Handles alien movement in the y-direction
    def move_alien_down(self, distance):
        # Only move alien if it exists
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    # Makes aliens shoot lasers
    def alien_shoot(self):
        # Only existing aliens shoot
        if self.aliens.sprites():
            random_alien = random.choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, screen_height, -2)
            self.alien_lasers.add(laser_sprite)

    def display_lives(self):
        for life in range(self.lives - 1):
            x = self.lives_x_start_pos + life * self.lives_surface.get_size[0] + 20
            screen.blit(self.lives_surface, (x, 8))


    # Main run method for the program
    def run(self):
        # Get new player and alien status
        self.player.update()
        self.aliens.update(self.alien_movement)
        self.check_alien_position()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.aliens.draw(screen)

        self.alien_lasers.update()
        self.alien_lasers.draw(screen)

        self.check_collision()


    def check_collision(self):
        # Player laser collision with aliens
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                if pygame.sprite.spritecollide(laser, self.aliens, True):
                    laser.kill()
        
        # Alien laser collision with player
        if self.alien_lasers:
            for laser in self.alien_lasers:
                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    print("AHHH!!!!")
        
        # Alien collision with player
        if self.aliens:
            for alien in self.aliens:
                if pygame.sprite.spritecollide(alien, self.player, False):
                    print("You lost :((((")
                    

            


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
        
        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)



# maybe make extra points alien later
# make ifa as the shield