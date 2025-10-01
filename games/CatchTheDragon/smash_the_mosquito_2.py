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

mouse_motion_x = 0
mouse_motion_y = 0









#pygame.mixer.music.play(-1,0.0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mouse_motion_x = event.pos[0]
            mouse_motion_y = event.pos[1]
            print(f'mmx: {mouse_motion_x}')
            print(f'mmy: {mouse_motion_y}')
            # move clown in new direction
            print(f' newX : {mouse_motion_x - mos_rect.x}')
            print(f' newY : {mouse_motion_y - mos_rect.y}')





            if mouse_motion_x == mos_rect.x and mouse_motion_y == mos_rect.y  :
                player_lives-1


        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y= event.pos[1]
        #here the clown was clicked
            print(f' mouse rec {mos_rect.x}')
            print(f' mouse rec {mos_rect.y}')
            if mos_rect.collidepoint(mouse_x,mouse_y):
                score += 1
                mosquito_velocity += MOSQUITO_ACCELERATION

                #move clown in new direction
                mos_dx = random.choice([-1,1])
                mos_dy = random.choice([-1,1])

                # if mos_dx == -1 or mos_dy == -1:
                #     mos_d,mos_dy = 1,1
                # if mos_dx == 1 or mos_dy == 1:
                #     mos_dx,mos_dy = -1,-1
                prev_dx = mos_dx
                prev_dy = mos_dy
                while(prev_dx == mos_dx and prev_dy == mos_dy):
                    mos_dx = random.choice([-1,1])
                    mos_dx = random.choice([-1,1])
            else:
                player_lives -= 1


    # #move the clown
    # mos_rect.x += mos_dx*mosquito_velocity
    # mos_rect.y += mos_dy*mosquito_velocity

    #able to get the score decresing wwhen the mosuquito tries to bite you

    if mouse_motion_x - mos_rect.x == 0 and  mouse_motion_y - mos_rect.y == 0:
        score -= 1

    pygame.time.delay(500)


    if mos_rect.x > mouse_motion_x:
        for x in range(abs(mouse_motion_x - mos_rect.x)):
            mos_rect.x -= 1
    if mos_rect.x < mouse_motion_x:
        for x in range(abs(mouse_motion_x - mos_rect.x)):
            mos_rect.x += 1
    if mos_rect.y > mouse_motion_y:
        for y in range(abs(mouse_motion_y - mos_rect.y)):
            mos_rect.y -= 1
    if mos_rect.y < mouse_motion_y:
        for y in range(abs(mouse_motion_y - mos_rect.y)):

            mos_rect.y += 1


    # mos_rect.x += (mouse_motion_x - mos_rect.x) * 1
    # mos_rect.y += (mouse_motion_y - mos_rect.y) * 1


#bounce clown
    if mos_rect.left <= 0 or mos_rect.right >= WINDOW_WIDTH:
        mos_dx = -1*mos_dx
    if mos_rect.top <= 0 or mos_rect.bottom >= WINDOW_HEIGHT:
        mos_dy = -1*mos_dy

    #update HUD
    score_text = font.render("Score: " + str(score), True, BLACK)
    lives_text = font.render("Lives: " + str(player_lives), True, BLACK)

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
    surface_display.blit(mos_image,mos_rect)



    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()



