import os
import pygame

pygame.init()
# MAIN WINDOW
SCREENSIZE = WIDTH, HEIGHT = 928, 793
os.environ['SDL_VIDEO_CENTERED'] = '1'
SCREEN = pygame.display.set_mode(SCREENSIZE)
# SCREEN SETTINGS
pygame.display.set_caption('Coordinates_system')


# image loading
file_names = sorted(os.listdir('sprites'))

# PURE FUCKING GARBAGE WAY TO HANDLE THIS BUT I DON'T HAVE IDEA HOW TO DO IT PROPERLY
BACKGROUND = pygame.image.load(os.path.join('sprites', 'Background.png')).convert()


IDLE_0 = pygame.image.load(os.path.join('sprites', 'IDLE_0.png')).convert_alpha(BACKGROUND)
IDLE_1 = pygame.image.load(os.path.join('sprites', 'IDLE_1.png')).convert_alpha(BACKGROUND)
IDLE_2 = pygame.image.load(os.path.join('sprites', 'IDLE_2.png')).convert_alpha(BACKGROUND)
IDLE_3 = pygame.image.load(os.path.join('sprites', 'IDLE_3.png')).convert_alpha(BACKGROUND)
IDLE_4 = pygame.image.load(os.path.join('sprites', 'IDLE_4.png')).convert_alpha(BACKGROUND)
IDLE_5 = pygame.image.load(os.path.join('sprites', 'IDLE_5.png')).convert_alpha(BACKGROUND)
IDLE_6 = pygame.image.load(os.path.join('sprites', 'IDLE_6.png')).convert_alpha(BACKGROUND)
IDLE_7 = pygame.image.load(os.path.join('sprites', 'IDLE_7.png')).convert_alpha(BACKGROUND)

IDLE_L_0 = pygame.image.load(os.path.join('sprites', 'IDLE_L_0.png')).convert_alpha(BACKGROUND)
IDLE_L_1 = pygame.image.load(os.path.join('sprites', 'IDLE_L_1.png')).convert_alpha(BACKGROUND)
IDLE_L_2 = pygame.image.load(os.path.join('sprites', 'IDLE_L_2.png')).convert_alpha(BACKGROUND)
IDLE_L_3 = pygame.image.load(os.path.join('sprites', 'IDLE_L_3.png')).convert_alpha(BACKGROUND)
IDLE_L_4 = pygame.image.load(os.path.join('sprites', 'IDLE_L_4.png')).convert_alpha(BACKGROUND)
IDLE_L_5 = pygame.image.load(os.path.join('sprites', 'IDLE_L_5.png')).convert_alpha(BACKGROUND)
IDLE_L_6 = pygame.image.load(os.path.join('sprites', 'IDLE_L_6.png')).convert_alpha(BACKGROUND)
IDLE_L_7 = pygame.image.load(os.path.join('sprites', 'IDLE_L_7.png')).convert_alpha(BACKGROUND)

RUN_R_0 = pygame.image.load(os.path.join('sprites', 'RUN_0.png')).convert_alpha(BACKGROUND)
RUN_R_1 = pygame.image.load(os.path.join('sprites', 'RUN_1.png')).convert_alpha(BACKGROUND)
RUN_R_2 = pygame.image.load(os.path.join('sprites', 'RUN_2.png')).convert_alpha(BACKGROUND)
RUN_R_3 = pygame.image.load(os.path.join('sprites', 'RUN_3.png')).convert_alpha(BACKGROUND)
RUN_R_4 = pygame.image.load(os.path.join('sprites', 'RUN_4.png')).convert_alpha(BACKGROUND)
RUN_R_5 = pygame.image.load(os.path.join('sprites', 'RUN_5.png')).convert_alpha(BACKGROUND)
RUN_R_6 = pygame.image.load(os.path.join('sprites', 'RUN_6.png')).convert_alpha(BACKGROUND)
RUN_R_7 = pygame.image.load(os.path.join('sprites', 'RUN_7.png')).convert_alpha(BACKGROUND)
RUN_R_8 = pygame.image.load(os.path.join('sprites', 'RUN_8.png')).convert_alpha(BACKGROUND)
RUN_R_9 = pygame.image.load(os.path.join('sprites', 'RUN_9.png')).convert_alpha(BACKGROUND)

