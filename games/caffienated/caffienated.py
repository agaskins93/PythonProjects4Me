import random

import pygame

from PythonProjects4Me.games.CatchTheDragon.catch_the_dragon import title_text, game_over_text, miss_sound, \
    BUFFER_DISTANCE
from PythonProjects4Me.games.CatchTheDragon.smash_the_mosquito import PLAYER_STARTING_LIVES, player_lives
from PythonProjects4Me.games.snake.snake import continue_text

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode(WINDOW_WIDTH,WINDOW_HEIGHT)
pygame.display.set_caption("Caffienated")


#set FPS
FPS = 60
clock = pygame.time.Clock()

#Game Values:

PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_COFFEE_VELOCITY = 3
COFFEE_ACCELERATION = .25
BUFFER_DISTANCE  = 100

score = 0
coffee_points = 0
coffee_drunken = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY

boost_level = STARTING_BOOST_LEVEL

coffee_velocity =  STARTING_COFFEE_VELOCITY


#set Colors

GREEN = (0,115,67)
BLACK = (0,0,0)
WHITE = ( 255,255,255)

font = pygame.font.Font("");

points_text = font.render("Reward Points: " + str(coffee_points), True, ORANGE)
points_rect = points_text.get_rect()
points_rect.topleft(10,10)

score_text = font.render("Score: " + str(score), True, WHITE)
score_rect = score_text.get_rect()
score_rect.topleft=(10,50)

title_text = font.render("Caffienated", True, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

consumed_text = font.render("Cups Consumed: " + str(coffee_drunken), True,ORANGE)
consumed_rect = consumed_text.get_rect()
consumed_rect.centerx = WINDOW_WIDTH//2
consumed_rect.y = 50

lives_text = font.render("Lives: " + str(player_lives),True,ORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

boost_level_text = font.render("Caffiene High: " + str(boost_level), True, ORANGE)
boost_level_rect = boost_level_text.get_rect()

game_over_text  = font.render("FINAL SCORE: " + str(score), True, ORANGE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center(WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, ORANGE)
continue_rect =  continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#sound
drink_sound = pygame.mixer.Sound("")
miss_sound = pygame.mixer.Sound("")
pygame.mixer.music.load("")

player_image_right = pygame.image.load("")
player_image_left = pygame.image.load("")
player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH//2
player_rect.bottom = WINDOW_HEIGHT

coffee_image = pygame.image.load("")
coffee_rect = coffee_image.get_rect()
coffee_rect.topleft = (random.randint(0,WINDOW_WIDTH-32), -BUFFER_DISTANCE)











#set music

#Sounds music

running = True
while running:
    for event in event.get():
       if event.type == pygame.QUIT:
           running = False

    #fill the surace
    display_surface.fill(GREEN)

    display_surface.blit(points_text,points_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(continue_text,consumed_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_level_text, boost_level_rect)
    pygame.draw.line(display_surface, WHITE, (0,100), (WINDOW_WIDTH, 100), 3)

    #BLite Assets
    display_surface.blit(player_image,player_rect)
    display_surface.blit(coffee_image,coffee_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
