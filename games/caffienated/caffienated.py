import pygame
import random


pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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

font = pygame.font.Font("../caffienated/assets/RindeyaRegular.ttf")

points_text = font.render("Reward Points: " + str(coffee_points), True, WHITE)
points_rect = points_text.get_rect()
points_rect.topleft = (10,10)

score_text = font.render("Score: " + str(score), True, WHITE)
score_rect = score_text.get_rect()
score_rect.topleft = (10,50)

title_text = font.render("Caffienated", True, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

consumed_text = font.render("Cups Consumed: " + str(coffee_drunken), True,WHITE)
consumed_rect = consumed_text.get_rect()
consumed_rect.centerx = WINDOW_WIDTH//2
consumed_rect.y = 50

lives_text = font.render("Lives: " + str(player_lives),True,WHITE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

boost_level_text = font.render("Caffiene High: " + str(boost_level), True, WHITE)
boost_level_rect = boost_level_text.get_rect()
boost_level_rect.topright = (WINDOW_WIDTH - 10, 50)

game_over_text = font.render("FINAL SCORE: " + str(score), True, WHITE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, WHITE)
continue_rect =  continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#sound
drink_sound = pygame.mixer.Sound("../caffienated/assets/cartoon-slurp.mp3")
miss_sound = pygame.mixer.Sound("../caffienated/assets/crumple-03-40747.mp3")
pygame.mixer.music.load("../caffienated/assets/good-night-lofi-cozy.mp3")

player_image_right = pygame.image.load("../caffienated/assets/player-right.png")
player_image_left = pygame.image.load("../caffienated/assets/player_left.png")
player_image = player_image_left

player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH//2
player_rect.bottom = WINDOW_HEIGHT

after_image_right = pygame.image.load("../caffienated/assets/player-right.png")
after_image_left = pygame.image.load("../caffienated/assets/player_left.png")
after_image = after_image_left

after_rect = after_image.get_rect()
after_rect.centerx = WINDOW_WIDTH//2 + 10
after_rect.bottom = WINDOW_HEIGHT + 10

coffee_image = pygame.image.load("../caffienated/assets/Coffee.32.png")
coffee_rect = coffee_image.get_rect()
coffee_rect.topleft = (random.randint(0,WINDOW_WIDTH-32), - BUFFER_DISTANCE)

coffee_image_frenzy = pygame.image.load("../caffienated/assets/Coffee.32.png")
coffee_rect_frenzy = coffee_image_frenzy.get_rect()
coffee_rect_frenzy.center = (random.randint(0,WINDOW_WIDTH-32), - BUFFER_DISTANCE)

after_images = []
coffee_frenzy_coords = [(random.randint(0,WINDOW_WIDTH),random.randint(0,WINDOW_HEIGHT)) for i in range(25)]

class Coffee(pygame.sprite.Sprite):
    """ moves lattes at hyper slow pace while in caffience high"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../caffienated/assets/Coffee.32.png")
        self.rect = coffee_image.get_rect()
        self.rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), - BUFFER_DISTANCE)
        self.velocity = STARTING_COFFEE_VELOCITY
        self.boost_level = STARTING_BOOST_LEVEL
        self.player_lives = PLAYER_STARTING_LIVES
        self.is_drunk = False
        self.points = 0


    def update(self):
        self.rect.y += self.velocity
        if self.rect.y > WINDOW_HEIGHT:
            #sel -= 1
            self.rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), - BUFFER_DISTANCE)
            self.velocity = STARTING_COFFEE_VELOCITY

            self.boost_level = STARTING_BOOST_LEVEL
            miss_sound.play()
            print("here2")
        # return player_lives

    def _slowDrop(self):
        """ allows coffee to drop slowly vertically"""


    def sip(self):
        """resets coffecup and boost acceleration"""
        self.rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), - BUFFER_DISTANCE)
        self.velocity += COFFEE_ACCELERATION
    def coffee_points_by_y(self):
        self.points = 0
        self.points = int(self.velocity * (WINDOW_HEIGHT - self.rect.y + 100))
        return self.points



class CoffeeFrenzy(pygame.sprite.Sprite):
    """ moves lattes at hyper slow pace while in caffience high"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../caffienated/assets/Coffee.32.png")
        self.rect = coffee_image.get_rect()
        self.rect.center = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT))

        self.is_drunk = False
    def set_frenzy_mode_on(self):
        self.is_drunk = True

    def set_frenzy_mode_off(self):
        self.is_drunk = False


    def update(self):
        self._slowDrop()

    def _slowDrop(self):
        """ allows coffee to drop slowly vertically"""
        self.rect.y += 1


