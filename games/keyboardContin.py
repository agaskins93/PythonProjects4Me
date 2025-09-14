import pygame

##### Allows cntinous movment when holding down a key
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
surface_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Keyboard Continuation")

#setFPS and Clock
FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
surface_display.fill(WHITE)

VELOCITY = 5

dragon_image = pygame.image.load('Dragon.64.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #get a list of all keys being held
        #if event.type == pygame.
        #if event.type == pygame.
    keys = pygame.key.get_pressed()
    print(keys)
    #Move the  dragon contiinouly
    if keys[pygame.K_LEFT]:
        dragon_image_rect.left -= VELOCITY

    if keys[pygame.K_RIGHT]:
        dragon_image_rect.right += VELOCITY

    if keys[pygame.K_UP]:
        dragon_image_rect.top -= VELOCITY

    if keys[pygame.K_DOWN]:
        dragon_image_rect.bottom += VELOCITY

    surface_display.fill(WHITE)
    surface_display.blit(dragon_image, dragon_image_rect)
    pygame.display.update()

    #tick the clock
    clock.tick(FPS)


pygame.quit()