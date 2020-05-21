import pygame
from image_loading import IDLE, RUN_R, RUN_L, IDLE_0, IDLE_L, JUMP_R, JUMP_L, FALL_R, FALL_L

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = IDLE_0
        self.is_idle = True
        self.movement_x = 0
        self.movement_y = 0
        self.movement_speed = 2
        self.rect = pygame.Rect(0, 675, 100, 55)
        self.frame = 0
        self.game = game
        self.direction_of_movement = 'right'
        self._gravity = 5
        self.is_jumping = False
        self.is_falling = False

    def control(self, x, y):
        # CONTROL PLAYER MOVEMENT
        self.movement_x += x
        self.movement_y += y

    def stop(self):
        self.movement_x = 0
        self.is_idle = True

    def update(self, animation_cycle):
        if -20 < self.rect.x + self.movement_x < 928 - 58 and 0 < self.rect.y + self.movement_y < 680:
            self.rect.x = self.rect.x + self.movement_x
            self.rect.y = self.rect.y - self.movement_y
            # moving left
            if self.direction_of_movement == 'left' and not self.is_idle:
                self.frame += 1
                if self.frame > 3 * animation_cycle:
                    self.frame = 0
                self.image = RUN_L[self.frame // animation_cycle]
            # moving right
            if self.direction_of_movement == 'right' and not self.is_idle:
                self.frame += 1
                if self.frame > 3 * animation_cycle:
                    self.frame = 0
                self.image = RUN_R[(self.frame // animation_cycle)]
            # idle
            if self.is_idle and self.direction_of_movement == 'right' and self.movement_x == 0:
                self.frame += 1
                if self.frame > 3 * animation_cycle:
                    self.frame = 0
                self.image = IDLE[(self.frame // animation_cycle - 3)]

            if self.is_idle and self.direction_of_movement == 'left' and self.movement_x == 0:
                self.frame += 1
                if self.frame > 3 * animation_cycle:
                    self.frame = 0
                    # Need to flip the idle images to make it suitable for idle left
                self.image = IDLE_L[(self.frame // animation_cycle - 3)]
            # jump
            if self.is_jumping and self.direction_of_movement == 'right':
                self.frame += 1
                if self.frame > 3 * animation_cycle:
                    self.frame = 0
                self.image = JUMP_R[(self.frame // animation_cycle - 7)]
            if self.is_jumping and self.direction_of_movement == 'left':
                self.frame += 1
                if self.frame > 3 * animation_cycle:
                    self.frame = 0
                self.image = JUMP_L[(self.frame // animation_cycle - 7)]
            # fall
            if self.is_falling and self.direction_of_movement == 'right':
                self.frame += 1
                if self.frame > 3 * animation_cycle:
                    self.frame = 0
                self.image = FALL_R[(self.frame // animation_cycle - 4)]
            if self.is_falling and self.direction_of_movement == 'left':
                self.frame += 1
                if self.frame > 3 * animation_cycle:
                    self.frame = 0
                self.image = FALL_L[(self.frame // animation_cycle - 4)]


def draw(self, surface):
    surface.blit(self.image, self.rect)
