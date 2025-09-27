import pygame
import random

from anyio import current_time

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 700

surface_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Stack the Burger")

#set clock
clock = pygame.time.Clock()
FPS = 60

#set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
PLAYER_VELOCITY_MINI = 9

COIN_STARTING_VELOCITY = 5

COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

#events
SPAWN_HAPPY_MEAL = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_HAPPY_MEAL,30000)
should_blit_spider = False


CUSTOM_EVENT_DURATION = 20000


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (127, 127, 127)



#set fonts
font = pygame.font.Font('../basic_tutorial_assets/basic_tutorial_assets/AttackGraffiti.ttf', 18)


#set text
score_text = font.render("Score: " + str(score), True, BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10,10)

title_text = font.render("Stack the Burger", True, BLACK)
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

burger_image = pygame.image.load('../CatchTheDragon/images/Plain-Burger.64.png')
burger_image_rect = burger_image.get_rect()
burger_image_rect.bottom = 675
burger_image_rect.centerx = WINDOW_WIDTH //2

trash_image = pygame.image.load('../assets/Trash.64.png')
trash_rect = trash_image.get_rect()
trash_rect.y = 0 + BUFFER_DISTANCE
trash_rect.x = random.randint(0, WINDOW_WIDTH - 32)
coin_sound.play()

rat_image = pygame.image.load('../assets/rat.64.png')
rat_rect = rat_image.get_rect()
rat_rect.y = 0 + BUFFER_DISTANCE
rat_rect.x = random.randint(0, WINDOW_WIDTH - 32)
coin_sound.play()

bug_image = pygame.image.load('../assets/Bug-Flat.64.png')
bug_rect = bug_image.get_rect()
bug_rect.y = 0 + BUFFER_DISTANCE
bug_rect.x = random.randint(0, WINDOW_WIDTH - 32)
coin_sound.play()

spider_image = pygame.image.load('../assets/spider.64.png')
spider_rect = spider_image.get_rect()
spider_rect.y = 0 + BUFFER_DISTANCE
spider_rect.x = random.randint(0, WINDOW_WIDTH - 32)
coin_sound.play()

ketchup_image = pygame.image.load('../CatchTheDragon/images/Ketchup.64.png')
ketchup_image_rect = ketchup_image.get_rect()
ketchup_image_rect.y = 0 + BUFFER_DISTANCE
ketchup_image_rect.x = random.randint(0, WINDOW_WIDTH - 32)
coin_sound.play()

cheese_image = pygame.image.load('../CatchTheDragon/images/Cheese.64.png')
cheese_image_rect = cheese_image.get_rect()
cheese_image_rect.y = 0 + BUFFER_DISTANCE
cheese_image_rect.x = random.randint(0, WINDOW_WIDTH - 32)
coin_sound.play()

mini_burger_image = pygame.image.load('../assets/MiniBurger.32.png')
mini_burger_rect = mini_burger_image.get_rect()
mini_burger_rect.y = 600
mini_burger_rect.x = WINDOW_WIDTH //2
coin_sound.play()

random_velocity = random.randint(1, 7)
random_velocity2 = random.randint(1, 7)
random_velocity3 = random.randint(1, 7)


