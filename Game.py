import pygame
# import sys
import image_loading as il
from Player import Player

SCREENSIZE = WIDTH, HEIGHT = 928, 793


# import Player as pl
class Game:
    def __init__(self):
        # CONFIG
        self.fps = 100
        self.clock = pygame.time.Clock()
        self.animation_cycle = 10
        self.background = il.BACKGROUND
        self.done = True
        # INITIALIZATION
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption('Hero Knight')
        pygame.mouse.set_visible(0)
        self.player = Player(self)
        self.player_list = pygame.sprite.Group()
        self.player_list.add(self.player)
        # EVENT LOOP
        while self.done:
            # EVENT HANDLING
            for event in pygame.event.get():
                # QUIT EVENTS
                if event.type == pygame.QUIT:
                    self.done = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = False
                    if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                        self.player.is_jumping = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.player.direction_of_movement = 'left'
                self.player.is_idle = False
                self.player.control(-self.player.movement_speed, 0)
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.player.direction_of_movement = 'right'
                self.player.is_idle = False
                self.player.control(self.player.movement_speed, 0)
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.player.stop()
                self.player.is_idle = True
                print(self.player.rect)
            # RENDERING
            self.screen.blit(self.background, (0, 0))
            self.player.update(10)

            self.player.stop()
            self.player_list.draw(self.screen)
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    Game()

pygame.quit()
