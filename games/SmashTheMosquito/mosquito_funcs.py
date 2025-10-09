import os
import  random

import pygame.sprite

WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
MOSQUITO_STARTING_VELOCITY = 3
mosquito_velocity = MOSQUITO_STARTING_VELOCITY
mos_dx = random.choice([-1,1])
mos_dy = random.choice([-1,1])



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


    def swat(self, target):
        if not self.spray:
            self.spray = True
            hitbox = self.rect.inflate(5,5)
            return hitbox.colliderect(target.rect)


    def un_swat(self):
        self.spray = False

class Mosquito(pygame.sprite.Sprite):
    """ moves the mosquito acroos the screen randomly for the user to click on"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("mosquito.png",-1,1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.sprayed = False
        self.mos_dx = mos_dx
        self.mos_dy = mos_dy

    def update(self):
        if self.sprayed:
            self._exterminated()
        else:
            self._fly()
    def _fly(self):
        """ Allows the fly to  fly by on the screen form random postions"""
        # self.mos_dy = random.choice([-1, 1])
        self.rect.x += self.mos_dx * mosquito_velocity
        self.rect.y += self.mos_dy * mosquito_velocity

        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.mos_dx = -1 * self.mos_dx



        if self.rect.top >= WINDOW_HEIGHT:
            choice = random.choice([1, 2])
            if choice == 1:
                north_south_border_rules(self.rect, WINDOW_HEIGHT, 0, WINDOW_WIDTH)
                self.mos_dy = -1
            if choice == 2:
                north_south_border_bounce(self.rect, -10, 0, WINDOW_WIDTH)
                self.mos_dy = 1
        if self.rect.top <= 0:
            choice = random.choice([1, 2])
            if choice == 1:
                north_south_border_rules(self.rect, 0, 0, WINDOW_WIDTH)
                self.mos_dy = 1
            if choice == 2:
                north_south_border_rules(self.rect, 610, 0, WINDOW_WIDTH)
                self.mos_dy = -1


    def _exterminated(self):
        """will cause the mosquito to drop to the botoom of the screen"""
        self.rect.y += mosquito_velocity

        if self.rect.top >= WINDOW_HEIGHT:
           self.sprayed = False


    def caught(self):
        if not self.sprayed:
           self.sprayed = True

class Fly(pygame.sprite.Sprite):
    """ moves the mosquito acroos the screen randomly for the user to click on"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("Fly.64.png",-1,1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.sprayed = False
        self.mos_dx = mos_dx
        self.mos_dy = mos_dy

    def update(self):
        if self.sprayed:
            self._exterminated()
        else:
            self._fly()
    def _fly(self):
        """ Allows the fly to  fly by on the screen form random postions"""
        # self.mos_dy = random.choice([-1, 1])
        self.rect.x += self.mos_dx * mosquito_velocity
        self.rect.y += self.mos_dy * mosquito_velocity

        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.mos_dx = -1 * self.mos_dx



        if self.rect.top >= WINDOW_HEIGHT:
            choice = random.choice([1, 2])
            if choice == 1:
                north_south_border_rules(self.rect, WINDOW_HEIGHT, 0, WINDOW_WIDTH)
                self.mos_dy = -1
            if choice == 2:
                north_south_border_bounce(self.rect, -10, 0, WINDOW_WIDTH)
                self.mos_dy = 1
        if self.rect.top <= 0:
            choice = random.choice([1, 2])
            if choice == 1:
                north_south_border_rules(self.rect, 0, 0, WINDOW_WIDTH)
                self.mos_dy = 1
            if choice == 2:
                north_south_border_rules(self.rect, 610, 0, WINDOW_WIDTH)
                self.mos_dy = -1


    def _exterminated(self):
        """will cause the mosquito to drop to the botoom of the screen"""
        self.rect.y += mosquito_velocity

    def caught(self):
        if not self.sprayed:
           self.sprayed = True

