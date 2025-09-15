import pygame
import random

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
surface_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision Detection")

WHITE = (255, 255, 255)
surface_display.fill(WHITE)

dragon_image = pygame.image.load('Dragon.64.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.topleft = (25,25)

coin_image = pygame.image.load('Coin.png')
coin_image_rect = coin_image.get_rect()
coin_image_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

FPS = 60
clock = pygame.time.Clock()

VELOCITY = 5

running = True
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


# check fro colllisons
    if dragon_image_rect.colliderect(coin_image_rect):
        coin_image_rect.x =  random.randint(0,WINDOW_WIDTH-48 )
        coin_image_rect.y = random.randint(0,WINDOW_HEIGHT-48 )



    surface_display.fill(WHITE)

    #Draw rectangels to rep the rects of each object
    pygame.draw.rect(surface_display, ( 0, 255 , 0 ), dragon_image_rect, 1)
    pygame.draw.rect(surface_display, ( 255, 0 , 0 ), coin_image_rect, 1)

    surface_display.blit(dragon_image, dragon_image_rect)
    surface_display.blit(coin_image, coin_image_rect)
    pygame.display.update()
    clock.tick(FPS)



pygame.quit()

