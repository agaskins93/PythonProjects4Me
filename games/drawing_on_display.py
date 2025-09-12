import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Draw on Me!')


#Define colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#give a background color to display
display_surface.fill(MAGENTA)

#Draw various shapes
#Line(surface , color , start point , end point , thickness)
pygame.draw.line(display_surface, YELLOW, (0,0), (100,100), 5  )
pygame.draw.line(display_surface, YELLOW, (200,200), (300,300), 2  )

#Circ;e ( surface, color, ceneter , radius, thicjness)
pygame.draw.circle(display_surface, CYAN, (WINDOW_WIDTH//2,WINDOW_HEIGHT//2), 200, 6)
pygame.draw.circle(display_surface, RED, (WINDOW_WIDTH//2,WINDOW_HEIGHT//2), 190, 6)

#Rec(surface, color , (top lef x, top left y, width , height))
pygame.draw.rect(display_surface, GREEN,(500, 0, 100, 100))
pygame.draw.rect(display_surface, GREEN,(500, 300, 50, 100))






running = True
while running:
    #loop through a list of Events objects that have occured
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    #update the diplay
    pygame.display.update()


pygame.quit()