RUN_L_0 = pygame.image.load(os.path.join('sprites', 'RUN_L_0.png')).convert_alpha(BACKGROUND)
RUN_L_1 = pygame.image.load(os.path.join('sprites', 'RUN_L_1.png')).convert_alpha(BACKGROUND)
RUN_L_2 = pygame.image.load(os.path.join('sprites', 'RUN_L_2.png')).convert_alpha(BACKGROUND)
RUN_L_3 = pygame.image.load(os.path.join('sprites', 'RUN_L_3.png')).convert_alpha(BACKGROUND)
RUN_L_4 = pygame.image.load(os.path.join('sprites', 'RUN_L_4.png')).convert_alpha(BACKGROUND)
RUN_L_5 = pygame.image.load(os.path.join('sprites', 'RUN_L_5.png')).convert_alpha(BACKGROUND)
RUN_L_6 = pygame.image.load(os.path.join('sprites', 'RUN_L_6.png')).convert_alpha(BACKGROUND)
RUN_L_7 = pygame.image.load(os.path.join('sprites', 'RUN_L_7.png')).convert_alpha(BACKGROUND)
RUN_L_8 = pygame.image.load(os.path.join('sprites', 'RUN_L_8.png')).convert_alpha(BACKGROUND)
RUN_L_9 = pygame.image.load(os.path.join('sprites', 'RUN_L_9.png')).convert_alpha(BACKGROUND)

JUMP_R_0 = pygame.image.load(os.path.join('sprites', 'JUMP_R_0.png')).convert_alpha(BACKGROUND)
JUMP_R_1 = pygame.image.load(os.path.join('sprites', 'JUMP_R_1.png')).convert_alpha(BACKGROUND)
JUMP_R_2 = pygame.image.load(os.path.join('sprites', 'JUMP_R_2.png')).convert_alpha(BACKGROUND)

JUMP_L_0 = pygame.image.load(os.path.join('sprites', 'JUMP_L_0.png')).convert_alpha(BACKGROUND)
JUMP_L_1 = pygame.image.load(os.path.join('sprites', 'JUMP_L_1.png')).convert_alpha(BACKGROUND)
JUMP_L_2 = pygame.image.load(os.path.join('sprites', 'JUMP_L_2.png')).convert_alpha(BACKGROUND)

FALL_R_0 = pygame.image.load(os.path.join('sprites', 'FALL_R_0.png')).convert_alpha(BACKGROUND)
FALL_R_1 = pygame.image.load(os.path.join('sprites', 'FALL_R_1.png')).convert_alpha(BACKGROUND)
FALL_R_2 = pygame.image.load(os.path.join('sprites', 'FALL_R_2.png')).convert_alpha(BACKGROUND)
FALL_R_3 = pygame.image.load(os.path.join('sprites', 'FALL_R_3.png')).convert_alpha(BACKGROUND)

FALL_L_0 = pygame.image.load(os.path.join('sprites', 'FALL_L_0.png')).convert_alpha(BACKGROUND)
FALL_L_1 = pygame.image.load(os.path.join('sprites', 'FALL_L_1.png')).convert_alpha(BACKGROUND)
FALL_L_2 = pygame.image.load(os.path.join('sprites', 'FALL_L_2.png')).convert_alpha(BACKGROUND)
FALL_L_3 = pygame.image.load(os.path.join('sprites', 'FALL_L_3.png')).convert_alpha(BACKGROUND)

IDLE = [IDLE_0, IDLE_1, IDLE_2, IDLE_3, IDLE_4, IDLE_5, IDLE_6, IDLE_7]
IDLE_L = [IDLE_L_0, IDLE_L_1, IDLE_L_2, IDLE_L_3, IDLE_L_4, IDLE_L_5, IDLE_L_6, IDLE_L_7]
RUN_R = [RUN_R_0, RUN_R_2, RUN_R_3, RUN_R_4, RUN_R_5, RUN_R_6, RUN_R_7, RUN_R_8, RUN_R_9]
RUN_L = [RUN_L_0, RUN_L_1, RUN_L_2, RUN_L_3, RUN_L_4, RUN_L_5, RUN_L_6, RUN_R_7, RUN_L_8, RUN_L_9]
JUMP_R = [JUMP_R_0, JUMP_R_1, JUMP_R_2]
JUMP_L = [JUMP_L_0, JUMP_L_1, JUMP_L_2]
FALL_R = [FALL_R_0, FALL_R_1, FALL_R_2, FALL_R_3]
FALL_L = [FALL_L_0, FALL_L_1, FALL_L_2, FALL_L_3]
