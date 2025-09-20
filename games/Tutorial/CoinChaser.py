# Can you add text X
# keep track when you collied with the coin X
# can you add sounds effect evvery time you collied with the coin X
# could you channge to mouse controles
# could you give win screen : Extra
import random
import pygame


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Coin Chaser')

FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

VELOCITY = 5

#define sounds
sound1_hit = pygame.mixer.Sound('../assets/sound1Hit.wav')
sound2_zap = pygame.mixer.Sound('../assets/sound1Zap.wav')


custom_font = pygame.font.Font("../assets/DripOctober-vm0JA.ttf", 50)
custom_text = custom_font.render("Dragon Coin Chase", True, BLACK)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 250)

custom_win_text = custom_font.render("YOU WIN", True, BLACK)
custom_win_text_rect = custom_win_text.get_rect()
custom_win_text_rect.center = (300, 300)


def custom_count(counter):
    custom_counter = custom_font.render(f'Catches {count}' , True, BLACK)
    custom_counter_rect = custom_counter.get_rect()
    custom_counter_rect.bottomright = (500,500)
    return custom_counter_rect, custom_counter

dragon_image = pygame.image.load('../assets/Dragon.64.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

coin_image = pygame.image.load('../assets/Coin.png')
coin_image_rect = coin_image.get_rect()
coin_image_rect.topleft = (100, 100)


running = True
count = 0
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and dragon_image_rect.left > 0:
        dragon_image_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and dragon_image_rect.right < WINDOW_WIDTH:
        dragon_image_rect.x += VELOCITY
    if keys[pygame.K_UP] and dragon_image_rect.top > 0:
        dragon_image_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and dragon_image_rect.bottom < WINDOW_HEIGHT:
        dragon_image_rect.y += VELOCITY



    if dragon_image_rect.colliderect(coin_image_rect):
        coin_image_rect.x =  random.randint(0,WINDOW_WIDTH-48 )
        coin_image_rect.y = random.randint(0,WINDOW_HEIGHT-48 )
        sound1_hit.play()
        count += 1

    if count > 5:
        display_surface.blit(custom_win_text, custom_win_text_rect)
        pygame.display.update()
        pygame.time.wait(10000)
        pygame.display.update()
        pygame.quit()






    custom_counter_rect, custom_counter = custom_count(count)

    display_surface.fill(WHITE)
    display_surface.blit(coin_image, coin_image_rect)
    display_surface.blit(dragon_image, dragon_image_rect)
    display_surface.blit(custom_text, custom_text_rect)
    display_surface.blit(custom_counter, custom_counter_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
