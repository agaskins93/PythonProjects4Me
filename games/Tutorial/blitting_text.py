import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('blitting Games')

#Define colors
GREEN = (0,255,0)
DARKGREEN = (10,50,10)
BLACK = (0,0,0)
WHITE = (255,255,255)

#printing out list of fonts
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)


#give a background color to display
display_surface.fill(WHITE)

#load fonts
system_font = pygame.font.SysFont("monospace", 65)
custom_font = pygame.font.Font("../assets/DripOctober-vm0JA.ttf", 50)

#Define Text
system_text = system_font.render("Legacy", True, BLACK)
system_text_rect = system_text.get_rect()
system_text_rect.center  = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


custom_text = custom_font.render("Move Dragon Soon", True, BLACK)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #blit copies text surface
    display_surface.blit(system_text,system_text_rect)
    display_surface.blit(custom_text,custom_text_rect)
    pygame.display.update()


pygame.quit()



