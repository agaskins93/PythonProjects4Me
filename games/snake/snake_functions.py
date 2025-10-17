#External functions to be implemented within snake
#extra features: portals, and coin wrap around
import pygame.sprite
#Overall attributes
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

#Snake attributes
SNAKE_SIZE = 20
head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT //2 + 100
snake_dx = 0
snake_dy = 0


class Snake(pygame.sprite.Sprite):
    """ Moves a fly trap across the screen, following the moust """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # initializing sprite
        self.image, self.rect = load_image("Deadly-Spray.64.png", -1)
        self.spray_offset = (-10, -10)
        self.spray = False

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.spray_offset)


    def swat(self, target):
        if not self.spray:
            self.spray = True
            hitbox = self.rect.inflate(5,5)
            return hitbox.colliderect(target.rect)


    def un_swat(self):
        self.spray = False
