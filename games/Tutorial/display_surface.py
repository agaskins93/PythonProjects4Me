import pygame

#intailize pygame
pygame.init()

#creae a display surface and set itscaption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hello World')
clock = pygame.time.Clock()

#the main game
running = True
while running:
    #loop through a list of Events objects that have occured
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    pygame.display.update()


#endthe game
pygame.quit()




