import pygame

###### Shows how to restrict avatar movement along with using
###### alt keys for directions

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface= pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Mouse Movement Restrict')

WHITE = (255, 255, 255)
display_surface.fill(WHITE)

dragon_image = pygame.image.load('../assets/Dragon.64.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

VELOCITY = 5

FPS = 60
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
 # bound to the fgame window
    if (keys[pygame.K_LEFT] or keys[pygame.K_a])and dragon_image_rect.left > 0:
        dragon_image_rect.left -= VELOCITY

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_image_rect.right < WINDOW_WIDTH:
        dragon_image_rect.right += VELOCITY

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_image_rect.top > 0:
        dragon_image_rect.top -= VELOCITY

    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_image_rect.bottom < WINDOW_HEIGHT:
        dragon_image_rect.bottom += VELOCITY

    display_surface.fill(WHITE)
    display_surface.blit(dragon_image, dragon_image_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()


