import random
import mosquito_funcs as ms
from mosquito_funcs import Insecticide, Mosquito, Fly
import os

import pygame

pygame.init()

WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
surface_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Smash the Mosquito')

FPS = 60
clock = pygame.time.Clock()
BUFFER_DISTANCE = 100

PLAYER_STARTING_LIVES = 5
MOSQUITO_STARTING_VELOCITY = 3
MOSQUITO_ACCELERATION = .5
mos_dx = random.choice([-1,1])
mos_dy = random.choice([-1,1])

#events
MOSQUITO_BITE_MODE = pygame.USEREVENT + 1
pygame.time.set_timer(MOSQUITO_BITE_MODE,30000)
mosquito_bite_mode = False
normal_mode = True
start_time = pygame.time.get_ticks()
event_end_time = 0



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



mouse_motion_x = 0
mouse_motion_y = 0







insecticide = Insecticide()
insecticide_sprite = pygame.sprite.GroupSingle(insecticide)


mosquito_sprites = pygame.sprite.Group()

for _ in range(3):
    mosquito = Mosquito()
    mosquito_sprites.add(mosquito)






fly1 = Fly()
fly2 = Fly()
fly3 = Fly()
fly4 = Fly()
fly5 = Fly()
fly6 = Fly()













dropped = False
#pygame.mixer.music.play(-1,0.0)
running = True
while running:
    for event in pygame.event.get():
        print('start')
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            insecticide.un_swat()
            print('calling func')

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.sprite.spritecollide(insecticide, mosquito_sprites, dokill=False):
                collided_enemies = pygame.sprite.spritecollide(insecticide, mosquito_sprites, dokill=False)
                for mos in collided_enemies:
                    score += 1
                    mos.caught()
                    print('most1 got caught')
            else:
                player_lives -= 1


    #update HUD
    score_text = font.render("Score: " + str(score), True, BLACK)
    lives_text = font.render("Lives: " + str(player_lives), True, BLACK)

    # if score >= 5:
    #     one_fly.update()
    #     one_fly.draw(surface_display)
    # if score >= 10:
    #     two_fly.update()
    #     two_fly.draw(surface_display)
    # if score >= 15:
    #     three_fly.update()
    #     three_fly.draw(surface_display)

    if player_lives == 0:
        surface_display.blit(game_over_text, game_over_rect)
        surface_display.blit(continue_text, continue_rect)
        pygame.display.update()

        # pause the game until player presses a key , then reset the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # the playyer want to play again
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    mos_rect.center = ((WINDOW_WIDTH // 2, WINDOW_HEIGHT//2))
                    mosquito_velocity = MOSQUITO_STARTING_VELOCITY
                    mos_dx = random.choice([-1,1])
                    mos_dy = random.choice([-1,1])


                    # pygame.mixer.music.play(-1,0.0) #infintie loop
                    is_paused = False
                    # player want to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
    # Display Background
    surface_display.fill(WHITE)

    # Display HUD
    surface_display.blit(lives_text, lives_rect)
    surface_display.blit(title_text, title_rect)
    surface_display.blit(score_text, score_rect)

    #Display Mosquito
    insecticide_sprite.update()
    insecticide_sprite.draw(surface_display)
    mosquito_sprites.update()
    mosquito_sprites.draw(surface_display)

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()



