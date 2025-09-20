import pygame
import random


pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
surface_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Dragon")

#set clock
clock = pygame.time.Clock()
FPS = 60

#set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (127, 127, 127)

#set fonts
font = pygame.font.Font('../basic_tutorial_assets/basic_tutorial_assets/AttackGraffiti.ttf', 32)


#set text
score_text = font.render("Score: " + str(score), True, BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10,10)

title_text = font.render("Feed the dragon", True, BLACK)
title_text_rect = title_text.get_rect()
title_text_rect.centerx = WINDOW_WIDTH // 2
title_text_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, BLACK)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = ( WINDOW_WIDTH - 10, 10)

game_over_text = font.render("GAMEOVER", True, BLACK)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any button to play again", True, BLACK)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32

#set sound
coin_sound = pygame.mixer.Sound('../basic_tutorial_assets/basic_tutorial_assets/sound_1.wav')
miss_sound = pygame.mixer.Sound('../basic_tutorial_assets/basic_tutorial_assets/sound_2.wav')
miss_sound.set_volume(.1)
#pygame.mixer.music.load('../assets/Dragon.64.wav')

#setimages

dragon_image = pygame.image.load('../assets/Dragon.64.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.left = 32
dragon_image_rect.centery = WINDOW_HEIGHT //2

coin_image = pygame.image.load('../assets/Coin.png')
coin_image_rect = coin_image.get_rect()
coin_image_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_image_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
coin_sound.play()





running = True
while running:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
     surface_display.fill(WHITE)
     surface_display.blit(dragon_image, dragon_image_rect)
     #BLIT the HUD
     surface_display.blit(score_text, score_text_rect)
     surface_display.blit(title_text, title_text_rect)
     surface_display.blit(lives_text, lives_text_rect)
     pygame.draw.line(surface_display, BLACK, (0,64), (WINDOW_WIDTH, 64), 2)

     #BLIT assests to screen
     surface_display.blit(coin_image, coin_image_rect)
     surface_display.blit(dragon_image, dragon_image_rect)

     #check to see if the user wants to move
     keys = pygame.key.get_pressed()
     if keys[pygame.K_UP] and dragon_image_rect.top > 64:
         dragon_image_rect.y -= PLAYER_VELOCITY

     if keys[pygame.K_DOWN] and dragon_image_rect.bottom < WINDOW_HEIGHT:
         dragon_image_rect.y += PLAYER_VELOCITY

    #move the coin
     if coin_image_rect.x < 0 :
         #playyer missed coin
         player_lives -= 1
         miss_sound.play()
         coin_image_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
         coin_image_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
     else:
        #move the conin
        coin_image_rect.x -= coin_velocity

     #check for collisons
     if dragon_image_rect.colliderect(coin_image_rect):
         score += 1
         coin_sound.play()
         coin_velocity += COIN_ACCELERATION
         coin_image_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
         coin_image_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

         #Accelearion Tactics - determine the rate increase of the coin based on the missed
         # 5
         # 5.5 -> 5
         # 6
         # 6.5 - > 6

        #update the HUD
     score_text = font.render("Score: " + str(score), True, BLACK)
     lives_text = font.render("Lives: " + str(player_lives), True, BLACK)









     pygame.display.update()
     clock.tick(FPS)


pygame.quit()
