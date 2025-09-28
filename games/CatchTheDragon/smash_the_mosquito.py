import random

import pygame

pygame.init()

WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
surface_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Smash the Mosquito')

FPS = 60
clock = pygame.time.Clock()

PLAYER_STARTING_LIVES = 5
MOSQUITO_STARTING_VELOCITY = 3
MOSQUITO_ACCELERATION = .5
mos_dx = random.choice([-1,1])
mos_dy = random.choice([-1,1])

WHITE = (255, 255, 255)
RED = (255, 0 , 0)
BLACK = (0, 0 ,0 )

score = 0
player_lives = PLAYER_STARTING_LIVES
mosquito_velocity = MOSQUITO_STARTING_VELOCITY

font = pygame.font.Font('../assets/RumbleThorns-V4oB6.ttf', 30)
font.bold = True

title_text = font.render('Smash the Mosquito', True, BLACK)
title_rect = title_text.get_rect()
title_rect.topleft = (50,10)

score_text = font.render('Score: ' + str(score), True, BLACK)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render('Lives: ' + str(player_lives), True, BLACK)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50 , 50)

game_over_text = font.render('GAME OVER', True, BLACK)
game_over_rect = lives_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render('Click anywhere to play again', True, BLACK)
continue_rect = lives_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

# hit_sound = pygame.mixer.Sound()
# miss_sound = pygame.mixer.Sound()
# pygame.mixer.music.load()

# #BAck ground Imgae
# background_image = pygame.image.load()
# background_rect = background_image.get_rect()
# background_rect.topleft = (0,0)

mos_image = pygame.image.load('../assets/mosquito.png')
mos_rect = mos_image.get_rect()
mos_rect.center = ((WINDOW_WIDTH//2, WINDOW_HEIGHT//2))












running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display Background
    surface_display.fill(WHITE)

    # Display HUD
    surface_display.blit(lives_text, lives_rect)
    surface_display.blit(title_text, title_rect)
    surface_display.blit(score_text, score_rect)

    #Display Mosquito
    surface_display.blit(mos_image,mos_rect)



    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()