#image updates
show_regular_burger = True
show_mini_burger = False
start_time = pygame.time.get_ticks()
count = 0
event_end_time = 0
event_end_time_2 = 0
running = True
while running:


     for event in pygame.event.get():

         if event.type == pygame.QUIT:
             running = False
         elif event.type == SPAWN_HAPPY_MEAL:

             should_blit_spider = True
             event_end_time = pygame.time.get_ticks() + 5000
             print(event_end_time)


     surface_display.fill(WHITE)
     #BLIT the HUD
     surface_display.blit(score_text, score_text_rect)
     surface_display.blit(title_text, title_text_rect)
     surface_display.blit(lives_text, lives_text_rect)
     pygame.draw.line(surface_display, BLACK, (0,64), (WINDOW_WIDTH, 64), 2)
     #BLIT assests to screen
     surface_display.blit(bug_image, bug_rect)
     surface_display.blit(ketchup_image, ketchup_image_rect)
     if show_regular_burger:
        event_end_time_2 = pygame.time.get_ticks() + 10000

        surface_display.blit(burger_image, burger_image_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and burger_image_rect.left > 0:
            burger_image_rect.x -= PLAYER_VELOCITY

        if keys[pygame.K_RIGHT] and burger_image_rect.right < WINDOW_WIDTH:
            burger_image_rect.x += PLAYER_VELOCITY

     if show_mini_burger:
         print('!!!!!!!!!!!!!!! in mini burger section')

         show_regular_burger = False
         surface_display.blit(mini_burger_image,mini_burger_rect)
         keys = pygame.key.get_pressed()
         if keys[pygame.K_LEFT] and mini_burger_rect.left > 0:
             mini_burger_rect.x -= PLAYER_VELOCITY_MINI

         if keys[pygame.K_RIGHT] and mini_burger_rect.right < WINDOW_WIDTH:
             mini_burger_rect.x += PLAYER_VELOCITY_MINI

     if should_blit_spider and pygame.time.get_ticks() < event_end_time:
         surface_display.blit(spider_image, spider_rect)
         pygame.display.flip()

         if spider_rect.y > WINDOW_HEIGHT:
             miss_sound.play()
             spider_rect.y = 0 - BUFFER_DISTANCE
             spider_rect.x = random.randint(0, WINDOW_WIDTH - 32)
             count += 1
         else:
             # move the conin
             spider_rect.y += random_velocity3
     elif should_blit_spider and pygame.time.get_ticks() >= event_end_time:
        should_blit_spider = False

        # move the coin
     if ketchup_image_rect.y > WINDOW_HEIGHT:
        ketchup_image_rect.y = 0 - BUFFER_DISTANCE
        ketchup_image_rect.x = random.randint(0, WINDOW_WIDTH - 32)
        random_velocity = random.randint(1,10)

     else:
        ketchup_image_rect.y += random_velocity

    #move the coin
     if bug_rect.y > WINDOW_HEIGHT:
         miss_sound.play()
         bug_rect.y = 0 - BUFFER_DISTANCE
         bug_rect.x = random.randint(0, WINDOW_WIDTH - 32)
     else:
        bug_rect.y += coin_velocity

     #check for collisons
     # Damage Collisions
     if burger_image_rect.colliderect(bug_rect):
        score -= 1
        player_lives -= 1
        coin_sound.play()
        bug_rect.y = 0 - BUFFER_DISTANCE
        bug_rect.x = random.randint(0, WINDOW_WIDTH - 32)

    #helpful collisons
     if burger_image_rect.colliderect(ketchup_image_rect):
        score += 1
        coin_sound.play()
        ketchup_image_rect.y = 0 - BUFFER_DISTANCE
        ketchup_image_rect.x = random.randint(0, WINDOW_WIDTH - 32)
        random_velocity = random.randint(1,10)

     if burger_image_rect.colliderect(spider_rect):
        score += 1
        coin_sound.play()
        spider_rect.y = 0 - BUFFER_DISTANCE
        spider_rect.x = random.randint(0, WINDOW_WIDTH - 32)
        random_velocity = random.randint(1,10)
        show_mini_burger = True

     if show_mini_burger and pygame.time.get_ticks() >= event_end_time_2:
        show_mini_burger = False
        show_regular_burger = True







         #Accelearion Tactics - determine the rate incre
         # ase of the coin based on the missed
         # 5
         # 5.5 -> 5
         # 6
         # 6.5 - > 6

        #update the HUD
     score_text = font.render("Score: " + str(score), True, BLACK)
     lives_text = font.render("Lives: " + str(player_lives), True, BLACK)

     # LEVEL_2
     if score >= 10:
         surface_display.blit(cheese_image, cheese_image_rect)

         if cheese_image_rect.y > WINDOW_HEIGHT:
             miss_sound.play()
             cheese_image_rect.y = 0 - BUFFER_DISTANCE
             cheese_image_rect.x = random.randint(0, WINDOW_WIDTH - 32)
             random_velocity2 = random.randint(1, 5)
         else:
             # move the conin
              cheese_image_rect.y += random_velocity2
             # print('here')

        # helpful collisons
         if burger_image_rect.colliderect(cheese_image_rect):
             score += 2
             coin_sound.play()
             cheese_image_rect.y = 0 - BUFFER_DISTANCE
             cheese_image_rect.x = random.randint(0, WINDOW_WIDTH - 32)
             random_velocity = random.randint(1, 10)

     if player_lives == 0:
        surface_display.blit(game_over_text, game_over_text_rect)
        surface_display.blit(continue_text, continue_text_rect)
        pygame.display.update()

        #pause the game until player presses a key , then reset the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #the playyer want to play again
                if event.type == pygame.KEYDOWN:
                    score=0
                    player_lives = PLAYER_STARTING_LIVES
                    burger_image_rect.x = WINDOW_WIDTH//2
                    coin_velocity = COIN_STARTING_VELOCITY

                    #pygame.mixer.music.play(-1,0.0) #infintie loop
                    is_paused = False
                    #player want to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


        print(f' BLITTING SPIDER {pygame.time.get_ticks()} | Event env time : {event_end_time} ')



         # helpful collisons
         # if burger_image_rect.colliderect(cheese_image_rect):
         #     score += 2
         #     coin_sound.play()
         #     cheese_image_rect.y = 0 - BUFFER_DISTANCE
         #     cheese_image_rect.x = random.randint(0, WINDOW_WIDTH - 32)
         #     random_velocity = random.randint(1, 10)




     pygame.display.flip()
     clock.tick(FPS)


pygame.quit()

# notes: images will drop incredients: (1)Ketchup, (2)Cheese, (3)Lettuce
# Obstacles: will be garbage to that you need to avoid of a point will be dedcuted from your life
# Specials: Kids Meal ! -> mini burge will replace regular sized burger and will move faster and smaller to avoid gargbage
