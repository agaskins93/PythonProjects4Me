import pygame

#sets up movement with mouse or mouse page alon with point and click

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_screen= pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mouse Movement")

#setFPS and Clock
FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
display_screen.fill(WHITE)

dragon_image = pygame.image.load('../assets/Dragon.64.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.topleft = (25,25)




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_image_rect.centerx = mouse_x
            dragon_image_rect.centery = mouse_y

        #Drag the mouse buttong when clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_image_rect.centerx = mouse_x
            dragon_image_rect.centery = mouse_y

    display_screen.fill(WHITE)
    display_screen.blit(dragon_image,dragon_image_rect)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()