class Player(pygame.sprite.Sprite):
    """ moves lattes at hyper slow pace while in caffience high"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player_lives = PLAYER_STARTING_LIVES
        self.player_velocity = PLAYER_NORMAL_VELOCITY

        self.boost_level = STARTING_BOOST_LEVEL
        self.player_image_right = pygame.image.load("../caffienated/assets/player-right.png")
        self.player_image_left = pygame.image.load("../caffienated/assets/player_left.png")
        self.image = self.player_image_left

        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH // 2
        self.rect.bottom = WINDOW_HEIGHT
        self.is_caffiene_high = False
        self.after_images = []


    def update(self, keys):
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            self.rect.x -= self.player_velocity
            self.image = self.player_image_left
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.player_velocity
            self.image = self.player_image_right
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.player_velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.player_velocity

        if keys[pygame.K_SPACE] and self.boost_level > 0:
            self.player_velocity = PLAYER_BOOST_VELOCITY
            self.boost_level -= 1
        else:
            self.player_velocity = PLAYER_NORMAL_VELOCITY

        if self.is_caffiene_high:
            self.caffiene_high()




    def caffiene_switch_on(self):
        """ set switch it intiate after images and slow down coffee frenzy cups"""
        self.is_caffiene_high = True

    def caffiene_high(self):
        """ set switch it intiate after images and slow down coffee frenzy cups"""
        self.after_images.append((self.rect.x, self.rect.y))
        if len(self.after_images) > 20:
            self.after_images.pop(0)

        display_surface.fill(GREEN)

        for i, (ax, ay) in enumerate(self.after_images):
            alpha = int(255 * (i + 1) / 3 / 2)  # fade factor
            faded = self.image.copy()
            faded.set_alpha(alpha)
            display_surface.blit(faded, (ax, ay))




    def caffiene_switch_off(self):
        """ set switch it intiate after images and slow down coffee frenzy cups"""
        self.is_caffiene_high = False

    def pickmeup(self):
        self.boost_level += 25
        if self.boost_level > STARTING_BOOST_LEVEL:
            self.boost_level = STARTING_BOOST_LEVEL



coffee_frenzy_sprites = pygame.sprite.Group()
player_sprite = Player()
player_sprite_single = pygame.sprite.GroupSingle(player_sprite)
coffee = Coffee()
coffee_sprite_single = pygame.sprite.GroupSingle(coffee)



for _ in range(20):
    coffee_frenzy_cup = CoffeeFrenzy()
    coffee_frenzy_sprites.add(coffee_frenzy_cup)

#events
FRENZY_MODE = pygame.USEREVENT + 1
pygame.time.set_timer(FRENZY_MODE,30000)
intiate_frenzy_mode = False
start_time = pygame.time.get_ticks()
count = 0
event_end_time = 0



#Sounds music
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       elif event.type == FRENZY_MODE:
        intiate_frenzy_mode = True
        event_end_time = pygame.time.get_ticks() + 10000
        print(event_end_time)


    #move the player
    keys = pygame.key.get_pressed()
    player_sprite.update(keys)

    if pygame.sprite.spritecollide(player_sprite, coffee_sprite_single, dokill=False):
        score += coffee.coffee_points_by_y()
        coffee_drunken += 1
        drink_sound.play()
        coffee.sip()
        player_sprite.pickmeup()

    points_text = font.render("Reward Points: " + str(coffee_points), True, WHITE)
    score_text = font.render("Score: " + str(score), True, WHITE)
    consumed_text = font.render("Cups Consumed: " + str(coffee_drunken), True, WHITE)
    lives_text = font.render("Lives: " + str(player_lives), True, WHITE)
    boost_level_text = font.render("Caffiene High: " + str(boost_level), True, WHITE)

    #check for game over
    if player_lives == 0:
        game_over_text = font.render("FINAL SCORE: " + str(score), True, WHITE)
        display_surface.blit(game_over_text,game_over_rect)
        display_surface.blit(consumed_text,consumed_rect)
        pygame.display.update()
        pygame.mixer.music.stop()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    coffee_drunken = 0
                    player_lives = PLAYER_STARTING_LIVES
                    boost_level = STARTING_BOOST_LEVEL
                    coffee_velocity = STARTING_COFFEE_VELOCITY
                    pygame.mixer.music.play()
                    is_paused = False

            if event.type == pygame.QUIT:
                is_paused = False
                running  = False


    if intiate_frenzy_mode:
        player_sprite.caffiene_switch_on()
    else:
        player_sprite.caffiene_switch_off()
        display_surface.fill(GREEN)

    display_surface.blit(points_text,points_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(consumed_text,consumed_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_level_text, boost_level_rect)
    pygame.draw.line(display_surface, BLACK, (0,100), (WINDOW_WIDTH, 100), 3)

    if intiate_frenzy_mode and pygame.time.get_ticks() < event_end_time:
        coffee_frenzy_sprites.update()
        coffee_frenzy_sprites.draw(display_surface)
        if pygame.sprite.spritecollide(player_sprite, coffee_frenzy_sprites, dokill=True):
            score += 50
    else:
        player_sprite.caffiene_switch_off()
        intiate_frenzy_mode = False
    player_sprite_single.draw(display_surface)
    coffee_sprite_single.update()
    coffee_sprite_single.draw(display_surface)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
