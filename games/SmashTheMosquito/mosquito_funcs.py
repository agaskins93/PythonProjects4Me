import os
import  random

import pygame.sprite


def north_south_border_rules(object_name, height, start_width, end_width):
    object_name.x = random.randint(start_width,end_width)
    object_name.y = height

def north_south_border_bounce(object_name,height,start_width, end_width):
    object_name.x = random.randint(start_width, end_width)
    object_name.y = height

def east_west_border_rules(object_name, height, width):
    object_name.x = random.randint(0,width)
    object_name.y = height

def east_west_border_bounce(object_name,width):
    object_name.x = random.randint(0, width)
    object_name.y = -10

def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join("../assets/", name)
    image = pygame.image.load(fullname)
    print(fullname)
    image = image.convert()

    image = pygame.transform.scale_by(image, scale)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

class Insecticide(pygame.sprite.Sprite):
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
        if self.spray:
            self.rect.move_ip(15,15)

    def swat(self, target):
        if not self.spray:
            self.spray = True
            hitbox = self.rect.inflate(-5,-5)
            return hitbox.colliderect(target.rect)


    def un_swat(self):
        self.spray = False