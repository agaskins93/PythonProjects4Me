import pygame
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images")

WHITE = (255, 255, 255)


#create images
#we can get the rect of the surafce and use the rect to psotion the images

dragon_image_left = pygame.image.load('../assets/Dragon.64.png')
dragon_image_left_rect = dragon_image_left.get_rect()
dragon_image_left_rect.topleft = (0,0)



dragon_image_right = pygame.image.load('../assets/Dragon.64.png')
dragon_image_right_rect = dragon_image_right.get_rect()
dragon_image_right_rect.topright = (WINDOW_WIDTH,0)


pygame.draw.rect(display_surface, WHITE,(500, 0, 100, 65))
pygame.draw.rect(display_surface, WHITE,(0, 0, 100, 65))




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit (copy  a surface object at the given coordinate to our displau
    display_surface.blit(dragon_image_left,dragon_image_left_rect)
    display_surface.blit(dragon_image_right,dragon_image_right_rect)
    pygame.draw.line(display_surface, WHITE, (0,75), (WINDOW_WIDTH,75), 4)

    #updating the display
    pygame.display.update()


pygame.quit()

