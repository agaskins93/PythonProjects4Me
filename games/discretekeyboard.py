import pygame
### Show how to move using direction pad ( 1 tap equals one movement only.
###
pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Discrete Keyboard')



#set game values
VELOCITY = 10


#color
WHITE = (255,255,255)

display_surface.fill(WHITE)

#load in images
dragon_image = pygame.image.load('Dragon.64.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.centerx = WINDOW_WIDTH // 2
dragon_image_rect.bottom = WINDOW_HEIGHT






running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

        #Check for descrete movement ( Left )
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                dragon_image_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT :
                dragon_image_rect.x += VELOCITY
            if event.key == pygame.K_UP :
                dragon_image_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN :
                dragon_image_rect.y += VELOCITY




    #fill the display surfaces to cover old images

    display_surface.fill(WHITE)



    display_surface.blit(dragon_image, dragon_image_rect)
    pygame.display.update()


pygame.quit()
